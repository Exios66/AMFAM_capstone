"""Unit tests for shared library gaps: constants, prompts, env_utils, image_utils, braintrust_config."""

import base64

import pytest
from PIL import Image

from src import braintrust_config as bc
from src import constants, env_utils, image_utils
from src.prompts import DEFAULT_PROMPT_VERSION, get_prompt, list_prompt_versions


class TestConstants:
    def test_sixteen_unique_classes(self):
        classes = constants.DOCUMENT_CLASSES
        assert len(classes) == 16
        assert len(set(classes)) == 16
        assert all(c.islower() and c.isidentifier() for c in classes)

    def test_image_extensions_have_leading_dots(self):
        assert constants.IMAGE_EXTENSIONS
        assert all(e.startswith(".") for e in constants.IMAGE_EXTENSIONS)


class TestPromptsRegistry:
    def test_default_version_is_registered(self):
        versions = list_prompt_versions()
        assert DEFAULT_PROMPT_VERSION in versions
        assert len(versions) == len(set(versions)), "duplicate prompt version names"
        assert len(versions) >= 15

    def test_all_prompts_are_nonempty(self):
        for version in list_prompt_versions():
            assert get_prompt(version).strip(), f"empty prompt for {version}"


class TestEnvUtils:
    def test_require_env_returns_values(self, monkeypatch):
        monkeypatch.setattr(env_utils, "load_dotenv_if_available", lambda: None)
        monkeypatch.setenv("AMFAM_TEST_VAR", "hello")
        monkeypatch.setenv("AMFAM_OTHER_VAR", "world")
        assert env_utils.require_env("AMFAM_TEST_VAR") == ("hello",)
        assert env_utils.require_env("AMFAM_TEST_VAR", "AMFAM_OTHER_VAR") == ("hello", "world")

    def test_require_env_exits_when_missing(self, monkeypatch):
        monkeypatch.setattr(env_utils, "load_dotenv_if_available", lambda: None)
        monkeypatch.delenv("AMFAM_TEST_MISSING_VAR", raising=False)
        with pytest.raises(SystemExit):
            env_utils.require_env("AMFAM_TEST_MISSING_VAR")


class TestImageUtils:
    def test_encode_image_base64_data_uri(self, tmp_path):
        img = Image.new("L", (4, 4), 128)
        path = tmp_path / "pixel.png"
        img.save(path)
        encoded = image_utils.encode_image_base64(path)
        assert isinstance(encoded, str)
        assert base64.b64decode(encoded) == path.read_bytes()

    def test_find_images_filters_by_extension(self, tmp_path):
        (tmp_path / "a.png").write_bytes(b"x")
        (tmp_path / "b.tiff").write_bytes(b"x")
        (tmp_path / "c.txt").write_bytes(b"x")
        found = image_utils.find_images(tmp_path)
        names = [p.name for p in found]
        assert "a.png" in names and "b.tiff" in names
        assert "c.txt" not in names


class TestBraintrustConfig:
    @pytest.fixture(autouse=True)
    def _hermetic_env(self, monkeypatch):
        monkeypatch.setattr(bc, "_load_dotenv", lambda path: None)
        for key in (
            "BRAINTRUST_ORG_ID", "BRAINTRUST_PROJECT_ID", "BRAINTRUST_PROJECT_NAME",
            "BRAINTRUST_DATASET_PROJECT", "BRAINTRUST_DATASET", "BRAINTRUST_SMOKE_DATASET",
            "BRAINTRUST_MODEL", "BRAINTRUST_API_BASE", "BRAINTRUST_API_KEY",
            "DATA_BRAINTRUST_KEY", "QWEN_EXPERIMENTS",
        ):
            monkeypatch.delenv(key, raising=False)

    def test_loads_defaults_when_unset(self):
        cfg = bc.load_braintrust_config(env_file="definitely-missing.env")
        assert cfg.org_id == bc.DEFAULT_ORG_ID
        assert cfg.project_id == bc.DEFAULT_PROJECT_ID
        assert cfg.project_name == bc.DEFAULT_PROJECT_NAME
        assert cfg.dataset == bc.DEFAULT_DATASET
        assert cfg.model == bc.DEFAULT_MODEL
        assert cfg.api_base == bc.DEFAULT_API_BASE
        assert cfg.api_key == ""
        assert cfg.qwen_experiments == ()

    def test_env_overrides_defaults(self, monkeypatch):
        monkeypatch.setenv("BRAINTRUST_PROJECT_ID", "custom-id")
        monkeypatch.setenv("BRAINTRUST_MODEL", "custom/model")
        monkeypatch.setenv("QWEN_EXPERIMENTS", "exp-a exp-b")
        cfg = bc.load_braintrust_config(env_file="definitely-missing.env")
        assert cfg.project_id == "custom-id"
        assert cfg.model == "custom/model"
        assert cfg.qwen_experiments == ("exp-a", "exp-b")

    def test_empty_env_values_fall_back_to_defaults(self, monkeypatch):
        monkeypatch.setenv("BRAINTRUST_DATASET", "")
        cfg = bc.load_braintrust_config(env_file="definitely-missing.env")
        assert cfg.dataset == bc.DEFAULT_DATASET
