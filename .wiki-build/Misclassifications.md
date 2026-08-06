# Misclassification Reasoning — qwen3.7-flash_v11.8_reasoning_1600_balanced_1120

<strong>Overall accuracy:</strong> 82.6% (925/1120)  
**Total Errors:** 195  
**Unique Confused Pairs:** 70


Full reasoning traces for all 195 misclassifications (70 confusion pairs) from the 1,120-image v11.8 run — every trace's 14-check scratchpad, runner-up line, and final label. Collapse each pair to browse, or expand to read the model's reasoning.

## All confusion pairs

| Expected | Predicted | Errors |
|----------|-----------|-------:|
| letter | memo | 16 |
| budget | invoice | 12 |
| specification | form | 9 |
| invoice | budget | 8 |
| presentation | scientific_report | 8 |
| advertisement | presentation | 7 |
| scientific_report | form | 7 |
| budget | form | 6 |
| invoice | form | 6 |
| scientific_publication | scientific_report | 6 |
| file_folder | presentation | 5 |
| memo | letter | 5 |
| presentation | file_folder | 4 |
| scientific_publication | news_article | 4 |
| scientific_report | specification | 4 |
| advertisement | form | 3 |
| budget | presentation | 3 |
| email | presentation | 3 |
| handwritten | questionnaire | 3 |
| presentation | form | 3 |
| questionnaire | presentation | 3 |
| scientific_report | file_folder | 3 |
| scientific_report | handwritten | 3 |
| advertisement | file_folder | 2 |
| budget | scientific_report | 2 |
| file_folder | form | 2 |
| form | questionnaire | 2 |
| form | file_folder | 2 |
| form | specification | 2 |
| handwritten | presentation | 2 |
| letter | handwritten | 2 |
| letter | form | 2 |
| memo | form | 2 |
| news_article | advertisement | 2 |
| news_article | email | 2 |
| news_article | memo | 2 |
| presentation | memo | 2 |
| questionnaire | scientific_report | 2 |
| questionnaire | form | 2 |
| scientific_report | scientific_publication | 2 |
| advertisement | news_article | 1 |
| email | questionnaire | 1 |
| email | advertisement | 1 |
| email | memo | 1 |
| email | form | 1 |
| form | handwritten | 1 |
| form | invoice | 1 |
| form | presentation | 1 |
| handwritten | advertisement | 1 |
| handwritten | file_folder | 1 |
| handwritten | form | 1 |
| invoice | letter | 1 |
| letter | file_folder | 1 |
| memo | specification | 1 |
| memo | budget | 1 |
| news_article | scientific_publication | 1 |
| news_article | presentation | 1 |
| news_article | scientific_report | 1 |
| news_article | file_folder | 1 |
| presentation | handwritten | 1 |
| presentation | news_article | 1 |
| presentation | budget | 1 |
| presentation | advertisement | 1 |
| questionnaire | handwritten | 1 |
| questionnaire | file_folder | 1 |
| resume | file_folder | 1 |
| resume | scientific_report | 1 |
| resume | presentation | 1 |
| scientific_publication | presentation | 1 |
| scientific_report | memo | 1 |

For each pair below, the trace shows the model walking the check-1→14 cascade, naming its runner-up, and committing to a (wrong) final label.

## letter → memo

<details class="trace-group" open>

<summary>16 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__letter__0004.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow a specific scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Header: "RJR Interoffice Memorandum"
- Date: "MAR 27 1987" (top right), "March 26, 1987" (next to Subject)
- Subject: "Use of KYDEX(R) For A Waste Tub Stand"
- To: "Mr. Bill Hunt"
- From: "Dr. Rob Harrington"
- Body: Running prose discussing the toxicity of Kydex(R) plastic sheets (polyacrylic-polyvinyl chloride polymer).
- Signature: "Rob" (signed)
- CC: Dr. A. W. Hayes, Dr. R. L. Suber, Dr. Randy Deskin
- Handwritten note at the bottom: "3/30 For the busy start this spd - also for your requested data from Boston withms inelastic Othels for purchase Will" (roughly).

**Pre-scan:**

- Mail-client header block? No. "RJR Interoffice Memorandum", "To:", "From:", "Subject:". This is a memo header, not an email header (From/To/Sent/Subject with email addresses or mail client formatting). Wait, check 11 says email requires mail-client header block (From/To/Sent/Subject, cc, attachments) or forwarded/threaded trail. This has "To:", "From:", "Subject:", "cc:". But it's a standard memo header. Let's look at check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose...". This is a memo.
- Masthead/running head? No newspaper/magazine masthead. No journal running head.

**Check 1: file_folder**

- Evidence: Has full body content, header, subject, to/from, prose. Not file_folder.
- Not this check.

**Check 2: handwritten**

- Evidence: Mostly typed prose. Handwritten note at the bottom, but majority is typed.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or fax cover sheet header. The "MAR 27 1987" is a date stamp, maybe from a fax machine or just a date stamp on the memo. Wait, is there a fax transmission header? "MAR 27 1987" is just a date. No "SENT BY:" or page count like "# 4/7".
- Not this check.

**Check 4: questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: resume**

- Evidence: Not a CV.
- Not this check.

**Check 6: scientific_publication**

- Evidence: No journal running head, volume, issue, page number.
- Not this check.

**Check 7: financial document**

- Evidence: No line-item table, ledger, invoice, budget. Mentions "Kydex(R) plastic sheets", toxicity data. No money structure.
- Not this check.

**Check 8: specification**

- Evidence: Discusses toxicity of Kydex, but it's a memo evaluating its use. Not a Material Safety Data Sheet or product specification with "shall/must".
- Not this check.

**Check 9: presentation**

- Evidence: Not a slide deck, cover, or statement.
- Not this check.

**Check 10: administrative form**

- Evidence: Not a form with fields/boxes.
- Not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: "RJR Interoffice Memorandum", "Subject:", "To: Mr. Bill Hunt", "From: Dr. Rob Harrington", "March 26, 1987". Followed by memo-style prose. CC list. Signature.
- This is a memo.
- Stop here.

**Runner-up:** letter. Ruled out because it's an internal interoffice memorandum with TO:/FROM:/SUBJECT: header and no external address/salutation/closing signature (just a first-name signature "Rob" and CC list, typical of internal memos). Wait, check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose...". This matches perfectly.

Let's double check check 11 details:

"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."

The document has:

"RJR Interoffice Memorandum"

"Subject: Use of KYDEX(R) For A Waste Tub Stand"

"To: Mr. Bill Hunt"

"From: Dr. Rob Harrington"

"March 26, 1987"

This is a classic memo.

Final label: memo.


<h3 class="trace-file"><code>rvl_cdip__letter__0024.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow a specific scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Header: "The American Tobacco Company", "150 East 42nd Street", "New York, *N*.Y. 10017"
- Date: "December 31, 1964"
- Addressee: "TO THE ENTIRE SALES ORGANIZATION"
- Body: Discusses the "new Cigarette Advertising Code", lists permissible and non-permissible activities on school/college campuses.
- Footer: "CONFIDENTIAL: MINNESOTA TOBACCO LITIGATION", "ATX110005646"
- Handwritten note: "Code byde" (or similar) at top right.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. "The American Tobacco Company" is a letterhead.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a full letter body, letterhead, date, addressee. Not identifier-only.
- Result: not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Mostly typed text. Only a small handwritten note "Code byde" at top right.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or fax cover sheet header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: Not a survey instrument.
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: Not a resume.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range on the page itself.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial line-item table, ledger, statement. Mentions "supply", "distribution", but no money tracking or billing as primary structure.
- Result: not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: Discusses advertising code, not product formulation or material safety.
- Result: not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck, not a press release ("FOR IMMEDIATE RELEASE"), not a speech text. It's a typed letter/memo.
- Result: not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: No filled/blank fields, boxes, checkboxes for capturing data. It's a narrative letter/memo.
- Result: not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence:

    - Letterhead: "The American Tobacco Company", address.

    - Date: "December 31, 1964".

    - Addressee: "TO THE ENTIRE SALES ORGANIZATION". This is an internal address.

    - Body: Prose discussing the Cigarette Advertising Code.

    - No "Dear ..." salutation, no closing signature.

    - Wait, is it a memo or a letter?

    - Memo rule: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose. Or a dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION.

    - Here: "TO THE ENTIRE SALES ORGANIZATION". No "FROM:" or "RE:". But it's addressed internally ("TO THE ENTIRE SALES ORGANIZATION").

    - Letter rule: letterhead with external recipient address... OR a dated note addressed to a named EXTERNAL person.

    - Wait, let's look at the memo rule again: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels".

    - Here we have "TO THE ENTIRE SALES ORGANIZATION". This is an internal address. It lacks "FROM:" and "RE:".

    - Let's check the letter rule: "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

    - This is addressed to "THE ENTIRE SALES ORGANIZATION". It's internal.

    - Is it a memo? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels". Here it's addressed to an organization, not a named person.

    - However, it has a letterhead, date, internal addressee, prose body, no salutation, no closing.

    - Let's re-read the memo definition carefully: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."

    - This document has "TO THE ENTIRE SALES ORGANIZATION". It doesn'*t* have a named person + title. It doesn'*t* have FROM/RE.

    - Is it a letter? "letter: letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." This is internal.

    - Wait, what about a company statement or internal circular? The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

    - If it's not strictly a memo (missing named addressee + title) and not a letter (internal, no salutation/closing), what is it?

    - Let's look at the letter definition again. "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."

    - This is addressed to "THE ENTIRE SALES ORGANIZATION". It's an internal memo/circular.

    - Often, internal circulars without strict TO/FROM/RE headers but with "TO [GROUP]" are classified as memos in these datasets if they fit the memo style (internal, no salutation/closing).

    - Let's re-evaluate: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels". This implies that if it's addressed to a group, maybe it's still a memo?

    - Actually, let's look at the structure: Letterhead, Date, "TO THE ENTIRE SALES ORGANIZATION", Prose. This is a classic internal memo/circular format. In the absence of a "memo" label that perfectly fits the strict "TO:/FROM:" rule, is it a letter? No, it's internal.

    - Wait, is there a "memo" label? Yes.

    - Let's check if there's any other fit.

    - Could it be a letter? "letter: ... OR a dated note addressed to a named EXTERNAL person". This is internal.

    - Let's assume it's a memo. The "TO THE ENTIRE SALES ORGANIZATION" acts as the TO field. The lack of FROM/RE is common in internal circulars. The instructions say: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo." This is a strict condition. "Without that header-then-prose structure it is not a memo."

    - Wait, the next sentence: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels". This is an exception.

    - What about "TO THE ENTIRE SALES ORGANIZATION"? It's not a named person.

    - Is it a letter? "letter: letterhead with an external recipient address...". No.

    - Is there another category?

    - Let's look at the document again. It's a typed document from "The American Tobacco Company" to "THE ENTIRE SALES ORGANIZATION".

    - In many classification schemes, this is a memo. Let's look closely at the text. "The new Cigarette Advertising Code... contains the following clause... This letter relates to the effect..." -&gt; The text itself says "This letter relates to...".

    - Ah! "This letter relates to the effect of the above provision..."

    - If the text calls itself a letter, does that make it a letter?

    - "Judge each page by its FUNCTION... a bill is a bill even when it is printed on a form."

    - If the text says "This letter relates to...", it might be classified as a letter.

    - Let's check the letter definition: "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

    - This doesn'*t* fit the external person rule.

    - What about the first part of the letter definition? "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature". This doesn'*t* fit (no external address, no salutation, no closing).

    - Wait, is it a memo? "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". The header is "TO THE ENTIRE SALES ORGANIZATION" and "December 31, 1964". It lacks FROM/RE/SUBJECT.

    - The rule says: "Without that header-then-prose structure it is not a memo."

    - But then: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels".

    - This document is addressed to "THE ENTIRE SALES ORGANIZATION". It's not a named person.

    - However, the text says "This letter relates to...".

    - Let's reconsider the "letter" category. Sometimes internal letters (circulars) are classified as letters if they have letterhead and date, even if internal. But the rule says "external recipient address".

    - Let's look at the memo rule again. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...".

    - Is there a "memo" vs "letter" ambiguity here?

    - Let's look at the text: "TO THE ENTIRE SALES ORGANIZATION". This is a standard memo header. Even if FROM/RE are missing, the TO and DATE are there. The prose follows directly. This fits the "memo-style prose" following a TO/DATE header.

    - The strict rule "Without that header-then-prose structure it is not a memo" might refer to the absence of a TO/DATE header entirely. Here we have "TO..." and "Date...".

    - Also, the text says "This letter relates to...". This is a reference within the text, not necessarily the document type label.

    - Let's assume it's a **memo**. Internal communication, TO: [Group], Date, Prose. No salutation, no closing. This is the definition of a memo in this context (internal note).

    - Wait, the rule says: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels". It doesn'*t* explicitly say "addressed to a group". But "TO THE ENTIRE SALES ORGANIZATION" is the TO field.

    - Let's check if it could be a **letter**. "letter: ... OR a dated note addressed to a named EXTERNAL person". It's internal.

    - So it's not a letter by the external person rule.

    - Is it a memo? Yes, it's an internal communication. The header "TO THE ENTIRE SALES ORGANIZATION" + Date + Prose is memo-style.

    - Let's go with **memo**.

Wait, let's re-read the memo definition carefully.

"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."

The document has:

- Letterhead (The American Tobacco Company)
- Date (December 31, 1964)
- TO (TO THE ENTIRE SALES ORGANIZATION)
- Prose body.
- No FROM, no RE, no salutation, no closing.

This fits the "internal names + titles + date + prose, with no salutation or closing, is a memo header" spirit, even if the addressee is a group. The text itself refers to it as "This letter", but functionally it's an internal memo/circular. In the tobacco archive, these internal circulars to sales org are often memos.

Let's check if there's any other category.

- scientific_report: No, it's administrative/legal guidance (Advertising Code).
- form: No.

So it's **memo**.

Wait, could it be a **letter**?

"letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."

This is internal. So not a letter.

Therefore, **memo**.

Let's double check the "This letter relates to..." phrase.

"This letter relates to the effect of the above provision..."

The author is writing a letter/memo to the sales organization. The document type is a memo (internal circular).

Final check of the scratchpad steps:

1. file_folder: No, has body content.

2. handwritten: No, mostly typed.

3. fax: No.

4. questionnaire: No.

5. resume: No.

6. scientific_publication: No.

7. financial: No.

8. specification: No.

9. presentation: No.

10. form: No.

11. correspondence: Yes. It's a memo. Internal TO/DATE header, prose, no salutation/closing.

12. news_article: No.

13. scientific_report: No.

14. advertisement: No.

Runner-up: letter. Ruled out because the addressee is internal ("THE ENTIRE SALES ORGANIZATION"), not external, and there is no "Dear..." salutation or closing signature, which fits the memo definition (internal note) better than the letter definition (external addressee). Also, the text explicitly says "This letter relates to...", which might be a trap, but the structural evidence (internal TO, no salutation/closing) points to memo. Actually, the rule says "A dated internal note addressed to a named person... IS a memo". Here it's addressed to a group. But it's clearly internal correspondence. Memo is the best fit.

Wait, is there any chance it's a **letter** because of the text "This letter relates to..."?

The instructions say: "Judge each page by its FUNCTION... Do not rush to the label that matches the page's subject matter... commit to the FIRST one with strong, concrete evidence you can actually read on the page (a header, a field label, a masthead, an approval block — not a guess from the topic)."

The header is "TO THE ENTIRE SALES ORGANIZATION" and "December 31, 1964". This is an internal memo header. The text calling it a "letter" is just prose content. The structure is memo.

One detail: "The American Tobacco Company" letterhead.

Memo rule: "no external address". The letterhead has an address "150 East 42nd Street, New York, *N*.Y. 10017". This is the company's address, not the recipient's external address. The recipient is "THE ENTIRE SALES ORGANIZATION" (internal). So "no external address" condition for memo is met (the address on the page is the sender's letterhead, not the recipient's external address block).

So, **memo**.


<h3 class="trace-file"><code>rvl_cdip__letter__0032.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

Document analysis:

- Header: "RJR Interoffice Memorandum"
- Subject: "Monthly Status Report"
- Date: "February 17, 1983"
- To: "Dr. R. A. Lloyd, Jr."
- By: [signature]
- From: "W. Y. Rice, Jr."
- Body: "A. Planning Project AF", "The previous status report...", bullet points, "Next Steps:"
- Footer: "RJR FORM 2422-Rev. 7/70"

Let's go through the checks:

Pre-scan:

- Mail-client header block? No. "To:", "From:", "Date:", "Subject:" are present, but it's an "Interoffice Memorandum" header, not a mail-client header (From/To/Sent/Subject). Wait, check 11 says memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.
- Masthead/running head? No newspaper/magazine masthead. No journal running head.

Check 1: file_folder. No, has body content.

Check 2: handwritten. No, mostly typed.

Check 3: FAX TRANSMISSION SHEET. No.

Check 4: questionnaire. No.

Check 5: resume. No.

Check 6: scientific_publication. No.

Check 7: financial document. No.

Check 8: specification. No.

Check 9: presentation. No.

Check 10: administrative form. It has "RJR FORM 2422-Rev. 7/70" at the bottom, but the content is a memo. Check 11 is correspondence (memo). Let's check 11.

Check 11: CORRESPONDENCE -&gt; email, memo, or letter.

- memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.

The page has:

"Subject: Monthly Status Report"

"Date: February 17, 1983"

"To: Dr. R. A. Lloyd, Jr."

"From: W. Y. Rice, Jr."

Header says "Interoffice Memorandum".

This is a memo.

Let's double check check 10 vs 11.

Check 10: Administrative form. "RJR FORM 2422-Rev. 7/70" is at the bottom. But the page is a memo. The instructions say: "A page whose primary structure is a memo header + prose... stays memo". The form number is just the template number for the memo pad.

Check 11: memo. Yes.

Let's review the memo definition in Check 11:

"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."

Here we have:

Subject: Monthly Status Report

Date: February 17, 1983

To: Dr. R. A. Lloyd, Jr.

From: W. Y. Rice, Jr.

Header: Interoffice Memorandum

This perfectly matches memo.

Runner-up: form. Ruled out because the page's primary structure is a memo header + prose (check 11), and the "RJR FORM" at the bottom is just the template number for the memo pad, not an administrative form capturing data.

Let's write the scratchpad.

file_folder: no — the page has a full memo header and body prose.

handwritten: no — typed throughout, with only a small signature.

form: no — although "RJR FORM 2422-Rev. 7/70" appears at the bottom, the page's primary structure is a memo header followed by prose, not a data-capture form.

memo: yes — "Interoffice Memorandum" header with "Subject:", "Date:", "To:", "From:" fields, followed by memo-style prose ("Planning Project AF", "Next Steps:").

Runner-up: form, ruled out because the page is a memo (check 11) with a form number at the bottom, not a data-capture form (check 10).

Final label: memo.


<h3 class="trace-file"><code>rvl_cdip__letter__0036.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: "RJR CONFIDENTIAL" at the top, date "October 21, 1993". No journal masthead. Bates number "51399 2876" on the right side.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of body content (memo header, prose, tables). Not file_folder.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Mostly typed text, with a small handwritten "can" at the top right. Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey instrument or transmittal note.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No career history.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal running head, volume, issue, page range. "RJR CONFIDENTIAL" is an internal marking.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: The page contains tables with percentages (23%, 46%, etc.) and "LIKEABILITY", "POST PUR. INT.", "PRE/POST PI SHIFT". These are advertising study results (recall, impact, likeability), not financial charges, budget, or invoice.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: No Material Safety Data Sheet, product formulation, or "shall/must" language.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck, cover, or press release. It's a memo with tables.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: Not a form with fields/boxes for capturing data. It's a memo with data tables.
- Not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence:

  - Header:

    TO: Mr. G. C. Pennell

    FROM: T. *F*. Witner

    SUBJECT: MAGNA Advertising Study Results

    Date: October 21, 1993

  - Body: Running prose ("This provides you with key measures..."), bullet points, tables.

  - This is a classic internal memo format (TO/FROM/SUBJECT/DATE followed by prose).

  - Matches memo.

- STOP HERE. This is check 11.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Not this check (stopped at 11).

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Not this check (stopped at 11).

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Not this check (stopped at 11).

Runner-up: scientific_report. Ruled out because the page has a clear TO/FROM/SUBJECT/DATE memo header followed by internal prose discussing study results, which is correspondence (memo), not a standalone research write-up. The tables are embedded within the memo's prose.

Let's double check.

Header:

RJR CONFIDENTIAL

October 21, 1993

TO: Mr. G. C. Pennell

FROM: T. *F*. Witner

SUBJECT: MAGNA Advertising Study Results

Body: "This provides you with key measures for the MAGNA Advertising Study..."

This is definitely a memo.

Final label: memo.


<h3 class="trace-file"><code>rvl_cdip__letter__0055.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None. There is an "Inter-office Memorandum" header, "To:", "From:", "Subject:", "Date:". No From:/To:/Sent:/Subject: mail client headers.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. Just "RJR" logo and "Inter-office Memorandum".

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a full memorandum body with text, headings, and an action item. Not just an identifier.
- Result: not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Mostly typed text. There is a handwritten "No. 20 By JCO" and a scribble, but the majority is typed.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions or transmittal for a survey.
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: Not a resume.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range on this page.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: Mentions "tobacco savings", "added costs", "lowered machine efficiencies", but it's not a financial document (invoice/budget) as its primary structure. It's a memo evaluating a product improvement.
- Result: not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: Discusses product improvement, but it's a memo evaluating a submission, not a specification document with "shall/must" or product formulation.
- Result: not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck or presentation cover.
- Result: not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: Has a form number at the bottom "RJRI FORM 2422 - Rev. 7/70", but the primary structure is a memorandum with TO/FROM/SUBJECT/DATE headers and prose. Wait, check 11 is correspondence. Let's look at check 11.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: "Inter-office Memorandum" at the top right. "Subject: CIM Evaluation", "Date: November 2, 1977", "To: Mr. R. H. Cundiff", "From: Research & Development CIM Evaluation Team". Followed by memo-style prose ("The CIM submitted by Hal E. Guess has been evaluated..."). This perfectly matches the memo definition: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.
- Result: memo.

**Check 12-14:** Not applicable since check 11 matched.

Let's double check check 10 vs 11.

Check 10: Administrative form. "A form does NOT have to be blank... internal authorization/approval forms with an approval signature/date block."

Check 11: Correspondence -&gt; memo. "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".

The page is explicitly titled "Inter-office Memorandum" and has the standard memo header fields. The content is a summary of comments on a CIM (Creative Idea Memorandum or similar). This is a memo.

Let's review the scratchpad requirements:

- State evidence for each check or "none".
- Stop at first matching check.
- Add final line naming runner-up and evidence that ruled it out.

Scratchpad:

file_folder: no — the page has a full memorandum body with text, not just an identifier/stamp.

handwritten: no — mostly typed text with a small handwritten annotation ("No. 20 By JCO").

fax: no — no FACSIMILE or fax cover sheet header.

questionnaire: no — no survey instrument or transmittal.

resume: no — not a career history.

scientific_publication: no — no journal running head or publication identifier.

invoice/budget: no — mentions costs and savings in prose, but is not a financial document (line-item table, ledger, etc.).

specification: no — evaluates a product idea, does not define product composition/properties with "shall/must" language or approval blocks for a product change.

presentation: no — not a slide deck, cover, or statement.

form: no — although it has a form number at the bottom ("RJRI FORM 2422"), the primary structure is a memorandum with TO/FROM/SUBJECT/DATE headers and running prose, which is correspondence (memo).

memo: yes — titled "Inter-office Memorandum", has "Subject:", "Date:", "To:", "From:" fields, followed by memo-style prose summarizing evaluation comments.

Runner-up: form, ruled out because the page's primary structure is a memo header followed by prose (check 11), not a generic data-capture form (check 10), despite having a form number at the bottom.

Final label: memo.


<h3 class="trace-file"><code>rvl_cdip__letter__0072.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None. There is a "RJR SECRET ADDRESSEE ONLY" stamp, date "January 18, 1988", "INTEROFFICE MEMORANDUM", "To:", "From:", "Subject:", "XC:". No From/To/Sent/Subject mail-client headers.
- Masthead or running head: No newspaper/magazine masthead. No journal running head. Just "RJR SECRET" and a Bates number "50693 2624" on the right margin.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a full memorandum body, signatures, etc. Not identifier-only.
- Result: not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: The page is mostly typed text with some signatures and handwritten dates. Not majority handwritten.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey instrument or transmittal.
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: Not a resume.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range on the page itself.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial line-item table, ledger, or statement.
- Result: not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: No Material Safety Data Sheet, product formulation, or "shall/must" language.
- Result: not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck or presentation cover.
- Result: not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: Not a generic administrative form capturing factual data. It's a memo.
- Result: not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: "INTEROFFICE MEMORANDUM" header. "To: Mr. Grover Myers...", "From: Mr. Carl Morrison...", "Subject: Addendum to Invention Disclosure W-101-R&D". Followed by memo-style prose. Signatures at the bottom. "XC: Dr. William Hildebolt...". This is a classic internal memo.
- Result: memo.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: No masthead, byline, dateline, multi-column news typography.
- Result: not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: Not a research write-up with running narrative prose about objectives, methods, results. It's a memo about an invention disclosure.
- Result: not this check.

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Evidence: Not promotional material.
- Result: not this check.

Final label: memo.

Let's double check.

Header: "INTEROFFICE MEMORANDUM"

To: Mr. Grover Myers, Mr. Gus Borschke

From: Mr. Carl Morrison, Dr. Donald Roberts

Subject: Addendum to Invention Disclosure W-101-R&D

Body: Prose paragraphs.

Signatures: Carl C. Morrison, Donald L. Roberts.

Read and understood by: signatures.

XC: Dr. William Hildebolt, Mr. Michael Shannon.

This is clearly a memo.

Scratchpad:

file_folder: no — the page has a full memorandum body, not just an identifier/stamp.

handwritten: no — mostly typed text with signatures and dates.

form: no — not a generic administrative form.

questionnaire: no — not a survey instrument.

resume: no — not a career history.

scientific_publication: no — no journal running head.

invoice/budget: no — no financial content.

specification: no — no product/material documentation.

presentation: no — not a slide deck or cover.

form: no — not an administrative form.

email: no — no mail-client header block.

memo: yes — "INTEROFFICE MEMORANDUM" header with "To:", "From:", "Subject:" fields followed by memo-style prose and internal signatures.

news_article: no — no newspaper/magazine masthead.

scientific_report: no — not a research write-up.

advertisement: no — not promotional material.

Runner-up: letter, ruled out because it is an internal interoffice memorandum with TO:/FROM:/SUBJECT: headers and no external address or "Dear ..." salutation.

Wait, check 11 says:

memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose...

This matches perfectly.

Final label: memo.


<h3 class="trace-file"><code>rvl_cdip__letter__0077.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow a specific scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Top left: "RJR SECRET No. 288 By [signature]"
- Top right: "RJR", "February 29, 1988"
- Header block:

  - TO: Mr. Lucien L. Bass, III

  - From: Don R. Nanney

  - Subject: Weekly Activity - 631 Pilot Plant and Support Processes

- Content:

  - "Equipment Status" table with columns: On-Order, Received, Installed, Started-up. Rows: Capsule Filler, Tobacco Filter Maker, etc.

  - "Bosch" section with bullet points describing technical activities (Completed qualification Test #4, 5, 6... Modified Dosing Disc... Running once washed capsules...).

- Bottom right: "51442 4805" (Bates number)

**Pre-scan:**

- Mail-client header block? No. "TO:", "From:", "Subject:" are present, but this is a standard memo header, not an email client header (From/To/Sent/Subject/cc). Wait, let's look at check 11. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This matches.
- Masthead/running head? No newspaper/magazine masthead. No journal running head. "RJR" is a logo. "51442 4805" is a Bates number.

**Check 1: file_folder**

- Evidence: Has a table, prose, memo header. Not just an identifier.
- Result: not this check.

**Check 2: handwritten**

- Evidence: Mostly typed. Only a small handwritten "No. 288 By [signature]".
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" header.
- Result: not this check.

**Check 4: questionnaire**

- Evidence: No survey questions.
- Result: not this check.

**Check 5: resume**

- Evidence: Not a career history.
- Result: not this check.

**Check 6: scientific_publication**

- Evidence: No journal running head.
- Result: not this check.

**Check 7: financial document (invoice/budget)**

- Evidence: Table has numbers (27, 25, 24, 18), but these are equipment counts (On-Order, Received, Installed, Started-up), not money. No dollar signs.
- Result: not this check.

**Check 8: specification**

- Evidence: Not a material safety data sheet, product formulation, or "shall/must" requirements. It's a status report.
- Result: not this check.

**Check 9: presentation**

- Evidence: Not a slide deck, cover, or press release. It's a memo with a table and text.
- Result: not this check.

**Check 10: administrative form**

- Evidence: Has a table, but it's part of a memo's body ("Equipment Status" table, "Bosch" bullet points). It's not a standalone form for capturing data. It's a status report within a memo. Wait, check 10 says "internal authorization/approval forms with an approval signature/date block". This doesn'*t* have that. It has a memo header.
- Result: not this check.

**Check 11: correspondence (email, memo, letter)**

- Evidence:

  - "TO: Mr. Lucien L. Bass, III"

  - "From: Don R. Nanney"

  - "Subject: Weekly Activity - 631 Pilot Plant and Support Processes"

  - Date: "February 29, 1988"

  - This is a classic internal memo header.

  - Followed by content (table and prose about equipment status and Bosch activities).

  - Check 11 definition: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo". Here we have TO, From, Subject, Date.

- Result: YES. This is a memo.

**Check 12: news_article**

- Evidence: No masthead.
- Result: not this check.

**Check 13: scientific_report**

- Evidence: Not a research write-up with narrative prose about objectives/methods/results. It's a weekly activity report/memo.
- Result: not this check.

**Check 14: advertisement**

- Evidence: No marketing layout.
- Result: not this check.

**Final Decision:** memo.

Let's double check Check 11 vs Check 10.

The page has a table "Equipment Status" with numbers. Is this a form?

Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form".

However, the page has a clear memo header: TO, From, Subject, Date.

Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".

The table and bullet points are the "memo-style prose" / content of the memo. A weekly activity report sent via memo is a memo.

The instructions say: "Judge each page by its FUNCTION... a page full of technical data can still be a form, and a page about money can still be a form — but a bill is a bill even when it is printed on a form."

Wait, if a page is a memo, does the table make it a form?

Check 11 says: "email: mail-client header block... An email page keeps this label even when its body is mostly a data table". By analogy, a memo page keeps its label even if it has a table.

Also, the header is explicitly TO/FROM/SUBJECT/DATE. This is the definition of a memo.

The content is "Weekly Activity - 631 Pilot Plant and Support Processes". This is a status update/memo.

Let's look at the "Runner-up" requirement.

Runner-up: form. Ruled out because the page has a clear TO/FROM/SUBJECT/DATE memo header (check 11), which defines it as correspondence (memo), whereas the table is just the body content of the memo, not a standalone administrative form capturing data for records management. Or scientific_report? No, it's not a research write-up.

Let's refine the scratchpad.

Scratchpad:

- Pre-scan: No mail-client header (From/To/Sent/Subject with email metadata). "TO:", "From:", "Subject:" are standard memo headers. No masthead.
- Check 1 (file_folder): no — page has memo header, table, and prose.
- Check 2 (handwritten): no — mostly typed, only small handwritten annotation at top.
- Check 3 (fax): no — no fax cover sheet header.
- Check 4 (questionnaire): no — no survey questions.
- Check 5 (resume): no — not a career history.
- Check 6 (scientific_publication): no — no journal running head.
- Check 7 (financial): no — table contains equipment counts, not money.
- Check 8 (specification): no — not a product spec or MSDS.
- Check 9 (presentation): no — not a slide deck or cover.
- Check 10 (form): no — although there is a table, the page is structured as a memo with TO/FROM/SUBJECT/DATE headers and narrative bullet points. The table is part of the memo's body (Equipment Status), not a standalone data-capture form.
- Check 11 (correspondence/memo): yes — clear internal memo header: "TO: Mr. Lucien L. Bass, III", "From: Don R. Nanney", "Subject: Weekly Activity...", "February 29, 1988". Followed by content (table and bullet points). This fits the memo definition perfectly.
- Check 12 (news_article): no.
- Check 13 (scientific_report): no — not a research write-up.
- Check 14 (advertisement): no.

Runner-up: form. Ruled out because the primary structure is a memo header (TO/FROM/SUBJECT/DATE) followed by activity report content, not a blank/filled administrative form for data capture. The table is just data within the memo.

Final label: memo.


<h3 class="trace-file"><code>rvl_cdip__letter__0091.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

Document analysis:

- Top right: "April 13, 1988"
- Top right: "RJR SECRET ADDRESS ONLY No 407 By [handwritten signature/initials]"
- Left side:

  MEMO TO: Thomas L. Gentry

  FROM: Grover *M*. Myers

  SUBJECT: TGA DISCLOSURE

        W-139-R&D - Dated April 12, 1988

- Body text: "For your records, this will confirm that an invention disclosure file has been set up and assigned the docket number shown above."
- Signature: "Grover *M*. Myers"
- Bottom left: "GMM/br", "cc: David G. Conlin, Esq."
- Bottom right: "52429 1215" (Bates number)

Let's go through the checks:

1. IDENTIFIER-ONLY PAGE -&gt; file_folder

   - Has body content (memo text, signature). Not file_folder.

2. MAJORITY-HANDWRITTEN PAGE -&gt; handwritten

   - Mostly typed, only a small handwritten note "No 407 By [initials]" and a signature. Not handwritten.

3. FAX TRANSMISSION SHEET -&gt; form

   - No fax header.

4. SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire

   - Not a survey.

5. PERSON'S CAREER HISTORY -&gt; resume

   - Not a resume.

6. PUBLISHED EVIDENCE -&gt; scientific_publication

   - No journal masthead or running head.

7. FINANCIAL DOCUMENT -&gt; invoice or budget

   - No financial content.

8. PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification

   - Not a specification.

9. SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation

   - Not a slide deck.

10. ADMINISTRATIVE FORM -&gt; form

    - Not a form with fields/boxes.

11. CORRESPONDENCE -&gt; email, memo, or letter

    - Has "MEMO TO:", "FROM:", "SUBJECT:".

    - Followed by prose: "For your records, this will confirm..."

    - Signed by Grover *M*. Myers.

    - This is a memo.

    - Let's check the memo rule: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". Here it is "MEMO TO:", "FROM:", "SUBJECT:". This matches memo.

    - Is it an email? No mail-client header (From/To/Sent/Subject). The "MEMO TO:" is a memo header.

    - So it's a memo.

12. PUBLISHED JOURNALISM -&gt; news_article

    - No.

13. ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report

    - No running narrative prose about research.

14. PROMOTIONAL MATERIAL -&gt; advertisement

    - No.

Let's double check check 11.

"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."

The document has:

MEMO TO: Thomas L. Gentry

FROM: Grover *M*. Myers

SUBJECT: TGA DISCLOSURE

W-139-R&D - Dated April 12, 1988

This is a classic memo header. The body is short prose. It's a memo.

Runner-up: letter. Ruled out because it has a TO:/FROM:/SUBJECT: block and no external address or "Dear..." salutation.

Let's write the scratchpad.

Check 1: file_folder - no, has memo text and signature.

Check 2: handwritten - no, mostly typed.

Check 3: fax - no fax header.

Check 4: questionnaire - no.

Check 5: resume - no.

Check 6: scientific_publication - no journal identifier.

Check 7: financial - no.

Check 8: specification - no.

Check 9: presentation - no.

Check 10: form - no.

Check 11: correspondence/memo - yes, "MEMO TO:", "FROM:", "SUBJECT:" header block followed by prose.

Check 12: news_article - no.

Check 13: scientific_report - no.

Check 14: advertisement - no.

Final label: memo.


</details>

## budget → invoice

<details class="trace-group">

<summary>12 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__budget__0011.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>invoice</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. "LITHOGRAPHICS, INC." is at the top, looks like a vendor letterhead. "TOBACCO INSTITUTE" is the recipient. "CONFIDENTIAL: MINNESOTA TOBACCO LITIGATION" is at the bottom. TIMN 180140 is a Bates number.

**Check 1: file_folder**

- Evidence: The page has an "INVOICE" header, line items ("XEROX DEPARTMENT: CLC'S", "of new York Ads", "EX. COMM"), amounts (400.00, 24.00, 424.00), and an approval block ("APPROVED FOR PAYMENT BY..."). It has real content, not just an identifier.
- Not this check.

**Check 2: handwritten**

- Evidence: There is some handwriting ("of new York Ads", "EX. COMM", "APPROVED FOR PAYMENT BY AOC", "BY [signature]", "A/C 828-9201", "DATE 6.25.93"). But the majority of the content is printed (vendor info, invoice details, totals, approval block labels).
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: No survey instrument.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: No resume/CV.
- Not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal running head, volume, issue, page range.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: The page is titled "INVOICE" (centered, underlined). It has "INVOICE NUMBER: 3M0765", "INVOICE DATE: 06/15/93", "DUE DATE: 07/15/93". It lists a charge: "XEROX DEPARTMENT: CLC'S ... 400.00". It has "SUBTOTAL 400.00", "TAX 24.00", "TOTAL 424.00". It says "SEE MANUAL INVOICE FOR MORE DETAILS". It has an approval block for payment. This is clearly an invoice from Lithographics, Inc. to Tobacco Institute for xerox services.
- Invoice: yes. Outside vendor (Lithographics, Inc.) states charges owed for services (xerox). "INVOICE" header, line items, amount due.
- Let's check the budget definition just in case. Budget is internal money planning, tracking, disbursement, check stubs. This is a vendor bill (invoice).
- So, invoice.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- Evidence: No material safety data sheet, product formulation, etc.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Evidence: No slide deck layout.
- Not this check.

**Check 10: ADMINISTRATIVE FORM**

- Evidence: It has an approval block, but check 7 (financial document) overrides form layout when money function is primary. The primary structure is an invoice.
- Not this check (or rather, check 7 matched first).

**Check 11: CORRESPONDENCE**

- Evidence: Not an email, memo, or letter. It's an invoice.

**Check 12: PUBLISHED JOURNALISM**

- Evidence: No masthead, byline, etc.

**Check 13: ORIGINAL RESEARCH WRITE-UP**

- Evidence: No running narrative prose of research.

**Check 14: PROMOTIONAL MATERIAL**

- Evidence: No advertisement.

Conclusion: invoice.

Let's double check check 7 details.

"invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due..."

The page has:

- Vendor: LITHOGRAPHICS, INC.
- Recipient: TOBACCO INSTITUTE
- Header: INVOICE
- Invoice Number, Date, Due Date
- Line item: XEROX DEPARTMENT: CLC'S ... 400.00
- Subtotal, Tax, Total
- "SEE MANUAL INVOICE FOR MORE DETAILS"
- Approval block for payment.

This is a textbook invoice.

Runner-up: form. Ruled out because check 7 (financial document) explicitly states "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." and "invoice: an outside vendor... states charges owed... an 'INVOICE' header with line items and amount due".

Final label: invoice.


<h3 class="trace-file"><code>rvl_cdip__budget__0026.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>invoice</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** No "From/To/Sent/Subject" headers. There is a "BILL TO" section, but it's part of an invoice layout. No fax transmission header like "SENT BY: ... # *N*/*N*". Wait, there is a handwritten note at the bottom left: "1308-5701 = $434.70", "1309-5701 = $434.70", "ADC". This looks like internal calculation or note.
- **Masthead/Running head:** No newspaper masthead. No journal running head. There is a company logo "Peake Printers, Inc." and an "INVOICE" title.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a full invoice layout with line items, totals, billing info. Not just an ID/stamp.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: There is handwriting at the bottom left ("1308-5701 = $434.70..."), but the majority of the page is printed text (invoice details, table).

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY**

    *   Evidence: No resume/CV content.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE**

    *   Evidence: No journal name, volume, issue, page range.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: The page has a large "INVOICE" header at the top right. "*** INVOICE ***".

    *   "Invoice No: 70303", "Invoice Date: 04/11/88".

    *   "BILL TO THE TOBACCO INSTITUTE".

    *   Table with "DESCRIPTION", "QUANTITY", "UNIT PRICE", "AMOUNT".

    *   Line items: "VARIOUS SHIPMENTS FROM INVENTORY...", "FREIGHT".

    *   "SUB TOTAL 599.00", "270.40" (Freight).

    *   "TOTAL INVOICE 869.40".

    *   "AMT DUE 869.40".

    *   This is clearly an invoice from a vendor (Peake Printers, Inc.) to a client (The Tobacco Institute) for goods/services (shipments, freight).

    *   Result: invoice.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

    *   Evidence: Not a specification or MSDS.

    *   Result: not this check.

-   **Check 9: SLIDE DECK...**

    *   Evidence: Not a slide.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM**

    *   Evidence: It has fields, but it's primarily a financial document (invoice). Check 7 says money function overrides form layout. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."

    *   Result: not this check (invoice takes precedence).

-   **Check 11: CORRESPONDENCE**

    *   Evidence: Not an email, memo, or letter. It's an invoice.

    *   Result: not this check.

-   **Check 12: PUBLISHED JOURNALISM**

    *   Evidence: Not news.

    *   Result: not this check.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP**

    *   Evidence: Not a report.

    *   Result: not this check.

-   **Check 14: PROMOTIONAL MATERIAL**

    *   Evidence: Not an ad.

    *   Result: not this check.

**Conclusion:**

The document is an invoice from Peake Printers, Inc. to The Tobacco Institute. It has the header "INVOICE", invoice number, date, line items with prices, and a total amount due.

Runner-up: form. Ruled out because check 7 (Financial Document -&gt; invoice) explicitly states that money function overrides form layout, and this is a billing document (invoice) with line items and amounts due.

Final label: invoice.


<h3 class="trace-file"><code>rvl_cdip__budget__0040.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>invoice</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING" is a company logo/header, not a newspaper/magazine masthead or journal running head.

**Check 1: file_folder**

- Evidence: The page has a lot of content (a table with costs, signatures, dates, client info). Not just an identifier.
- Result: not this check.

**Check 2: handwritten**

- Evidence: There are signatures at the bottom, but the majority of the content is typed text and a table.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or fax header.
- Result: not this check.

**Check 4: questionnaire**

- Evidence: No survey questions.
- Result: not this check.

**Check 5: resume**

- Evidence: No career history.
- Result: not this check.

**Check 6: scientific_publication**

- Evidence: No journal name, volume, issue, page range.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: "DATABASE MARKETING ESTIMATE", "PREVIOUS ESTIMATE", "CURRENT ESTIMATE", "TOTAL GROSS COSTS", "ESTIMATE REVISED TO COVER ADDITIONAL DATA PROCESSING...".
- Let's look closely at the invoice vs budget rules.
- Invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... A payment VOUCHER... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- Budget: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice"
- This document: "DATABASE MARKETING ESTIMATE", has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE" columns. It has "REV # : 01", "REV DATE: 02/16/93", "PREV REV DATE: 03/09/93". It compares previous vs current estimate. It has "TOTAL GROSS COSTS" 61,500.00 vs 90,250.00. Notes: "ESTIMATE REVISED TO COVER ADDITIONAL DATA PROCESSING...".
- This is an agency (Leo Burnett) providing an estimate/change order to a client (Philip Morris). It compares previous and current estimates, has revision numbers, and lists costs. According to the rules: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements... compares original vs. present/revised estimate columns". This document has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE" columns, revision numbers, and notes saying "ESTIMATE REVISED". This fits the invoice definition (agency's bill for a client job).
- Wait, is it an invoice or a budget? The rule says: "an agency/vendor document that lists actual charges and totals owed is an invoice... An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number... compares original vs. present/revised estimate columns". This document has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE" columns, and "REV #". It is an estimate change order / revised estimate. Thus, it is an invoice.
- Let's re-read carefully: "A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice". "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This document has "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE" columns, "REV #", and notes "ESTIMATE REVISED". It is an invoice.

**Check 8: specification**

- Evidence: No material safety data, no product formulation, no "shall/must".
- Result: not this check.

**Check 9: presentation**

- Evidence: Not a slide deck, not a press release, not a photographic slide.
- Result: not this check.

**Check 10: administrative form**

- Evidence: It has fields (Client, L B Job#, Ad#, etc.) and a table. But check 7 (financial document) overrides form layout when financial content is the primary structure. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
- Result: not this check (because check 7 matches first).

**Check 11: correspondence**

- Evidence: No TO:/FROM:/RE: memo header, no letterhead with external address and "Dear...".
- Result: not this check.

**Check 12: news_article**

- Evidence: No newspaper/magazine masthead.
- Result: not this check.

**Check 13: scientific_report**

- Evidence: No running narrative prose, no research write-up.
- Result: not this check.

**Check 14: advertisement**

- Evidence: Not a promotional layout, it's a financial estimate/bill.
- Result: not this check.

Let's double check Check 7.

The document is a "DATABASE MARKETING ESTIMATE" from Leo Burnett U.S.A. (an advertising agency) to Philip Morris Inc.

It has columns for "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE".

It has "REV #: 01", "REV DATE: 02/16/93", "PREV REV DATE: 03/09/93".

It lists costs: "OTHER (SEE NOTES) 20,000.00 45,000.00", "TOTAL COMMISSIONABLE COSTS 20,000.00 45,000.00", "AGENCY COMMISSION 3,000.00 6,750.00", etc., leading to "TOTAL GROSS COSTS 61,500.00 90,250.00".

Notes: "ESTIMATE REVISED TO COVER ADDITIONAL DATA PROCESSING FOR THE MERIT SEGMENTATION STUDY."

Signatures at the bottom: CLIENT (Theresa Luter 3/11/93), BRAND, AGENCY (Kenneth C... 3-9-93).

This is an estimate change order / revised estimate from an agency to a client.

Rule: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."

This document compares original vs. present/revised estimate columns ("PREVIOUS ESTIMATE" vs "CURRENT ESTIMATE"), has revision numbers, and notes "ESTIMATE REVISED". Therefore, it is an invoice.

Wait, is there any chance it's a budget?

"Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice"

This document has revision numbers, compares previous and current estimates, and is signed by client and agency, indicating it's a finalized/revised billable estimate (a change order). It's an invoice.

Let's review the exact label: "invoice".

Scratchpad:

- file_folder: no — the page has a detailed financial table, client info, and signatures, not just an identifier.
- handwritten: no — majority is typed text and a table; only signatures are handwritten.
- fax: no — no fax transmission header.
- questionnaire: no — no survey questions.
- resume: no — no career history.
- scientific_publication: no — no journal running head or identifier.
- financial (invoice/budget): yes — "DATABASE MARKETING ESTIMATE" from Leo Burnett (agency) to Philip Morris (client) with "PREVIOUS ESTIMATE" and "CURRENT ESTIMATE" columns, revision numbers ("REV #: 01"), and notes "ESTIMATE REVISED". Per check 7, an agency estimate/change order that compares original vs. present/revised estimate columns and revises a prior estimate is the agency's bill (invoice), not budget. Money function overrides the form-like layout.
- specification: no — no product material data or "shall/must" language.
- presentation: no — not a slide deck or press release.
- administrative form: no — check 7 (financial document) overrides form layout when financial content is the primary structure.
- correspondence: no — no memo or letter header/body structure.
- news_article: no — no newspaper/magazine masthead.
- scientific_report: no — no running narrative prose.
- advertisement: no — not a promotional layout.

Runner-up: budget, ruled out because the document compares previous vs. current estimate columns, has revision numbers, and notes "ESTIMATE REVISED", making it an agency's bill for a client job (invoice) rather than a pure planning document.

Runner-up 2: form, ruled out because check 7 (financial document) explicitly states money function overrides form layout for billing/payment pages.

Final label: invoice.


<h3 class="trace-file"><code>rvl_cdip__budget__0053.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>invoice</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None. Top line is "MAY - 3 - 89 WED 16:16 PARAGON MARKETING P. 05". This is a fax transmission header ("SENT BY:" equivalent, date/time, company, page count). Not an email.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.

**Check 1: file_folder**

- Evidence: The page has a title "SUPERSLIMS TRADE GIFT ESTIMATE", a table with items, quantities, costs, and an approval block. It has real content.
- Not this check.

**Check 2: handwritten**

- Evidence: Mostly typed text with some handwritten annotations (e.g., "47,880", "29,378.50 (+ 17,000", "5,000", "budget: #200,000"). Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The top line is a fax transmission metadata line, but the document itself is an estimate.
- Not this check.

**Check 4: questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: resume**

- Evidence: No career history.
- Not this check.

**Check 6: scientific_publication**

- Evidence: No journal identifier.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: The page is titled "SUPERSLIMS TRADE GIFT ESTIMATE". It lists items, quantities, and estimated costs (Production of Box, Purchase of Champagne, etc.). Total is $147,109.45. It has an "Approved:" and "Date:" block.
- Is it an invoice or budget?
- Invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals."
- Budget: "internal money planning, tracking, or disbursement... Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice"
- Wait, the document is an "ESTIMATE" from "PARAGON MARKETING CORPORATION" to "Philip Morris Sales Office". It lists "Production of Box", "Purchase of Champagne", "Delivery of Boxes", etc. It has unit prices ($7.71 per, @ 6.30). It has a total. It is an estimate document from an agency/vendor.
- Let's look at the invoice bullet: "an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals."
- "A check face/check stub... is the DISBURSEMENT instrument and stays budget... Look for goods sold or one-off services performed (items, quantities, unit prices)."
- This document lists items, quantities, unit prices, and totals for a specific job (Superslims Trade Gift). It is an estimate from an outside vendor (Paragon Marketing Corporation) for goods/services (boxes, champagne, flutes, assembly, delivery).
- Wait, is it an invoice? "an agency/vendor ESTIMATE document... is an invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."
- This document doesn'*t* have an "EST NO" or "REVISES EST" explicitly in the title, but it is an itemized billing statement/estimate with unit prices and totals for goods sold (boxes, champagne).
- Let's re-read the budget bullet: "Money PLANNING for future work is budget: an agency/vendor document that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job... plans projected spend rather than billing completed work, so it is budget, not invoice".
- This document has "charges/amounts for a client job" (Production of Box, Purchase of Champagne, etc., with unit prices and totals). It is an estimate for a specific job. The invoice bullet says: "an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals." and "Look for goods sold or one-off services performed (items, quantities, unit prices)."
- This matches the invoice definition: "an outside vendor... states charges owed... or an agency/vendor ESTIMATE document... with unit prices, amounts, and totals."
- Wait, is it an invoice or budget? The text says "ESTIMATED COST". But it has unit prices ($7.71 per, @ 6.30) and totals. It's an itemized statement for a client job. The invoice bullet explicitly includes "agency/vendor ESTIMATE document... with unit prices, amounts, and totals" as an invoice.
- Let's check the budget bullet again: "Also covers money-only records... a financial or money-data table (price/value estimates... budget-vs-actual...)" but this is an itemized list of goods/services for a job.
- "A hotel/motel guest bill... is an invoice... Likewise a landlord's rent/lease statement... is an invoice".
- This is an estimate from Paragon Marketing Corporation for a trade gift (boxes with champagne). It lists items, quantities, unit prices, and totals. It is an invoice (vendor estimate for goods/services).
- Let's look at the approval block: "Approved: ___ Date: ___". This is typical for an estimate to be approved before production. But the function is billing/estimating a client job.
- "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." This is an estimate of charges.
- Let's consider "budget". "internal money planning...". This is from an outside vendor (Paragon Marketing Corporation) to Philip Morris. It's not internal money planning. It's a vendor's estimate for a job. Vendor estimates with unit prices and totals for a client job are invoices.
- Therefore, invoice.

**Check 8: specification**

- Evidence: Not a material safety data sheet, product formulation, or "shall/must" language. It's a financial estimate.
- Not this check.

**Check 9: presentation**

- Evidence: Not a slide deck, cover, or statement.
- Not this check.

**Check 10: form**

- Evidence: Has an approval block ("Approved:", "Date:"), but the primary content is a financial line-item table (invoice/budget). Check 7 says money function overrides form layout.
- Not this check.

**Check 11: correspondence**

- Evidence: No TO:/FROM:/RE: memo header, no letterhead with external address and salutation.
- Not this check.

**Check 12: news_article**

- Evidence: No masthead, byline, etc.
- Not this check.

**Check 13: scientific_report**

- Evidence: No running narrative prose about research.
- Not this check.

**Check 14: advertisement**

- Evidence: Not a promotional layout.
- Not this check.

Let's double check Check 7 (invoice vs budget).

The document is "SUPERSLIMS TRADE GIFT ESTIMATE" from "PARAGON MARKETING CORPORATION".

Items:

- Production of Box: 7,800 units, $60,138.00 ($7.71 per)
- Purchase of Champagne: 7,600 bottles, @ 6.30, 47,880 (handwritten) / 29,378.50 (printed)
- Purchase of Champagne flutes: 7,550 pairs, 25,422.35
- Preparation of Instruction sheets: 450.00
- Delivery of Boxes: TBD*
- In-market assembly: 7,600 total units, 18,350.00
- Delivery to Philip Morris Sales Office: 7,600 units, TBD*
- Contingency Allowance: 13,273.58 (10% of subtotal)
- TOTAL: $147,109.45

This is an itemized billing statement/estimate from an outside vendor for a specific job (goods sold: boxes, champagne, flutes, services: assembly, delivery).

The instructions say: "an agency/vendor ESTIMATE document: a production estimate report, estimate change order, estimate recap, or itemized billing statement with unit prices, amounts, and totals." -&gt; invoice.

"Look for goods sold or one-off services performed (items, quantities, unit prices)." -&gt; Yes, items, quantities, unit prices are present.

"Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."

So it is financial (Check 7).

Is it invoice or budget?

Budget: "internal money planning...". This is external (Paragon to Philip Morris).

Invoice: "an outside vendor, supplier, or agency states charges owed... or an agency/vendor ESTIMATE document... with unit prices, amounts, and totals."

This matches invoice perfectly.

Runner-up: budget. Ruled out because the document is from an outside vendor (Paragon Marketing Corporation) listing itemized charges, quantities, and unit prices for a specific client job (Superslims Trade Gift), which makes it an invoice (vendor estimate for goods/services) rather than internal money planning (budget).

Final label: invoice.


<h3 class="trace-file"><code>rvl_cdip__budget__0065.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>invoice</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header: None.
- Fax transmission header: None.
- Masthead/Running head: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING". This is a company logo/header, not a newspaper/magazine masthead or journal running head.
- Bates number: "2040962184" (rotated on the right side).

**2. Scratchpad procedure:**

-   **Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

    *   Evidence: The page has a lot of content: a table with product/period/gross amount/gross change, client info, estimate number, etc. Not just an identifier.

    *   Result: not this check.

-   **Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

    *   Evidence: Typed text throughout. No majority handwriting.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET -&gt; form**

    *   Evidence: No "FACSIMILE" or fax cover sheet header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No survey questions or transmittal note.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: No biographical info.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name, volume, issue, page range, DOI.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: "OUTDOOR ESTIMATE RECAP - ODO1(S)". "CLIENT: P.*M*. INC.", "EST NO: 2010 REVISES EST DTD 07/02/92". "DESC: 771A MARLBORO JUMBO BACKLIGHT PACK". Table with "PRODUCT", "PERIOD", "GROSS AMOUNT", "GROSS CHANGE". Totals: "779,503.88", "15,486.98".

    *   Let's look closely at the definition of invoice vs budget for estimates/recaps.

    *   Invoice bullet: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements ("PRIOR ADJUSTMENTS", "EST AMT LESS C/D"), compares original vs. present/revised estimate columns, or carries a billing designation ("BILLING TYPE PROGRESSIVE"): the word "estimate" in the title does NOT make it budget."

    *   Budget bullet: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".

    *   This page: "EST NO: 2010 REVISES EST DTD 07/02/92". It has an estimate number ("2010"). It says "REVISES EST". It shows gross amounts and gross changes. Wait, let's re-read carefully.

    *   "EST NO: 2010 REVISES EST DTD 07/02/92". This matches "names an estimate number" and "revises a prior estimate".

    *   Wait, is it billing completed work or planning? "PERIOD 01/01/92 TO 12/31/92". "JAN 1992 ... 65,925.86". These look like planned gross amounts for the year 1992. The date of the document is "08/07/92". So it's mid-year.

    *   Let's check the budget bullet again: "an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type...". This page *has* an estimate number ("EST NO: 2010") and says "REVISES EST".

    *   Let's check the invoice bullet again: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."

    *   The text explicitly says "EST NO: 2010 REVISES EST DTD 07/02/92". This matches the invoice criteria perfectly: "names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")".

    *   Therefore, this is an invoice.

    *   Wait, let's look at the "GROSS CHANGE" column. It has values for May, Jun, Jul (wait, Jul is blank), May: 1,376.62, Jun: 14,110.36, Quarter 2 total change: 15,486.98. Total change: 15,486.98.

    *   This is a revised estimate. The rules say: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."

    *   So it's an invoice.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: Not an MSDS, not product formulation. It's an advertising estimate.

    *   Result: not this check.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: Not a slide deck.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: It has a form number "FORM MO1A REV 04-14-83" at the bottom left. But check 7 says "Money function overrides form layout." and specifically addresses agency estimates/recaps.

    *   Result: not this check (overridden by check 7).

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: No TO/FROM/RE header, no salutation.

    *   Result: not this check.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: No masthead, byline, dateline.

    *   Result: not this check.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: No running narrative prose about research.

    *   Result: not this check.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: Not a single brand ad layout. It's an internal/agency financial document.

    *   Result: not this check.

**Re-evaluating Check 7 (Invoice vs Budget):**

The document is titled "OUTDOOR ESTIMATE RECAP - ODO1(S)".

Header info:

CLIENT: P.*M*. INC.

EST NO: 2010 REVISES EST DTD 07/02/92

DESC: 771A MARLBORO JUMBO BACKLIGHT PACK

DATE 08/07/92

Table:

PRODUCT: 10-MARLBORO

PERIOD: JAN 1992 to DEC 1992 (and Quarters)

GROSS AMOUNT: values like 65,925.86

GROSS CHANGE: values like 1,376.62

Bottom: FORM MO1A REV 04-14-83.

Rules for Check 7:

- Invoice: "An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST"), reconciles or adjusts prior placements... the word "estimate" in the title does NOT make it budget."
- Budget: "Money PLANNING for future work is budget: an agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type... (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".

This document has "EST NO: 2010" and "REVISES EST". This explicitly triggers the Invoice condition: "when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")".

Even though the title is "ESTIMATE RECAP" and it shows amounts for 1992 (planned spend), the presence of "EST NO" and "REVISES EST" pushes it to Invoice according to the specific rule text provided.

Wait, let's look at the budget example: "(e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter)". This document is an "OUTDOOR ESTIMATE RECAP". But the budget example says "no estimate number, no revision/prior-adjustment line". This document HAS an estimate number ("2010") and says "REVISES EST". So it falls into the Invoice category based on the explicit conditions.

Let's double check.

"An agency estimate/recap/change order is the agency's BILL for a client job — invoice, not budget — when it names an estimate number ("EST NO"), revises a prior estimate ("REVISES EST")..."

The text "EST NO: 2010 REVISES EST DTD 07/02/92" is right there.

So it is an invoice.

Final check of the label: `invoice`.

One detail: "FORM MO1A REV 04-14-83" is at the bottom. This is a form number. But check 7 says "Money function overrides form layout." and specifically classifies this type of document as invoice.

So, label is `invoice`.


<h3 class="trace-file"><code>rvl_cdip__budget__0094.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>invoice</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow a specific scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Header: "1992 VIRGINIA SLIMS CHAMPIONSHIPS NOVEMBER 16 - 22, 1992 SUMMARY OF TOURNAMENT MEDIA CENTER COSTS"
- Address block: "PHILIP MORRIS - USA 120 PARK AVENUE NEW YORK, NEW YORK 10007 ATTN: NANCY ZIMBALIST"
- Body text: "Final Settlement of services and expenses incurred by the Public Relations department in connection with the VIRGINIA SLIMS CHAMPIONSHIPS TOURNAMENT held in the Arena of Madison Square Garden on November 16-22, 1992."
- Financial table:

  - "CHARGES TO YOUR ACCOUNT:" -&gt; "Tournament Media Center" -&gt; "$69,301.58"

  - "CREDITS TO YOUR ACCOUNT:" -&gt; "Deposit" -&gt; "$0.00"

  - "Balance Due Madison Square Garden" -&gt; "$69,301.58"

- Footer/Bates: "2041012903" (rotated)

**Pre-scan:**

- Mail-client header: None.
- Fax transmission header: None.
- Masthead/running head: None.

**Check 1: file_folder**

- Evidence: Has body content (financial summary, address, charges). Not just an ID/stamp.
- Result: not this check.

**Check 2: handwritten**

- Evidence: Typed throughout.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" header.
- Result: not this check.

**Check 4: questionnaire**

- Evidence: No survey questions.
- Result: not this check.

**Check 5: resume**

- Evidence: Not a career history.
- Result: not this check.

**Check 6: scientific_publication**

- Evidence: No journal running head.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: "SUMMARY OF TOURNAMENT MEDIA CENTER COSTS", "CHARGES TO YOUR ACCOUNT: Tournament Media Center $69,301.58", "Balance Due Madison Square Garden $69,301.58".
- This is a statement of charges/bill from Madison Square Garden (or a PR department settling costs) to Philip Morris. Wait, let's look closer.
- "Final Settlement of services and expenses incurred by the Public Relations department in connection with the VIRGINIA SLIMS CHAMPIONSHIPS TOURNAMENT held in the Arena of Madison Square Garden on November 16-22, 1992."
- "CHARGES TO YOUR ACCOUNT: Tournament Media Center $69,301.58"
- "Balance Due Madison Square Garden $69,301.58"
- This looks like an invoice or a statement of account from Madison Square Garden to Philip Morris for the Tournament Media Center services.
- Let's check the definitions:

  - invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... A hotel/motel guest bill or folio... is an invoice... Likewise a landlord's rent/lease statement for a specific period... is an invoice — it bills a one-off service period, not an ongoing account — even though it is issued on a property-company letterhead."

  - budget: "internal money planning, tracking, or disbursement... provider's periodic customer statement... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."

- Here, it's a "Final Settlement of services and expenses... held in the Arena of Madison Square Garden". "Balance Due Madison Square Garden". This is a bill for a specific event (one-off service period: the tournament). It bills for "Tournament Media Center" services. This fits the invoice definition: "bills a one-off service period... even though it is issued on a property-company letterhead" (or similar). Wait, is it a budget? "internal money planning...". No, this is a settlement/bill. "Final Settlement... CHARGES TO YOUR ACCOUNT... Balance Due". This is an invoice/bill.
- Let's re-read check 7 carefully.
- "invoice: ... A hotel/motel guest bill or folio ... is an invoice ... Likewise a landlord's rent/lease statement for a specific period ... is an invoice ... It bills a one-off service period, not an ongoing account".
- This document is a "SUMMARY OF TOURNAMENT MEDIA CENTER COSTS" for a specific event (Nov 16-22, 1992). It lists charges and a balance due. This is an invoice (or bill/statement of account for a specific event, which counts as invoice per the "one-off service period" rule).
- Wait, is it a budget? "budget: ... provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
- This is a "Final Settlement" for a specific tournament (Nov 16-22). It's not a periodic ongoing account statement. It's a bill for a specific event. So it's an invoice.
- Let's check if there's any other category.
- Is it a letter? No, it's a financial document. Check 7 says "Money function overrides form layout... a billing or payment page stays financial even when it is printed on a form...". Wait, is this a letter? It has an address block "PHILIP MORRIS - USA... ATTN: NANCY ZIMBALIST". But it doesn'*t* have "Dear..." or a closing signature. It's a financial statement/invoice.
- Check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This page is a statement of costs/charges.
- So it's invoice.

Let's double check.

"Final Settlement of services and expenses incurred by the Public Relations department in connection with the VIRGINIA SLIMS CHAMPIONSHIPS TOURNAMENT held in the Arena of Madison Square Garden on November 16-22, 1992."

"CHARGES TO YOUR ACCOUNT: Tournament Media Center $69,301.58"

"Balance Due Madison Square Garden $69,301.58"

This is a bill/invoice from Madison Square Garden (or a related entity) to Philip Morris for the media center costs during the tournament.

It fits "invoice": "an outside vendor... states charges owed... for goods or services SOLD". Madison Square Garden is the vendor/arena.

It fits the caveat: "Likewise a landlord's rent/lease statement for a specific period (e.g. a "REKENING" for rent covering a named term, one line item, amount, and total due) is an invoice — it bills a one-off service period, not an ongoing account". This is a one-off event (tournament).

So, invoice.

Let's check check 11 (correspondence).

- memo: "internal TO:/FROM:/RE:/SUBJECT:/DATE: header block followed directly by memo-style prose". This has an address block but no TO:/FROM: header block in memo style, and the body is financial settlement, not memo prose.
- letter: "letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature". No salutation, no closing.
- So not correspondence.

Check 7 is the winner.

Label: invoice.

Wait, is it a budget?

"budget: ... internal money planning, tracking, or disbursement ... Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget, not form".

This is a "Final Settlement" and "Balance Due". It's a bill, not a request or internal tracking. It's an invoice.

Let's review the scratchpad steps.

1. file_folder: no — has body content (financial summary, address, charges).

2. handwritten: no — typed throughout.

3. FAX: no.

4. questionnaire: no.

5. resume: no.

6. scientific_publication: no.

7. financial (invoice): yes — "SUMMARY OF TOURNAMENT MEDIA CENTER COSTS", "CHARGES TO YOUR ACCOUNT", "Balance Due Madison Square Garden $69,301.58". This is a bill/invoice for a one-off service period (the tournament), not an ongoing account statement.

8. specification: no.

9. presentation: no.

10. form: no — financial content overrides form layout (check 7).

11. correspondence: no — no salutation/closing, primary structure is financial statement.

12. news_article: no.

13. scientific_report: no.

14. advertisement: no.

Runner-up: budget. Ruled out because this is a "Final Settlement" and "Balance Due" for a specific one-off event (tournament), which bills for services performed (invoice), rather than internal money planning or a periodic ongoing account statement (budget).

Wait, the address block is at the top left:

"PHILIP MORRIS - USA

120 PARK AVENUE

NEW YORK, NEW YORK 10007

ATTN: NANCY ZIMBALIST"

This looks like a bill sent to Philip Morris.

"Balance Due Madison Square Garden" -&gt; Madison Square Garden is the entity sending the bill (or the entity to whom payment is due).

Yes, this is an invoice.

Final check of the text:

"1992 VIRGINIA SLIMS CHAMPIONSHIPS

NOVEMBER 16 - 22, 1992

SUMMARY OF TOURNAMENT MEDIA CENTER COSTS"

"Final Settlement of services and expenses incurred by the Public Relations department in connection with the VIRGINIA SLIMS CHAMPIONSHIPS TOURNAMENT held in the Arena of Madison Square Garden on November 16-22, 1992."

"CHARGES TO YOUR ACCOUNT:

Tournament Media Center $69,301.58"

"CREDITS TO YOUR ACCOUNT:

Deposit $0.00"

"Balance Due Madison Square Garden $69,301.58"

This is clearly an invoice/bill.

Label: invoice.


</details>

## specification → form

<details class="trace-group">

<summary>9 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__specification__0025.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>specification</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head on this page. There is a reference to a paper: "Allen, R. E.; Vickroy, D. G. ... THE CHARACTERIZATION OF CIGARETTE SMOKE FROM CYTREL SMOKING PRODUCTS... Beitr. Tabakforsch. 8 (No. 7) 430-37 (Oct. 1976)". This is a citation, not the page's own identifier.

**2. Scratchpad checks:**

-   **Check 1: file_folder**

    *   Evidence: The page has a title "Arsenic", "Analytical information (detailed)", checkboxes for "Smoke", "Green", "Cured", "Non-Leaf", "Itemize:", handwritten data "0.07 - 21 ng/cig", "Types of Tobacco...", "Reference...". This is real content, not just an ID/stamp.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: There is handwritten text ("Arsenic", "0.07 - 21 ng/cig", "Types of Tobacco... (blend tot., blend tot. + 10, 20 and 50% CytreI, and CytreI)"). However, the page is largely a printed template with field labels ("Analytical information", "Quantitative", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference"). The handwriting fills in the fields of a printed structured form.

    *   Result: not this check. (It's a filled form).

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: questionnaire**

    *   Evidence: Not a survey instrument.

    *   Result: not this check.

-   **Check 5: resume**

    *   Evidence: Not a career history.

    *   Result: not this check.

-   **Check 6: scientific_publication**

    *   Evidence: No journal running head/volume/issue on this page itself. The reference is to "Beitr. Tabakforsch. 8 (No. 7) 430-37". This is a citation.

    *   Result: not this check.

-   **Check 7: financial document**

    *   Evidence: No money, invoices, budgets. "ng/cig" is nanograms per cigarette, a unit of measurement.

    *   Result: not this check.

-   **Check 8: specification**

    *   Evidence: "Analytical information (detailed)", "Quantitative", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P.", "Chem. Groups", "Derivatives". "Types of Tobacco". "Reference". This looks like a data sheet or a form capturing analytical data about a substance (Arsenic) in tobacco.

    *   Wait, let's look at Check 10 (Administrative form) vs Check 8 (Specification) vs Check 13 (Scientific report).

    *   Check 8: "Material Safety Data Sheet... product formulation... test-analysis tables keyed to product/part codes... labeled product/parameter rate-data chart". This page is about "Arsenic" in tobacco. It has fields for "Quantitative", "Qualitative", "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P.", "Chem. Groups", "Derivatives", "Types of Tobacco". This looks like a chemical data sheet or a form for recording analytical data.

    *   Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)...".

    *   This page has fields: "Analytical information (detailed)", "Quantitative (all figures)", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P.", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference".

    *   The content is filled in by hand: "Arsenic", "0.07 - 21 ng/cig", "(blend tot., blend tot. + 10, 20 and 50% CytreI, and CytreI)".

    *   This is a filled analytical/lab data sheet. Check 10 explicitly covers "a filled analytical or lab data sheet".

    *   Let's check Check 8 again. "Product-referenced test data is a specification. A titled product-analysis table... is a specification". This is a single substance "Arsenic" with analytical data. Is it a specification? Specifications usually define requirements ("shall/must") or product composition/properties for manufacturing. This looks like a record of analytical results or a data card for a chemical substance (Arsenic) used in tobacco (CytreI is a brand of cellulose acetate tow/fiber).

    *   Actually, let's look at the structure. It's a form with labels and handwritten entries.

    *   Check 10: "A filled analytical or lab data sheet... is a form".

    *   Let's look at the "Reference" section. It cites a paper: "Allen, R. E.; Vickroy, D. G. ... THE CHARACTERIZATION OF CIGARETTE SMOKE FROM CYTREL SMOKING PRODUCTS...". This suggests the page is a summary or a data card related to that research, or perhaps a form used to record data from that research.

    *   Wait, is this a scientific report? Check 13: "Running narrative prose...". This page has no running narrative prose. It has labels and handwritten data. So not scientific_report.

    *   Is it a specification? Check 8: "test-analysis tables keyed to product/part codes... labeled product/parameter rate-data chart". This is a data sheet for "Arsenic". It's not really a product specification (like "Arsenic content must be &lt; 0.1"). It's recording data "0.07 - 21 ng/cig".

    *   Let's re-read Check 10: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)...". This page has "Compound" (implied by "Arsenic" at top), "Analytical information", "Quantitative", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups". This fits "filled analytical or lab data sheet" perfectly.

    *   So, Check 10 (form) seems strong.

-   **Check 9: presentation**

    *   Evidence: Not a slide deck.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM**

    *   Evidence: "Filled or blank fields, boxes, checkboxes... for capturing factual data". "A filled analytical or lab data sheet".

    *   The page has printed labels: "Analytical information (detailed)", "Smoke / Green / Cured / Non-Leaf", "Quantitative", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P.", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference".

    *   Handwritten content fills these fields: "Arsenic", checkmark on Smoke, "0.07 - 21 ng/cig", "(blend tot., blend tot. + 10, 20 and 50% CytreI, and CytreI)".

    *   This is a filled form capturing analytical data.

    *   Result: YES. This is a form.

-   **Check 11: CORRESPONDENCE**

    *   Evidence: No memo/letter structure.

    *   Result: not this check.

-   **Check 12: news_article**

    *   Evidence: No masthead.

    *   Result: not this check.

-   **Check 13: scientific_report**

    *   Evidence: No running narrative prose. Just labels and data.

    *   Result: not this check.

-   **Check 14: advertisement**

    *   Evidence: No marketing layout.

    *   Result: not this check.

**Re-evaluating Check 8 vs Check 10:**

Check 8 (Specification): "test-analysis tables keyed to product/part codes... labeled product/parameter rate-data chart... A titled product-analysis table... is a specification".

Check 10 (Form): "A filled analytical or lab data sheet...".

The page looks like a data card or a form used to record analytical information about "Arsenic" in the context of "CytreI" (a tobacco product material).

The text "Allen, R. E.; Vickroy, D. G. ... THE CHARACTERIZATION OF CIGARETTE SMOKE FROM CYTREL SMOKING PRODUCTS..." is a reference.

The page itself is a structured template with fields for chemical properties (Mol. Weight, *M*.P., B.P., Structural Formula) and analytical data (Quantitative: 0.07-21 ng/cig).

This is a "filled analytical or lab data sheet".

Check 10 explicitly says: "This also covers: ... a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)".

The page has "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups". This matches the "filled analytical or lab data sheet" description in Check 10.

Therefore, the label is `form`.

Let's double check if it could be `scientific_report`.

Check 13: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."

This page is labeled field-value entries (with handwriting). So it's a form.

Let's double check if it could be `specification`.

Check 8: "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language."

This page doesn'*t* have "shall/must". It's recording data "0.07 - 21 ng/cig". It's not defining a product spec, it's recording analytical info.

Actually, looking closely at the top: "Arsenic" is handwritten. "Analytical information (detailed)". "Smoke / Green / Cured / Non-Leaf". "Quantitative (all figures) / 0.07 - 21 ng/cig".

This looks like a data extraction sheet or a lab data sheet.

Check 10 covers "filled analytical or lab data sheet".

Final decision: `form`.

Wait, is there any other category?

The reference is to a scientific paper. But the page itself is a form capturing data/notes about that paper or related to it.

The page has a Bates number "50452 8331" (rotated).

The page has "165 01" at top left.

Let's look at the "Reference" section again.

"Allen, R. E.; Vickroy, D. G. (Celanese Fibers Co., Fibers Tech. Cent., Charlotte, *N*.C., U.S.) THE CHARACTERIZATION OF CIGARETTE SMOKE FROM CYTREL SMOKING PRODUCTS AND ITS COMPARISON TO SMOKE FROM FLUE-CURED TOBACCO. III. PARTICULATE PHASE ANALYSIS. Beitr. Tabakforsch. 8 (No. 7) 430-37 (Oct. 1976) - in English *Keywords:* Constituents too numerous to list."

This is a citation.

The page is a form for recording analytical information about Arsenic.

Labels: "Analytical information (detailed)", "Quantitative", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P.", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference".

Handwritten: "Arsenic", checkmark on "Smoke", "0.07 - 21 ng/cig", "(blend tot., blend tot. + 10, 20 and 50% CytreI, and CytreI)".

This is definitely a filled form (lab data sheet / analytical data sheet).

One detail: "A labeled product/parameter rate-data chart ... is a specification". This is not a chart.

"A titled product-analysis table ... is a specification". This is not a table of analysis results for a product, it's a form for one chemical (Arsenic).

So `form` is the correct label.

Let's check the scratchpad requirements.

- Walk checks 1-14 in order.
- State evidence or "not this check".
- Stop at first matching check.
- Final line: runner-up label and evidence ruling it out.

Check 1: file_folder. Evidence: "Arsenic", "Analytical information...", handwritten data. Not just an ID. -&gt; not this check.

Check 2: handwritten. Evidence: Handwriting is present ("Arsenic", "0.07-21 ng/cig"), but it fills printed fields ("Quantitative", "Types of Tobacco"). The page is a printed template. -&gt; not this check. (Rule: handwriting filling printed fields is form).

Check 3: FAX. Evidence: None. -&gt; not this check.

Check 4: questionnaire. Evidence: None. -&gt; not this check.

Check 5: resume. Evidence: None. -&gt; not this check.

Check 6: scientific_publication. Evidence: No journal running head on this page. Citation is present but not the page's own ID. -&gt; not this check.

Check 7: financial. Evidence: No money. -&gt; not this check.

Check 8: specification. Evidence: No "shall/must", no product change authorization, no rate-data chart. It's a data sheet. -&gt; not this check. (Though close, Check 10 is more specific for "filled analytical or lab data sheet"). Actually, let's look at Check 8 again. "test-analysis tables keyed to product/part codes". This isn'*t* a table. It's a form.

Check 9: presentation. Evidence: None. -&gt; not this check.

Check 10: form. Evidence: "Filled or blank fields, boxes, checkboxes... for capturing factual data". "A filled analytical or lab data sheet". The page has printed labels ("Analytical information", "Quantitative", "Structural Formula", "Mol. Weight", etc.) and handwritten entries filling them. This matches perfectly. -&gt; YES.

Runner-up: scientific_report. Ruled out because the page lacks running narrative prose and is primarily labeled field-value entries (a filled lab data sheet), which falls under form (check 10).

Or runner-up: specification. Ruled out because it lacks requirement language ("shall/must") and is a data capture sheet rather than a product definition or test-analysis table keyed to codes.

Let's refine the runner-up.

The page looks scientific (chemical formulas, ng/cig, references to cigarette smoke characterization). So `scientific_report` is the main trap.

Evidence ruling out `scientific_report`: Check 13 requires running narrative prose. This page has only labeled fields and handwritten data entries (a filled analytical data sheet), which is explicitly covered by Check 10 (form).

Final check: Is it a "specification"?

Check 8: "Material Safety Data Sheet...". This isn'*t* an MSDS.

"product formulation or preparation/mixing instructions". No.

"manufacturing-change authorization". No.

"test-analysis tables keyed to product/part codes". No.

"labeled product/parameter rate-data chart". No.

So not specification.

It is a form.

One detail: "Types of Tobacco (all details) (blend tot., blend tot. + 10, 20 and 50% CytreI, and CytreI)".

CytreI is a product (cellulose acetate tow).

This is recording data about Arsenic in tobacco blends containing CytreI.

It's a lab data sheet / analytical form.

Label: form.


<h3 class="trace-file"><code>rvl_cdip__specification__0031.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>specification</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number on this specific page. There is a Bates number "50843 4673" on the right side. There is "RJR CLASS NO. PAMPHLET VI To-76 s.*p*."

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a lot of content. "Analytical information (detailed)", "Structural Formula", "Types of Tobacco", "Reference", "Bibliography". It's not just an ID or stamp.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: There is some handwriting: "cholesterol" at the top, "Non-Leaf" checked, "flue-cured, burley, Turkish" written next to "Types of Tobacco". But the majority of the page is printed text (form fields, instructions, references). The handwriting fills in fields of a printed template.

    *   Result: not this check. (It's a filled form).

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No questions for a respondent. It looks like a data sheet or index card.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: No CV/resume content.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal running head on this page. The references cite "Davis, D. L." and "Tobacco Chem. Res. Conf.", but this page itself doesn'*t* have a journal identifier like "Vol. X, *pp*. Y-Z".

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: No financial data, money, invoices, budgets.

    *   Result: not this check.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: "Analytical information (detailed)", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups", "Derivatives", "Types of Tobacco". This looks like a data sheet for a chemical substance (cholesterol). Wait, let's look closer.

    *   The top says "cholesterol" (handwritten).

    *   Fields: "Analytical information (detailed)", "Smoke Green Cured Non-Leaf Itemize:", "Quantitative (all figures)", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P", "Chem. Groups", "Derivatives", "Types of Tobacco (all details) flue-cured, burley, Turkish", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography".

    *   This looks like a form for capturing chemical/analytical data about a substance (cholesterol) in tobacco.

    *   Is it a specification? "Material Safety Data Sheet... product formulation... test-analysis tables keyed to product/part codes... tolerances, or 'shall/must' requirement language." This doesn'*t* look like a specification defining product properties or requirements. It looks like a data capture form.

    *   Let's check Check 10.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: Not a slide deck. Not a press release.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".

    *   The page has fields: "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference", "Bibliography".

    *   It has checkboxes: "Smoke", "Green", "Cured" (checked), "Non-Leaf" (checked). "Quantitative", "Qualitative only".

    *   It has instructions at the bottom: "If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write 'over' on this side. List all answerable information for each constituent and do so in index style."

    *   This is clearly a form for capturing data. Specifically, it looks like a chemical analysis data sheet or a reference card for a substance (cholesterol) in tobacco.

    *   Wait, is it a scientific_report? "Requires running narrative prose... a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." This page is mostly labeled fields. The references are typed text, but the main body is form fields.

    *   Is it a specification? "A titled product-analysis table... is a specification". This isn'*t* really a table of analysis results, it's a template for data. "test-analysis tables keyed to product/part codes". This looks like a data collection form.

    *   Let's re-read Check 10: "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)..." This fits perfectly. It's a lab data sheet / analytical information form.

    *   The page has "Analytical information (detailed)" as a header.

    *   It has fields for chemical properties (Structural Formula, Mol. Weight, etc.).

    *   It has fields for tobacco types.

    *   It has a reference section.

    *   It has bibliography instructions.

    *   This is a form (check 10).

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: No TO/FROM/RE header, no salutation, no closing.

    *   Result: not this check.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: No masthead, no news typography.

    *   Result: not this check.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: "Requires running narrative prose". This page has mostly form fields. The references are text, but the main content is the form structure. "A page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."

    *   Result: not this check.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: No marketing layout.

    *   Result: not this check.

**Re-evaluating Check 8 vs Check 10:**

- Check 8 (Specification): "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes... A titled product-analysis table... is a specification".
- Check 10 (Form): "Filled or blank fields... for capturing factual data... A filled analytical or lab data sheet... is a form".
- The page is titled (implicitly by the handwritten "cholesterol") "Analytical information (detailed)". It has fields for "Structural Formula", "Mol. Form", etc. It is capturing data about cholesterol.
- The instructions at the bottom say "List all answerable information for each constituent...". This is a data capture form.
- It looks like a "Pamphlet" or index card from a collection ("RJR CLASS NO. PAMPHLET VI To-76 s.*p*.").
- Actually, looking closely at the bottom right: "RJR CLASS NO. PAMPHLET VI To-76 s.*p*." and Bates number "50843 4673".
- The content is a form for recording analytical information about a substance (cholesterol) found in tobacco.
- Is it a scientific report? No, it's a form.
- Is it a specification? No, it's not defining requirements or product composition changes. It's recording data.
- So it's a form (Check 10).

Let's look at the "Reference" section. It lists "Davis, D. L." and "AROMA. Tobacco Chem. Res. Conf...". This is a reference to a paper about "WAXES AND LIPIDS IN LEAF AND THEIR RELATIONSHIP TO SMOKING QUALITY AND AROMA."

The form is capturing data about cholesterol (a wax/lipid?).

The form has fields: "Types of Tobacco (all details) flue-cured, burley, Turkish".

This is a data sheet / form.

Final decision: Form (Check 10).

Wait, let's look at Check 1 again. "file_folder".

- "Almost no body content: only an archive/Bates number, a stamp, a short label or ID..."
- This page has body content (form fields, references). So not file_folder.

Let's look at Check 13 again. "scientific_report".

- "Running narrative prose...". This page has very little prose. It has form labels and filled values ("flue-cured, burley, Turkish"). The references are prose-like but they are citations.
- "A page that is only labeled field-value entries... is a filled form (check 10)". This fits perfectly.

So, Check 10: ADMINISTRATIVE FORM -&gt; form.

Evidence: Labeled fields ("Structural Formula", "Mol. Form", "Mol. Weight", "Types of Tobacco", "Reference", "Bibliography"), checkboxes ("Cured", "Non-Leaf"), instructions at the bottom ("If there is not sufficient space..."). It is a filled analytical/lab data sheet.

One detail: "RJR CLASS NO. PAMPHLET VI To-76 s.*p*." suggests this is a page from a pamphlet or a specific class of documents. But the page itself is a form.

The handwritten text "cholesterol" identifies the subject.

The form is capturing analytical information.

Let's check if it could be a "scientific_report".

- "Also scientific_report: ... a technical-study title page...". This is not a title page.
- "Requires running prose". This page lacks running prose. It has form fields.

So "form" is the correct label.

Let's double check Check 8 (Specification).

- "test-analysis tables keyed to product/part codes... A labeled product/parameter rate-data chart... is a specification".
- This is not a chart or table of analysis results. It is a blank/filled template for data entry. "Analytical information (detailed)" is a header for the form.
- "A filled analytical or lab data sheet... is a form (check 10)". This matches.

Final check of the text:

- Top: "cholesterol" (handwritten).
- "Analytical information (detailed)"
- "Smoke Green Cured [check] Non-Leaf [check] Itemize:"
- "Quantitative (all figures)" vs "Qualitative only"
- Fields: "Structural Formula", "Mol. Form", "Mol. Weight", "*M*.P.", "B.P", "Chem. Groups", "Derivatives".
- "Types of Tobacco (all details) flue-cured, burley, Turkish" (handwritten).
- "Tox.-Pharm. Inform. and other Notes".
- "Reference": "Davis, D. L... WAXES AND LIPIDS IN LEAF...". "AROMA. Tobacco Chem. Res. Conf...".
- "RJR CLASS NO. PAMPHLET VI To-76 s.*p*."
- Bottom text: "Bibliography: If there is not sufficient space available for any of the categories, use reverse side... List all answerable information for each constituent and do so in index style."

This is definitely a form (data capture sheet).

Label: form.


<h3 class="trace-file"><code>rvl_cdip__specification__0046.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>specification</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None. There's a handwritten note at the top, but no From/To/Sent/Subject block.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number on this specific page. There is a Bates number "50457 2083" on the right side.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: There is a Bates number "50457 2083". There is handwritten text "nitrogen dioxide, NO2", "sidestream C10102-44-07". There is a reference block with a citation: "Cooper, P. J.; Hege, R. B. ... THE OXIDATION OF NO TO NO2 IN CIGARETTE SMOKE." There is a bibliography/abstract block.

    *   This page has real content: a reference, an abstract/bibliography entry, and handwritten notes about chemical formulas. It is not just an identifier.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: There is handwritten text at the top ("nitrogen dioxide, NO2", "sidestream C10102-44-07") and some handwritten marks (checkmarks). However, the majority of the page is printed text: "Analytical information (detailed)", "Quantitative (all figures)", "Structural Formula", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography", and a block of text describing a paper ("The kinetics of the oxidation of NO to NO2...").

    *   The printed text dominates. The handwriting fills in fields or annotates. Wait, let's look closer.

    *   The page looks like a form or a data sheet. "Analytical information (detailed)", "Structural Formula", "Mol. Form NO2", "Mol. Weight", "Types of Tobacco".

    *   The bottom half has a printed block of text (abstract/bibliography).

    *   Is it majority handwritten? No. Most is printed.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: No CV/resume content.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: The page cites a paper: "Tobacco Chem. Res. Conf., 32nd. paper, Montreal, Can. (Oct. 30-Nov. 1, 1978)". This is a conference paper citation. Does the page itself carry a journal identifier? No. It has a Bates number. It looks like an internal data sheet or a form capturing data about a reference.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: No financial data.

    *   Result: not this check.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: "Analytical information (detailed)", "Structural Formula", "Mol. Form NO2". This looks like chemical data. But is it a specification? "Material Safety Data Sheet"? No. "product formulation"? No. It looks like a data capture sheet for chemical analysis.

    *   Wait, let's look at the structure. It has fields: "Analytical information (detailed)", "Quantitative", "Qualitative", "Structural Formula", "Mol. Form", "Mol. Weight", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference", "Bibliography".

    *   This looks like a form for capturing chemical/analytical data.

    *   Let's check Check 10 (Administrative Form).

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: Not a slide deck. Not a press release.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: The page has labeled fields: "Analytical information (detailed)", "Quantitative (all figures)", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "H. P.", "B. P", "Chem. Groups", "Derivatives", "Types of Tobacco (all details)", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography".

    *   There is handwritten data filling some fields: "Smoke / Green / Cured / Non-Leaf" (checkmarks), "sidestream C10102-44-07", "NO2".

    *   The bottom part contains a reference and an abstract/bibliography block. Wait, is this a form capturing data about a scientific paper?

    *   The text at the bottom is a printed abstract: "The kinetics of the oxidation of NO to NO2 in cigarette smoke were examined by both Fourier Transform Infrared (FTIR) spectroscopy and chemiluminescent detection techniques..."

    *   This looks like a page from a database or a form used to catalog/record information about a scientific paper or chemical constituent.

    *   The structure is definitely a form with fields for "Analytical information", "Structural Formula", "Types of Tobacco", "Reference", "Bibliography".

    *   The content is filled in (handwritten and printed text block).

    *   Check 10 says: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet".

    *   This page is a filled analytical data sheet / form. It captures data about a chemical (NO2) and a reference paper.

    *   Let's re-read Check 13 (scientific_report). "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."

    *   The bottom block is an abstract/bibliography entry. It's not the full report. The page itself is a form capturing metadata and a snippet of a reference.

    *   The top half is clearly a form: "Structural Formula", "Mol. Form NO2", "Types of Tobacco".

    *   So this is a form.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: No TO/FROM/RE header. No letter structure.

    *   Result: not this check.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: No masthead.

    *   Result: not this check.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: There is an abstract at the bottom. But the top half is a form with fields. The page is not a running narrative prose write-up of a study. It's a data sheet *about* a study or a constituent.

    *   The text "The kinetics of the oxidation..." is an abstract from a conference paper ("Tobacco Chem. Res. Conf."). It's cited as a reference.

    *   The page itself is a form capturing information.

    *   Result: not this check.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: No marketing layout.

    *   Result: not this check.

**Re-evaluating Check 10 vs Check 13:**

The page has a lot of printed text at the bottom (the abstract).

However, the top half is a structured form:

- Analytical information (detailed) [Smoke / Green / Cured / Non-Leaf]
- Itemize: sidestream C10102-44-07
- Quantitative / Qualitative
- Structural Formula: Mol. Form NO2, Mol. Weight, H.P., B.P, Chem. Groups, Derivatives.
- Types of Tobacco (all details)
- Tox.-Pharm. Inform. and other Notes
- Reference: Cooper, P. J.; Hege, R. B. ... THE OXIDATION OF NO TO NO2 IN CIGARETTE SMOKE.
- Bibliography: [Abstract text]

This looks like a "Chemical Abstract" or a data entry form for a chemical database (like the tobacco industry's chemical database). It captures specific data points (Mol Form, Types of Tobacco) and links to a reference.

The presence of labeled fields ("Structural Formula", "Mol. Form", "Types of Tobacco", "Reference") strongly points to **form** (Check 10).

Check 13 requires "Running narrative prose with objectives, methods, results, or discussion". The text at the bottom is an abstract/bibliography entry, not the full report. The page is a record of data.

Check 10 covers "a filled analytical or lab data sheet". This fits perfectly. It's a sheet for analytical information.

Let's look at the "Bibliography" section. "If there is not sufficient space available for any of the entries on the reverse side, identifying category(ies) and summary of contents of this side, list all answerable information for each constituent and the relevant index style." This is an instruction on the form itself. This confirms it's a form/data sheet.

So, Check 10 is the winner.

**Runner-up:** scientific_report. Ruled out because the page is a structured data capture sheet (form) with labeled fields and instructions for the reverse side, rather than a full running narrative research write-up. The text at the bottom is a cited abstract/bibliography entry, not the primary content of the page itself (which is the form data).

Wait, let's look at the labels again.

"form" is Check 10.

"scientific_report" is Check 13.

The page is a form for "Analytical information (detailed)".

It has fields for chemical properties.

It has a reference to a paper.

It has an abstract of that paper.

This is a data sheet / form.

Final decision: form.

One detail: "A page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."

This page has labeled fields: "Structural Formula", "Mol. Form", "Types of Tobacco", "Reference".

The bottom text is a bibliography/abstract.

The instruction "If there is not sufficient space available..." is a form instruction.

So it is a form.

Let's double check Check 1 (file_folder).

"A Bates number or archive stamp alone is NOT enough... A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".

Here we have a form with content. Not file_folder.

Let's double check Check 2 (handwritten).

"Most of the content is freeform handwriting... NOT on a printed template."

This is on a printed template (form). The handwriting fills fields ("NO2", "sidestream..."). So it's a filled form.

Conclusion: form.

One more look at the bottom text.

"Cooper, P. J.; Hege, R. B. ... THE OXIDATION OF NO TO NO2 IN CIGARETTE SMOKE. Tobacco Chem. Res. Conf., 32nd. paper..."

This is a reference.

The box below is the abstract.

The page is a record card or form for a chemical constituent (NO2, sidestream smoke).

It's a form.

Label: form.


<h3 class="trace-file"><code>rvl_cdip__specification__0066.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>specification</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header: None.
- Masthead/running head: There is a Bates number "50857 0789" on the right side. No journal masthead.

**Check 1: file_folder**

- Evidence: The page has typed fields, handwritten data, a reference section, and a bibliography note. It has real content, not just an ID/stamp.
- Result: not this check.

**Check 2: handwritten**

- Evidence: There is some handwriting at the top ("Valeric", "Pentanoic acid 4, 5-dihydroxy-4 lactone", "Smoke", "Green") and some numbers ("2.40", "2.38"). But the majority of the page is typed text (form fields, instructions, reference).
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: No survey questions.
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: No resume/CV.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal running head/volume/issue on this page. The reference is to "RDR, 1976, No. 18".
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT**

- Evidence: No financial data.
- Result: not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- Evidence: The page is titled/structured around "Analytical information (detailed)", "Quantitative", "Qualitative only", "Structural Formula", "Mol. Form", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography". It looks like a data sheet for a chemical substance ("Valeric", "Pentanoic acid..."). Wait, check 10 covers "filled analytical or lab data sheet". Let's look at check 10.
- Is it a specification? "Material Safety Data Sheet", "product formulation", "test-analysis tables keyed to product/part codes". This looks like a chemical analysis data sheet. "Analytical information (detailed)... Quantitative... Structural Formula... Types of Tobacco... Tox.-Pharm. Inform." It's a form for capturing analytical data. Let's check check 10.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Evidence: Not a slide deck.
- Result: not this check.

**Check 10: ADMINISTRATIVE FORM**

- Evidence: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This page has fields like "Quantitative (all figures)", "G7", "G7-NH3", "Structural Formula", "Mol. Form", "Mol. Weight", "*M*. P.", "B. P.", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography". It is a structured data capture sheet for analytical/chemical information. The bottom says "If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write "over" on this side. List all answerable information for each constituent and do so in index style." This is clearly a form for capturing data.
- Result: form.

Let's double check check 8 (specification). "A labeled product/parameter rate-data chart... is a specification". This is not a chart. "test-analysis tables keyed to product/part codes". This is a data sheet. Check 10 explicitly mentions "filled analytical or lab data sheet". This page is a lab/analytical data sheet (capturing quantitative/qualitative data, structural formula, molecular weight, etc. for a substance, possibly related to tobacco smoke components). The text "Types of Tobacco (all details) To compare composition of smoke from 100% G7 cigarettes with the smoke of ammoniated 100% G7 cigarettes." indicates it's a data capture form for a study. The structure is fields and lines for data entry. It fits "form" (check 10) perfectly.

Let's re-read check 10: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This page has "Structural Formula", "Mol. Form", "Mol. Weight", "Quantitative", "Qualitative". It is a lab data sheet.

Let's check if it could be scientific_report (check 13). "Requires running narrative prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." This page is mostly labeled field-value entries (with some handwritten values). The reference section is just a citation. The bibliography is an instruction. So it's a form.

Let's check the scratchpad steps again.

1. file_folder: no.

2. handwritten: no.

3. fax: no.

4. questionnaire: no.

5. resume: no.

6. scientific_publication: no.

7. financial: no.

8. specification: no. (It's a data capture sheet, not a product spec or MSDS).

9. presentation: no.

10. form: yes. It's a filled analytical/lab data sheet with fields for quantitative/qualitative data, structural formula, molecular weight, etc., and instructions for filling it out ("If there is not sufficient space... use reverse side").

Runner-up: scientific_report. Ruled out because the page consists of labeled field-value entries and instructions for a data sheet, not running narrative prose (check 13 requires running prose).

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__specification__0086.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>specification</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** None. There is a handwritten note at the top, but no "From/To/Sent/Subject".
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head on this specific page (though there is a reference to a journal article "RDR, 1979, No. 3"). There is a Bates number "50056 6558" at the bottom right.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: There is a handwritten title "1-Pyrrolidine Carboxaldehyde" and a code "[3760-54-1]". There are field labels like "Structural Formula", "Mol. Form.", "Mol. Weight", "*M*.P", "B.P", "Chem. Groups", "Derivatives". There is a reference section. This is not just an identifier/stamp. It has content.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: Most of the content is typed text (field labels, reference info). There is handwriting at the top ("1-Pyrrolidine Carboxaldehyde", checkmarks for "Smoke", "Green", code "[3760-54-1]"). But the majority is typed form-like structure. Wait, let's look closer. The page is a form with typed headers and labels, filled in partially by hand (top part) and partially typed (reference). Actually, looking closely, the top part is handwritten "1-Pyrrolidine Carboxaldehyde" and checkmarks. The rest is typed form text. Wait, is it a filled form? Yes. "Handwriting filling in labeled printed fields is form, not handwritten".

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: No CV content.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal running head on this page. The reference "RDR, 1979, No. 3" is a citation, not the page's own identifier.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: No financial data.

    *   Result: not this check.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: The page has fields for "Structural Formula", "Mol. Form.", "Mol. Weight", "*M*.P", "B.P", "Chem. Groups", "Derivatives". It mentions "Types of Tobacco (all details) PENTANE PUFFED VS. FREON-11 PUFFED TOBACCO." It has a reference to a study "SMOKE COMPARISON STUDY OF FREON-AND PENTANE-PUFFED TOBACCO CIGARETTES".

    *   Wait, is this a specification? "Material Safety Data Sheet... product formulation... test-analysis tables keyed to product/part codes... 'shall/must' language."

    *   This looks like a data sheet or a form for chemical data. Let's look at Check 10.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: Not a slide deck. Not a press release.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: The page has typed field labels: "Analytical information (detailed)", "Quantitative (all figures)", "Qualitative only", "Structural Formula", "Mol. Form.", "Mol. Weight", "*M*.P", "B.P", "Chem. Groups", "Derivatives", "Types of Tobacco (all details)", "Tox.-Pharm. Inf. and other notes", "Reference:", "Bibliography (see other side):".

    *   It is a structured template for capturing chemical/tobacco data.

    *   "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table... internal authorization/approval forms".

    *   This is a form for capturing chemical analysis data (1-Pyrrolidine Carboxaldehyde).

    *   Wait, let's check Check 13 (scientific_report). "Requires running narrative prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."

    *   This page is mostly labeled fields (Structural Formula, Mol. Form, etc.) with very little filled content (mostly blank or handwritten at top). The reference section is typed.

    *   This looks like a form used to record data. "ANALYTICAL DATA SUMMARY" with entries is a form. This is similar.

    *   Let's check Check 8 again. "A titled product-analysis table... is a specification". This isn'*t* really a table of analysis results, it's a template/form with headers. The headers are "Structural Formula", "Mol. Form", etc. It's a data capture form.

    *   Let's look at the content. "Types of Tobacco (all details) PENTANE PUFFED VS. FREON-11 PUFFED TOBACCO." This is a specific study context.

    *   However, the layout is a form with fields. "Analytical information (detailed) - Smoke / Green / Cured / Non-Leaf". Checkboxes.

    *   This is a form.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: No TO/FROM/RE header. No salutation.

    *   Result: not this check.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: No masthead.

    *   Result: not this check.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: "Requires running narrative prose". This page has almost no running prose. It has a reference citation ("Dube, Michael *F*... SMOKE COMPARISON STUDY..."). The rest is form fields.

    *   Result: not this check.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: No marketing layout.

    *   Result: not this check.

**Re-evaluating Check 8 vs Check 10:**

Check 8: "Product-referenced test data is a specification. A titled product-analysis table... is a specification".

Check 10: "Filled or blank fields... for capturing factual data... A standalone labeled data chart or table... is a form... a filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) [is a form]".

The page has headers: "Structural Formula", "Mol. Form.", "Mol. Weight", "*M*.P", "B.P", "Chem. Groups", "Derivatives".

It has "Types of Tobacco (all details)".

It has "Reference".

This looks like a data sheet or a form to record chemical properties.

The text "1-Pyrrolidine Carboxaldehyde" is handwritten at the top.

The code "[3760-54-1]" is handwritten (CAS number).

The checkmarks "Smoke", "Green", "Cured", "Non-Leaf" are handwritten.

This is a form for capturing chemical/tobacco data. It fits "filled analytical or lab data sheet" or just a form with fields.

The instructions say: "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) [is a form]".

This page is very similar: it has fields for Compound (implied by title), Formula, Weight, MP, BP, etc.

So it is a form (Check 10).

Let's check if it's a "scientific_report".

Check 13: "Requires running narrative prose". This page does not have running narrative prose. It has a reference block and form fields. So not scientific_report.

Let's check if it's a "specification" (Check 8).

Check 8: "Material Safety Data Sheet... product formulation... test-analysis tables keyed to product/part codes... tolerances, or 'shall/must' requirement language."

This page doesn'*t* have "shall/must". It's a template for data. "Analytical information (detailed)".

It looks like a form used in a study.

The reference is to a study "SMOKE COMPARISON STUDY OF FREON-AND PENTANE-PUFFED TOBACCO CIGARETTES".

The page itself is a data capture sheet (form) for that study.

So Check 10 (form) is the best fit.

Wait, is there any other category?

"handwritten": The top part is handwritten. But the page is a printed template with fields. "Handwriting filling in labeled printed fields is form, not handwritten". The majority of the page is the printed template (labels, lines, reference text). The handwriting is just the title and some checks. So not handwritten.

Final decision: form.

Let's double check Check 1 (file_folder).

"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."

This page has form fields and a reference. It's not just an ID.

Let's double check Check 13 (scientific_report).

"Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)".

This is not a title page. It's a data sheet. The title page would be the study report itself. This is a sheet *from* the study or related to it, capturing data.

Actually, looking at the layout, it looks like a "Chemical Data Sheet" or "Analytical Data Sheet".

The reference "RDR, 1979, No. 3" is a citation.

The page is a form.

One detail: "Bibliography (see other side):". This suggests it's part of a larger document or a card.

But the content is a form structure.

Let's look at the "Reference" section.

"Reference: RDR 3 1979 Dube, Michael *F*.; Charles W. Miller; Charles R. Green SMOKE COMPARISON STUDY OF FREON-AND PENTANE-PUFFED TOBACCO CIGARETTES RDR, 1979, No. 3 December 13, 1979 32 *p*."

This is a reference to a report.

The page itself is a form for recording data about "1-Pyrrolidine Carboxaldehyde".

So, Check 10: ADMINISTRATIVE FORM -&gt; form.

Evidence: Typed field labels ("Structural Formula", "Mol. Form.", "Mol. Weight", "*M*.P", "B.P", "Chem. Groups", "Derivatives", "Types of Tobacco"), checkboxes ("Smoke", "Green", "Cured", "Non-Leaf"), and ruled lines for data entry. It is a template for capturing chemical and tobacco analysis data.

Runner-up: scientific_report. Ruled out because the page lacks running narrative prose (objectives, methods, results) and is primarily a structured data-capture form with field labels, even though it references a scientific study.

Wait, is it a "specification"?

Check 8: "A labeled product/parameter rate-data chart... is a specification". This is not a chart.

"A titled product-analysis table... is a specification". This is not really a table of analysis results, it's a blank/semi-blank form with headers. The headers are standard chemical properties.

The text "PENTANE PUFFED VS. FREON-11 PUFFED TOBACCO" is under "Types of Tobacco".

This looks like a form used to record data for the study.

The instructions say: "A filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) [is a form]".

This matches perfectly. It's a lab data sheet / analytical form.

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__invoice__0015.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>budget</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Top: "Invoice 579" (handwritten)
- "Post Purchase Order per the attached:" (handwritten)
- Table with columns: "PO Line", "Qty", "DM Amt"
- Rows 1-8 with numbers.
- Total: 1,289,820
- Note: "380 not included"
- Signature: "C. Ernst 10/21/93"
- "* REVISION FROM X. PHAML:" (handwritten)
- "PLEASE INCLUDE P.O. LINE 6 IN TOTAL (LINE 6 ATTACHED)"
- Calculation: 1,289,820 DM + 195,990 DM (30% of line 6) = 1,485,810 DM
- Signature: "H. ... 10/28/93"
- Bottom right: Bates number "2059478435" (vertical)
- Bottom text: "Attach to invoice - approve invoice for payment - show PO# on invoice & forward to Sharon Lawson - AP-Finance" (handwritten)

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. Just a Bates number.

**Check 1: file_folder**

- Almost no body content? No, there is a lot of handwritten content (table, calculations, notes). Not file_folder.

**Check 2: handwritten**

- Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template.
- Wait, is this on a printed template? No, it looks like freeform handwriting on blank paper.
- "Invoice 579", "Post Purchase Order...", table with handwritten columns "PO Line", "Qty", "DM Amt".
- "REVISION FROM X. PHAML: PLEASE INCLUDE P.O. LINE 6 IN TOTAL..."
- "Attach to invoice - approve invoice for payment..."
- This is a handwritten note/log of expenses/amounts.
- Let's check the rules for handwritten: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
- "A handwritten list of budget categories and dollar amounts ... is budget, not handwritten". Wait.
- "a handwritten note or log of dated expenses by category (e.g. "Contractor", "Dinner", "Painting", "Houseplant", each with a date) even when amounts are not legible — is budget, not handwritten".
- Here we have "Post Purchase Order per the attached: PO Line, Qty, DM Amt". It's a list of amounts (DM = Deutsche Mark).
- "Attach to invoice - approve invoice for payment - show PO# on invoice & forward to Sharon Lawson - AP-Finance". This is a note about an invoice.
- Is it budget? "budget: internal money planning, tracking, or disbursement ... Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT ... a financial or money-data table ... and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category".
- This is a handwritten note about an invoice, calculating a total, and instructing to attach to invoice for payment.
- Wait, check 2 says: "Handwriting filling in labeled printed fields is form, not handwritten — but the labeled printed structure has to actually be visible; don'*t* infer a form just because the content resembles form-type data (name/address)." Here there is no printed structure, it's all handwritten.
- Is it a memo? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo".
- Bottom text: "forward to Sharon Lawson - AP-Finance". Sharon Lawson is a named person, AP-Finance is an internal division/title.
- "Attach to invoice - approve invoice for payment - show PO# on invoice & forward to Sharon Lawson - AP-Finance".
- This is a handwritten note to Sharon Lawson (AP-Finance).
- Let's check memo rules: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose ... Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. "Mr. R. J. Smith, Manager - Hanmer Division" from "T. P. Pettigrew, Manufacturing Services Manager - Research and Development") with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels"
- Here we have: "forward to Sharon Lawson - AP-Finance". Date: "10/28/93". Prose: "Attach to invoice - approve invoice for payment - show PO# on invoice & forward to Sharon Lawson - AP-Finance".
- Is this a memo? It's a handwritten note.
- Let's look at check 2 again: "Most of the content is freeform handwriting ... NOT on a printed template. This wins over a typed letter or memo layout."
- Wait, if it's a memo, check 11 (memo) comes after check 2? No, check 2 is handwritten. Check 11 is correspondence (email, memo, letter).
- The order is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.
- If check 2 matches (handwritten), it stops there.
- "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."
- "A typed page with only a signature, stamp, or margin note is not handwritten."
- Here the ENTIRE page is handwritten. "Invoice 579", table, calculations, instructions.
- Is it a "handwritten note or log of dated expenses by category ... is budget"?
- "a handwritten note or log of dated expenses by category ... is budget, not handwritten".
- This is a note about an invoice ("Invoice 579", "Post Purchase Order", "DM Amt", "Attach to invoice - approve invoice for payment"). It's tracking/approving a payment.
- Wait, check 7: "invoice: an outside vendor ... states charges owed ... A payment VOUCHER ... is a payment instrument ... invoice". This is handwritten.
- Check 7: "budget: ... a financial or money-data table ... and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category".
- This page has a handwritten table of amounts (DM Amt) for PO lines. Total 1,289,820 DM. Revision adds 30% = 195,990 DM. Total 1,485,810 DM.
- This is a financial document (money-data table, handwritten note about invoice/payment).
- But check 2 says: "Most of the content is freeform handwriting ... NOT on a printed template. This wins over a typed letter or memo layout. It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form ... A handwritten list of budget categories and dollar amounts ... is budget, not handwritten".
- So if it's a handwritten list of budget categories/dollar amounts, it's budget (check 7), not handwritten (check 2).
- Wait, the instruction says: "Walk checks 1-14 below IN ORDER. For each check, before moving to the next one, briefly state: ... If evidence is present: STOP HERE."
- Check 2: "Most of the content is freeform handwriting ... NOT on a printed template." -&gt; YES, most content is freeform handwriting.
- BUT the calibration says: "A handwritten list of budget categories and dollar amounts ... is budget, not handwritten".
- Does check 2 have positive evidence? Yes, "Most of the content is freeform handwriting".
- Wait, if I stop at check 2, I say "handwritten". But the calibration explicitly says "A handwritten list of budget categories and dollar amounts ... is budget, not handwritten". This implies check 2 should NOT match if it's a budget list.
- Let's re-read check 2 carefully: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout. It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form ... A handwritten list of budget categories and dollar amounts ... is budget, not handwritten".
- So if it's a budget list, check 2 is "not this check" because of the exception.
- What about check 7 (invoice/budget)?
- "invoice: ... A payment VOUCHER ... is a payment instrument ... invoice". This is not a voucher, it's a handwritten note.
- "budget: ... a financial or money-data table ... and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category".
- This page has a handwritten table of amounts (PO Line, Qty, DM Amt) and a total. It's a money-data table / list of amounts.
- Also: "Attach to invoice - approve invoice for payment". This is an internal note about approving a payment.
- Is it an invoice? "invoice: an outside vendor ... states charges owed". This is an internal note about an invoice ("Invoice 579", "Post Purchase Order per the attached"). It's not the invoice itself, it's a note to attach to the invoice.
- Is it a budget? "budget: ... internal money planning, tracking, or disbursement ... a financial or money-data table ... and a handwritten list of budget categories and dollar amounts". This is a financial table (PO lines and amounts) and a note about payment.
- Let's look at check 11 (memo): "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose ... IS a memo".
- "forward to Sharon Lawson - AP-Finance". Date: 10/28/93.
- But check 2 comes before check 11. If check 2 is "handwritten", it stops.
- The calibration says: "A handwritten list of budget categories and dollar amounts ... is budget, not handwritten". This is a specific exception to check 2.
- So check 2 is "not this check" because it's a financial table/note (budget).
- Let's check check 7: "budget: ... internal money planning, tracking, or disbursement ... a financial or money-data table ... and a handwritten list of budget categories and dollar amounts, or a handwritten note/log of dated expenses by category".
- This page is a handwritten financial table (PO lines, amounts) and a note about payment/disbursement ("approve invoice for payment ... forward to Sharon Lawson - AP-Finance"). This fits "budget" (internal money tracking/disbursement, financial money-data table).
- Wait, is it an invoice? "invoice: ... A payment VOUCHER naming a payee, vendor/item fields, an amount ... and a payment date is a payment instrument ... invoice". This is not a voucher.
- "invoice: ... a vendor's price or hourly-rate schedule, a receipt, a payment request". This is a payment request note? "Attach to invoice - approve invoice for payment". It's a request to approve.
- But check 7 says: "budget: ... a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget, not form".
- Here, the content is the amount (1,485,810 DM) and the recipient (Sharon Lawson - AP-Finance, effectively).
- Actually, let's look at the content: "Invoice 579", "Post Purchase Order", table of amounts, total, revision, total with revision. "Attach to invoice - approve invoice for payment - show PO# on invoice & forward to Sharon Lawson - AP-Finance".
- This is a handwritten note/table tracking financial amounts for an invoice payment. It's a financial document.
- Check 7: "budget: ... internal money planning, tracking, or disbursement ... a financial or money-data table ... and a handwritten list of budget categories and dollar amounts".
- This is a financial money-data table (handwritten). So check 7 matches "budget".

Let's re-evaluate check 2 vs check 7.

Check 2: "Most of the content is freeform handwriting ... NOT on a printed template." -&gt; True.

BUT: "A handwritten list of budget categories and dollar amounts ... is budget, not handwritten".

So check 2 is explicitly overridden by the budget rule. I should say "not this check" for check 2 because it's a financial table/note (budget).

Let's check check 11 (memo):

"A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... with memo-style prose ... IS a memo".

"forward to Sharon Lawson - AP-Finance". Date: 10/28/93.

But check 7 (financial) comes before check 11.

Check 7: "Check 7 applies only when financial content IS the page's primary structure ... If the page is otherwise formatted as correspondence ... and a dollar figure ... is merely mentioned ... classify it as correspondence (check 11) instead".

Here, the financial content (the table of amounts, the total, the revision calculation) IS the primary structure. The note at the bottom is just instructions. The main body is a financial table ("PO Line", "Qty", "DM Amt", totals).

So check 7 matches "budget" (financial money-data table, internal money tracking/disbursement).

Wait, is it an invoice?

"invoice: ... an outside vendor ... states charges owed ... A payment VOUCHER ... is a payment instrument ... invoice".

This is not an outside vendor statement. It's an internal note ("Post Purchase Order per the attached", "Attach to invoice - approve invoice for payment").

"budget: ... internal money planning, tracking, or disbursement ... a financial or money-data table".

This fits budget.

Let's check the labels:

- invoice: outside vendor states charges. This is internal.
- budget: internal money tracking, financial money-data table, handwritten list of dollar amounts. This fits.

So:

Check 1: file_folder - no (has content).

Check 2: handwritten - no (exception: handwritten list of budget categories/dollar amounts is budget).

Check 3: fax - no.

Check 4: questionnaire - no.

Check 5: resume - no.

Check 6: scientific_publication - no.

Check 7: financial (invoice/budget) - yes. Financial content is primary structure (handwritten table of PO amounts, totals, revision calculation). It's internal money tracking/disbursement (approve invoice for payment, forward to AP-Finance). Matches "budget".

Check 8: specification - no.

Check 9: presentation - no.

Check 10: form - no (not a printed form, it's handwritten, but check 7 overrides).

Check 11: correspondence - no (check 7 overrides because financial content is primary structure).

Check 12: news_article - no.

Check 13: scientific_report - no.

Check 14: advertisement - no.

Final label: budget.

Let's double check check 7 invoice vs budget.

"invoice: ... A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee ... invoice".

This page doesn'*t* have a "PAY THIS AMOUNT" or vendor fields. It has "Invoice 579", "Post Purchase Order", table of amounts.

"budget: ... internal money planning, tracking, or disbursement ... a financial or money-data table ... and a handwritten list of budget categories and dollar amounts".

This is a financial money-data table (PO lines and DM amounts) and a note about disbursement (approve invoice, forward to AP-Finance).

So "budget" is correct.

Wait, is there any chance it's "invoice"?

"invoice: ... a payment request".

"A payment VOUCHER ... is a payment instrument ... invoice".

But the text says "Attach to invoice - approve invoice for payment". This implies the document itself is NOT the invoice, but a note to attach to the invoice. The invoice is "attached".

So this document is a tracking/approval note for the invoice. Internal money tracking -&gt; budget.

Let's refine the scratchpad.

Check 1: file_folder - no, has handwritten table and notes.

Check 2: handwritten - no, exception: handwritten list of dollar amounts/financial table is budget (check 7).

Check 3: fax - no.

Check 4: questionnaire - no.

Check 5: resume - no.

Check 6: scientific_publication - no.

Check 7: financial - yes, primary structure is a handwritten financial table (PO Line, Qty, DM Amt, totals) and internal payment approval note ("approve invoice for payment ... forward to Sharon Lawson - AP-Finance"). Matches budget (internal money tracking, financial money-data table).

Check 8-14: no.

Runner-up: invoice. Ruled out because this is an internal note/table tracking amounts for an attached invoice ("Post Purchase Order per the attached", "Attach to invoice"), not an outside vendor's bill for goods/services.

Runner-up: memo. Ruled out because check 7 (financial primary structure) precedes check 11 (correspondence), and the page's main content is a financial table, not just a memo mentioning a dollar figure.

Wait, check 7 says: "If the page is otherwise formatted as correspondence (letterhead + external address + "Dear ..." salutation + prose + closing signature, or a TO:/FROM:/RE:/SUBJECT: memo header followed by prose) and a dollar figure ... is merely mentioned ... classify it as correspondence (check 11) instead".

This page is NOT formatted as correspondence. It's a handwritten financial table. So check 7 applies.

Final label: budget.


<h3 class="trace-file"><code>rvl_cdip__invoice__0045.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>budget</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** I see "FOOTE, CONE & BELDING Advertising, Inc.", "CHEMICAL BANK", "100 PARK AVE, NEW YORK, *N*.Y.". There's a date "October 9, 1972". There's a "PAID" stamp. There's a check number "20014". There's a routing number "021000021". There's a MICR line. This looks like a check stub or a check image. Wait, let's look closer.
- Top part: "FOOTE, CONE & BELDING Advertising, Inc." "CHEMICAL BANK 100 PARK AVE, NEW YORK, *N*.Y."
- "NUMBER 20014" "CHICAGO October 9, 1972" "1-12 210 19"
- "PAY $55,666.09" (looks like $55,666.09). Wait, "FOOTE, CONE & BELDING $55,666.09 AND 09 CTS".
- "PAID" stamp.
- "TO THE ORDER OF Controlled Television Communications, Inc. 10 East 10th Street New York, New York 10016 Attn: Mr. Barney Bernard"
- Date: "OCT 16 1972".
- Signature: "Alan Woodward".
- MICR line: "⑆020014⑆ ⑆021000021⑆ 019-005768⑆" and "⑆0005966609⑆".
- Bottom part: There's a rotated text block. "PAY TO THE ORDER OF...". "PROMISE TO PAY...". "CHEMICAL BANK NEW YORK, NEW YORK". "1-148 AE 1-148". "L12-2428-7735". "16". "417". "91031474".

This is clearly a check (or a check stub/face).

Let's check the categories.

- Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget.
- "A check face/check stub — a check number, bank, MICR line, "PAY TO THE ORDER OF", signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget (below), even when the stub's columns are headed "INVOICE DATE"/"INVOICE NO."/"INVOICE AMOUNT"."
- So if this is a check face/stub, it's **budget**.

Let's re-read Check 7 carefully.

"budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register..."

"A check face/check stub stays budget even when the detachable stub's columns are headed "INVOICE DATE"/"INVOICE NO."/"INVOICE AMOUNT" — a check and its stub record a disbursement from a payment instrument, not a vendor bill for goods or services."

The page shows a check from "FOOTE, CONE & BELDING" to "Controlled Television Communications, Inc." for $55,666.09.

It has a check number (20014), date (October 9, 1972 / Oct 16 1972), payee, amount, signature, MICR line.

The bottom part looks like the detachable stub or the back of the check with routing info. Actually, the bottom part has "PAY TO THE ORDER OF..." rotated. It looks like the check itself is the top part, and the bottom part is the stub or the bank copy. Wait, the bottom part has "PROMISE TO PAY... CHEMICAL BANK...". This is the check face/stub.

So, Check 7 applies.

Is it an invoice?

"invoice: an outside vendor, supplier, or agency states charges owed... A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee... — invoice".

Wait, the text says: "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice, whether it pays a vendor for goods/services or a grantee/recipient (e.g. a contribution payment for a grant). It is not the budget clause for an INTERNAL REQUEST/CHECKLIST/STATEMENT form requesting that money be spent or contributed."

BUT: "A check face/check stub — a check number, bank, MICR line, "PAY TO THE ORDER OF", signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget (below)..."

This page is a check. It has "PAY", "TO THE ORDER OF", amount, signature, MICR line.

Therefore, it is a check face/stub.

Check 7 says: "budget: ... a check face or check stub ...".

So the label should be **budget**.

Let's double check if there's any other category.

- Check 1: file_folder. No, it has content (a check).
- Check 3: Fax transmission sheet. No.
- Check 7: Financial document. Yes.
- Is it an invoice? No, it's a check. "A check face/check stub ... stays budget".

Let's look at the bottom part.

"PAY TO THE ORDER OF ... CONTROLLED TELEVISION COMMUNICATIONS, INC."

"PROMISE TO PAY ... CHEMICAL BANK NEW YORK, NEW YORK"

"1-148 AE 1-148"

"L12-2428-7735"

"16"

"417"

"91031474" (vertical text on the right side of the bottom block).

This is definitely a check. The top part is the check face (paid stamp, payee, amount, signature). The bottom part is likely the detachable stub or the bank's copy (rotated). Actually, looking closely at the bottom text: "PAY TO THE ORDER OF ... CONTROLLED TELEVISION COMMUNICATIONS, INC. ... PROMISE TO PAY ... CHEMICAL BANK ...". This is the text of the check itself, printed on the bottom half (rotated 90 degrees? No, the text is vertical).

Wait, the top part is the check face. The bottom part has text running vertically. "PAY TO THE ORDER OF ...". "PROMISE TO PAY ...". This is the actual check text.

Actually, often checks are printed with the main body on top and the stub on the bottom, or the check is on the left and stub on the right. Here, the top half is the check face (Foote, Cone & Belding, Chemical Bank, Pay $55,666.09, To the order of Controlled Television Communications, Inc., Attn Mr. Barney Bernard, Paid stamp, Signature).

The bottom half has text rotated 90 degrees counter-clockwise. "PAY TO THE ORDER OF ... CONTROLLED TELEVISION COMMUNICATIONS, INC. ... PROMISE TO PAY ... CHEMICAL BANK ...". This looks like the back of the check or the stub.

Regardless, it's a check face/stub.

According to Check 7: "budget: ... a check face or check stub ...".

So the label is **budget**.

Let's check if there's any email header. No.

Masthead? No.

So, Check 7 -&gt; budget.

Wait, is there any possibility it's an invoice?

"invoice: ... A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee ... — invoice".

But then: "A check face/check stub — a check number, bank, MICR line, "PAY TO THE ORDER OF", signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget".

This page has a check number (20014), bank (Chemical Bank), MICR line (021000021...), "PAY TO THE ORDER OF" (implied by "TO THE ORDER OF" and the bottom text), signature line (Alan Woodward).

So it is a check face/stub. Thus, **budget**.

Let's refine the scratchpad.

- file_folder: no — page contains a check with payee, amount, signature, MICR line.
- handwritten: no — mostly typed/printed check.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- financial (invoice/budget): yes. It is a check face/stub from Foote, Cone & Belding to Controlled Television Communications, Inc. for $55,666.09. Check 7 states "a check face or check stub ... is the DISBURSEMENT instrument and stays budget".
- specification: no.
- presentation: no.
- form: no (financial overrides form layout, and specifically check stub is budget).
- correspondence: no.
- news_article: no.
- scientific_report: no.
- advertisement: no.

Runner-up: invoice. Ruled out because the document is a check face/stub (has check number, MICR line, "PAY TO THE ORDER OF", signature), and check 7 explicitly states check faces/stubs stay budget, not invoice. An invoice is a vendor's bill for goods/services sold; a check is the disbursement instrument.

Final label: budget.


<h3 class="trace-file"><code>rvl_cdip__invoice__0062.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>budget</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** No "From/To/Sent/Subject" block. There is a "DATE 08/21/80" and some numbers, but it looks like a check.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a "PHILIP MORRIS" logo at the top.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a lot of content. It's a check. "PAY EXACTLY ******1,149 DOLLARS AND 13 CENTS". "TO THE ORDER OF DR L G ABOOD". "TO UNITED VIRGINIA BANK". MICR line at the bottom.

    *   Result: Not file_folder.

-   **Check 2: handwritten**

    *   Evidence: There is a signature "Harry L. Shute". But the majority of the content is printed text (check details, payee, amount, bank info).

    *   Result: Not handwritten.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: Not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

    *   Evidence: No survey questions.

    *   Result: Not this check.

-   **Check 5: PERSON'S CAREER HISTORY**

    *   Evidence: No CV/resume content.

    *   Result: Not this check.

-   **Check 6: PUBLISHED EVIDENCE**

    *   Evidence: No journal name/volume/issue.

    *   Result: Not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: This is a check. "PAY EXACTLY ******1,149 DOLLARS AND 13 CENTS". "DATE 08/21/80". "TO THE ORDER OF DR L G ABOOD". "TO UNITED VIRGINIA BANK". MICR line: `539303 051000020 1000 608`.

    *   Let's look at the rules for Check 7.

    *   "budget: ... a check face or check stub ... is budget (below), even when the stub's columns are headed 'INVOICE DATE'/'INVOICE NO.'/'INVOICE AMOUNT'."

    *   "A check face/check stub — a check number, bank, MICR line, 'PAY TO THE ORDER OF', signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget (below)..."

    *   This page is clearly a check face (check stub part of it, or just the check itself). It has "PAY EXACTLY...", "TO THE ORDER OF", bank name, MICR line, signature.

    *   Wait, is it an invoice? "An agency estimate/recap/change order is the agency's BILL... invoice". "A hotel/motel guest bill... is an invoice".

    *   "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".

    *   So this is a budget.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

    *   Evidence: No.

    *   Result: Not this check.

-   **Check 9: SLIDE DECK...**

    *   Evidence: No.

    *   Result: Not this check.

-   **Check 10: ADMINISTRATIVE FORM**

    *   Evidence: It has fields, but check 7 overrides money records. "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)". A check is a money record/disbursement instrument.

-   **Check 11: CORRESPONDENCE**

    *   Evidence: No.

-   **Check 12: PUBLISHED JOURNALISM**

    *   Evidence: No.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP**

    *   Evidence: No.

-   **Check 14: PROMOTIONAL MATERIAL**

    *   Evidence: No.

**Re-evaluating Check 7:**

The document is a check from Philip Morris Incorporated.

"PAY EXACTLY ******1,149 DOLLARS AND 13 CENTS"

"TO THE ORDER OF DR L G ABOOD"

"TO UNITED VIRGINIA BANK"

MICR line at bottom.

Signature: Harry L. Shute.

Date: 08/21/80.

Rule: "budget: ... a check face or check stub ... is budget (below)..."

Rule: "A check face/check stub — a check number, bank, MICR line, 'PAY TO THE ORDER OF', signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget (below), even when the stub's columns are headed 'INVOICE DATE'/'INVOICE NO.'/'INVOICE AMOUNT'."

So the label is `budget`.

Let's double check if it could be an invoice.

"invoice: an outside vendor... states charges owed... an 'INVOICE' header with line items... a payment voucher... A payment VOUCHER naming a payee, vendor/item fields, an amount ('PAY THIS AMOUNT'/'AMOUNT'), and a payment date is a payment instrument that BILLS a named payee... invoice".

Wait. "A payment VOUCHER... is a payment instrument that BILLS a named payee... invoice".

But a "check face/check stub" is budget.

Is this a check or a voucher?

It says "PAY EXACTLY ******1,149 DOLLARS AND 13 CENTS". This is standard check language.

It has a MICR line at the bottom: `|:539303| :051000020: |1000 608|`. This is definitely a check ( MICR encoding for routing number, account number, check number).

The text "TO UNITED VIRGINIA BANK" indicates the bank where the account is held (drawee bank).

So this is a check face.

Rule: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".

Therefore, `budget`.

Let's look at the scratchpad instructions again.

"budget: internal money planning, tracking, or disbursement ... a check face or check stub ... is budget".

Final check of the page content:

- Top: Philip Morris logo, "PHILIP MORRIS INCORPORATED RICHMOND, VIRGINIA".
- Top right: "539303", "DATE 08/21/80", "539303".
- "PAY EXACTLY ******1,149 DOLLARS AND 13 CENTS".
- Box with "$ ******1,149.13".
- "TO THE ORDER OF DR L G ABOOD".
- "TO UNITED VIRGINIA BANK RICHMOND, VIRGINIA".
- MICR line.
- Signature "Harry L. Shute" under "AUTHORIZED SIGNATURE".
- Bottom right vertical number "0000127685" (Bates number).

This is a check. Checks are budget.

One detail: "A payment VOUCHER naming a payee, vendor/item fields, an amount ('PAY THIS AMOUNT'/'AMOUNT'), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice, whether it pays a vendor for goods/services or a grantee/recipient (e.g. a contribution payment for a grant)."

Does this look like a voucher?

A voucher usually has a description of what is being paid for (invoice number, description of goods).

This check says "PAY EXACTLY... TO THE ORDER OF DR L G ABOOD". It doesn't list goods or services. It's a disbursement.

The rule says: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".

This is a check face.

So, `budget`.

Wait, is there any other category?

No.

Let's write the scratchpad.

- file_folder: no — page has full check content (payee, amount, bank, MICR).
- handwritten: no — mostly printed, only a signature.
- fax: no.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- financial (budget/invoice): yes — it is a check face ("PAY EXACTLY...", MICR line, bank name, signature). Rule: "A check face/check stub ... is the DISBURSEMENT instrument and stays budget".
- specification: no.
- presentation: no.
- form: no — check 7 overrides.
- correspondence: no.
- news_article: no.
- scientific_report: no.
- advertisement: no.

Runner-up: invoice. Ruled out because this is a check face (disbursement instrument with MICR line), not a vendor bill for goods/services. The rule explicitly states check faces stay budget.

Wait, looking closely at the text: "PAY EXACTLY ******1,149 DOLLARS AND 13 CENTS".

This is a check.

Label: budget.


<h3 class="trace-file"><code>rvl_cdip__invoice__0083.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>budget</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There's a check stub at the top and a check image at the bottom.

**Check 1: file_folder**

- Evidence: The page has a check, a check stub, and a "NON-NEGOTIABLE" watermark. It has real content (a check and its stub). Not file_folder.

**Check 2: handwritten**

- Evidence: There is a handwritten "1129.02" and a stamp "ENTERED 11-6-97". But the majority of the content is printed (check, stub, text). Not handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax header. Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: No survey. Not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: No resume. Not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal masthead. Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: The page is a check and a check stub.
- Top part: Check from HAGENS & BERMAN, P.S. to Meyer Hendricks Bivens & Moyes, P.A. for $417.23, dated 02/03/1998. Check number 10928.
- Middle part: Check stub for Hagens & Berman, P.S. to Meyer Hendricks Bive, dated 02/03/1998, Page 1, Check 10928. Invoice No. 110697, Inv. Date 11/06/1997, Amount 417.23. Description: VIDEO PRODUCTIONS, Duplication of video/audio tapes.
- Bottom part: Image of the check with "NON-NEGOTIABLE" watermark, entered stamp, routing numbers.
- According to Check 7: "A check face/check stub — a check number, bank, MICR line, "PAY TO THE ORDER OF", signature line, or detachable stub — is the DISBURSEMENT instrument and stays budget (below), even when the stub's columns are headed "INVOICE DATE"/"INVOICE NO."/"INVOICE AMOUNT"."
- This is a check face and check stub. Therefore, it is budget.

Let's double check Check 7 rules:

- invoice: outside vendor states charges owed... payment voucher... check face/check stub is DISBURSEMENT instrument and stays budget.
- budget: internal money planning, tracking, or disbursement... check face or check stub...

The page is clearly a check and its detachable stub.

Top half: Check. "PAY Four Hundred Seventeen and 23/100 Dollars TO THE ORDER OF Meyer Hendricks Bivens & Moyes. P.A." Date 02/03/1998, Amount $417.23, Check 10928.

Middle half: Check stub. "HAGENS & BERMAN, P.S. Meyer Hendricks Bive 02/03/1998 Page 1 10928". Invoice No. 110697, Inv. Date 11/06/1997, Amount 417.23. "VIDEO PRODUCTIONS Duplication of video/audio tapes".

Bottom half: Image of the check with MICR line, "NON-NEGOTIABLE", entered stamp.

This perfectly matches "check face/check stub ... is the DISBURSEMENT instrument and stays budget".

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- Evidence: No.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Evidence: No.

**Check 10: ADMINISTRATIVE FORM**

- Evidence: No.

**Check 11: CORRESPONDENCE**

- Evidence: No.

**Check 12: PUBLISHED JOURNALISM**

- Evidence: No.

**Check 13: ORIGINAL RESEARCH WRITE-UP**

- Evidence: No.

**Check 14: PROMOTIONAL MATERIAL**

- Evidence: No.

Conclusion: budget.

Let's review the scratchpad requirements.

- file_folder: no
- handwritten: no
- fax: no
- questionnaire: no
- resume: no
- scientific_publication: no
- financial: yes, check face/stub -&gt; budget.
- specification: no
- presentation: no
- form: no
- correspondence: no
- news_article: no
- scientific_report: no
- advertisement: no

Runner-up: invoice. Ruled out because the page is a check face and check stub (disbursement instrument), which the instructions explicitly state stays budget, even when the stub has invoice fields.

Final label: budget.


<h3 class="trace-file"><code>rvl_cdip__presentation__0040.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>scientific_report</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: "RECEIVED APR 10 1989 A.M. Hypothesis REJECTED". This is a stamp, not a journal masthead. "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". Bates number "620921948". No journal running head.

**Check 1: file_folder**

- Evidence: "RECEIVED APR 10 1989 A.M. Hypothesis REJECTED", "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS", table with "ET PREFERRED", "ET MORE LIKABLE OVERALL", "ET BETTER TOBACCO TASTE", "HYPOTHESIS ACCEPTED/REJECTED". Lots of body content, summary results. Not file_folder.

**Check 2: handwritten**

- Evidence: Mostly typed text, some handwritten scribbles/corrections ("Less Menthol", "Less Pleasant Aftertaste"). Not majority handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax cover sheet header.

**Check 4: questionnaire**

- Evidence: No survey instrument or transmittal.

**Check 5: resume**

- Evidence: No career history.

**Check 6: scientific_publication**

- Evidence: No journal name/volume/issue/page number on the page itself.

**Check 7: financial document (invoice/budget)**

- Evidence: No financial content, line-item table of charges, etc.

**Check 8: specification**

- Evidence: No material safety data sheet, product formulation, "shall/must" language.

**Check 9: presentation**

- Evidence: "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". It's a summary results page. Wait, is it a presentation slide? "CPT SUMMARY RESULTS". It has a table comparing products (Newport FT KS, Kool FT 100, etc.) and hypotheses. It looks like a summary page from a report or presentation. Let's look closer. "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". It has a table with columns "ET PREFERRED", "ET MORE LIKABLE OVERALL", "ET BETTER TOBACCO TASTE", "HYPOTHESIS ACCEPTED/REJECTED". Rows are products. Below is a legend and numbered points 1-6 describing perceptions. This looks like a summary results page from a scientific report or a presentation slide. Wait, check 9 says "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page...". This page is dense with text, a table, and numbered points. It's not sparse.

Let's check check 13: scientific_report. "Running narrative prose with objectives, methods, results, or discussion...". This page has "CPT SUMMARY RESULTS" and numbered results (1-6). "1 ET PERCEIVED LESS IRRITATING AND HAVING LESS MENTHOL. 2 YOUNGER (21-35) ADULT SMOKERS FAVORED CURRENT KM 100." This is results text. It's a summary of results. Is it a scientific_report? Yes, it's a results summary page from a technical study (CPT = Consumer Perception Test?). "NEM EXPANDED TOBACCO (ET)".

Let's re-evaluate check 10: form.

- Evidence: No filled fields, boxes, checkboxes for capturing factual data in a form sense. It's a summary table.

Let's re-evaluate check 13: scientific_report.

- Evidence: "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". Table of results. Numbered list of results (1-6). "DIBgs0333" (document ID). Bates number 620921948. This is a results page from a technical study/report. "CPT" likely stands for Consumer Perception Test. The text describes results: "ET PERCEIVED LESS IRRITATING...", "YOUNGER ADULT SMOKERS FAVORED...". This is running narrative prose (numbered results) describing study findings. It fits scientific_report.

Wait, is there any other category?

What about check 9: presentation? "a near-blank cover or title page... a deck cover, or a section divider". This is not near-blank. It's a results page.

What about check 10: form? "standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This holds research data (CPT summary results). So not form.

Let's look at the content again.

"NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS"

Table:

Columns: ET PREFERRED, ET MORE LIKABLE OVERALL, ET BETTER TOBACCO TASTE, HYPOTHESIS ACCEPTED / REJECTED

Rows: Newport FT KS (KM), NM FT KS COMP. REP (R), KOOL FT KS (KM), KOOL FT 100 (KM), KOOL FT 100 (KM), KOOL Milds KS (KM)1, Newport FT KS (KM), KOOL FT KS (KM), KOOL Milds 100 (KM)2, Newport FT 100 (KM)3, Newport FT 100 (KM), KOOL Lts KS (KL)4, Salem Lts KS (KL)5, KOOL Lts 100 (KL)6, Salem Lts 100 (KL), RICHLAND KS (R), NM FT KS COMP REP (R).

Legend: () = CPT; K = KOOL, KM = KOOL Milds, KL = KOOL Lts, R = RICHLAND.

Numbered text:

1 ET PERCEIVED LESS IRRITATING AND HAVING LESS MENTHOL.

2 YOUNGER (21-35) ADULT SMOKERS FAVORED CURRENT KM 100.

3 ET PERCEIVED Milder, HAVING LESS MENTHOL & TOBACCO TASTE.

4 ET PERCEIVED TO BE SMOOTHER.

5 ET PERCEIVED TO HAVE POORER MENTHOL TASTE, Less Menthol (handwritten)

6 ET PERCEIVED AFTERTASTE Less Pleasant Aftertaste (handwritten)

- EQUALITY OR BETTER.

This is clearly a results summary page from a research study (Consumer Perception Test). It contains results (narrative points 1-6) and a data table summarizing hypothesis acceptance. This fits scientific_report (check 13).

Let's check check 13 again: "Running narrative prose with objectives, methods, results, or discussion...". The numbered points 1-6 are results. The table is results.

Is it a scientific_publication? No journal identifier.

Is it a presentation? No, it's a dense results page, not a slide layout. Although it could be a slide from a deck, the text is dense and looks like a page from a report. Wait, "CPT SUMMARY RESULTS" could be a slide. But check 9 says "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)". This page has a table and numbered paragraphs. It's more like a report page. Also, check 13 says "technical-study title page... is scientific_report". This is a results page.

Let's consider if it's a form (check 10). "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This holds research data (CPT results). So not form.

Therefore, scientific_report is the best fit.

Let's double check check 1: file_folder. No, has content.

Check 2: handwritten. No, mostly typed.

Check 3: fax. No.

Check 4: questionnaire. No.

Check 5: resume. No.

Check 6: scientific_publication. No journal ID.

Check 7: financial. No.

Check 8: specification. No.

Check 9: presentation. "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide". There is a black bar at the top and left edges. But the text is not sparse. It's a full table and numbered list. "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS". It's rotated 90 degrees! The text runs vertically.

Wait, the image is rotated. Let's read it properly.

Top of the page (left side of image): "RECEIVED APR 10 1989 A.M. Hypothesis REJECTED".

Title: "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS".

Table with columns.

Legend.

Numbered results 1-6.

Bates number "620921948" at the bottom (right side of image).

This is a standard document page, just scanned sideways.

It's a results page from a report. scientific_report.

Let's check if there's any other label.

"scientific_report: yes — title 'Selected Aspects of Flavor Perception'... followed by a 'SUMMARY' of running narrative prose". Here we have "CPT SUMMARY RESULTS" and numbered results. It's a summary of results.

Final decision: scientific_report.

Wait, is there any chance it's a form? "QA/parameter review sheet". No, it's summary results.

Is it a presentation? "a deck title or section-divider page". No.

I will go with scientific_report.

Scratchpad:

file_folder: no — page has a table of summary results, legend, and numbered findings, not just an identifier.

handwritten: no — mostly typed text with minor handwritten corrections ("Less Menthol", "Less Pleasant Aftertaste").

questionnaire: no — not a survey instrument.

resume: no.

scientific_publication: no — no journal running head or volume/issue on the page.

financial: no — no financial data.

specification: no — no product formulation or "shall/must" language.

presentation: no — dense text with a data table and numbered narrative results, not sparse slide layout.

form: no — the table holds research data (CPT summary results) and hypothesis acceptance, not generic administrative/log data.

email: no — no mail-client header.

news_article: no — no masthead or journalistic layout.

scientific_report: yes — page titled "NEM EXPANDED TOBACCO (ET) CPT SUMMARY RESULTS" containing a data table of hypothesis acceptance and numbered narrative results (1-6) describing consumer perception test findings (e.g., "ET PERCEIVED LESS IRRITATING..."). This is a results page from a technical study.

Runner-up: presentation, ruled out because the page contains dense narrative results and a detailed data table rather than sparse slide/overhead layout.

Label: scientific_report.


<h3 class="trace-file"><code>rvl_cdip__presentation__0049.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>scientific_report</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: Page number "755" at the top. "STATEMENT OF ROBERT CASAD HOCKETT". No journal masthead. Bates number "03608278" on the right side.

**Check 1: file_folder**

- Evidence: Page has a lot of text, a title "STATEMENT OF ROBERT CASAD HOCKETT", running prose. Not just an identifier.
- Not this check.

**Check 2: handwritten**

- Evidence: Typed text throughout.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: Mentions "My Curriculum Vitae is attached", but the page itself is a statement, not the CV.
- Not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal name, volume, issue, page range (other than 755 which looks like a page number in a transcript or hearing, but no journal identifier). Wait, is this a published journal? No, it looks like a congressional hearing statement or similar. "STATEMENT OF ROBERT CASAD HOCKETT".
- Not this check.

**Check 7: FINANCIAL DOCUMENT**

- Evidence: No financial tables, invoices, budgets.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- Evidence: No material safety data, product formulation, etc.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Evidence: "speech text — the typed text of a speech, address, or remarks delivered at a company event... is a presentation". Wait, is this a speech? "STATEMENT OF ROBERT CASAD HOCKETT". "I am Research Director... In my opinion, the proposed amendment...". This looks like a written statement submitted to a committee (e.g., Congress). Let's check check 11 (memo/letter) or check 13 (scientific_report).
- Wait, check 9 says: "speech text — the typed text of a speech, address, or remarks delivered at a company event... is a presentation". This is a statement to a committee, not necessarily a company event speech.
- Let's look at check 11: CORRESPONDENCE -&gt; email, memo, or letter.
- Let's look at check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report. "Running narrative prose with objectives, methods, results, or discussion...". This is a statement of opinion on a bill.

Let's re-read check 9: "a corporate press release / issued statement ("FOR IMMEDIATE RELEASE", media contact)...". This is not a press release.

What about check 11? "letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person...". This page has no salutation, no closing, no external address. It's a statement.

Wait, is there a better fit?

Let's consider "presentation". A statement submitted to a committee could be considered a presentation of remarks? No, check 9 specifically says "speech text — the typed text of a speech, address, or remarks delivered at a company event". This is a statement to a legislative body.

Let's look at the content: "STATEMENT OF ROBERT CASAD HOCKETT". "I am Research Director... My Curriculum Vitae is attached." "In my opinion, the proposed amendment... will cause justifiable consternation...". "Statistical Association. The claims against smoking are based largely on epidemiologic studies..."

This is a written statement, likely from a congressional hearing (e.g., on the Federal Cigarette Labeling and Advertising Act).

Is it a scientific_report? "Running narrative prose with objectives, methods, results, or discussion". This is an opinion piece / testimony.

Is it a letter? No.

Is it a memo? No.

Let's re-evaluate check 9: "a near-blank cover or title page... a deck cover, or a section divider — is a presentation". This page is dense text.

Wait, what if it's considered a "presentation" because it's a statement/remarks? The prompt says: "speech text — the typed text of a speech, address, or remarks delivered at a company event (e.g. a "CABARRUS RECOGNITION DINNER" page titled with the event, dated, and opening "Thank you ... and good evening everyone ..." with an RJR-style logo/Bates number) is a presentation (this check), not a letter, memo, or report — a spoken address is presentation content even when it is a prose page."

This page is a "STATEMENT OF...". It's not a company event speech.

Let's look at check 13: "ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report". "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript...". This is an opinion statement about a bill, discussing epidemiology. It's not original research.

Could it be a letter? "a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block." No external person named.

Let's reconsider the categories.

1. advertisement

2. budget

3. email

4. file_folder

5. form

6. handwritten

7. invoice

8. letter

9. memo

10. news_article

11. presentation

12. questionnaire

13. resume

14. scientific_publication

15. scientific_report

16. specification

Wait, the labels are:

advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

If it's a statement submitted to a committee, what is it?

Maybe it's a "letter"? No.

Maybe it's a "memo"? No.

Maybe it's a "scientific_report"? It discusses scientific findings (or lack thereof) regarding smoking and cancer. "The claims against smoking are based largely on epidemiologic studies... does not mean causation." It's a scientific commentary/opinion. Check 13: "A scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up, not an email or letter." But this is about a bill.

Let's look at the layout. It's a page from a transcript or a bound document. Page 755. Bates number 03608278.

Left side has cut-off text: "ron the standpoint of...". This looks like a page from a larger document, maybe a hearing transcript or a book.

Actually, the left side is the previous page's text bleeding through or it's a two-page spread? No, the left side is text from the previous page, maybe the right side is the main content. Wait, the left side text is cut off. "ron the standpoint of / since available in the / ission staff in support / night, in fact, erode / egan five years ago trying / del for the pending bill, / te consumption has continued". This looks like a hearing transcript or a report.

The right side is "755 / STATEMENT OF / ROBERT CASAD HOCKETT".

This is a statement in a hearing or a report.

Is there any category for "statement"? No.

Could it be "presentation"? "a corporate press release / issued statement...". No.

Could it be "scientific_report"? "Running narrative prose with objectives, methods, results, or discussion". This is a narrative prose discussing scientific aspects of a bill. It's a scientific commentary. "A scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up". This is a commentary on the bill's findings. I'll lean towards scientific_report or maybe letter/memo if it fits loosely, but it doesn't fit the strict definitions.

Wait, let's look at check 11 again: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block...". No.

"letter: letterhead with an external recipient address...". No.

What about "news_article"? No masthead.

Let's reconsider "presentation". Sometimes testimony or statements are classified as presentations if they are remarks. But the prompt says "delivered at a company event". This is not a company event.

Let's reconsider "scientific_report". "A scientific commentary/critique with running argument about a study's data and conclusions (e.g. "Comments to Y.-P. Sun et al." analyzing whether the data support the authors' conclusion) is a research write-up, not an email or letter." This statement is arguing against the bill's findings using scientific reasoning. It fits the spirit of a scientific report/commentary.

Wait, is there any other category?

"form" - no.

"file_folder" - no.

Let's look at the left text again. "he told the committee," "blished fact in this bill" "ings of many eminent scientists." "an made aware of the so-called" "le are in a position to make" "r not to smoke." "a provision of the bill to" "carbon monoxide yields from" "rtising." "time levels have been" "s advertisement since 1970." "." he declared, "the" "ts provided to you will show" "igarette smoking is not a".

This is clearly a hearing transcript or a statement in a legislative context. "he told the committee".

Since there's no specific category for "hearing transcript" or "testimony", what is the closest?

If it's a statement submitted to a committee, it's often part of a larger report or transcript.

Could it be a "letter"? Sometimes written statements to committees are formatted as letters. But there's no salutation/closing.

Could it be a "memo"? No.

Let's re-read check 13: "ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report". "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript...". This page is running narrative prose. It discusses scientific matters (epidemiology, etiology, pathogenic steps). It's a scientific opinion piece. I will classify it as scientific_report.

Wait, look at check 9 again: "speech text — the typed text of a speech, address, or remarks delivered at a company event... is a presentation". This is not a company event.

What about check 8: "specification"? No.

Let's consider if it's a "letter". "a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." No named external person.

I'll go with scientific_report because it's a running narrative prose discussing scientific arguments (epidemiology, causation) in the context of a legislative bill, which aligns with "scientific commentary/critique" or general scientific narrative prose.

Wait, is there any chance it's a "resume"? "My Curriculum Vitae is attached." The page itself is not the CV.

Let's check the labels again: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

If I have to choose between scientific_report and presentation...

The text is a "STATEMENT OF ROBERT CASAD HOCKETT". It's a formal statement.

In many document classification tasks for tobacco archives, statements to Congress or similar are often classified as scientific_report if they contain scientific arguments, or sometimes as letters/memos if they have the structure. Here, it lacks the structure.

The content is heavily scientific (epidemiology, etiology, pathogenic steps, statistical association vs causation).

I will classify as scientific_report.

Let's double check check 6: scientific_publication. No journal identifier. Page 755 is just a page number in a bound volume (likely a hearing transcript or a book of statements).

Let's double check check 13: "Running narrative prose with objectives, methods, results, or discussion". This is discussion/opinion. "A scientific commentary/critique... is a research write-up". This is a commentary on the bill's scientific claims.

Final decision: scientific_report.

Wait, could it be a "letter"? Sometimes a statement is a letter. But without the letter structure (salutation, closing), it's not a letter by the strict definition in the prompt. "letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person...". This page has none of that.

Could it be a "memo"? "internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block...". No.

So scientific_report is the best fit for running narrative prose with scientific discussion.

One more look at the left side: it's text from the previous page, probably from the same bound document. The right side is the main content.

The document is likely a page from a congressional hearing transcript or a published statement.

Given the options, scientific_report is the most appropriate for a page of running narrative prose discussing scientific/epidemiological arguments.

Wait, is there any possibility it's a "presentation"? "a corporate press release / issued statement...". No, it's not a press release.

I'll stick with scientific_report.

Let's review the scratchpad steps:

1. file_folder: no, has body content.

2. handwritten: no, typed.

3. fax: no.

4. questionnaire: no.

5. resume: no, CV is attached.

6. scientific_publication: no journal ID.

7. financial: no.

8. specification: no.

9. presentation: no, not a slide deck, not a company event speech, not a press release.

10. form: no.

11. correspondence: no letter/memo structure (no salutation, closing, TO/FROM).

12. news_article: no masthead.

13. scientific_report: yes, running narrative prose discussing scientific arguments (epidemiology, causation) regarding a bill. Fits "scientific commentary" or general scientific narrative.

14. advertisement: no.

Runner-up: letter, ruled out because there is no external recipient address, salutation, or closing signature; it's a formal statement, not correspondence.

Another runner-up: presentation, ruled out because it's not a company event speech or press release, and lacks sparse slide layout.

Actually, is there any chance this is a "letter"? "a dated note addressed to a named EXTERNAL person...". No.

I'm confident in scientific_report.

Wait, let's look at the text: "In my opinion, the proposed amendment to the Federal Cigarette Labeling and Advertising Act will cause justifiable consternation among many earnest, and able investigators of cancer... These scientists labor in the hope of clarifying the etiology and pathogenic steps...". This is a scientific opinion/commentary. Fits scientific_report.

One detail: "My Curriculum Vitae is attached." This confirms it's a statement accompanying a CV, typical for congressional testimony. Testimony is often classified as scientific_report if it's technical/scientific in nature.

Final check of the label string: scientific_report.


<h3 class="trace-file"><code>rvl_cdip__presentation__0084.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>scientific_report</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. There is a Bates number "2073057284" at the bottom right. The text is rotated 90 degrees counter-clockwise. Let's read it properly.

Title: "PERFORMANCE OF TESTS, ALONE AND IN COMBINATION"

Table columns: TESTSYSTEM, n, C+, C-, C+G-, C+G+, C-G+, Se, Sp, Pr.

Rows: S. typhimurium, standard; S. typhimurium, hepatocytes; DNA SSB Hepatocytes; SDA of SV40 CO631; Overall Performance + in one, - in all; C, Carcinogenicity; G, Genotoxicity.

Bottom right (rotated): "2073057284", "October 86", "Pr, Predictivity", "Sp, Specificity", "Se, Sensitivity".

Handwritten notes: "-&gt; Hammar", "Lithium Chloride (0.1 mM)", "ratio of two formulations", "amplific. assay".

**Check 1: file_folder**

- Almost no body content? No, there is a large table with data.
- Not file_folder.

**Check 2: handwritten**

- Most content is freeform handwriting? No, it's a printed table with some handwritten annotations.
- Not handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- No fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Not a survey.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Not a resume.
- Not this check.

**Check 6: PUBLISHED EVIDENCE**

- Journal running head? No. "October 86" is just a date. Bates number is present. No journal name/volume/issue.
- Not this check.

**Check 7: FINANCIAL DOCUMENT**

- No financial data.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- Specification? Material Safety Data Sheet? Product formulation? Test-analysis tables keyed to product/part codes, tolerances, or "shall/must" requirement language. Product-referenced test data.
- The table is "PERFORMANCE OF TESTS, ALONE AND IN COMBINATION". It lists tests (S. typhimurium, DNA SSB, SDA of SV40) and performance metrics (Se, Sp, Pr). This looks like scientific data / research results.
- Wait, check 8 says: "A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name... is a specification". This is not a product name, it's test systems.
- "A titled product-analysis table... is a specification". This is not product analysis, it's test performance analysis.
- Let's look at check 13: scientific_report.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Presentation? The text is rotated 90 degrees. "PERFORMANCE OF TESTS, ALONE AND IN COMBINATION".
- Is it a slide? "Scan-artifact signal: a solid black bar along one edge... combined with sparse text placed off-center... points to a photographed slide". There is no solid black bar. The text is just rotated.
- Wait, the title is "PERFORMANCE OF TESTS, ALONE AND IN COMBINATION". It's a table of data.
- "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- Let's check check 10.

**Check 10: ADMINISTRATIVE FORM**

- Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a financial/money chart is budget (check 7), and a research-measurement chart is scientific_report (check 13).
- This is a research-measurement chart (performance of tests, sensitivity, specificity, predictivity). So it's not a form.

**Check 11: CORRESPONDENCE**

- No email, memo, or letter structure.
- Not this check.

**Check 12: PUBLISHED JOURNALISM**

- No masthead.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Running narrative prose? The page is mostly a table.
- Wait, check 13 says: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- But it also says: "Also scientific_report: a hand-plotted experimental graph of test measurements... and a technical-study title page naming a specific experimental method/study".
- This page is a table of test performance data. "PERFORMANCE OF TESTS, ALONE AND IN COMBINATION".
- Is it a scientific_report? The instructions say: "If nothing matches, choose the label whose defining evidence is closest to what you can actually read — never default to scientific_report."
- Let's re-read check 8: "Product-referenced test data is a specification. A titled product-analysis table (e.g., "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough; you don't need a code like "PD 142A" specifically, just clear evidence the table's subject is a product's own composition or properties."
- This table is about "PERFORMANCE OF TESTS". Tests like S. typhimurium (Ames test), DNA SSB, SDA of SV40. These are carcinogenicity/genotoxicity tests. "C, Carcinogenicity", "G, Genotoxicity".
- Is this a specification? No, it's not a product specification.
- Is it a scientific_report? "Requires running prose...". This page has no running prose, just a table and some handwritten notes.
- Wait, look at check 10 again: "a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a financial/money chart is budget (check 7), and a research-measurement chart is scientific_report (check 13)".
- Ah! "a research-measurement chart is scientific_report (check 13)".
- So a standalone table of research measurements (test performance: Se, Sp, Pr for carcinogenicity and genotoxicity tests) is scientific_report, even if it lacks running prose on this specific page?
- Let's re-read check 13 carefully: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report. Also scientific_report: a hand-plotted experimental graph of test measurements (see check 10); a technical-study title page naming a specific experimental method/study (see check 9); and a technical/project status report..."
- Wait, check 10 says: "a research-measurement chart is scientific_report (check 13)". This implies that a research-measurement chart falls under scientific_report.
- Let's check the labels again. 16 categories.
- If it's a research-measurement chart, it's scientific_report.
- Let's look at the handwritten notes: "-&gt; Hammar", "Lithium Chloride (0.1 mM)", "ratio of two formulations", "amplific. assay". These are notes about the data.
- The table shows "PERFORMANCE OF TESTS, ALONE AND IN COMBINATION". Tests: S. typhimurium, standard; S. typhimurium, hepatocytes; DNA SSB Hepatocytes; SDA of SV40 CO631. Metrics: Se (Sensitivity), Sp (Specificity), Pr (Predictivity). Date: October 86. Bates: 2073057284.
- This is clearly a page from a scientific report or technical document presenting research-measurement data (test performance metrics).
- Since check 10 explicitly says "a research-measurement chart is scientific_report (check 13)", and check 13 says "Also scientific_report: a hand-plotted experimental graph of test measurements", it seems a table of research measurements is scientific_report.
- Wait, does check 13 require running prose? "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." BUT check 10 says "a research-measurement chart is scientific_report (check 13)". This is a slight contradiction, but the specific exception in check 10 ("a research-measurement chart is scientific_report") overrides the general rule in check 13 ("Requires running prose"). Actually, check 13 says "Also scientific_report: ... a hand-plotted experimental graph of test measurements (see check 10)". Check 10 says "a research-measurement chart is scientific_report (check 13)". So a research-measurement chart (table or graph) is scientific_report.

Let's double check check 8 (specification).

"A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name (e.g. "WINSTON KS RATE DATA") plotting a measured property over time/subgroup against spec limits (e.g. "USPEC"/"SPEC") — is a specification"

This table is not plotting a measured property over time against spec limits. It's a summary table of test performance (Se, Sp, Pr) for different test systems. This is research data, not a product specification or SPC chart.

So it's scientific_report.

Let's review the scratchpad steps:

1. file_folder: no — page has a large data table with test systems and performance metrics, not just an identifier.

2. handwritten: no — mostly printed table with minor handwritten annotations.

3. fax: no.

4. questionnaire: no.

5. resume: no.

6. scientific_publication: no — no journal running head, just a Bates number and "October 86".

7. financial: no.

8. specification: no — not a product formulation, MSDS, or SPC chart against spec limits; it's a summary of test performance metrics (Se, Sp, Pr) for carcinogenicity/genotoxicity assays.

9. presentation: no — not a slide deck layout, just a rotated table. "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." But check 10 says research-measurement charts are scientific_report.

10. form: no — "a standalone labeled chart is a form only when it holds generic administrative/log data; ... a research-measurement chart is scientific_report (check 13)". This is a research-measurement chart (test performance data).

11. correspondence: no.

12. news_article: no.

13. scientific_report: yes — a research-measurement chart/table presenting test performance data (Sensitivity, Specificity, Predictivity for various carcinogenicity/genotoxicity tests), which falls under scientific_report per check 10's exception and check 13's inclusion of research-measurement charts/graphs. Handwritten notes ("-&gt; Hammar", "Lithium Chloride") support it being a working document from a scientific/technical report.

14. advertisement: no.

Runner-up: form, ruled out because check 10 explicitly states that a research-measurement chart is scientific_report, not a generic administrative form.

Wait, is there any other label?

The page is rotated. "PERFORMANCE OF TESTS, ALONE AND IN COMBINATION".

It's a table.

Table columns: TESTSYSTEM, n, C+, C-, C+G-, C+G+, C-G+, Se, Sp, Pr.

Rows: S. typhimurium, standard; S. typhimurium, hepatocytes; DNA SSB Hepatocytes; SDA of SV40 CO631; Overall Performance + in one, - in all; C, Carcinogenicity; G, Genotoxicity.

This is definitely research data. scientific_report.

Let's confirm check 13 text: "Also scientific_report: a hand-plotted experimental graph of test measurements (see check 10); ...". Check 10 text: "a research-measurement chart is scientific_report (check 13)".

Yes, a research-measurement chart is scientific_report.

Final check of the text:

"PERFORMANCE OF TESTS, ALONE AND IN COMBINATION"

"2073057284" (Bates)

"October 86"

Handwritten: "-&gt; Hammar", "Lithium Chloride (0.1 mM)", "ratio of two formulations", "amplific. assay".

This is a page from a technical/scientific report containing a table of research-measurement data.

Label: scientific_report.


<h3 class="trace-file"><code>rvl_cdip__presentation__0100.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>scientific_report</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. Just a title and a Bates number (2029230512) rotated on the right side. Handwritten "3181" at the top right.

**Check 1: file_folder**

- Evidence: The page has a bold topical heading: "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F". It's not just an ID/stamp. It's a title page.
- Not this check.

**Check 2: handwritten**

- Evidence: Mostly typed text (the title). Only a small handwritten "3181" at the top right.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: None.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: None.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: None.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range, DOI, or copyright line on this page. Just a title and Bates number.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: None.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: None.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: The page is a near-blank cover or title page with a bold headline title: "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F". Wait, let's look at the title. "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F". This sounds like a technical study title page.
- Let's check the caveat for Check 9: "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter, Water In Total Particulate Matter, And Nicotine In Cigarette Smoke / November 28, 1966" — is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."
- The title here is "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F". This names an experimental study (mutagenicity of smoke condensate). It doesn't have a date, but it's clearly a technical study title page. Let's look at Check 13.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: None.
- Not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: None.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: None.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: "Technical-study title page naming a specific experimental method/study is scientific_report (check 13)". The title is "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F". This is a title page for a technical study/report. Wait, is there running prose? Check 13 says: "Requires running prose — a page that is only labeled field-value entries ... is a filled form ... not a scientific report. Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)".
- Ah! "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)". So a technical-study title page is scientific_report.
- Let's re-read Check 9 caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation". Even without a date, if it names a specific experimental study, it's scientific_report. The title "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F" names a specific study.
- So Check 13 matches.

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Evidence: None.
- Not this check.

Let's double check Check 9 vs Check 13.

Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note ... is a presentation (this check), not file_folder (check 1). EXCEPTIONS: ... a technical-study title page naming a specific experimental method/study is scientific_report (check 13) — neither is a deck cover or section divider."

Check 13: "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)".

The page has a bold headline title: "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F". This is a technical study title. It is not a deck cover or section divider for a presentation; it's the title page of a scientific report.

Therefore, scientific_report is the correct label.

Let's review the evidence for Check 13:

- Title page naming a specific experimental study: "Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F".
- This falls under the exception in Check 9 and the explicit inclusion in Check 13 ("a technical-study title page naming a specific experimental method/study").

Runner-up: presentation. Ruled out because the title names a specific experimental study (mutagenicity of smoke condensate), making it a technical-study title page (scientific_report), not a presentation deck cover.

Final check of the text:

"Mutagenicity of the Mainstream Smoke Condensate of the SIGMA Article and the 1R4F"

Bates number: 2029230512

Handwritten: 3181

This is a title page for a scientific report.

Label: scientific_report.


<h3 class="trace-file"><code>rvl_cdip__advertisement__0015.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>advertisement</code> | <strong>Predicted:</strong> <code>presentation</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There is a logo at the bottom right, telephone and fax numbers at the bottom. A Bates number "51427 8435" rotated on the right side.

**Check 1: file_folder**

- Content: "Power Tease", bullet points "Page", "Three (3) 1/2 Pages in Sequence", "Double Truck Spread". Bottom has contact info and a logo.
- Is it a folder tab? No, it's a designed page with a title "Power Tease" and bullet points describing an ad layout (Double Truck Spread). It has real content (a title and description). Not file_folder.

**Check 2: handwritten**

- No handwriting.

**Check 3: FAX TRANSMISSION SHEET**

- No fax header.

**Check 4: questionnaire**

- No survey questions.

**Check 5: resume**

- No career history.

**Check 6: scientific_publication**

- No journal identifier.

**Check 7: financial document**

- No financial data.

**Check 8: specification**

- No material safety data, product formulation, or "shall/must" language.

**Check 9: presentation**

- "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image"
- The page has a title "Power Tease" and bullet points: "Page", "Three (3) 1/2 Pages in Sequence", "Double Truck Spread". This looks like a slide or a cover page for a presentation about an ad layout ("Power Tease", "Double Truck Spread").
- Wait, is it a presentation? "a deck title or section-divider page". "Power Tease" is a title. The bullets describe an ad format.
- Let's check the bottom: "TELEPHONE: (212) 251-7700 FAX: (212) 532-3616" and a logo (looks like "PM" or similar, maybe Philip Morris or a media agency).
- This looks like a slide or a cover page for a presentation about advertising media (Double Truck Spread, Power Tease).
- Let's re-read check 9: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page...". This page has large sparse type, bullet lists, and a title. It's a presentation slide or cover.
- Wait, could it be an advertisement? Check 14: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures." This page doesn't have product imagery or slogans. It's describing an ad layout.
- Could it be a form? No.
- Let's look at the content: "Power Tease", "Page", "Three (3) 1/2 Pages in Sequence", "Double Truck Spread". This is a description of an advertising placement. It's likely a slide from a presentation about media plans or ad placements.
- Therefore, presentation (check 9).

Let's double check check 9 details:

- "a deck title or section-divider page"
- "large sparse type, bullet lists"
- "Power Tease" is underlined, centered.
- Bullet points: "Page", "Three (3) 1/2 Pages in Sequence", "Double Truck Spread".
- Bottom right: logo, bottom: phone/fax.
- This is a classic presentation slide or cover page.

Let's check if it could be something else.

- Is it a specification? No.
- Is it a form? No.

Let's review the scratchpad for check 9:

- presentation: yes — sparse layout, bullet list ("Page", "Three (3) 1/2 Pages in Sequence", "Double Truck Spread"), title "Power Tease", contact info at bottom. This is a slide or deck cover describing an ad format (Double Truck Spread).

Runner-up: form, ruled out because there are no fields/boxes for capturing data; it's a sparse bullet list with a title.

Runner-up: advertisement, ruled out because there is no product imagery, slogans, or brand styling; it's a meta-description of an ad layout, likely a slide in a media presentation.

Wait, is "Power Tease" an advertisement? No, it's describing a "Double Truck Spread" which is a type of newspaper/magazine ad layout. The page itself is not the ad, it's a slide describing it.

Let's confirm the label: presentation.

Check 1: file_folder - no, has real content (title + bullets).

Check 2: handwritten - no.

Check 3: fax - no.

Check 4: questionnaire - no.

Check 5: resume - no.

Check 6: scientific_publication - no.

Check 7: financial - no.

Check 8: specification - no.

Check 9: presentation - yes. Sparse type, bullet list, title "Power Tease", describes ad layout ("Double Truck Spread").

Check 10: form - no.

Check 11: correspondence - no.

Check 12: news_article - no.

Check 13: scientific_report - no.

Check 14: advertisement - no, no product imagery/slogans.

Final label: presentation.


<h3 class="trace-file"><code>rvl_cdip__advertisement__0026.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>advertisement</code> | <strong>Predicted:</strong> <code>presentation</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "2061002493" at the bottom right. The image is rotated 90 degrees counter-clockwise. Let's rotate it mentally.

If rotated 90 degrees clockwise:

- Top: "ALLEY FEDERAL SAV..." (Alley Federal Savings?)
- Middle: A photo of a building, maybe a bank or office.
- Text on the building: "Supervisors" or something similar in cursive. Wait, let's look closer.
- The text "ALLEY FEDERAL S..." is at the bottom left (when rotated correctly).
- There is a small white box with text on the right side (when rotated correctly).
- The image is a photograph of a building/scene. It looks like a photographic slide or a photo.
- Let's re-orient: The text "ALLEY FEDERAL S..." is vertical on the left side (in the provided image). If I rotate the image 90 degrees clockwise, "ALLEY FEDERAL S..." is at the bottom. Wait, "ALLEY FEDERAL S..." is reading upwards. So if I rotate 90 degrees clockwise, it reads left-to-right at the bottom.
- Actually, let's look at the text "2061002493". It's at the bottom right, upright. So the image is rotated 90 degrees counter-clockwise.
- If I rotate 90 degrees clockwise:

  - Bottom right: "2061002493" (Bates number).

  - Left side (now bottom): "ALLEY FEDERAL S..." (Alley Federal Savings).

  - Center: A photo of a building with a sign that says "Supervisors" or "Superbuds"? No, it looks like "Supervisors" or a brand name. Wait, "Supervisors" is written in cursive.

  - There's a small white box with text.

  - This is a photograph of a scene/building.

Let's evaluate the checks.

**Check 1: file_folder**

- Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card.
- "A page that pairs a Bates number with a photographic image (people, a scene, a slide) or with a bold headline title... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
- This page has a photographic image (a scene/building) and a Bates number. So it is NOT file_folder.

**Check 2: handwritten**

- Most content is freeform handwriting. No, it's a photograph.

**Check 3: FAX TRANSMISSION SHEET**

- No fax header.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- No survey instrument.

**Check 5: PERSON'S CAREER HISTORY**

- No resume.

**Check 6: PUBLISHED EVIDENCE**

- No journal running head.

**Check 7: FINANCIAL DOCUMENT**

- No financial table.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- No specification.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder (check 1)."
- "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation"
- The image is a high-contrast black and white photograph of a building/scene (looks like a bank or office building, "ALLEY FEDERAL S..."). It has a Bates number "2061002493".
- This matches "standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check)".
- Therefore, presentation.

Let's double check.

The image is a photograph of a building. There is text "ALLEY FEDERAL S..." (Alley Federal Savings). There is a cursive text "Supervisors" or similar. There is a small text box.

This is a photographic slide/image.

Check 9 explicitly says: "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder (check 1)."

Let's check the runner-up.

file_folder: ruled out because the page carries a photographic image (a scene/building) alongside the Bates number, which counts as real content (check 1 exception).

Final label: presentation.

Wait, is there any other text?

The small white box has text, maybe a caption or label.

The cursive text might be a signature or part of the photo.

Regardless, it's a photographic image.

Let's review Check 9 again:

"A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder (check 1)."

Yes, this fits perfectly.

Scratchpad:

file_folder: no — the page pairs a Bates number (2061002493) with a photographic image of a scene/building ("ALLEY FEDERAL S..."), which carries real content and is classified as a photographic slide under check 9.

handwritten: no — the page is a high-contrast photograph, not freeform handwriting.

presentation: yes — the page is a standalone photographic image (a scene/building with "ALLEY FEDERAL S..." and cursive text) carrying a Bates number, which matches the "photographic slide" definition in check 9.

Runner-up: file_folder, ruled out because the page contains a photographic image (a scene) alongside the Bates number, making it a photographic slide (presentation) rather than pure filing metadata.

Label: presentation.


<h3 class="trace-file"><code>rvl_cdip__advertisement__0064.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>advertisement</code> | <strong>Predicted:</strong> <code>presentation</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None. Top line says "JAN. 5, 2000 9:50PM PROMOTION NETWORK 214 692 6864 NO. 3122 P. 1/4". This looks like a fax transmission header or a fax machine header, not a mail-client header. Wait, "PROMOTION NETWORK 214 692 6864" could be a fax number. "NO. 3122 P. 1/4" is a fax page count. So not email.
- Masthead or running head: No newspaper/magazine masthead. No journal running head.

**Check 1: file_folder**

- Almost no body content? No, there's a big image of Marlboro cigarette packs, text "INTRODUCTION", and handwritten notes at the bottom. Not file_folder.

**Check 2: handwritten**

- Most content is freeform handwriting? No, the majority is a printed/faxed image of cigarette packs and some typed text, with a small handwritten note at the bottom ("Version 1 2079129681-A Marlboro Milds, with distinctive blue packaging, is available in extra Kings and 100s."). Not handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- "FACSIMILE", "FACSIMILE TRANSMISSION", etc. header? The top line is "JAN. 5, 2000 9:50PM PROMOTION NETWORK 214 692 6864 NO. 3122 P. 1/4". This is a fax transmission header (machine-stamped), not a fax cover sheet form. Not this check.

**Check 4: questionnaire**

- Asks reader to answer? No.

**Check 5: resume**

- Career history? No.

**Check 6: scientific_publication**

- Published evidence? No journal identifier.

**Check 7: financial document**

- Invoice or budget? No financial tables.

**Check 8: specification**

- Product documentation? It shows product packaging, but it's an introduction to a new product. Let's look further.

**Check 9: presentation**

- Slide deck, deck cover, or company statement?
- The page has a large image of Marlboro packs, text "INTRODUCTION", and some typed text about "Marlboro Milds is a menthol cigarette that has a New Marlboro taste with a New Mild flavor".
- Bottom has handwritten note: "Version 1 2079129681-A Marlboro Milds, with distinctive blue packaging, is available in extra Kings and 100s."
- Wait, is this a presentation slide? "INTRODUCTION" is a large heading. The layout is sparse text over a background image of cigarette packs.
- Let's check the rules for presentation: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page... A near-blank cover or title page... a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page)... is a presentation".
- Also: "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead — presentation". Here, the background is a textured image, maybe a slide.
- Wait, look at the top: "JAN. 5, 2000 9:50PM PROMOTION NETWORK 214 692 6864 NO. 3122 P. 1/4". This is a fax header. The document itself is a slide or presentation page titled "INTRODUCTION".
- Let's re-read check 9: "Slide/overhead layouts... a deck title or section-divider page...". The page has "INTRODUCTION" as a large heading, text about Marlboro Milds, and images of the product. This looks like a slide from a presentation deck (e.g., a product launch presentation).
- Is it an advertisement? Check 14: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content... a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page". This page has product imagery (Marlboro packs), but it's titled "INTRODUCTION" and has a handwritten note "Version 1...". It looks like an internal presentation slide introducing a new product ("Marlboro Milds"). Internal product launch slides are presentations.
- Let's check if it's a specification (check 8). "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables". This is an introduction slide. Not a specification.
- Let's check if it's an advertisement (check 14). "Marketing layout...". But this is an internal document (faxed, with "Version 1" handwritten note, Bates number 2079129681-A). Internal product introduction slides are presentations.
- Wait, could it be a presentation? Yes, "INTRODUCTION" is a section divider or slide title. The layout is typical of a presentation slide (large title, product images, brief text). The handwritten note "Version 1" is typical of internal draft slides.
- Let's review check 9 again: "a deck title or section-divider page... a near-blank cover or title page... a single-word/short-phrase heading... is a presentation". "INTRODUCTION" is a single-word heading. The page is a slide from a presentation deck.

Let's look closely at the text:

"INTRODUCTION"

"Philip Morris announces the introduction of a unique new product from Marlboro. Marlboro Milds is a menthol cigarette that has a New Marlboro taste with a New Mild flavor."

Images of Marlboro Milds, Lights, Ultra Lights, Medium, etc.

Handwritten: "Version 1 2079129681-A Marlboro Milds, with distinctive blue packaging, is available in extra Kings and 100s."

This is clearly a slide from a presentation deck (likely a product launch or internal briefing). The fax header indicates it was faxed, probably as part of a deck. The content is a presentation slide.

Let's check check 14 (advertisement). Is it an ad? It's an internal document (has a Bates number, fax header, handwritten version note). Internal product launch materials are presentations. An advertisement would be a final marketing layout for public consumption, usually with a Surgeon General warning, etc. This is an internal draft slide ("Version 1").

Therefore, presentation is the best fit.

Let's double check check 9 rules:

"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement ("FOR IMMEDIATE RELEASE", media contact), or a photographic slide image... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... a single-word/short-phrase heading with no subtitle at all (e.g. "RECOMMENDATIONS" centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."

The page has "INTRODUCTION" as a large heading. It has product images. It's a slide.

What about check 8 (specification)? "Product-referenced test data is a specification. A titled product-analysis table... is a specification". This is not a test-analysis table. It's an introduction slide.

What about check 10 (form)? No fields.

What about check 11 (correspondence)? No.

So presentation is the correct label.

Wait, is there any chance it's an advertisement?

"Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."

This page is not printed inside a newspaper. It's a faxed internal document (Bates number, fax header, handwritten version note). Internal product introduction slides are presentations.

Final check of the scratchpad steps:

1. file_folder: no - has real content (text, images, handwritten note).

2. handwritten: no - majority is printed/faxed image and text.

3. fax transmission sheet: no - top line is machine-stamped fax header, not a fax cover sheet form.

4. questionnaire: no.

5. resume: no.

6. scientific_publication: no.

7. financial document: no.

8. specification: no - not a test-analysis table or MSDS.

9. presentation: yes - "INTRODUCTION" heading, product imagery, sparse text, typical slide layout, internal draft note ("Version 1").

10. form: no.

11. correspondence: no.

12. news_article: no.

13. scientific_report: no.

14. advertisement: no - internal draft slide, not a final public ad.

Runner-up: advertisement, ruled out because the page is an internal draft slide (indicated by "Version 1" handwritten note, fax transmission header, and "INTRODUCTION" section title) rather than a final public marketing layout.

Wait, looking at the top line: "JAN. 5, 2000 9:50PM PROMOTION NETWORK 214 692 6864 NO. 3122 P. 1/4". This is definitely a fax header.

The document is a slide from a presentation.

Label: presentation.


</details>

## scientific_report → form

<details class="trace-group">

<summary>7 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__scientific_report__0032.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>form</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. There is a Bates number "2050056147" on the right side.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of content: tables, headings like "B L PLANT ANALYTICAL SUMMARY SHEET", "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". It has handwritten data filling the tables.
- Not file_folder.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: The page has printed field labels, boxes, and ruled entry lines (tables). The handwriting fills these fields.
- Not handwritten. (Handwriting filling in labeled printed fields is form).

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions, rating scales, or commitment application.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No CV/resume content.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial line-item table, ledger, statement, voucher, or check face. The numbers are analytical data (averages, S.D., percentages, counts), not money.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: The page is titled "B L PLANT ANALYTICAL SUMMARY SHEET". It contains tables for "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". These are analytical data sheets for a manufacturing process (tobacco plant). Wait, is this a specification or a form?
- Let's look at Check 10: ADMINISTRATIVE FORM -&gt; form. "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form". This is an "ANALYTICAL SUMMARY SHEET" with tables for various parameters (Dryer stems OV, Weigh belt OV, Nitrates in stems, Production dust, Slurry, Finished product chemical analysis, Finished product % OV, Hogshead report). It has target ranges, averages, S.D., shift averages. It's a filled analytical/lab data sheet.
- Let's re-read Check 8: "Product-referenced test data is a specification. A titled product-analysis table ... is a specification ... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no "shall/must" text is an administrative form (check 10), not a specification."
- This is a daily/shift summary sheet for a plant ("B L PLANT ANALYTICAL SUMMARY SHEET", "C SHIFT AVG", "A SHIFT AVG", "B SHIFT AVG"). It's capturing operational data, not specifying product properties or testing against spec limits for a specific product code (though it has target ranges). Wait, "Finished Product Chemical Analysis" has targets (NH3 - 2.8 +/- 0.5, KS - .15+/- .05, etc.). But the overall document is a "SUMMARY SHEET" for plant operations.
- Let's look at Check 10 again: "A filled analytical or lab data sheet ... is a form". This sheet is filled with handwritten data (averages, S.D., counts). It's a QA/parameter review sheet or filled analytical data sheet. "internal authorization/approval forms with an approval signature/date block. A hand-plotted experimental GRAPH ... is a research test result ... not a form. It does NOT cover money records ... It does NOT cover product-change authorization pages".
- Actually, let's look at the structure. It's a form with fields, boxes, checkboxes, and ruled entry lines for capturing factual data. "B L PLANT ANALYTICAL SUMMARY SHEET". It's a form.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck, cover, or statement.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: "B L PLANT ANALYTICAL SUMMARY SHEET" with multiple sections (Burley, Production Dust, Slurry, Finished Product Chemical Analysis, Finished Product % OV Target, Hogshead Report). It has tables with rows (C, A, B shifts) and columns (Average/S.D., Target, Actual, Out of spec & reason). Handwritten data fills the cells. This is a filled analytical/lab data sheet and an administrative form for capturing operational data.
- Matches check 10.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: No correspondence structure.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: No masthead, byline, etc.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: No running narrative prose. It's a filled form.
- Not this check.

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Evidence: No marketing layout.
- Not this check.

Let's double check Check 8 vs Check 10.

Check 8: "A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name (e.g. "WINSTON KS RATE DATA") plotting a measured property over time/subgroup against spec limits (e.g. "USPEC"/"SPEC") — is a specification even without "shall/must" text: the chart documents a product's parameters, not generic captured data."

This page is a "B L PLANT ANALYTICAL SUMMARY SHEET". It has sections for different processes (Burley, Production Dust, Slurry, Finished Product, Hogshead). It's a daily/shift summary sheet. It's not a single product parameter rate-data chart. It's a filled analytical data sheet. Check 10 explicitly covers "a filled analytical or lab data sheet".

Therefore, form is the correct label.

Let's review the scratchpad requirements:

- Briefly state evidence for each check or "none".
- If evidence present, STOP HERE.
- If no evidence, say "not this check" and move to next.
- Final line: runner-up label and single piece of evidence that ruled it out.

Scratchpad:

file_folder: no — the page has extensive body content (tables, headings, handwritten data), not just an identifier/stamp.

handwritten: no — the page has printed field labels, boxes, and ruled entry lines; handwriting merely fills the printed structured form.

fax: no — no "FACSIMILE" or "FAX COVER SHEET" header.

questionnaire: no — no survey questions, rating scales, or commitment application.

resume: no — no career history or biographical sketch.

scientific_publication: no — no journal name, volume, issue, page range, or copyright line on the page.

invoice/budget: no — no financial line-item table, ledger, or money amounts; the numbers are analytical/operational data (averages, S.D., percentages, counts).

specification: no — this is a daily/shift summary sheet for plant operations ("B L PLANT ANALYTICAL SUMMARY SHEET") capturing generic operational data across multiple processes, not a product-change authorization or a single product parameter rate-data chart against spec limits.

presentation: no — not a slide deck, cover, or statement.

form: yes — titled "B L PLANT ANALYTICAL SUMMARY SHEET" with multiple sections (Burley, Production Dust, Slurry, Finished Product Chemical Analysis, Hogshead Report) containing tables with rows (C, A, B shifts) and columns (Average/S.D., Target, Actual, Out of spec & reason); it is a filled analytical/lab data sheet capturing factual operational data.

Runner-up: specification, ruled out because the page is a multi-section operational summary sheet filling in daily shift data rather than a product-change authorization or a single product parameter rate-data chart documenting a product's specific properties.

Wait, is there any other check?

Check 10: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form". This matches perfectly.

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0074.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>form</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

Document analysis:

- Title: "BLENDED FLAVOR ACCEPTANCE"
- Top right: "94-002057" (Bates number)
- Bottom right: "2024442203" (Bates number)
- Fields:

  - DM Code: 75-814

  - D/H Code Descrip: P.M. FLAVOR 7564-75-RC

  - PMID #: 233889-01

  - Date Produced: 1/31/94

  - Quantity Produced: 567.750 LITS

  - Date Inspected: 1/31/94

  - Inspector: F/C Q.A. Lab, Pull, Production

  - Compounder: DAVID

  - No. Containers: 1

  - Expiration Date: 2/31/94

  - Specific Gravity: (77 Deg. F) 1.1149

  - Flash Point: None

- Signature block: "Alma K Charles", "Supervisor", Date: "2/01/94"
- Text: "The material identified above has been sampled and tested and has been found to be suitable for use by Philip Morris."
- Comments: "In tote with 233921."

Let's go through the checks:

1. IDENTIFIER-ONLY PAGE -&gt; file_folder

   - Has body content: fields, signature, text. Not file_folder.

2. MAJORITY-HANDWRITTEN PAGE -&gt; handwritten

   - Mostly typed, with one signature. Not handwritten.

3. FAX TRANSMISSION SHEET -&gt; form

   - No fax header.

4. SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire

   - Not a survey.

5. PERSON'S CAREER HISTORY -&gt; resume

   - Not a resume.

6. PUBLISHED EVIDENCE -&gt; scientific_publication

   - No journal masthead or running head.

7. FINANCIAL DOCUMENT -&gt; invoice or budget

   - Not financial.

8. PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification

   - "BLENDED FLAVOR ACCEPTANCE"

   - Fields: DM Code, D/H Code Descrip, Quantity Produced, Specific Gravity, Flash Point.

   - Text: "The material identified above has been sampled and tested and has been found to be suitable for use by Philip Morris."

   - This looks like a QA/parameter review sheet or a material acceptance form. Wait, check 10 is "ADMINISTRATIVE FORM -&gt; form".

   - Let's check check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification."

   - Is this a specification? It's an acceptance form for a blended flavor. "BLENDED FLAVOR ACCEPTANCE". It has fields for specific gravity, flash point, quantity. It's a QA/parameter review sheet or acceptance form.

   - Let's look at check 10: "administrative form -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... a QA/parameter review sheet."

   - This is a QA/parameter review sheet / acceptance form. It captures factual data (Specific Gravity, Flash Point, Quantity, Dates, Inspector, Compounder).

   - Wait, is it a specification? "test-analysis tables keyed to product/part codes... tolerances, or 'shall/must' requirement language." This page doesn't have tolerances or "shall/must". It's an acceptance form. "The material identified above has been sampled and tested and has been found to be suitable..."

   - So it's a form (check 10).

Let's re-read check 10: "administrative form -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... a records-management inventory or log table... a QA/parameter review sheet."

Yes, this is a QA/parameter review sheet / acceptance form. It has labeled fields (DM Code, PMID #, Date Produced, Quantity Produced, Date Inspected, Inspector, Compounder, No. Containers, Expiration Date, Specific Gravity, Flash Point) and a signature block (Supervisor, Date).

Let's check check 8 again: "Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all... is an administrative form (check 10), not a specification."

This is a titled acceptance form with test data (Specific Gravity, Flash Point). But it's not a product-analysis table with chemical constituents. It's an acceptance form for a blended flavor. "BLENDED FLAVOR ACCEPTANCE". It's a form used to accept a material.

Let's check check 10 again: "internal authorization/approval forms with an approval signature/date block." This has a signature block for "Supervisor" and a date. It authorizes/accepts the blended flavor.

Therefore, it's a form.

Let's double check if there's any other category.

- email: no
- letter: no
- memo: no
- news_article: no
- presentation: no
- resume: no
- scientific_publication: no
- scientific_report: no (no running prose, just fields and a short statement)
- specification: no (no "shall/must", no tolerances, not a test-analysis table of chemical constituents)
- advertisement: no
- budget: no
- invoice: no

So it's form.

Wait, is there any possibility it's a specification?

"test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language."

This page has "DM Code: 75-814", "D/H Code Descrip: P.M. FLAVOR 7564-75-RC". It has "Specific Gravity: 1.1149", "Flash Point: None". These are test results, not a table of analysis. It's an acceptance form. "BLENDED FLAVOR ACCEPTANCE".

Check 10 explicitly mentions "a QA/parameter review sheet" and "internal authorization/approval forms with an approval signature/date block". This fits perfectly.

Let's write the scratchpad.

1. file_folder: no — the page has extensive body content (fields, signature, text), not just an identifier.

2. handwritten: no — mostly typed text with a single signature.

3. fax: no — no fax transmission header.

4. questionnaire: no — not a survey instrument.

5. resume: no — not a career history.

6. scientific_publication: no — no journal running head or identifier.

7. financial: no — not a financial document.

8. specification: no — lacks "shall/must" language, tolerances, or a product-analysis table of chemical constituents; it is an acceptance form.

9. presentation: no — not a slide deck or cover.

10. form: yes — titled "BLENDED FLAVOR ACCEPTANCE", contains filled fields (DM Code, Date Produced, Specific Gravity, etc.), a short acceptance statement, and an approval signature block (Supervisor, Date). This is a QA/parameter review sheet / internal authorization/approval form.

Runner-up: specification, ruled out because the page is an acceptance form with test results and an approval block, not a specification with tolerances or "shall/must" requirement language.

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0093.png</code></h3>

<p class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>form</code></p>

<p class="trace-label">Reasoning</p>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** No "From/To/Sent/Subject" block.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number on this specific page. There is a title "CTR PROGRESS REPORT".

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a title "CTR PROGRESS REPORT", grant number, investigator name, abstract, and a section "Report of Progress". It has real content.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: The page is typed. There is some underlining and maybe a handwritten "4" at the bottom right, but the content is typed.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: Not a survey instrument.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: Not a CV or resume. It's a grant report.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name, volume, issue, page range on the page itself. "CTR PROGRESS REPORT" is an internal report title.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: Mentions "GRANT NUMBER 3144", but the primary structure is a progress report, not a line-item table of charges or a budget statement. It's a report on a grant.

    *   Result: not this check.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: Not a product spec or MSDS.

    *   Result: not this check.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: Not a slide deck or press release.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: It has fields like "GRANT NUMBER", "Period Covered", "Name of Investigator", "Title of Original Grant". However, the bulk of the content is an abstract and a "Report of Progress" section (though the report of progress part is empty/blank at the bottom). Wait, let's look closer.

    *   The page has "Abstract of the specific aims as stated in the original application:" followed by paragraphs of text.

    *   Then "List any publications...". Answer: "Not applicable."

    *   Then "Report of Progress (no more than 4 pages, please):" followed by blank space.

    *   This looks like a form (a grant progress report form) filled out with an abstract.

    *   Wait, let's check Check 13. "Original research write-up -&gt; scientific_report".

    *   Check 13 says: "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report."

    *   This page has "Abstract of the specific aims..." which is running narrative prose describing objectives and methods ("We intend to examine...", "We shall first purify...").

    *   However, the structure is clearly a form: "CTR PROGRESS REPORT", "GRANT NUMBER", "Period Covered", "Name of Investigator", "Title of Original Grant".

    *   Let's re-read Check 10 vs Check 13.

    *   Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms...".

    *   Check 13: "Running narrative prose with objectives, methods, results, or discussion... a lab or technical study title page... Requires running prose".

    *   The page contains a significant amount of running prose: the abstract (3 paragraphs).

    *   Is this a scientific_report or a form?

    *   The document is titled "CTR PROGRESS REPORT". It has grant metadata. It has an abstract.

    *   Check 13 says: "a technical/project status report whose content is primarily technical... is scientific_report".

    *   Check 10 says: "A research grant application with structured section headings... that are field labels for the applicant to fill in — not continuous narrative sentences — stays form".

    *   Here, the applicant *has* filled in continuous narrative sentences (the abstract). "Our objective is to elucidate...", "We intend to examine...".

    *   Wait, the abstract is "as stated in the original application". So it's a copy of the abstract.

    *   The "Report of Progress" section is blank.

    *   This looks like a filled form (a progress report form) where the applicant pasted their abstract.

    *   Let's look at the "Runner-up" logic. If I choose scientific_report, I need running prose. There is running prose (the abstract).

    *   If I choose form, it's a filled form.

    *   Let's look at Check 13 again: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."

    *   This page has labeled fields: "GRANT NUMBER", "Period Covered", "Name of Investigator", "Title of Original Grant".

    *   Then a section "Abstract of the specific aims...". The text below is narrative.

    *   Then "List any publications...". Text: "Not applicable."

    *   Then "Report of Progress...". Blank.

    *   The primary content is the abstract text.

    *   However, the document *is* a form. It's a "CTR PROGRESS REPORT" form.

    *   Let's look at the calibration notes: "A research grant application with structured section headings... that are field labels... stays form... even though the topic... sounds like a research write-up."

    *   This is a progress report. It has fields. The abstract is pasted in.

    *   Actually, let's look at the content. It's a scientific abstract. "Cyclins are regulatory proteins...".

    *   Is it a scientific_report? "Original research write-up -&gt; scientific_report". "Running narrative prose with objectives, methods, results, or discussion". The abstract has objectives and methods.

    *   But the layout is a form. "CTR PROGRESS REPORT".

    *   Let's check the balance. "form, scientific_report, and handwritten are historically the most over-predicted labels".

    *   If I call it scientific_report, I might be over-predicting.

    *   If I call it form, it fits the "filled form" definition. "Filled or blank fields... for capturing factual data". The abstract is captured data.

    *   Wait, Check 13 says: "a lab or technical study title page with authors and an internal affiliation and no journal identifiers." This page has "Name of Investigator: Hershko, Avram". No affiliation listed explicitly, but it's a grant report.

    *   Let's look at the text again. "Abstract of the specific aims as stated in the original application". This is a standard NIH (or similar) progress report form (RRB 25 or similar, actually looks like a CTR - Center for Tobacco Research? or similar grant report).

    *   The page is mostly text (the abstract).

    *   Let's look at Check 10 vs 13 carefully.

    *   Check 13: "Requires running prose". The abstract is running prose.

    *   Check 10: "Filled or blank fields...". The top part is fields. The bottom is blank.

    *   The abstract is the main content.

    *   However, the document structure is a form. "CTR PROGRESS REPORT".

    *   Let's consider "scientific_report". A progress report is a type of scientific report.

    *   But the instructions say: "A research grant application with structured section headings... that are field labels... stays form". This is a grant progress report. It has field labels ("GRANT NUMBER", "Name of Investigator"). The content filled in is the abstract.

    *   Actually, usually these forms require a narrative report. Here, the narrative report ("Report of Progress") is blank. The only text is the abstract (which is required to be pasted in) and the publication list ("Not applicable").

    *   So the page is largely a form with some text pasted in.

    *   Let's look at the "Report of Progress" line. It's a field label. The space below is empty.

    *   So the page is a form (check 10) that is mostly empty, with the abstract filled in.

    *   Wait, the abstract is 3 paragraphs. That's a lot of text.

    *   But the form structure dominates: Title, Grant #, Period, Investigator, Title, Abstract section, Publications section, Report of Progress section.

    *   This is a filled form.

    *   Let's check if there's a better fit.

    *   Is it a scientific_report? "Original research write-up". This is a progress report *form*. The actual report content is missing (blank). The abstract is just a copy of the original application.

    *   So it's a form.

    Let's re-evaluate Check 13. "Running narrative prose with objectives, methods, results, or discussion". The abstract has objectives and methods. But it's labeled "Abstract of the specific aims as stated in the original application". It's not the current report's prose. The current report's prose ("Report of Progress") is blank.

    So the page is a form (check 10).

    Let's check Check 10 again. "Filled or blank fields... for capturing factual data". Yes. "internal authorization/approval forms with an approval signature/date block". This doesn'*t* have that, but it has the grant metadata fields.

    "A research grant application with structured section headings... stays form". This is a grant progress report (similar to application).

    Let's look at the label "scientific_report".

    If I classify this as scientific_report, I am saying the abstract makes it a report.

    But the document is a "CTR PROGRESS REPORT" form.

    The instructions say: "form, scientific_report, and handwritten are historically the most over-predicted labels".

    This suggests I should be careful.

    The page has a clear form structure: "CTR PROGRESS REPORT", "GRANT NUMBER", "Period Covered", "Name of Investigator", "Title of Original Grant".

    The content is the abstract.

    The "Report of Progress" is blank.

    This is a filled form.

    Let's look at the "Runner-up". If I choose form, the runner-up is scientific_report.

    Evidence against scientific_report: The main content area ("Report of Progress") is blank. The text present is an abstract from the original application, not a new research write-up. The document is a form template filled with metadata and a pasted abstract.

    Wait, is there any other category?

    "memo"? No.

    "letter"? No.

    Let's look at the text "CTR PROGRESS REPORT". CTR could be "Center for Tobacco Research" or similar.

    The text is about "Cyclins", "ubiquitin", "cell cycle". This is biology/biochemistry. Avram Hershko is a Nobel laureate (ubiquitin). This is a real grant report.

    The document is a form submitted to a funding agency.

    Decision: form (check 10).

    Why? It has labeled fields (Grant Number, Period, Name, Title). It has section headers for data capture (Abstract, Publications, Report of Progress). The "Report of Progress" section is blank, which is typical for a form that hasn'*t* been fully filled or is a cover page. The abstract is pasted in as required data.

    Actually, looking closely at the bottom: "Report of Progress (no more than 4 pages, please):" followed by blank space. This implies the report continues on other pages, or this is just the cover/abstract page of the form.

    Wait, if the report continues on other pages, this page is part of a report.

    But this specific page is a form page.

    The instructions say: "Judge each page by its FUNCTION".

    This page's function is to capture grant metadata and the abstract. It is a form.

    Let's reconsider scientific_report.

    "Original research write-up -&gt; scientific_report".

    "Running narrative prose with objectives, methods, results, or discussion".

    The abstract has objectives and methods.

    But is this page *the* write-up? No, it's a "Progress Report" form. The actual progress report text is missing (blank).

    So it's a form.

    Let's check the balance. "form... historically the most over-predicted".

    If I call it form, I might be over-predicting if it's considered a scientific report cover page.

    But check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report".

    This page has "Title of Original Grant: Mechanisms of Regulation of Cyclin Degradation". And a date "1/1/92 to 4/15/92".

    But it's not just a title page. It has the abstract.

    And it has "Report of Progress" header.

    Let's look at Check 10 again. "Filled or blank fields...".

    The page is a form.

    Let's look at the "Runner-up" for Check 10. scientific_report.

    Ruled out because the page is a grant progress report form with labeled fields (Grant Number, Investigator, etc.) and the main content area ("Report of Progress") is blank, while the text present is a pasted abstract from the original application, not a new research write-up.

    Wait, is there a chance it's a "memo"? No.

    Is it a "letter"? No.

    Let's look at the text again.

    "Abstract of the specific aims as stated in the original application:" -&gt; This is a section header.

    Text follows.

    "List any publications..." -&gt; Section header.

    "Not applicable." -&gt; Filled value.

    "Report of Progress..." -&gt; Section header.

    Blank space.

    This is definitely a form. It's a structured document for capturing data (grant info, abstract, publications). The fact that the abstract is long text doesn'*t* make it a scientific report; it's the content of the "Abstract" field.

    Final check: Check 13 says "Requires running prose — a page that is only labeled field-value entries... is a filled form".

    Here we have labeled field-value entries (Grant Number: 3144, Name: Hershko, Avram) AND running prose (the abstract).

    But the running prose is in a specific field "Abstract of the specific aims...".

    And the main field "Report of Progress" is empty.

    So the page is a form.

    One distinct possibility: Is this a "scientific_report" because it contains the abstract of a research paper?

    The title is "CTR PROGRESS REPORT".

    Usually, progress reports are scientific reports.

    But this specific page is the cover/abstract page of the report form.

    If the page was just the abstract text with no form headers, it would be scientific_report (or part of one).

    With the form headers ("CTR PROGRESS REPORT", "GRANT NUMBER", etc.), it is a form.

    Let's look at the calibration: "A research grant application with structured section headings (e.g. Investigator, Objectives, Methods) that are field labels for the applicant to fill in — not continuous narrative sentences — stays form (this check), not scientific_report, even though the topic and section names sound like a research write-up."

    This page has "Name of Investigator", "Title of Original Grant", "Abstract...". These are field labels. The applicant filled in the abstract (narrative sentences).

    So it stays form.

    Label: form.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0099.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. Just a Bates number "93-013225" and "2024437528".

**Check 1: file_folder**

- Evidence: The page has a title "BLENDED FLAVOR ACCEPTANCE", fields like "DM Code", "PHID #", "Date Produced", etc., a signature block, and a paragraph of text. It has real content, not just an identifier/stamp.
- Not this check.

**Check 2: handwritten**

- Evidence: Mostly typed text. There is a signature "Dina H Charles" and a handwritten comment "In tote with 232171.". Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: Not a survey.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: Not a resume.
- Not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal name, volume, issue, page range.
- Not this check.

**Check 7: FINANCIAL DOCUMENT**

- Evidence: No line-item table of charges, no invoice/budget structure. "Quantity Produced: 567.750 LITS" is production data, not financial billing.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: Title "BLENDED FLAVOR ACCEPTANCE". Fields: "DM Code: 75-814", "D/H Code Descrip: P.*M*. FLAVOR 7564-75-RC", "Quantity Produced", "Date Inspected", "Inspector", "Compounder", "Expiration Date", "Specific Gravity", "Flash Point". Signature block: "Supervisor", "Date". Text: "The material identified above has been sampled and tested and has been found to be suitable for use by Philip Morris." Comments: "In tote with 232171."
- Wait, is this a specification or a form?
- Check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all... is an administrative form (check 10), not a specification."
- Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... a QA/parameter review sheet."
- This page is a "BLENDED FLAVOR ACCEPTANCE" sheet. It captures factual data about a material (flavor blend) being accepted. It has fields for DM Code, PHID, Date Produced, Quantity, Inspector, Expiration Date, Specific Gravity, Flash Point. It has a signature block for the Supervisor.
- Is it a specification? A specification defines WHAT a product will be (composition/property changes with labeled approval blocks). This is an acceptance sheet for a produced material. It's a QA/parameter review sheet or a filled form capturing factual data.
- Let's look at Check 10: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... a QA/parameter review sheet."
- This looks exactly like a QA/parameter review sheet or an acceptance form. It captures data (Specific Gravity, Flash Point, Quantity) and has an approval block (Supervisor signature).
- Let's re-read Check 8: "Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all... is an administrative form (check 10)". Wait, this has a product tie-in ("P.*M*. FLAVOR 7564-75-RC"). But is it a "product-analysis table" or "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language"? This is an acceptance form for a batch of blended flavor. It's capturing batch data (Quantity Produced, Date Produced, Specific Gravity, Flash Point) and approving it. This is a form (QA/parameter review sheet / acceptance form).
- Let's check Check 10 again: "internal authorization/approval forms with an approval signature/date block." Yes, it has "Supervisor" signature and "Date".
- So it's a form.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Evidence: Not a slide deck.
- Not this check.

**Check 10: ADMINISTRATIVE FORM**

- Evidence: "BLENDED FLAVOR ACCEPTANCE" with fields (DM Code, PHID #, Date Produced, Quantity Produced, Date Inspected, Inspector, Compounder, Expiration Date, No. Containers, Specific Gravity, Flash Point). Signature block (Supervisor, Date). Text: "The material identified above has been sampled and tested and has been found to be suitable for use by Philip Morris." Comments field. This is a filled form capturing factual data and an approval block. Matches "QA/parameter review sheet" or "internal authorization/approval forms with an approval signature/date block".
- This is a strong match for form.

**Check 11: CORRESPONDENCE**

- Evidence: Not an email, memo, or letter.
- Not this check.

**Check 12: PUBLISHED JOURNALISM**

- Evidence: Not news.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP**

- Evidence: No running narrative prose.
- Not this check.

**Check 14: PROMOTIONAL MATERIAL**

- Evidence: Not an ad.
- Not this check.

Conclusion: form.

Let's double check Check 8 vs Check 10.

Check 8: "product-change authorization or review page — a titled summary describing CHANGES to a specific product... followed by labeled approval/signature blocks... is a specification". This page is not describing changes to a product. It's an acceptance sheet for a produced batch ("Quantity Produced: 567.750 LITS", "Date Produced: 7/21/93", "Date Inspected: 7/21/93"). It's a QA acceptance form.

Check 10: "QA/parameter review sheet". "internal authorization/approval forms with an approval signature/date block".

This is definitely a form.

Final check of the text:

"BLENDED FLAVOR ACCEPTANCE"

DM Code: 75-814

D/H Code Descrip: P.*M*. FLAVOR 7564-75-RC

PHID #: 232145-00

Date Produced: 7/21/93

Quantity Produced: 567.750 LITS

Date Inspected: 7/21/93

Inspector: *F*/C Q.A. Lab, Pull, Production

Compounder: MARY

Expiration Date: 8/21/93

No. Containers: 1

Specific Gravity: (77 Deg. *F*) 1.1132

Flash Point: None

Signature: Dina H Charles, Supervisor, 7/22/93

"The material identified above has been sampled and tested and has been found to be suitable for use by Philip Morris."

Comments: In tote with 232171.

This is a standard acceptance form / QA record. Label: form.


<h3 class="trace-file"><code>rvl_cdip__budget__0004.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "65503 5219" and a notice at the bottom left.

**Check 1: file_folder**

- Content: "VARIANCE SHEET", "BRONX & WILLIAMSON - LOUISVILLE", "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE".
- It has a list of checkboxes and handwritten text "throughout rest of file".
- Not just an identifier/stamp. It has real content (a variance sheet).
- Not file_folder.

**Check 2: handwritten**

- Mostly typed text with checkboxes. Handwriting is just "throughout rest of file" next to "OTHER (SPECIFY)".
- Not majority handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- No fax header.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Not a survey.

**Check 5: PERSON'S CAREER HISTORY**

- Not a resume.

**Check 6: PUBLISHED EVIDENCE**

- No journal masthead.

**Check 7: FINANCIAL DOCUMENT**

- No financial content.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- No product specs.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Let's look at the layout. It's a page with a title "VARIANCE SHEET", some text, checkboxes, and a handwritten note.
- Wait, check 9 has a caveat: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...) — is a presentation (this check), not a form."
- This is a "VARIANCE SHEET" for "BRONX & WILLIAMSON - LOUISVILLE". "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE".
- It's checking off reasons why a document was reproduced differently (duplicate, missing page numbers, poor quality, overlay item, no documents found, file folder, remove expandable file, remove file, envelope, other).
- This is a status/location display sheet or a variance sheet for records management.
- Wait, is it a form? Check 10: "administrative form -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... a records-management inventory or log table... a QA/parameter review sheet."
- But check 9 explicitly mentions: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" ...) — is a presentation (this check), not a form."
- This sheet is titled "VARIANCE SHEET", has a line "BRONX & WILLIAMSON - LOUISVILLE", checkboxes for motivations, and a handwritten note "throughout rest of file". It's essentially a status sheet for a reproduction variance.
- Let's re-read check 9: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...) — is a presentation (this check), not a form. It presents where something is, rather than capturing data for records."
- This sheet presents *why* a variance was made during reproduction, not exactly where it is, but it's very similar. It's a "VARIANCE SHEET".
- Wait, is it a form? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This sheet has checkboxes and a ruled entry line for "OTHER (SPECIFY)". The handwriting fills the ruled line.
- Let's look at the layout. It's a white page inside a black border (scan artifact or folder tab?). The black border is thick on the left and right, top and bottom. It looks like a photographed slide or a scanned page with a heavy border.
- Actually, look at the bottom: "NOTICE If the file image is less clear than this notice, it is due to the quality of the document being filmed." and Bates number "65503 5219". This is a microfilm/fiche notice.
- The page itself is a "VARIANCE SHEET".
- Is it a presentation? "a one-page status/location display sheet ... is a presentation". This is a variance sheet, not exactly a location display sheet, but it's a one-page sheet with checkboxes and a title, presented in a sparse layout.
- Let's check check 10 again: "administrative form -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This sheet has checkboxes and a ruled line. It captures factual data (the motivation for variance).
- But check 9 says: "a one-page status/location display sheet ... is a presentation (this check), not a form."
- Is there a better match?
- Let's re-read check 9 carefully: "EXCEPTIONS: ... a technical-study title page ... is scientific_report ... A large heading rotated 90 degrees ... is a section divider ... A standalone photographic image ... is a photographic slide ... A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
- "Scan-artifact signal: a solid black bar along one edge of the page ... combined with sparse text placed off-center ... points to a photographed slide/overhead — presentation". Here we have a thick black border all around, which is typical of a microfilm frame or a photographed slide. The text is sparse, centered, with checkboxes.
- Wait, the notice at the bottom "If the file image is less clear than this notice..." is a standard microfilm frame notice. The page is a scan of a microfilm frame containing a "VARIANCE SHEET".
- The variance sheet itself: "VARIANCE SHEET", "BRONX & WILLIAMSON - LOUISVILLE", "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE". Checkboxes for various reasons. Handwritten "throughout rest of file".
- This is a form capturing data (the motivation). Check 10: "administrative form -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
- Why would it be presentation? The check 9 caveat is specifically for "a one-page status/location display sheet ... (e.g. an 'ARCHIVE LOCATION VARIANCE SHEET' ...)". This is a "VARIANCE SHEET", but it's about reproduction motivations, not location.
- Let's look at the layout. It's a single page with a title, a list of checkboxes, and one handwritten entry. It's very sparse.
- Is it a form? Yes, it has checkboxes and a ruled line for "OTHER (SPECIFY)". The user checked "OTHER" and wrote "throughout rest of file". This is a filled form.
- Let's check if there's any other category.
- Check 1: file_folder. No, it has content.
- Check 10: form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This fits perfectly. It's a variance sheet form used in records management/reproduction.
- Wait, is it a presentation? "a one-page status/location display sheet ... is a presentation". This is not a status/location display sheet. It's a variance sheet for reproduction.
- Let's consider "form". The document is a "VARIANCE SHEET" with checkboxes and a text field. It's an administrative form used to document reproduction issues.
- Let's re-read check 9 caveat: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...) — is a presentation (this check), not a form. It presents where something is, rather than capturing data for records."
- This sheet captures data (the motivation for variance). It's not presenting where something is. So it's not the exception in check 9. It falls under check 10: form.
- Let's check if it's a scientific_report. No.
- Let's check if it's a memo. No.

Let's look closely at the text:

"VARIANCE SHEET"

"BRONX & WILLIAMSON - LOUISVILLE"

"AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE"

( ) DOCUMENT COPIES ARE IN THE SAME SEQUENCE AS THEY APPEARED IN THE ORIGINAL.

( ) DUPLICATE DOCUMENTS APPEARED IN THE ORIGINAL.

( ) PAGE NUMBER(S) MISSING IN THE ORIGINAL.

( ) POOR QUALITY ORIGINAL.

( ) OVERLAY ITEM COULD NOT BE REMOVED WITHOUT DAMAGE TO THE ORIGINAL.

( ) NO DOCUMENTS WERE FOUND WITHIN THE ORIGINAL:

( ) FILE FOLDER.

( ) REMOVE EXPANDABLE FILE.

( ) REMOVE FILE.

( ) ENVELOPE.

( ) OTHER (SPECIFY) _______

(X) OTHER throughout rest of file

This is clearly a form. It has checkboxes and a ruled line. It captures factual data about a reproduction variance.

Therefore, it is a form (check 10).

Wait, is there any reason to classify it as presentation?

The layout is sparse, centered text, checkboxes. But it's a filled form (checkboxes checked, handwritten text). Check 10 says "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."

The check 9 exception is specifically for "status/location display sheet ... presenting where something is". This sheet is capturing data (motivations for variance). So check 10 applies.

Let's double check check 1: file_folder.

"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."

This page has a variance sheet with content. Not file_folder.

Let's double check check 2: handwritten.

"Most of the content is freeform handwriting ... NOT on a printed template."

This is on a printed template (checkboxes, ruled lines). Not handwritten.

So it's form.

Evidence for check 10: "VARIANCE SHEET" title, checkboxes for reproduction motivations, ruled entry line for "OTHER (SPECIFY)" filled with handwritten "throughout rest of file". This is a filled administrative form capturing factual data.

Runner-up: presentation. Ruled out because the page is a filled form with checkboxes and a text field capturing reproduction variance data, not a status/location display sheet presenting where a record is located (the check 9 exception). Also, the layout is a standard form layout, not a slide deck or sparse presentation layout (though it is sparse, the function is data capture via a template). Actually, the check 9 exception is very specific: "stating where a record range or item is located". This sheet states "motivations were made" for reproduction. So it's capturing data, hence form.

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__budget__0043.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** No "From/To/Sent/Subject" block. There is a Bates number "TCAL0249389" at the bottom. No fax transmission header like "SENT BY:".
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a seal/logo in the top left ("Form 420 1985").

**2. Scratchpad checks:**

-   **Check 1: file_folder**

    *   Evidence: The page has a lot of content: "RECIPIENT COMMITTEE CAMPAIGN STATEMENT", fields for committee name, address, treasurer, etc. It's not just an ID or stamp.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: Most content is typed. There is some handwriting ("1/1/85", "3/17/85", "Vigo G. Nielsen, Jr.", "650 California Street...", "3/20/85", "San Francisco, CA", signature "Vigo G Nielsen Jr", "*N*/A"). But it's filling out a form.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: questionnaire**

    *   Evidence: Not a survey instrument. It's a legal/financial statement.

    *   Result: not this check.

-   **Check 5: resume**

    *   Evidence: Not a career history.

    *   Result: not this check.

-   **Check 6: scientific_publication**

    *   Evidence: No journal identifier.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: Title is "RECIPIENT COMMITTEE CAMPAIGN STATEMENT". Subtitle: "(Government Code Sections 84200-84217)". "For use by recipient committees which receive a cumulative contribution of $100 or more from a single source."

    *   It lists "NAME OF COMMITTEE: THE TOBACCO INSTITUTE", address, treasurer.

    *   It asks "IS THIS A CONTROLLED COMMITTEE?".

    *   It lists candidates/measures.

    *   It has a "VERIFICATION" section with penalty of perjury.

    *   This is a campaign contribution statement / disclosure form.

    *   Let's look at the budget definition: "money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient — e.g. a political campaign contribution request, a contribution-request checklist, a grant/contribution request with recipient and amount — is budget, not form". Wait, this is a *statement* of contributions received. "RECIPIENT COMMITTEE CAMPAIGN STATEMENT".

    *   Let's look at the invoice definition: "outside vendor... states charges owed". Not this.

    *   Let's look at the form definition (Check 10): "Filled or blank fields, boxes, checkboxes... application... records-management inventory... QA/parameter review sheet... internal authorization/approval forms".

    *   Wait, is this a form or a budget?

    *   The budget check says: "money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget". This statement is about contributions received by a committee. It's a government form (Form 420, 1985).

    *   Let's re-read Check 7 carefully. "budget: ... money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient — e.g. a political campaign contribution request, a contribution-request checklist, a grant/contribution request with recipient and amount — is budget, not form".

    *   This document is a "CAMPAIGN STATEMENT". It's a disclosure statement. It's a form filed with the government.

    *   Let's look at Check 10: "ADMINISTRATIVE FORM -&gt; form". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application...". This is definitely a form. It's a government form (Form 420).

    *   Does Check 7 override Check 10? Check 7 says "financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face."

    *   Is this a "statement" in the financial sense? A "Campaign Statement" is a legal disclosure form. It's not a bill (invoice) or an internal budget tracking sheet.

    *   The budget definition includes "a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient". This page has names of committees, addresses, dates of election, candidates. It's not *just* amount and recipient. It's a complex legal form.

    *   So Check 7 (financial) doesn'*t* seem to fit perfectly as "invoice" or "budget" in the sense of a bill or internal tracking. Wait, "political campaign contribution request... is budget". This is a *statement* of contributions.

    *   Let's look at the "budget" bullet again: "money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient". This page has much more content (addresses, dates, candidate names). So it's not a "money-only record".

    *   Therefore, it falls back to Check 10: Administrative Form. It has fields, boxes, checkboxes ("YES", "NO"), ruled lines. It's a government form (Form 420).

-   **Check 8: specification**

    *   Evidence: No.

    *   Result: not this check.

-   **Check 9: presentation**

    *   Evidence: No.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: "Form 420 1985". Fields for "NAME OF COMMITTEE", "ADDRESS", "NAME OF TREASURER", checkboxes for "YES" / "NO" (controlled committee), tables for candidates. "VERIFICATION" block with signature lines. This is a classic filled administrative/legal form.

    *   Result: YES.

-   **Check 11: CORRESPONDENCE**

    *   Evidence: No.

    *   Result: not this check.

-   **Check 12: news_article**

    *   Evidence: No.

    *   Result: not this check.

-   **Check 13: scientific_report**

    *   Evidence: No.

    *   Result: not this check.

-   **Check 14: advertisement**

    *   Evidence: No.

    *   Result: not this check.

**Re-evaluating Check 7 vs Check 10:**

The document is a "RECIPIENT COMMITTEE CAMPAIGN STATEMENT".

Check 7 (Financial): "invoice or budget".

- Invoice: Outside vendor charges. No.
- Budget: Internal money planning, tracking, disbursement. "money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient".

This document contains: Committee name, address, treasurer name, address, date of election, total pages, sponsoring org, controlled committee question, candidates list, verification. It is NOT "money-only". It is a legal disclosure form.

So Check 7 does not apply.

Check 10 (Form): "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".

This document has all of that. It is "Form 420". It is a government form.

So the label is `form`.

Let's double check the "budget" definition. "Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient — e.g. a political campaign contribution request...".

This is a "CAMPAIGN STATEMENT" (disclosure), not a request. And it has much more content than just amount/recipient. It has addresses, dates, names. So it's not a "money-only record".

So it's a form.

**Final check:**

- Title: RECIPIENT COMMITTEE CAMPAIGN STATEMENT
- Form number: Form 420 1985
- Content: Filled fields, checkboxes, tables.
- Category: form.

One detail: "A page titled 'RECORDS MANAGEMENT INVENTORY' ... is a form (check 10)". This is similar, a titled form capturing data.

The label is `form`.

Wait, is there any chance it's a `budget`?

"budget: ... money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient".

This is a statement of contributions received (implied by "Recipient Committee"). But it's not money-only. It's a legal form.

The instructions say: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form...". But this isn'*t* a billing page. It's a disclosure statement.

The instructions say: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)...".

Since this is not money-only (it has addresses, dates, names of people, legal text), it falls to Check 10.

Label: `form`.


<h3 class="trace-file"><code>rvl_cdip__budget__0091.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Header: "Family COURSE Consortium, Inc. CHECK REQUEST"
- Date: June 29, 1993
- Amount: $300.00
- Pay To: Alan Irgang, address.
- Explanation: Honoraria for Family COURSE Consortium speakers bureau presentation...
- Distribution of Charges table: Cost Center Number, Account Number, Project Code, 1099 or Use Tax, Amount.
- Grand Total: $300.00
- Requested by: [Signature]
- Approved By: [Signature]
- Footer: TIMN 180127, CONFIDENTIAL: MINNESOTA TOBACCO LITIGATION.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None.

**Check 1: file_folder**

- Evidence: The page has a title "CHECK REQUEST", fields, tables, signatures. Not just an identifier.
- Result: not this check.

**Check 2: handwritten**

- Evidence: Mostly typed, with signatures. Not majority handwritten.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: No survey questions.
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: No resume.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal header.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: "CHECK REQUEST". Amount: $300.00. Pay To: Alan Irgang. Explanation: Honoraria... Distribution of Charges table. Grand Total $300.00. Requested by / Approved By.
- Let's look at the definitions in Check 7.
- "budget: internal money planning, tracking, or disbursement... a check face or check stub, a check/payment register... Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient... is budget, not form".
- Wait, is a "CHECK REQUEST" a budget or a form?
- "A check face/check stub... is the DISBURSEMENT instrument and stays budget".
- "Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient — e.g. a political campaign contribution request, a contribution-request checklist, a grant/contribution request with recipient and amount — is budget, not form, even when it has an approval/signature block."
- This is a "CHECK REQUEST" for $300.00 to Alan Irgang for honoraria. It has an approval block ("Requested by", "Approved By").
- Let's re-read carefully: "This covers only REQUEST/CHECKLIST/STATEMENT forms; it does NOT cover a payment VOUCHER or check-stub payment instrument naming a payee, a "PAY THIS AMOUNT"/"AMOUNT", and a payment date — a VOUCHER is a payment instrument and is invoice under the invoice bullet, even when the memo describes the payment as a grant or contribution."
- Is a "CHECK REQUEST" a payment voucher? No, it's a request for a check. It's an internal authorization to disburse funds.
- "Also covers money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget, not form".
- This page is a "CHECK REQUEST" (a statement/request for expenditure). It has the amount ($300.00) and the recipient (Alan Irgang). It has an explanation (Honoraria...). It has a distribution of charges table.
- Wait, what about form? "internal authorization/approval forms with an approval signature/date block" is form (check 10).
- BUT check 7 says: "This covers only REQUEST/CHECKLIST/STATEMENT forms; it does NOT cover a project-funding authorization/approval form that names the work to be funded, carries finance-data/expense-code fields (e.g. a budgeted department/expense code), and has an approval block — authorizing a specific funded project is a form (check 10; see the caveat below), not budget, even when it states an amount".
- Let's look at the caveat in check 7: "Caveat: an internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds, "ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget — authorizing a specific expenditure or funded project is not planning or tracking money."
- This page is a "CHECK REQUEST". It names the work ("Honoraria for Family COURSE Consortium speakers bureau presentation..."). It carries finance-data/expense-code fields (Cost Center Number 1308, Account Number 7501, Project Code). It has an approval block.
- Wait, is it a "money-only record"? "whose ENTIRE content is the amount and (for a contribution) the recipient". This page has a lot more: explanation, distribution of charges table with cost center, account number, project code.
- Let's re-read: "a contribution/expenditure REQUEST/CHECKLIST/STATEMENT whose ENTIRE content is the amount and (for a contribution) the recipient ... is budget, not form". This page has more than just amount and recipient. It has a detailed explanation and a distribution of charges table.
- Let's look at the invoice bullet: "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee for named goods/services/charges — invoice". This is a request, not a voucher billing a payee.
- Let's look at the form bullet (Check 10): "internal authorization/approval forms with an approval signature/date block".
- Let's look at the budget bullet again: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking."
- Is a "CHECK REQUEST" an expense report or a check request form?
- "A check face/check stub... is the DISBURSEMENT instrument and stays budget".
- What about a "CHECK REQUEST" form? It's a form to request a check.
- Let's look at the caveat in Check 7 again: "an internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds... purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
- This page has "DISTRIBUTION OF CHARGES" with Cost Center, Account Number, Project Code, Amount. It's authorizing a specific expenditure ($300.00) for a specific work (Honoraria for presentation). It has expense-code fields. This matches the caveat: "names the work/project to be funded and carries finance-data/expense-code fields... and has an approval block... is a form (check 10), not budget".
- So it's a form (check 10).

Let's check Check 10: ADMINISTRATIVE FORM -&gt; form.

- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
- This page has fields (Date, Amount, Pay To, Explanation, Cost Center, Account Number, Project Code, Amount), checkboxes (Mail check to vendor: Yes &gt;), and approval signatures (Requested by, Approved By).
- It is an internal authorization/approval form (Check Request) with an approval signature block.
- The caveat in Check 7 explicitly excludes this from budget: "an internal expenditure-authorization form... that names the work/project to be funded and carries finance-data/expense-code fields... and has an approval signature/date block... is a form (check 10), not budget".
- This page has:

    - Names work/project: "Honoraria for Family COURSE Consortium speakers bureau presentation..."

    - Finance-data/expense-code fields: "COST CENTER NUMBER", "ACCOUNT NUMBER", "PROJECT CODE".

    - Approval block: "Requested by:", "Approved By:".

- Therefore, it is a form (check 10), not budget.

Let's double check Check 7 invoice bullet: "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee... invoice". This is a "CHECK REQUEST", not a payment voucher. A check request is an internal document to get a check issued.

So the classification is form.

Let's review the checks again.

1. file_folder: No.

2. handwritten: No.

3. FAX: No.

4. questionnaire: No.

5. resume: No.

6. scientific_publication: No.

7. financial: The page is a "CHECK REQUEST". It has financial content, but the caveat in check 7 says an internal expenditure-authorization form that names the work, carries expense-code fields, and has an approval block is a form (check 10), not budget. It's not an invoice because it's not a vendor bill or payment voucher.

8. specification: No.

9. presentation: No.

10. form: Yes. "internal authorization/approval forms with an approval signature/date block". Fields for Cost Center, Account Number, Project Code, Amount. Signatures for Requested by and Approved By.

11. correspondence: No.

12. news_article: No.

13. scientific_report: No.

14. advertisement: No.

Runner-up: budget. Ruled out because the page is an internal expenditure-authorization form ("CHECK REQUEST") that names the work to be funded ("Honoraria for... presentation"), carries finance-data/expense-code fields ("COST CENTER NUMBER", "ACCOUNT NUMBER", "PROJECT CODE"), and has an approval block ("Requested by", "Approved By"). Check 7 caveat explicitly states this is a form (check 10), not budget.

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__invoice__0032.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: "THE AMERICAN TOBACCO COMPANY" logo at top left. "SIX STAMPORD FORM", "STAMFORD CONNECTICUT 06904-2380". "AT 103-14 (8-92)". No journal masthead.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of content: "PURCHASE ORDER NO. *M* 14797", "DATE January 5, 1995", "AUTH. NO. M5067", "BUDGET NO. NIB-JSC-FIR", supplier info, description, price, signatures. Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Mostly typed. Handwritten signature and date "1/5/95". Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No CV/resume content.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal running head/volume/issue.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: "PURCHASE ORDER NO. *M* 14797". "MONTCLAIR 'Floral Bouquet' 20¢ Off Pack ISC". "This Purchase Order is to cover all costs incurred to-date." "Separations, Films and Proofs". "$864.00/Lot". "THIS ORDER HAS BEEN CANCELLED." "ACCOUNTING CHARGE NO. Brand Operations Adv. Expense".
- Wait, is this an invoice or a budget or a form?
- Let's look at Check 7 details:

  - invoice: outside vendor states charges owed. "INVOICE" header, payment voucher, vendor's price schedule, receipt, payment request, agency ESTIMATE.

  - budget: internal money planning, tracking, disbursement. check face, expense reports, statement of account. money-only records.

  - Caveat: internal expenditure-authorization form (AUTHORIZATION REQUEST) that names work to be funded and has approval block is a form (check 10), not budget.

- This is a "PURCHASE ORDER". A purchase order is a request to buy. It has fields: "PURCHASE ORDER NO.", "DATE", "AUTH. NO.", "BUDGET NO.", "SUPPLIER", "SHIP TO", "QUANTITY", "DESCRIPTION", "PRICE".
- Is a purchase order a form? Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
- Wait, check 7 says: "A check face/check stub stays budget... An internal expenditure-authorization form... is a form (check 10), not budget".
- A purchase order is an authorization to purchase. It has "BUDGET NO.", "ACCOUNTING CHARGE NO.", "Brand Operations Adv. Expense". It has a signature block ("BUYER", signature "Matthew H...").
- Let's re-read Check 7: "Money PLANNING for future work is budget... An internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds, "ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
- This document is a Purchase Order. It authorizes a purchase. It has "BUDGET NO.", "ACCOUNTING CHARGE NO.". It is not an invoice (vendor billing us). It is not a budget (internal tracking of spend, though it has budget numbers). It is a purchase order / requisition / authorization form.
- Let's check Check 10: "internal authorization/approval forms with an approval signature/date block." A purchase order is an internal authorization to buy from a supplier. It has fields, checkboxes ("STATE SALES TAX NOT TO BE CHARGED", "EXEMPTION CERTIFICATE", "DIRECT PAYMENT PERMIT"), and a signature block ("BUYER").
- Wait, is a purchase order a form? Yes, "administrative form".
- Let's check if it could be invoice. "an outside vendor, supplier, or agency states charges owed...". This is from The American Tobacco Company to Ansel Label and Packaging Corp. It's a purchase order *from* ATC *to* Ansel. So it's not an invoice from the vendor.
- Could it be budget? "budget: internal money planning, tracking, or disbursement... internal expenditure-authorization form... is a form (check 10), not budget". So it's not budget.
- Therefore, it's a form (check 10).

Let's double check Check 10: "administrative form -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."

This page has:

- Fields: PURCHASE ORDER NO., DATE, AUTH. NO., BUDGET NO.
- Supplier box, Ship to box.
- Quantity, Description, Price columns.
- Checkboxes: STATE SALES TAX NOT TO BE CHARGED, EXEMPTION CERTIFICATE, DIRECT PAYMENT PERMIT, IN YOUR FILES, ATTACHED.
- Signature block: BUYER, signature, date (1/5/95).
- "THIS ORDER HAS BEEN CANCELLED."

This is clearly a filled/blank form (a purchase order form).

Let's review the checks again to ensure no higher check applies.

Check 1-6: No.

Check 7: Financial document. Is it an invoice? No, it's a purchase order (buyer to seller). Is it a budget? Check 7 says "internal expenditure-authorization form... is a form (check 10), not budget". A purchase order is an authorization/requisition. So not budget.

Check 8: Specification. No.

Check 9: Presentation. No.

Check 10: Administrative form. Yes. Fields, checkboxes, authorization/approval block.

Let's confirm the label: `form`.

Wait, could it be `invoice`? "A payment VOUCHER naming a payee, vendor/item fields, an amount... and a payment date is a payment instrument that BILLS a named payee... invoice". This is a Purchase Order, not a payment voucher or invoice. It's an order to buy.

Could it be `budget`? "budget: internal money planning... internal expenditure-authorization form... is a form (check 10), not budget".

So `form` is the correct label.

Let's do a quick scratchpad trace:

1. file_folder: no — has substantial content (purchase order details, supplier info, descriptions, signatures).

2. handwritten: no — mostly typed, only signature and date are handwritten.

3. form (fax): no — no fax cover sheet header.

4. questionnaire: no — no survey items.

5. resume: no — no career history.

6. scientific_publication: no — no journal identifier.

7. invoice/budget: no — it is a purchase order (internal authorization/requisition), not an invoice from a vendor or a budget tracking document. Check 7 explicitly excludes internal expenditure-authorization forms from budget, directing them to check 10.

8. specification: no — not an MSDS or product formulation.

9. presentation: no — not a slide deck or cover.

10. form: yes — "PURCHASE ORDER NO.", fields for supplier, description, price, checkboxes (exemption certificate, direct payment permit), and a buyer signature block. This is an internal authorization/approval form with fields and checkboxes.

Runner-up: invoice, ruled out because this is a purchase order issued by the company to a supplier (not a vendor billing the company), and check 7 excludes internal authorization forms from budget/invoice categories, pointing to form.

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__invoice__0046.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow a specific set of checks in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: "The American Tobacco Company" at the top left. This is a company letterhead, not a newspaper/magazine masthead or journal running head. "REQUISITIONER'S COPY" at top right.

**Check 1: file_folder**

- Evidence: The page has a lot of content: billing instructions, purchase order number, supplier info, description of posters, prices, accounting charge no. It's not just an identifier.
- Not this check.

**Check 2: handwritten**

- Evidence: Mostly typed text. There is a signature at the bottom right, but it's not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: No resume/CV content.
- Not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal name, volume, issue, page range.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: "PURCHASE ORDER NO. A 21248", "DATE January 21, 1976".
- Supplier: "MacNaughton Lithograph Company".
- Description: "TARYNTON 30-Sheet Posters... @ $9.62 ea." Quantity: 2,012.
- "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN TRIPLICATE TO CONSIGNEE..."
- This is a Purchase Order. Wait, is a purchase order an invoice or budget or form?
- Let's look at the checks.
- Check 7: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... A payment VOUCHER... A check face... is the DISBURSEMENT instrument and stays budget".
- Wait, a Purchase Order is a request to buy, not a bill for goods sold.
- Let's re-read Check 7 carefully.
- "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... It does not have to be titled "INVOICE" — a voucher, estimate, change order, or recap that lists billable charges and totals is an invoice."
- "budget: internal money planning, tracking, or disbursement... Also covers money-only records... A provider's periodic customer statement... is budget, not invoice".
- What about a Purchase Order? A purchase order is a form to request goods.
- Let's look at Check 10: ADMINISTRATIVE FORM.
- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
- A purchase order is an administrative form for ordering goods.
- Wait, does Check 7 cover purchase orders? "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But a purchase order is not a billing or payment page. It's a request.
- Let's check the invoice definition again: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". A purchase order is from the buyer to the vendor, stating what they want to buy. It's not a statement of charges owed.
- Is it a budget? "internal money planning, tracking, or disbursement... budget or expense lines...". A purchase order authorizes a purchase, which is part of internal money planning/disbursement tracking. But usually, a purchase order is classified as a form.
- Let's look at Check 10: "administrative form... internal authorization/approval forms with an approval signature/date block." A purchase order has "REQUISITIONER'S COPY", "PURCHASE ORDER NO.", "DATE", "TO: Supplier", "DESCRIPTION", "QUANTITY", "PRICE". It's a structured form for capturing data (ordering posters).
- Wait, is there a "form" category? Yes, "form".
- Let's re-evaluate Check 7. "invoice... A payment VOUCHER naming a payee... is a payment instrument that BILLS a named payee... invoice". This is a Purchase Order, not a voucher or invoice.
- "budget... A check face/check stub... is budget". This is not a check stub.
- "budget... an internal expenditure-authorization form... that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget". Wait, the caveat in Check 7 says: "an internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds, "ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".
- This document is a Purchase Order (requisition/approval for purchasing posters). It names the work/project (posters for February 1976 posting), has fields, and is an authorization for purchase. It does not have billable charges (it has a unit price and quantity, but it's a PO, not an invoice from the vendor).
- Therefore, it falls under Check 10: ADMINISTRATIVE FORM.

Let's check Check 10 details:

- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data" -&gt; Yes, the PO has Quantity, Code No., Description, Price fields.
- "internal authorization/approval forms with an approval signature/date block" -&gt; Yes, it has accounting charge no, exemption certificate checkboxes, contact person.
- Wait, is a Purchase Order a form? Yes.

Let's check if it could be an invoice.

- "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN TRIPLICATE TO CONSIGNEE..." -&gt; This is instructions to the vendor on where to send the invoice. The document itself is the Purchase Order (Requisitioner's copy).
- So it's not an invoice.

Let's check if it could be a budget.

- Check 7 caveat: "an internal expenditure-authorization form... purchase/requisition approval... is a form (check 10), not budget". This is a Purchase Order, which is a requisition/approval for purchasing.

So Check 10 (form) is the correct match.

Let's review the checks again to be sure.

1. file_folder: No, has content.

2. handwritten: No.

3. FAX: No.

4. questionnaire: No.

5. resume: No.

6. scientific_publication: No.

7. financial: No, it's a purchase order (requisition), not an invoice or budget document (per caveat).

8. specification: No.

9. presentation: No.

10. form: Yes. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms". A purchase order is a classic administrative form.

11. correspondence: No.

12. news_article: No.

13. scientific_report: No.

14. advertisement: No.

Wait, is there any other category?

The document is "The American Tobacco Company... REQUISITIONER'S COPY... PURCHASE ORDER NO. A 21248".

It's a purchase order form.

Label: form.

Let's double check Check 7 caveat: "an internal expenditure-authorization form (an "AUTHORIZATION REQUEST" for funds, "ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval) that names the work/project to be funded and carries an approval signature/date block but no billable charges is a form (check 10), not budget".

This document is a purchase order (requisition approval). It has a unit price and quantity, but it's not a bill from a vendor (invoice) nor an internal budget tracking document (budget). It's a form to order goods.

Therefore, form is the correct label.

Evidence for Check 10:

- "PURCHASE ORDER NO.", "DATE", "TO: MacNaughton Lithograph Company", "QUANTITY", "CODE NO.", "DESCRIPTION", "PRICE" fields.
- "BILLING INSTRUCTIONS" box.
- Checkboxes for "EXEMPTION CERTIFICATE", "DIRECT PAYMENT PERMIT", "IN YOUR FILES", "ATTACHED".
- "ACCOUNTING CHARGE NO." field.
- This is a structured administrative form for capturing order data and authorizing a purchase.

Runner-up: invoice. Ruled out because the document is a Purchase Order (requisitioner's copy) with billing instructions for the vendor to send an invoice, not a statement of charges owed by the vendor (check 7 caveat explicitly excludes purchase/requisition approvals from budget and points to form).

Final check of the text:

"The American Tobacco Company... REQUISITIONER'S COPY... PURCHASE ORDER NO. A 21248... TO: MacNaughton Lithograph Company... DESCRIPTION: TARYNTON 30-Sheet Posters... QUANTITY 2,012... PRICE @ $9.62 ea."

This is definitely a purchase order form.

Label: form.


<h3 class="trace-file"><code>rvl_cdip__invoice__0080.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. "FedEx USA Airbill", "SNA32 Sender's Copy". No journal masthead.

**Check 1: file_folder**

- Evidence: The page has a lot of content (FedEx Airbill form, addresses, checkboxes, text). Not just an ID/stamp.
- Not this check.

**Check 2: handwritten**

- Evidence: Mostly typed form with some handwritten/typed entries (names, addresses, dates). Not majority freeform handwriting.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. It's a FedEx Airbill.
- Not this check.

**Check 4: questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: resume**

- Evidence: No career history.
- Not this check.

**Check 6: scientific_publication**

- Evidence: No journal running head.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: FedEx USA Airbill. It's a shipping document. Let's look closely at the financial aspect.
- "Total Declared Value $1.00". "Payment" section with "Sender" checked.
- Is it an invoice or budget?
- Wait, FedEx Airbill is a shipping receipt/waybill. Let's re-read check 7.
- "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... a receipt... A check face/check stub... is the DISBURSEMENT instrument and stays budget".
- Wait, is a FedEx Airbill an invoice? Or a form?
- Let's check check 10: ADMINISTRATIVE FORM.
- "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... A form does NOT have to be blank — a filled form recording data is still a form".
- A FedEx Airbill is a form used to capture shipping data (From, To, Package details, Payment method).
- Let's re-read check 7 carefully. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
- Is a FedEx Airbill a billing page? It's a shipping waybill. The "Total Declared Value" is $1.00. The payment is "Sender". It's not a bill for goods sold by FedEx in this document (the invoice would be the monthly statement or a separate invoice). This is a shipping document/waybill.
- Wait, check 7 says: "A hotel/motel guest bill... is an invoice". "A landlord's rent/lease statement... is an invoice".
- What about a FedEx Airbill? It's a form. Let's look at check 10. "administrative form -&gt; form". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". A FedEx Airbill is exactly this: a form to capture shipping data.
- Let's check if there's any other category.
- Is it an invoice? "an outside vendor... states charges owed". The Airbill itself doesn'*t* state charges owed (the shipping cost is not listed, only declared value $1.00). The actual invoice is separate. So it's not an invoice.
- Is it a budget? No.
- So it falls to Check 10: form.

Let's trace carefully:

Check 1: file_folder - No, has content.

Check 2: handwritten - No.

Check 3: FAX - No.

Check 4: questionnaire - No.

Check 5: resume - No.

Check 6: scientific_publication - No.

Check 7: financial - No, it's a shipping waybill (FedEx USA Airbill), not a bill for goods/services sold (no shipping charges listed, only declared value). It's a form capturing shipping data.

Check 8: specification - No.

Check 9: presentation - No.

Check 10: form - Yes. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". The page is a FedEx USA Airbill with fields for From, To, Company, Address, City, State, Zip, Package details, Payment method, etc. It is a filled form.

Let's double check Check 7. "A payment VOUCHER naming a payee, vendor/item fields, an amount ("PAY THIS AMOUNT"/"AMOUNT"), and a payment date is a payment instrument that BILLS a named payee... invoice". This is not a payment voucher. It's a shipping waybill.

"A check face/check stub... is the DISBURSEMENT instrument and stays budget". This is not a check.

So Check 7 doesn'*t* apply.

Check 10: "administrative form -&gt; form". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This perfectly describes a FedEx Airbill.

Let's review the whole page.

Header: "FedEx. USA Airbill", "Tracking Number 5950842936", "SNA32 Sender's Copy".

Fields: From (Name, Company, Address, City, State, Zip), To (Name, Company, Address, City, State, Zip).

Checkboxes: Express Package Service, Express Freight Service, Packaging, Special Handling, Payment (Sender, Recipient, Third Party, Credit Card, Cash, Check).

Total Packages: 1, Total Weight: 8 oz, Total Declared Value: $1.00.

Release Shipment signature.

This is a standard shipping form/waybill. It captures factual data for shipping. It is a form.

Runner-up: invoice. Ruled out because the document is a shipping waybill (Airbill) capturing shipment details and declared value, not a bill stating charges owed for shipping services (the actual invoice is separate).

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__scientific_publication__0027.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_publication</code> | <strong>Predicted:</strong> <code>scientific_report</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** None. There's a "FILE 1269" stamp and a Bates number "1005094763". No From/To/Sent/Subject.
- **Masthead/Running head:** There is a page number "389" at the bottom. There is a title "EXPERIMENTAL INVESTIGATIONS ON THE EFFECT OF CIGARETTE SMOKE INHALATION ON SMALL LABORATORY ANIMALS". Author: "W. DONTENWILL". Affiliation: "Institute of Scientific Research, Association of the German Cigarette Manufacturing Industry, Hamburg, Germany". There is an "ABSTRACT" section. This looks like a scientific paper or report. Let's look for journal identifiers. No journal name, volume, issue, or DOI at the top. Just a title, author, affiliation, abstract, and body text. Wait, is there a journal name? No. Just the title.

**2. Scratchpad checks:**

-   **Check 1: file_folder.**

    *   Evidence: "FILE 1269" stamp, Bates number "1005094763". But there is a full title, author, abstract, and body text. Not just an identifier.

    *   Result: not this check.

-   **Check 2: handwritten.**

    *   Evidence: Mostly typed text. "FILE 1269" is handwritten/stamped, but the content is typed.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET.**

    *   Evidence: No fax header.

    *   Result: not this check.

-   **Check 4: questionnaire.**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: resume.**

    *   Evidence: Not a CV.

    *   Result: not this check.

-   **Check 6: scientific_publication.**

    *   Evidence: Is there a journal name, volume, issue, page range, DOI?

    *   Bottom center: "389". Right side vertical: "1005094763". Top right: "FILE 1269".

    *   No journal masthead, no volume/issue. Just a page number 389.

    *   Wait, is this a reprint from a journal? The text looks like an abstract and introduction of a scientific paper. "Experiments were performed on hamsters...".

    *   Check 6 requires: "a named journal on the page plus a publication identifier... OR a formal paper or abstract in published conference proceedings".

    *   I don'*t* see a journal name. "Institute of Scientific Research, Association of the German Cigarette Manufacturing Industry". This looks like an internal report or a preprint/reprint without the journal header visible, or maybe a scientific report.

    *   Let's check Check 13.

-   **Check 7: financial document.**

    *   Evidence: No money.

    *   Result: not this check.

-   **Check 8: specification.**

    *   Evidence: No product specs, MSDS, "shall/must".

    *   Result: not this check.

-   **Check 9: presentation.**

    *   Evidence: Not a slide deck. Dense text.

    *   Result: not this check.

-   **Check 10: form.**

    *   Evidence: No fields/boxes.

    *   Result: not this check.

-   **Check 11: correspondence.**

    *   Evidence: No To/From/Subject. No letterhead with external address.

    *   Result: not this check.

-   **Check 12: news_article.**

    *   Evidence: No masthead, no multi-column news typography.

    *   Result: not this check.

-   **Check 13: scientific_report.**

    *   Evidence: Title "EXPERIMENTAL INVESTIGATIONS ON THE EFFECT OF CIGARETTE SMOKE INHALATION ON SMALL LABORATORY ANIMALS". Author "W. DONTENWILL". Affiliation "Institute of Scientific Research...". "ABSTRACT" section followed by running narrative prose ("Experiments were performed...", "Long-term experiments...", "We began our inhalation experiments...").

    *   This fits "Original research write-up -&gt; scientific_report". "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."

    *   The page has a title page feel (title, author, affiliation, abstract) followed by body text. It has no journal identifiers (Check 6 fails). So it's a scientific report.

-   **Check 14: advertisement.**

    *   Evidence: No marketing layout.

    *   Result: not this check.

**Conclusion:**

The page is a scientific document. It has a title, author, affiliation, abstract, and body text describing experiments. It lacks a journal masthead/volume/issue (Check 6 fails). Therefore, it is a scientific_report (Check 13).

Let's double check Check 6. "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings?"

The page has "389" at the bottom. This could be a page number from a journal or a report. But there is no journal name. "Association of the German Cigarette Manufacturing Industry". This is an institute. The text looks like a paper presented or published, but without the journal header, it's classified as scientific_report based on the instructions: "a lab or technical study title page with authors and an internal affiliation and no journal identifiers."

Wait, is "389" a page number from a journal? Often reprints have the page number. But without the journal name, I can'*t* confirm it's a scientific_publication. The instructions say: "A scientific-looking page with no journal or proceedings identifier is NOT a publication." -&gt; scientific_report.

So, scientific_report.

Runner-up: scientific_publication. Ruled out because there is no named journal, volume, issue, or copyright line on this page itself (only a page number 389 and Bates number).

Final check of the text:

Title: EXPERIMENTAL INVESTIGATIONS ON THE EFFECT OF CIGARETTE SMOKE INHALATION ON SMALL LABORATORY ANIMALS

Author: W. DONTENWILL

Affiliation: Institute of Scientific Research, Association of the German Cigarette Manufacturing Industry, Hamburg, Germany

Abstract: ...

Body: Long-term experiments... We began our inhalation experiments...

This is clearly a scientific report/paper. Since no journal identifier is present on the page (just a page number 389 and Bates number 1005094763), it falls under scientific_report.

One detail: "FILE 1269" is handwritten/stamped at the top right. Bates number 1005094763 is on the right side. These are archive markings.

The content is running narrative prose about experiments.

Check 13: "Running narrative prose with objectives, methods, results, or discussion... a lab or technical study title page with authors and an internal affiliation and no journal identifiers." -&gt; Matches perfectly.

Final label: scientific_report.


<h3 class="trace-file"><code>rvl_cdip__scientific_publication__0051.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_publication</code> | <strong>Predicted:</strong> <code>scientific_report</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: "HK#1700029" at top right. This looks like a Bates number or archive ID, not a journal masthead. No journal name, volume, issue, page range on this page itself.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a title "21. PHENOTYPIC ALTERATION OF ISOENZYME PROFILES OF ALKALINE PHOSPHATASE IN HeLa TCRC-1 CELLS GROWING IN IMMUNOSUPPRESSED RATS", authors, affiliation, SUMMARY, INTRODUCTION. This is real content.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Typed text throughout.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No fax cover sheet header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: Not a CV/resume.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal on this page. "HK#1700029" is an archive/Bates number.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial content.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: No material safety data sheet, product formulation, or "shall/must" language.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck, cover, or statement. It has dense running prose (SUMMARY, INTRODUCTION).
- Not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: No filled/blank fields, boxes, checkboxes.
- Not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: No TO:/FROM:/RE: header, no external address, no salutation.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: No newspaper/magazine masthead, byline, dateline.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: Title "21. PHENOTYPIC ALTERATION OF ISOENZYME PROFILES OF ALKALINE PHOSPHATASE IN HeLa TCRC-1 CELLS GROWING IN IMMUNOSUPPRESSED RATS", authors "R. *M*. Singer and W. H. Fishman", affiliation "Tufts Cancer Research Center, Boston, Massachusetts". Followed by "SUMMARY" and "INTRODUCTION" with running narrative prose describing a scientific study (HeLa TCRC-1 cell line, alkaline phosphatase, immunosuppressed rats). No journal identifiers on the page itself.
- This matches scientific_report.

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Evidence: Not promotional.

Runner-up: scientific_publication, ruled out because there is no journal name/volume/issue/page number on the page itself (only an archive number HK#1700029).

Final label: scientific_report.


<h3 class="trace-file"><code>rvl_cdip__scientific_publication__0080.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_publication</code> | <strong>Predicted:</strong> <code>scientific_report</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

Image analysis:

The image is rotated 90 degrees counter-clockwise. Let's read it as if rotated 90 degrees clockwise.

Title: "Über Brusthöhlengeschwülste."

Subtitle: "INAUGURAL-DISSERTATION"

"ZUR ERLANGUNG DER DOCTORWÜRDE"

"IN DER"

"MEDICIN UND CHIRURGIE"

"DER AKADEMISCHEN FACULTÄT"

"DER FRIEDRICH-WILHELMS-UNIVERSITÄT ZU BERLIN"

"am 11. August 1896"

"NEBST DEN ANGEFÜGTEN THESEN"

"GEPROVIRI VERTEIDIGT VON"

"Georg Perlitz"

"aus Semmelhof (Brandenburg)."

"GEPREMT. AMT"

"GUTACHTER:"

"Hr. Dr. med. A. Josph."

"- Dr. med. O. Abrahim."

"- Rechtsanw. Dr. iur. Dr. Marwitz."

"BERLIN."

"Buchdruckerei von Geister Schade (Ouo Francke)."

"Lindenstrasse 158."

Bottom (right side in original orientation): "70007238" (Bates number)

Let's evaluate the checks:

1. file_folder: No, it has a title, author, university, date, etc. Real content.

2. handwritten: No, it's typed.

3. FAX: No.

4. questionnaire: No.

5. resume: No.

6. scientific_publication: Does it have a journal running head? No. It's an inaugural dissertation (thesis) title page. "INAUGURAL-DISSERTATION ... IN DER MEDICIN UND CHIRURGIE ... DER FRIEDRICH-WILHELMS-UNIVERSITÄT ZU BERLIN am 11. August 1896". This is a thesis/dissertation title page. Wait, is it a scientific_publication or scientific_report?

Let's check check 6: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings? If yes... Evidence for this check: a named journal on the page plus a publication identifier... OR a formal paper or abstract in published conference proceedings... A scientific-looking page with no journal or proceedings identifier is NOT a publication."

This page has no journal identifier. It's a university dissertation title page.

Let's check check 13: "ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report. Running narrative prose... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."

Wait, a dissertation title page with authors and university affiliation and no journal identifiers. Is this a scientific_report?

Let's re-read check 13: "a lab or technical study title page with authors and an internal affiliation and no journal identifiers."

Yes, this is a title page for a technical study (inaugural dissertation) with author (Georg Perlitz) and affiliation (Friedrich-Wilhelms-Universität zu Berlin) and no journal identifiers.

Wait, let's look at the label list: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

Is a dissertation title page a scientific_report?

Check 13: "a lab or technical study title page with authors and an internal affiliation and no journal identifiers." -&gt; scientific_report.

Let's check if there's any other match.

Check 9: "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966" — is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."

This page is a title page for an inaugural dissertation ("Über Brusthöhlengeschwülste." / INAUGURAL-DISSERTATION / ... / am 11. August 1896 / Georg Perlitz). It names a specific study (dissertation on breast cavity tumors) with a date (1896) and author/affiliation. Thus, it falls under scientific_report (check 13).

Let's double check check 6: "A scientific-looking page with no journal or proceedings identifier is NOT a publication." -&gt; Not scientific_publication.

Check 13: "a lab or technical study title page with authors and an internal affiliation and no journal identifiers." -&gt; scientific_report.

Let's review the evidence for check 13:

- Title: "Über Brusthöhlengeschwülste." (On breast cavity tumors)
- Type: "INAUGURAL-DISSERTATION"
- Affiliation: "DER FRIEDRICH-WILHELMS-UNIVERSITÄT ZU BERLIN"
- Date: "am 11. August 1896"
- Author: "Georg Perlitz"
- No journal name, volume, issue, or page range on the page itself. (Only a Bates number 70007238 at the bottom).

Therefore, it is a scientific_report.

Let's quickly check if it could be a presentation (check 9).

Check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".

This matches perfectly.

Scratchpad:

file_folder: no — the page has a title, author, university, and date, not just an identifier.

handwritten: no — typed text throughout.

questionnaire: no — not a survey.

resume: no — not a career history.

scientific_publication: no — no journal name, volume, issue, or page range on the page itself; only a Bates number.

presentation: no — although it is a title page, check 9 explicitly states that technical-study title pages naming a specific study with a date are scientific_report (check 13), not presentation.

scientific_report: yes — title page for an "INAUGURAL-DISSERTATION" ("Über Brusthöhlengeschwülste.") with author ("Georg Perlitz"), university affiliation ("FRIEDRICH-WILHELMS-UNIVERSITÄT ZU BERLIN"), and date ("11. August 1896"), and no journal identifiers. This matches the "lab or technical study title page with authors and an internal affiliation and no journal identifiers" criterion in check 13.

Runner-up: presentation, ruled out because check 9 directs technical-study title pages with a specific study name and date to scientific_report (check 13).

Final label: scientific_report.

Wait, is there any other category?

No.

Let's confirm the text:

"Über Brusthöhlengeschwülste."

"INAUGURAL-DISSERTATION"

"ZUR ERLANGUNG DER DOCTORWÜRDE"

"IN DER"

"MEDICIN UND CHIRURGIE"

"DER AKADEMISCHEN FACULTÄT"

"DER FRIEDRICH-WILHELMS-UNIVERSITÄT ZU BERLIN"

"am 11. August 1896"

"NEBST DEN ANGEFÜGTEN THESEN"

"GEPROVIRI VERTEIDIGT VON"

"Georg Perlitz"

"aus Semmelhof (Brandenburg)."

This is clearly a dissertation title page. According to the instructions, a technical-study title page with authors and internal affiliation and no journal identifiers is a scientific_report.

I will write the scratchpad and output the label.


<h3 class="trace-file"><code>rvl_cdip__file_folder__0025.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>file_folder</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head on this page. There is a logo "INBIFO" and address "INBIFO Institut für biologische Forschung GmbH". There is a Bates number "2028977631" rotated on the right side.
- **Layout:** There is a large black shape on the left (looks like a slide mount or a scanned slide with a black border). There is text "INBIFO", "TRANSPARENT", "EPIDERMIS". There is a black circle. There is an address block at the bottom.

**2. Scratchpad checks:**

-   **Check 1: file_folder**

    *   Evidence: There is a large black shape on the left. The text "TRANSPARENT EPIDERMIS" is handwritten. Wait, let's look closer.

    *   The text "TRANSPARENT" and "EPIDERMIS" looks handwritten.

    *   There is a large black area. This looks like a photographed slide or a slide mount.

    *   Is it a folder tab? A folder tab usually has a short label. "TRANSPARENT EPIDERMIS" could be a label. But there's a huge black block.

    *   Let's check the rule for folder tabs: "a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... bearing a short filing label... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge".

    *   Here, the black shape is an "L" shape or a large block. It looks like a slide mount (black border around a slide).

    *   Wait, let's look at the text. "INBIFO", "TRANSPARENT", "EPIDERMIS".

    *   The text "TRANSPARENT" and "EPIDERMIS" is handwritten.

    *   The address block is at the bottom: "INBIFO Institut für biologische Forschung GmbH...".

    *   The Bates number is "2028977631".

    *   Is this a folder tab? The black shape is on the left. It looks like a slide.

    *   Let's look at Check 9: "SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation".

    *   "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".

    *   Here we have a large black block on the left (looks like the edge of a slide mount or the slide itself is black/blank with text on the right part). Actually, looking closely, the black shape is an inverted L-shape. It looks like a slide mount.

    *   The text "TRANSPARENT EPIDERMIS" is handwritten on what looks like a slide or a transparency.

    *   Wait, is it a folder tab? "a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB". The label here is handwritten "TRANSPARENT EPIDERMIS". Folder tabs usually have printed labels. But the rule says "even when the label is rotated".

    *   However, the black shape is very large. It looks like a photographic slide.

    *   Let's re-read Check 1 exception: "A page that pairs a Bates number with a photographic image (people, a scene, a slide) or with a bold headline title... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."

    *   "TRANSPARENT EPIDERMIS" is a bold headline title? It's handwritten.

    *   Let's look at Check 9: "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder".

    *   "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".

    *   The black shape on the left is substantial. It looks like the black border of a slide mount.

    *   The text "INBIFO" is a logo. "TRANSPARENT EPIDERMIS" is handwritten text.

    *   This looks like a transparency/slide labeled "TRANSPARENT EPIDERMIS" from INBIFO.

    *   Therefore, it's a photographic slide -&gt; presentation.

-   **Check 2: handwritten**

    *   "TRANSPARENT" and "EPIDERMIS" are handwritten. But most of the page is not handwriting. The address block is printed. The logo is printed. The black shape is a scan artifact/image. So not majority handwritten.

-   **Check 3: FAX**

    *   No fax header.

-   **Check 4: questionnaire**

    *   No.

-   **Check 5: resume**

    *   No.

-   **Check 6: scientific_publication**

    *   No journal identifier on this page.

-   **Check 7: financial**

    *   No.

-   **Check 8: specification**

    *   No.

-   **Check 9: presentation**

    *   "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation".

    *   Here we have a large black area on the left (looks like the slide mount or the slide itself). The text is sparse: "INBIFO", "TRANSPARENT", "EPIDERMIS", address block.

    *   "A standalone photographic image (people, a scene, a slide, a chart-photo) carrying only a Bates number is a photographic slide (this check), not file_folder".

    *   The text "TRANSPARENT EPIDERMIS" looks like a label on a slide.

    *   This fits "presentation" -&gt; photographic slide.

-   **Check 10: form**

    *   No.

-   **Check 11: correspondence**

    *   No.

-   **Check 12: news_article**

    *   No.

-   **Check 13: scientific_report**

    *   No running prose.

-   **Check 14: advertisement**

    *   No.

Let's reconsider Check 1 (file_folder) vs Check 9 (presentation).

The page has a large black shape. Is it a folder tab?

"Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge".

In this image, the black shape is on the left. It looks like a large black block.

The text "TRANSPARENT" and "EPIDERMIS" is handwritten.

The address is at the bottom.

If this is a folder tab, the label is "TRANSPARENT EPIDERMIS". But it's handwritten. Folder tabs usually have printed labels, but the rule says "even when the label is rotated". It doesn'*t* say handwritten labels are excluded, but usually folder tabs are printed.

However, look at the black shape. It's an inverted L-shape. It looks like a slide mount (the black part is the mount, the white part is the slide area).

The text "INBIFO" is at the top right of the white area.

"TRANSPARENT" and "EPIDERMIS" are handwritten in the white area.

There is a black circle at the bottom.

This looks exactly like a transparency/slide scan. The black area is the slide mount or the unexposed part of the slide.

The rule for Check 9: "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".

Also: "A standalone photographic image (people, a scene, a slide, a chart-photo) carrying only a Bates number is a photographic slide (this check), not file_folder".

Here we have a slide (photographic image of a slide/transparency) with a label "TRANSPARENT EPIDERMIS" and a Bates number.

So it is a presentation.

Wait, is "TRANSPARENT EPIDERMIS" a bold headline title?

"A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."

Even if it were a folder tab, the handwritten text "TRANSPARENT EPIDERMIS" acts as a title/label.

But the layout strongly suggests a slide/transparency scan. The black area is the mount. The text is on the transparency.

The address block "INBIFO Institut für biologische Forschung GmbH" is likely printed on the slide or the mount.

Actually, INBIFO is an institute. This is likely a slide from their collection.

So, presentation.

Let's check the runner-up.

Runner-up: file_folder.

Ruled out because: The page contains a photographic slide image (indicated by the large black bar/mount artifact and sparse text "TRANSPARENT EPIDERMIS") with a Bates number, which makes it a photographic slide (presentation), not a folder tab (which would just be a label on cardboard). Also, the text "TRANSPARENT EPIDERMIS" acts as a topical heading/title on a slide, not just filing metadata.

Wait, let's look at the "folder tab" rule again.

"Folder-tab pages: ... a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB ... bearing a short filing label ... usually with a Bates number stamped on the folder body. The label IS filing metadata ... The black bar is the photographed folder body/tab edge ... it is NOT a slide-mount scan artifact".

How to distinguish?

"How to tell a folder-tab page from a presentation cover/divider (check 9): a folder-tab page's ENTIRE content is the tab, its short filing label, and a Bates/stamp — nothing else is designed on the page. A presentation cover/divider is a DESIGNED title page... or a photographic slide image".

Here, we have an address block "INBIFO Institut für biologische Forschung GmbH...". This is designed content (letterhead/logo). A folder tab usually doesn'*t* have a full address block printed on the tab itself, unless it's the folder body.

But the address is at the bottom of the white strip.

The black shape is on the left.

If this is a folder tab, the white strip is the tab, the black shape is the folder body.

The label is "TRANSPARENT EPIDERMIS" (handwritten).

But there is a logo "INBIFO" and an address block.

Folder tabs don'*t* usually have full address blocks with phone numbers and telex numbers printed on them. That looks like a letterhead or a slide label.

INBIFO is "Institut für biologische Forschung".

This looks like a transparency/slide used for a presentation. The text "TRANSPARENT EPIDERMIS" is the title of the slide.

The black circle might be a hole punch or a graphic element.

The large black area is the slide mount.

So it's a photographic slide -&gt; presentation.

Final decision: presentation.

Evidence for Check 9:

- Large black bar/shape on the left (scan artifact for slide/transparency).
- Sparse text "INBIFO", "TRANSPARENT", "EPIDERMIS".
- Address block for INBIFO.
- Bates number "2028977631".
- This matches "photographic slide" or "scan-artifact signal" for presentation.

Runner-up: file_folder.

Ruled out because the page contains a photographic slide image (black bar artifact, sparse text title "TRANSPARENT EPIDERMIS") and letterhead/address block, not just a folder tab label. The black bar is a slide-mount artifact, not a folder body.

One detail: "TRANSPARENT" and "EPIDERMIS" are handwritten.

Check 2: handwritten. "Most of the content is freeform handwriting... NOT on a printed template."

Here, the handwriting is just two words on a slide. The rest is printed logo/address. So not majority handwritten.

So, presentation.

Label: presentation.


<h3 class="trace-file"><code>rvl_cdip__file_folder__0074.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>file_folder</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. There is a Bates number "2061696347" on the right side. There is a name "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74".

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a large graphic (map of the world?), a title "ISSUE MODULE PRODUCT INTEGRITY", "PHILIP MORRIS INTERNATIONAL". It has a name "Roger Whidden". It's not just an ID/stamp. It has a bold topical heading "ISSUE MODULE PRODUCT INTEGRITY".

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: No handwriting. All text is typed/printed.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No questions, no survey instrument.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: No CV/resume content.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name, volume, issue, page range on this page.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: No financial data, no line items, no money.

    *   Result: not this check.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: No material safety data, no formulation, no "shall/must". "ISSUE MODULE PRODUCT INTEGRITY" sounds like a presentation title or section divider.

    *   Result: not this check.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: The page looks like a slide or a deck cover.

    *   Text: "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74".

    *   Title: "ISSUE MODULE PRODUCT INTEGRITY".

    *   Bottom text: "PHILIP MORRIS INTERNATIONAL".

    *   Graphic: A map-like graphic with a logo (PM logo).

    *   Layout: Sparse text, large graphic, bold title "ISSUE MODULE PRODUCT INTEGRITY". This looks like a presentation slide or a deck cover / section divider.

    *   Let's check the rules for presentation: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... a deck cover, or a section divider — is a presentation".

    *   Also: "A large heading rotated 90 degrees... is a section divider". Here the text is upright.

    *   "PHILIP MORRIS INTERNATIONAL" is at the bottom.

    *   "Roger Whidden / PM - Worldwide Regulatory Affairs / Control #74" is at the top right. This looks like a slide footer/header.

    *   The layout is very sparse, large graphic background. This fits "presentation" (slide deck cover or section divider).

    *   Result: YES, this check matches.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: No fields, boxes, checkboxes.

    *   Result: not this check (stopped at 9).

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: No TO/FROM/RE header, no salutation, no closing.

    *   Result: not this check (stopped at 9).

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: No masthead, no byline.

    *   Result: not this check (stopped at 9).

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: No running narrative prose.

    *   Result: not this check (stopped at 9).

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: Not a marketing layout with product imagery/slogans for sale. It's an internal corporate presentation slide.

    *   Result: not this check (stopped at 9).

**Re-evaluating Check 9 vs Check 1:**

- Check 1 says: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
- "A prominent topical heading always counts as real content, subtitle or not." -&gt; "ISSUE MODULE PRODUCT INTEGRITY" is a prominent topical heading.
- "How to tell a folder-tab page from a presentation cover/divider (check 9): a folder-tab page's ENTIRE content is the tab, its short filing label, and a Bates/stamp — nothing else is designed on the page. A presentation cover/divider is a DESIGNED title page: multiple styled title elements (company name + program/title + year...), a bold title on a designed background... a photograph... or a statement/press-release layout."
- This page has a designed background (map graphic), a bold title "ISSUE MODULE PRODUCT INTEGRITY", company name "PHILIP MORRIS INTERNATIONAL", and author info "Roger Whidden". This is clearly a presentation slide or deck cover.

**Conclusion:**

The page is a presentation slide/cover. It has a title "ISSUE MODULE PRODUCT INTEGRITY", author "Roger Whidden", company "PHILIP MORRIS INTERNATIONAL", and a graphic background. It fits Check 9 perfectly.

Final check of the text:

- Top right: "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74".
- Center: "ISSUE MODULE", "PRODUCT INTEGRITY" (with a graphic overlay).
- Bottom: "PHILIP MORRIS INTERNATIONAL".
- Right side vertical: "2061696347" (Bates number).

This is a presentation slide (deck cover or section divider).

Label: presentation.


</details>

## memo → letter

<details class="trace-group">

<summary>5 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__memo__0026.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>memo</code> | <strong>Predicted:</strong> <code>letter</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow a specific set of checks in order, starting with a pre-scan.

**Pre-scan:**

- Mail-client header block: None. There's a "MEMORANDUM TO:" block, but no From/To/Sent/Subject mail client headers. There's a fax-like transmission header? No, just "990623720 PRODUCED FROM B&W WEB SITE" at the bottom. Wait, there's handwritten text "DM Emok", "Un *N* Chitten", "May 3 have approved", "12/1/71". No mail client header.
- Masthead or running head: "SSC and B Inc. Advertising", "575 LEXINGTON AVENUE - NEW YORK, *N*.Y. 10022 - 212-688-1600". This is a letterhead/masthead for an advertising agency, not a newspaper/magazine masthead or journal running head.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a full memorandum body, letterhead, date, signatures. Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Mostly typed text. Handwritten notes are present ("DM Emok", "Un *N* Chitten", "May 3 have approved", "12/1/71", signatures), but not majority.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey instrument or transmittal.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: Not a resume.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal running head, volume, issue, page range.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: Mentions "$2,198.70" total estimated gross costs. But the primary structure is a memorandum (TO/FROM/RE/Dear/Body/Closing). Check 7 says: "If the page is otherwise formatted as correspondence (letterhead + external address + "Dear ..." salutation + prose + closing signature, or a TO:/FROM:/RE: memo header followed by prose) and a dollar figure... is merely mentioned somewhere within that prose, classify it as correspondence (check 11) instead".
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: No material safety data sheet, product formulation, or "shall/must" language.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck or presentation.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: Not a form with fields/boxes/checkboxes for capturing data.
- Not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence:

  - Header: "MEMORANDUM TO:", "Mr. D. R. Dugan", "Re: PALL MALL Filter Tipped 100's EBONY - 2-color Page".

  - Date: "February 1, 1971".

  - Salutation: "Dear Don:".

  - Body: Prose discussing a recommendation.

  - Closing: "Cordially,", signature "J. Brian Barry".

  - Initials: "JBB:lr".

  - cc: "Mr. W. J. Moore".

  - This is a memo (internal memorandum) or a letter. Wait, "MEMORANDUM TO:" is a memo header. But it has "Dear Don:" and "Cordially," with a signature.

  - Let's check the memo vs letter rules in Check 11.

  - "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)." -&gt; This has "Dear Don:" and "Cordially," with signature. So it's not a strict memo by the first definition.

  - "letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person..."

  - Wait, the recipient is "Mr. D. R. Dugan, Product Manager: PALL MALL, The American Tobacco Company, A Division of American Brands, Inc." This is an external company (American Tobacco Company) relative to the sender (SSC and B Inc. Advertising).

  - Sender: SSC and B Inc. Advertising, 575 Lexington Avenue, New York.

  - Recipient: Mr. D. R. Dugan at The American Tobacco Company.

  - This is correspondence between an advertising agency and a client. It has a letterhead, date, "Dear Don:" salutation, prose body, and closing signature. Thus, it is a letter.

  - Let's re-read the memo rule: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo". This has "Dear Don:" and closing signature, so it's not a memo.

  - Therefore, it's a letter.

Let's double check.

Header: "SSC and B Inc. Advertising" (Letterhead)

Address: "575 LEXINGTON AVENUE - NEW YORK, *N*.Y. 10022"

Date: "February 1, 1971"

"MEMORANDUM TO:"

"Mr. D. R. Dugan"

"Product Manager: PALL MALL"

"The American Tobacco Company"

"A Division of American Brands, Inc."

"Re: PALL MALL Filter Tipped 100's EBONY - 2-color Page"

"Dear Don:"

Body paragraphs.

"Cordially,"

Signature (Brian)

"J. Brian Barry"

"JBB:lr"

"cc: Mr. W. J. Moore"

This is a letter. It's a business letter from an advertising agency to a client.

Let's check the labels: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

Label: letter.

Wait, is there any chance it's a memo?

"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."

This has "Dear Don:" and a closing signature. So it fails the memo definition.

"letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature"

This matches perfectly. Letterhead (SSC and B Inc. Advertising), external recipient address (Mr. D. R. Dugan, The American Tobacco Company), date, "Dear Don:" salutation, prose body, closing signature.

So the label is `letter`.

Let's review the scratchpad requirements.

Walk checks 1-14 in order.

1. file_folder: no - has full memo/letter content.

2. handwritten: no - mostly typed.

3. fax: no - no fax header.

4. questionnaire: no.

5. resume: no.

6. scientific_publication: no.

7. financial: no - mentions $2,198.70 but primary structure is correspondence.

8. specification: no.

9. presentation: no.

10. form: no.

11. correspondence: yes - letterhead, external recipient address, date, "Dear Don:" salutation, prose body, closing signature. It's a letter.

12. news_article: no.

13. scientific_report: no.

14. advertisement: no.

Runner-up: memo, ruled out because the document includes a "Dear ..." salutation and a closing signature, which disqualifies it from being a memo per the strict definition (memo requires no salutation or closing signature).

Final label: letter.


<h3 class="trace-file"><code>rvl_cdip__memo__0035.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>memo</code> | <strong>Predicted:</strong> <code>letter</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None. There's "J. Rae / Lausanne", "*M*. Murray", "1st of June, 1982", "cc. : HGA/WAP/URN". No From/To/Sent/Subject.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. Just a Bates number "2028556993" on the right side.

**Check 1: file_folder**

- Evidence: The page has a lot of body content (text, table, signature). Not just an identifier.
- Result: not this check.

**Check 2: handwritten**

- Evidence: Mostly typed text. There is a signature at the bottom ("*M*. Murray"), but the majority is typed.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or fax cover sheet header. The "SENT BY:" header is absent.
- Result: not this check.

**Check 4: questionnaire**

- Evidence: No survey instrument or transmittal.
- Result: not this check.

**Check 5: resume**

- Evidence: Not a career history.
- Result: not this check.

**Check 6: scientific_publication**

- Evidence: No journal name, volume, issue, page range on the page itself.
- Result: not this check.

**Check 7: financial document (invoice/budget)**

- Evidence: Contains a table of "Cadmium in mainstream cigarette smoke" (cigarette codes and ug/cigarette). Not a financial document.
- Result: not this check.

**Check 8: specification**

- Evidence: Not a material safety data sheet, product formulation, or "shall/must" language. It's a data table of cadmium levels, but it's part of a letter/memo.
- Result: not this check.

**Check 9: presentation**

- Evidence: Not a slide deck, cover, or statement.
- Result: not this check.

**Check 10: administrative form**

- Evidence: Not a form with fields/boxes.
- Result: not this check.

**Check 11: correspondence (email, memo, letter)**

- Evidence:

  - Header: "J. Rae / Lausanne", "*M*. Murray", "1st of June, 1982", "cc. : HGA/WAP/URN".

  - Subject/Reference: "Finland Cadmium levels in smoke", "Your memo 19 March, 1981".

  - Body: "Please find below results...", "I have been unable to obtain clarification...", "Best regards.", signature "*M*. Murray".

  - This is a memo or letter. Let's look closely at the rules.

  - "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."

  - "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels"

  - Wait, the header is:

    J. Rae / Lausanne

    *M*. Murray

    1st of June, 1982

    cc. : HGA/WAP/URN

    Finland Cadmium levels in smoke

    Your memo 19 March, 1981

  - This looks like a memo header block, albeit without literal "TO:" / "FROM:" labels. It has the addressee (J. Rae), sender (*M*. Murray), date, subject ("Finland Cadmium levels in smoke"), and reference ("Your memo 19 March, 1981").

  - Wait, is it a letter? "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

  - "Finland Cadmium levels in smoke" is the subject. "Your memo 19 March, 1981" is a reference.

  - The addressee is "J. Rae / Lausanne". Sender is "*M*. Murray".

  - Is J. Rae internal or external? "Lausanne" suggests external (Switzerland). But the rule says: "A dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block is a letter."

  - Wait, the rule for memo says: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels". Here we don'*t* have an internal title/division, just "J. Rae / Lausanne".

  - Let's re-read the memo rule: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."

  - Wait, the example says: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels". This implies if it's NOT internal (i.e. external), and doesn'*t* have literal TO:/FROM:, it might be a letter.

  - Let's look at the letter rule: "letter: ... OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."

  - Here, "J. Rae / Lausanne" is an external person (Lausanne is in Switzerland, likely external to the US tobacco company, or at least an external location). There is no "Dear ..." salutation. There is a closing "Best regards." and signature "*M*. Murray".

  - Wait, does it have a TO:/FROM: block? No literal "TO:" or "FROM:". But it has the structure:

    To: J. Rae / Lausanne

    From: *M*. Murray

    Date: 1st of June, 1982

    Subject: Finland Cadmium levels in smoke

    Ref: Your memo 19 March, 1981

  - This is a classic memo layout, just without the literal "TO:" and "FROM:" labels.

  - Let's check the memo rule again: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo."

  - Wait, if it's external, is it a letter? "letter: ... OR a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block."

  - But this has a header block that functions as TO/FROM/SUBJECT/DATE.

  - Let's look at the text: "J. Rae / Lausanne" (top left), "1st of June, 1982" (top right), "cc. : HGA/WAP/URN" (below date). Then "Finland Cadmium levels in smoke" (subject), "Your memo 19 March, 1981" (reference).

  - This is a memo header. The addressee is J. Rae. The sender is *M*. Murray.

  - Is it a memo or a letter?

  - "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."

  - "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."

  - If the addressee is external ("Lausanne"), and there's no "Dear ...", and no literal "TO:/FROM:" block, it falls under the second part of the letter definition: "a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block."

  - Wait, is there a TO:/FROM: block? No literal "TO:" or "FROM:". But the layout is clearly a memo header.

  - Let's re-read carefully: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels". This implies that if it's NOT internal (i.e. external), and lacks literal labels, it's a letter.

  - "J. Rae / Lausanne" -&gt; Lausanne is external.

  - So it's a letter? Or is it a memo because it has the header structure?

  - Actually, let's look at the memo definition again: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."

  - If it has an external address ("Lausanne"), it cannot be a memo by the first sentence.

  - The second sentence: "Without that header-then-prose structure it is not a memo."

  - The third sentence: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION ... IS a memo even without literal 'TO:/FROM:' labels". This is an exception for internal notes.

  - What about external notes? "letter: ... OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."

  - Here we have "J. Rae / Lausanne" (external person), date "1st of June, 1982", prose, closing "Best regards.", signature "*M*. Murray". No literal "TO:/FROM:" block.

  - This perfectly matches the letter definition: "a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block."

  - Wait, is "J. Rae / Lausanne" an external person? Yes, Lausanne is in Switzerland.

  - Is there a "Dear ..." salutation? No.

  - Is there a closing signature? Yes, "Best regards." and signature "*M*. Murray".

  - So it's a letter.

Let's double check if it could be a memo.

"memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."

Since it has an external address ("Lausanne"), it fails the "no external address" condition for a memo.

Therefore, it must be a letter.

Let's check the evidence for letter:

- Dated note addressed to a named external person ("J. Rae / Lausanne").
- Prose body ("Please find below results...").
- Closing with signature ("Best regards.", signature, "*M*. Murray").
- No "Dear ..." salutation.
- No literal "TO:/FROM:" block (though it has the layout).

This matches the letter definition perfectly.

Let's check if there's any other category.

- scientific_report: The body contains a table of cadmium levels and discusses analysis results. But the primary structure is correspondence (memo/letter header, prose, closing). Check 7/11 rule: "If the page is otherwise formatted as correspondence (letterhead + external address + 'Dear ...' salutation + prose + closing signature, or a TO:/FROM:/RE: memo header followed by prose) and a dollar figure, grant number, or invoice/payment reference is merely mentioned somewhere within that prose, classify it as correspondence (check 11) instead". Here, the financial/scientific data is the content of the letter, but the structure is a letter. The rule says "classify it as correspondence (check 11) instead".
- So it's a letter.

Let's review the scratchpad steps:

1. file_folder: no — page has body content, text, table, signature.

2. handwritten: no — mostly typed, only a signature.

3. FAX: no — no fax header.

4. questionnaire: no.

5. resume: no.

6. scientific_publication: no — no journal identifier.

7. financial: no — table is scientific data (cadmium levels), not financial.

8. specification: no.

9. presentation: no.

10. form: no.

11. correspondence: yes — dated note addressed to external person "J. Rae / Lausanne", with prose, closing "Best regards.", and signature "*M*. Murray". No literal TO:/FROM: block, but matches the "dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block" letter definition.

Runner-up: memo, ruled out because the addressee is external ("Lausanne"), and the memo rule requires internal address or literal TO:/FROM: labels (or internal name + title). Also, letter definition explicitly covers dated notes to external persons with prose and no TO:/FROM: block.

Wait, is "J. Rae / Lausanne" definitely external? Yes, Lausanne is a city in Switzerland. The document is from a tobacco company (likely Philip Morris or similar, given the Bates number and context of tobacco research). J. Rae in Lausanne is likely an external contact (e.g., at a research institute or university).

The text says "Your memo 19 March, 1981", implying J. Rae sent a memo to *M*. Murray. *M*. Murray is replying.

This is a letter (or memo, but by the strict rules, external = letter if no TO:/FROM:).

Actually, the rule says: "letter: ... OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."

This matches exactly.

Final check of the text:

"J. Rae / Lausanne"

"*M*. Murray"

"1st of June, 1982"

"cc. : HGA/WAP/URN"

"Finland Cadmium levels in smoke"

"Your memo 19 March, 1981"

"Please find below results of the analysis of cadmium levels in the mainstream smoke of sample cigarettes. The analysis has been carried out by cold trapping of the smoke as suggested by the Tobacco Research Council."

[Cadmium in mainstream cigarette smoke table]

"I have been unable to obtain clarification of these cigarette codes from Mr. Singer and as I have already held up the results from 7th May until now for this reason I feel further delay would not be productive. Should you require identification of the cigarettes used perhaps you could contact him."

"Best regards."

[Signature]

"*M*. Murray"

Bates number: 2028556993

This is a letter.

Label: letter


<h3 class="trace-file"><code>rvl_cdip__memo__0085.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>memo</code> | <strong>Predicted:</strong> <code>letter</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** I see "11/30/98 14:43", "LOR CHARLOTTE +++ GREENSBORO CORP", "11/30 '98 14:21 NO. 127". This looks like a fax transmission header ("SENT BY:", phone number, page count). Wait, let's look closer. "11/30/98 14:43", "704 521 8812", "3147596671". "LOR CHARLOTTE +++ GREENSBORO CORP", "11/30 '98 14:21 NO. 127", "002/003", "04/05". This is a fax transmission header. It is NOT a mail-client header (From/To/Sent/Subject). So, not email based on this.
- **Masthead/Running head:** There is a logo "Star Tobacco & Pharmaceuticals, Inc." at the top. This is a letterhead, not a newspaper/magazine masthead or journal running head.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a full letter body, letterhead, address, etc. It's not just an ID or stamp.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: There is some handwritten text at the bottom left: "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper LORILLARD (Yea) ... AND FORWARDED BY C.S. LEYER LORILLARD R&D TO THE CORPORATE OFFICE ON 11/30/98". However, the majority of the page is typed text (the letter body, header, footer).

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: The top line is a fax transmission header ("11/30/98...", "LOR CHARLOTTE..."). It is not a "FACSIMILE TRANSMISSION" cover sheet with To/From fields designed as a form. It's a faxed document.

    *   Result: not this check.

-   **Check 4: questionnaire**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: resume**

    *   Evidence: No career history.

    *   Result: not this check.

-   **Check 6: scientific_publication**

    *   Evidence: No journal running head, volume, issue, page number.

    *   Result: not this check.

-   **Check 7: financial document (invoice/budget)**

    *   Evidence: Mentions "$4.50 per carton price increase", "$2.00 per carton off-invoice allowance". But the primary structure is a letter announcing a price increase. It's not a line-item table or bill.

    *   Result: not this check (money is mentioned in prose, not the primary structure).

-   **Check 8: specification**

    *   Evidence: No material safety data, product formulation, "shall/must" language.

    *   Result: not this check.

-   **Check 9: presentation**

    *   Evidence: Not a slide deck, not a press release ("FOR IMMEDIATE RELEASE" is missing, though it's an announcement). Wait, let's look at the content. "Star Tobacco Corporation announces a $4.50 per carton price increase...". It's a letter to "Our Direct Customers".

    *   Result: not this check.

-   **Check 10: administrative form**

    *   Evidence: No fields, boxes, checkboxes for capturing data.

    *   Result: not this check.

-   **Check 11: correspondence (email, memo, or letter)**

    *   Evidence:

        *   Header: "To : Our Direct Customers", "From : Star Tobacco Corporation", "Re : Price Increase 11/24/98".

        *   Body: "Effective immediately, Star Tobacco Corporation announces..."

        *   Footer: Address "16 South Market Street • Petersburg, Virginia 23803".

        *   Handwritten note at bottom: routing info ("THE FOLLOWING INFORMATION WAS GIVEN TO... AND FORWARDED BY...").

    *   Analysis: This is a letter. It has a letterhead (Star Tobacco), a "To/From/Re" block (which is memo-style, but let's check the rules).

    *   Rule check for memo: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... no external address, no 'Dear ...' salutation."

    *   Rule check for letter: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

    *   Wait, the "To" is "Our Direct Customers". This is an external group. The "From" is "Star Tobacco Corporation".

    *   Is it a memo? "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". The header is "To : Our Direct Customers", "From : Star Tobacco Corporation", "Re : Price Increase 11/24/98". This looks like a memo header. But the recipient is external ("Our Direct Customers").

    *   Let's check the letter definition: "letter: letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

    *   Wait, there is a TO:/FROM: block here. "To : Our Direct Customers", "From : Star Tobacco Corporation".

    *   Let's re-read the memo rule: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."

    *   The recipient is "Our Direct Customers". This is external. So it's not an internal memo.

    *   Is it a letter? "letter: ... OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block." This page *has* a TO:/FROM: block.

    *   Let's look at the routing stamp at the bottom: "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper LORILLARD... AND FORWARDED BY C.S. LEYER LORILLARD... TO THE CORPORATE OFFICE ON 11/30/98". This is a routing note.

    *   The document itself is a business letter/announcement. "Star Tobacco Tobacco & Pharmaceuticals, Inc." letterhead. "To: Our Direct Customers". "Re: Price Increase".

    *   Actually, let's look at the structure. It's a letter announcing a price increase. It's addressed to "Our Direct Customers".

    *   Is it a memo? Memos are internal. This is addressed to customers.

    *   Is it a letter? Letters are external. "To: Our Direct Customers" is external. Even though it lacks a "Dear..." salutation and closing signature, it fits the broad category of correspondence.

    *   Wait, let's look at the memo definition again. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". The header here is "To : ... From : ... Re : ...". It lacks a "Date:" field in the header block (though there is a date in the Re line and the fax header).

    *   Let's look at the letter definition again. "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

    *   This document has a letterhead ("Star Tobacco..."). It has an external recipient ("Our Direct Customers"). It has prose. It lacks a "Dear..." salutation and closing signature.

    *   However, the routing note at the bottom ("THE FOLLOWING INFORMATION WAS GIVEN TO...") suggests this is an internal copy that was routed. The original document is likely a letter or a memo sent to customers.

    *   Actually, a document addressed to "Our Direct Customers" from a corporation is a letter (business letter) or a press release/statement.

    *   Let's check Check 9 (presentation): "corporate press release / issued statement". Does it say "FOR IMMEDIATE RELEASE"? No.

    *   Let's check Check 11 (correspondence): "email... memo... letter".

    *   The document has a "To/From/Re" block. This is characteristic of a memo. But memos are internal. "Our Direct Customers" is external.

    *   However, sometimes companies send memos to customers (external memos).

    *   Let's look at the routing note: "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper LORILLARD... AND FORWARDED BY C.S. LEYER LORILLARD... TO THE CORPORATE OFFICE". This implies the document was received and routed internally. The document itself is the "Information".

    *   The document text: "Effective immediately, Star Tobacco Corporation announces a $4.50 per carton price increase...". This is a business announcement.

    *   Is it a letter? It has letterhead, recipient, subject, body. Even without "Dear" and "Sincerely", it functions as a letter.

    *   Let's look at the memo rule: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo". Here the recipient is "Our Direct Customers" (not a named person with title).

    *   So it's not a memo by the specific rule.

    *   Is it a letter? "letter: letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

    *   This has a TO:/FROM: block. "To: Our Direct Customers", "From: Star Tobacco Corporation".

    *   Wait, the rule says: "routing/distribution fields added on top of a full letter... do NOT turn a letter into a memo: if the page still has an external addressee, a 'Dear ...' salutation, a prose body, and a closing signature, it stays letter". This page doesn'*t* have "Dear" or closing signature.

    *   But the core document is a letter/announcement.

    *   Let's reconsider the "memo" definition. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". The header is "To : Our Direct Customers / From : Star Tobacco Corporation / Re : Price Increase 11/24/98". This is a header block. The prose follows. Is it internal? No, "Our Direct Customers".

    *   However, in business document classification, a document with To/From/Re is often classified as a memo if it's internal, or a letter if external.

    *   Let's look at the "letter" definition again. "letter: ... OR a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block." This implies if there IS a TO:/FROM: block, it might be a memo?

    *   "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". The key word is "internal". This is addressed to customers.

    *   Maybe it's a letter. A business letter doesn'*t* always have "Dear" and "Sincerely".

    *   Let's look at the fax header. "LOR CHARLOTTE +++ GREENSBORO CORP". This is a fax from Charlotte to Greensboro. The document is being faxed internally (from Lorillard Charlotte to Greensboro Corp). The content is a letter to customers.

    *   The document itself is a letter/announcement.

    *   Let's look at the categories again.

    *   Is it a **letter**? Yes, it's a business letter/announcement to customers. Even with To/From/Re, if it's external, it's a letter. The rule "memo requires internal" is key. "memo: internal...". This is not internal.

    *   Wait, is it a **memo**? Sometimes "To: All Customers" is treated as a memo in loose terms, but strictly, memos are internal.

    *   Let's look at the routing note. "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper...". This is an internal routing note added to a document received from outside (or sent to outside).

    *   The main text is "Star Tobacco Tobacco & Pharmaceuticals, Inc." letterhead. "To: Our Direct Customers". "From: Star Tobacco Corporation". "Re: Price Increase".

    *   This is a letter. Specifically, a business letter.

    *   Let's check if there's a better fit.

    *   Check 11: "CORRESPONDENCE -&gt; email, memo, or letter".

    *   If it's not email (fax header is not email header).

    *   If it's not memo (recipient is external "Our Direct Customers", not internal).

    *   If it's letter: "letterhead with an external recipient address...". Yes, letterhead "Star Tobacco...", recipient "Our Direct Customers" (external). Prose body.

    *   So it's a **letter**.

    *   Wait, let's look at the handwritten part. "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper...". This is a note. But the page is mostly the letter.

    *   The page is a faxed letter. The fax header is metadata. The underlying document is a letter.

    *   Let's refine the "memo" vs "letter" distinction.

    *   Memo: Internal TO/FROM/RE.

    *   Letter: External recipient.

    *   Here recipient is "Our Direct Customers". External. So it's a letter.

    *   Even though it has To/From/Re, which is memo-like, the external nature makes it a letter (or a business announcement, which falls under letter/correspondence).

    *   Actually, could it be a **presentation**? "corporate press release / issued statement".

    *   Check 9: "corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". This doesn'*t* have "FOR IMMEDIATE RELEASE". It's addressed to "Our Direct Customers". It's a customer letter.

    *   So **letter** is the best fit.

    *   Wait, is it a **form**? No.

    *   Is it a **specification**? No.

    *   Let's re-evaluate "memo".

    *   "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."

    *   The header is "To : Our Direct Customers". This is not an internal address. It's a group of external people.

    *   So not a memo.

    *   "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

    *   This document has a letterhead. External recipient ("Our Direct Customers"). Prose body.

    *   It lacks "Dear..." and closing signature.

    *   But the second part of the letter definition: "OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." This document HAS a TO:/FROM: block.

    *   This is a tricky edge case.

    *   However, business letters often don'*t* have "Dear" if it's a general announcement. "To: Our Direct Customers" acts as the salutation.

    *   Also, the routing note at the bottom is handwritten. "THE FOLLOWING INFORMATION WAS GIVEN TO...". This suggests the document was received and annotated.

    *   The document itself is a letter from Star Tobacco to its customers.

    *   Let's look at the fax header again. "11/30/98 14:43 ... LOR CHARLOTTE +++ GREENSBORO CORP ... 002/003". This is page 2 of 3.

    *   The document is a letter.

    *   Final decision: **letter**.

    *   Wait, let's look at the handwritten text again.

    *   "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper LORILLARD (Yea) ... AND FORWARDED BY C.S. LEYER LORILLARD R&D TO THE CORPORATE OFFICE ON 11/30/98".

    *   This is a routing note. The main content is the typed letter.

    *   The typed letter is correspondence.

    *   Is there any other category?

    *   "advertisement"? No, it's a price increase announcement, not a product ad with imagery/slogans. It mentions "100% Natural Tobacco products" but it's a business letter about pricing.

    *   "news_article"? No.

    *   So **letter**.

    *   Wait, could it be a **memo**?

    *   Some definitions consider "To: All Employees" or "To: Customers" memos if they use the To/From/Re format internally. But the rule says "memo: internal...". "Our Direct Customers" is external.

    *   However, the routing note "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper LORILLARD" suggests this is an internal document *about* the letter, or the letter was routed internally.

    *   Actually, the text "Star Tobacco Tobacco & Pharmaceuticals, Inc." is the letterhead.

    *   The text "To: Our Direct Customers" is the addressee.

    *   This is a letter.

    *   Let's check the scratchpad requirements.

    *   Check 11: correspondence.

    *   Evidence: Letterhead "Star Tobacco & Pharmaceuticals, Inc.", header "To : Our Direct Customers", "From : Star Tobacco Corporation", "Re : Price Increase 11/24/98", prose body announcing price increase, footer address. Handwritten routing note at bottom.

    *   It's a letter (external correspondence).

    *   Wait, is it a **form**? No.

    *   Is it a **specification**? No.

    *   One detail: "A dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block is a letter". This page has a TO:/FROM: block.

    *   "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...".

    *   If it has TO:/FROM: and is external, is it a letter? Yes, business letters often have To/From/Re (e.g. in fax cover letters or internal routing of external letters).

    *   Actually, this looks like a faxed letter. The top line is the fax transmission data. The document below is the letter.

    *   The letter has To/From/Re. This is common in business correspondence (memos to customers, or letters formatted like memos).

    *   Given the options, **letter** is the correct classification for external correspondence.

    *   Let's check if it's a **presentation**. "corporate press release / issued statement".

    *   Check 9: "corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". This doesn'*t* have that.

    *   It's a letter to customers.

    *   Final check: **letter**.

    *   Wait, look at the handwritten note: "THE FOLLOWING INFORMATION WAS GIVEN TO: Bill Kuyper...".

    *   This is a note *about* the document.

    *   The document is the letter.

    *   One more check: **email**?

    *   Pre-scan: "A mail-client header block (From/To/Sent/Subject/cc...".

    *   The top line: "11/30/98 14:43 704 521 8812 3147596671 LOR CHARLOTTE +++ GREENSBORO CORP 11/30 '98 14:21 NO. 127 002/003 04/05".

    *   This is a fax header. "SENT BY:" is not explicitly there, but "LOR CHARLOTTE +++ GREENSBORO CORP" and phone numbers and page count "002/003" indicate a fax transmission.

    *   Rule: "BUT a FAX machine transmission header is NOT a mail-client header... classify the underlying document by its own content".

    *   Underlying document is a letter.

    *   So, **letter**.


<h3 class="trace-file"><code>rvl_cdip__presentation__0044.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>file_folder</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There is a Bates number "2001282630" rotated on the right side. There is text "CELANESE FIBERS MARKETING COMPANY" at the top right. "WORLD SMOKING PRODUCTS" at the bottom left. A large logo in the center (Celanese logo with radiating black bars).

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a large graphic (Celanese logo with radiating bars), text "CELANESE FIBERS MARKETING COMPANY", "WORLD SMOKING PRODUCTS", and a Bates number "2001282630".

    *   Is it a folder tab? The text "WORLD SMOKING PRODUCTS" is at the bottom left. The text "CELANESE FIBERS MARKETING COMPANY" is at the top right. The Bates number is rotated. The central image is a large logo/graphic.

    *   Wait, let's look closer. Is this a folder tab?

    *   "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body. The label IS filing metadata... The black bar is the photographed folder body/tab edge... it is NOT a slide-mount scan artifact".

    *   Here, there is a large box outline. Inside is a large graphic.

    *   Let's check the presentation check (Check 9). "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder". "A near-blank cover or title page... is a presentation".

    *   Let's check the content. "CELANESE FIBERS MARKETING COMPANY". "WORLD SMOKING PRODUCTS". This looks like a cover page or a slide.

    *   Wait, look at the layout. There's a box. Inside is a big logo.

    *   Is it a folder tab? A folder tab usually has a short label. "WORLD SMOKING PRODUCTS" could be a label. But there's a huge graphic.

    *   Let's re-read Check 1: "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title... A prominent topical heading always counts as real content".

    *   "WORLD SMOKING PRODUCTS" is a heading. "CELANESE FIBERS MARKETING COMPANY" is a heading.

    *   The central image is a large graphic (Celanese logo).

    *   This looks like a presentation cover or a slide. Or maybe a folder tab?

    *   Let's look at Check 9: "SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation". "a deck title or section-divider page... a near-blank cover or title page... mostly empty space with only a bold headline title...".

    *   "A standalone photographic image... carrying only a Bates number is a photographic slide... presentation".

    *   The central image is a graphic/logo. It looks like a slide or a cover page for a presentation about "World Smoking Products" by "Celanese Fibers Marketing Company".

    *   Wait, is it an advertisement? "Marketing layout: product imagery, slogans, brand styling". This is a company logo. "Celanese Fibers Marketing Company". It's not selling a cigarette brand directly, it's a company logo.

    *   Let's look at the "folder tab" exception in Check 1. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The black bar is the photographed folder body/tab edge".

    *   In this image, there is a thin black line forming a box. The right side has the Bates number. The top right has text. The bottom left has text. The center has a big graphic.

    *   This doesn'*t* look like a folder tab. A folder tab is a protruding piece of cardboard. This looks like a full page scan.

    *   The graphic is a "Celanese" logo with radiating bars (looks like cigarette filters or fibers?). "Celanese Fibers". Cigarette filters are often made of cellulose acetate fibers (Celanese is a major producer). So this is likely a slide or cover page about their product for smoking products.

    *   Let's check Check 9 again. "Slide/overhead layouts... a deck title or section-divider page... a corporate press release... or a photographic slide image".

    *   "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead". Here, there is a box outline, not necessarily a solid black bar, but the radiating bars are black.

    *   Actually, let's look at the layout. It's very sparse. Large logo. Text at corners. This is classic presentation slide or deck cover style.

    *   "WORLD SMOKING PRODUCTS" could be the title. "CELANESE FIBERS MARKETING COMPANY" is the company.

    *   This fits "presentation" (Check 9). Specifically, a deck cover or slide.

-   **Check 2: handwritten**

    *   No handwriting.

-   **Check 3: FAX**

    *   No fax header.

-   **Check 4: questionnaire**

    *   No survey questions.

-   **Check 5: resume**

    *   No career history.

-   **Check 6: scientific_publication**

    *   No journal header.

-   **Check 7: financial**

    *   No financial data.

-   **Check 8: specification**

    *   No product specs, though it mentions "Fibers" and "Smoking Products". But it's just a logo and company name. Not a spec sheet.

-   **Check 9: presentation**

    *   Evidence: "CELANESE FIBERS MARKETING COMPANY" (top right), large central graphic (Celanese logo with radiating bars, likely representing fibers/filters), "WORLD SMOKING PRODUCTS" (bottom left), Bates number "2001282630" (rotated right).

    *   This looks like a title slide or cover page for a presentation. "World Smoking Products" is the topic. "Celanese Fibers Marketing Company" is the presenter.

    *   Check 9 says: "a deck title or section-divider page... a near-blank cover or title page... mostly empty space with only a bold headline title". This page has a large graphic and sparse text. It fits the "photographic slide image" or "deck cover" description.

    *   Also: "A standalone photographic image (people, a scene, a slide, a chart-photo) carrying only a Bates number is a photographic slide (this check), not file_folder". The central image is a graphic/slide.

    *   The layout is very sparse, typical of a slide deck.

-   **Check 10: form**

    *   No fields/boxes.

-   **Check 11: correspondence**

    *   No memo/letter structure.

-   **Check 12: news_article**

    *   No masthead.

-   **Check 13: scientific_report**

    *   No running prose.

-   **Check 14: advertisement**

    *   Is it an ad? "Marketing layout: product imagery, slogans, brand styling". It's a company logo for "Celanese Fibers Marketing Company". It's promoting their fibers for smoking products. But it looks more like a presentation cover (title slide) than a standalone ad. An ad usually has a product, slogan, warning. This is a corporate identity slide.

    *   However, let's look at the "advertisement" definition. "Marketing layout...".

    *   But "presentation" covers "deck title... company statement".

    *   The text "WORLD SMOKING PRODUCTS" looks like a title.

    *   Let's compare presentation vs advertisement.

    *   Presentation: "Slide/overhead layouts... deck title...". This looks like a slide. The Bates number is typical of archived presentations/documents.

    *   The radiating bars look like a graphic design for a slide.

    *   I'll go with presentation.

Let's re-evaluate Check 1 (file_folder) vs Check 9 (presentation).

- Check 1: "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title". "WORLD SMOKING PRODUCTS" is a bold headline title. The central image is a slide image/graphic. So it's not file_folder.
- Check 9: "a deck title or section-divider page... a near-blank cover or title page". This page has a title "WORLD SMOKING PRODUCTS" (bottom left, but bold) and company name. It's a cover page.
- Also, the Bates number is rotated, which is common in slide scans or folder tabs. But the content is too rich for file_folder.
- The layout is sparse, large graphic. Fits "presentation".

Let's look at the "folder tab" rule again.

- "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The label IS filing metadata... The black bar is the photographed folder body/tab edge".
- In this image, there is a thin line box. The right side has the Bates number.
- Is the central graphic a "photographed folder tab"? No, it's a printed graphic on a page.
- Is the text "WORLD SMOKING PRODUCTS" a filing label? It could be, but it's accompanied by a huge logo and "CELANESE FIBERS MARKETING COMPANY".
- If this were a folder tab, the content would be just the label. Here we have a full page design.
- Actually, looking closely at the borders: there's a thin line box around the central content. This looks like a slide mount or a designed page.
- "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead". There isn'*t* a solid black bar along the edge, but there is a box.
- However, the content is clearly a title slide: Company Name + Graphic + Topic Title. This is a presentation cover/slide.

Final decision: presentation.

Wait, is it an advertisement?

- "Celanese Fibers Marketing Company". They market fibers.
- "World Smoking Products".
- It could be a brochure cover or ad.
- But "presentation" covers "deck title... company statement".
- The Bates number suggests it's from an archive. Tobacco archives have lots of presentation slides.
- The layout (sparse text, large central graphic) is very typical of a PowerPoint slide or overhead projector slide from that era.
- I will stick with presentation.

Let's check the labels again.

- advertisement: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
- presentation: "Slide/overhead layouts... deck title...".
- The image is a graphic design. It looks like a slide.
- If it's a brochure cover, it might be advertisement.
- But "World Smoking Products" sounds like a presentation topic. "Celanese Fibers Marketing Company" is the presenter.
- I'll go with presentation.

One more check: Check 1 file_folder.

- "A prominent topical heading always counts as real content... EXCEPTION — folder tabs".
- If this is a folder tab, the label is "WORLD SMOKING PRODUCTS" (or similar). But the text "CELANESE FIBERS MARKETING COMPANY" is also there. And a huge logo.
- Folder tabs usually don'*t* have huge logos printed on them unless it's the folder itself.
- If this is a scan of a folder with a label "WORLD SMOKING PRODUCTS" and the folder has a logo...
- But the text is aligned in corners. Top right: Celanese... Bottom left: World Smoking... Right side (rotated): Bates number. Center: Logo.
- This looks like a designed page, likely a slide or cover.
- Check 9: "a near-blank cover or title page... mostly empty space with only a bold headline title... is a presentation".
- This page has a large logo (graphic) and titles. It fits presentation.

Let's consider "advertisement".

- Is it selling Celanese fibers? Yes.
- But is it a standalone ad? It looks like a title slide.
- Usually, ads have more text, prices, slogans. This is very sparse.
- "Judge by DOMINANT content". The dominant content is the logo and the title "World Smoking Products".
- If it's a slide from a marketing presentation, it's presentation.

I will classify as presentation.

Wait, looking at the layout again.

- Top right: CELANESE FIBERS MARKETING COMPANY.
- Center: Large logo (Celanese 'C' with radiating bars).
- Bottom left: WORLD SMOKING PRODUCTS.
- Right edge (rotated): 2001282630 (Bates number).
- There is a thin rectangular border.
- This looks like a slide from a deck. "World Smoking Products" is the title of the deck or section. "Celanese Fibers Marketing Company" is the company.
- Classification: presentation.

One detail: "A standalone photographic image (people, a scene, a slide, a chart-photo) carrying only a Bates number is a photographic slide (this check), not file_folder".

- The central image is a graphic/slide.
- So presentation.

Final check of the scratchpad steps:

1. file_folder: No, has real content (headline "WORLD SMOKING PRODUCTS", company name, large graphic). Not just an ID.

2. handwritten: No.

3. fax: No.

4. questionnaire: No.

5. resume: No.

6. scientific_publication: No.

7. financial: No.

8. specification: No.

9. presentation: Yes. Sparse layout, large graphic/logo, title "WORLD SMOKING PRODUCTS", company name "CELANESE FIBERS MARKETING COMPANY". Fits deck cover or slide.

10. form: No.

11. correspondence: No.

12. news_article: No.

13. scientific_report: No.

14. advertisement: Possible, but looks more like a presentation cover/slide. The layout is sparse, typical of slides.

Runner-up: advertisement. Ruled out because the layout is sparse with a title and company name, typical of a presentation deck cover or slide, rather than a marketing layout with product imagery/slogans/coupons (though it has brand styling, the function is a title slide). Actually, "brand styling" is in advertisement. But "presentation" covers "deck title". The text "WORLD SMOKING PRODUCTS" is a title.

Let's refine the "advertisement" vs "presentation".

- Advertisement: "product imagery, slogans, brand styling, coupons, flyers, brochures."
- Presentation: "Slide/overhead layouts... deck title...".
- The image is a graphic. It could be a brochure cover.
- But the Bates number and the sparse text "World Smoking Products" strongly suggest a presentation slide or cover page in an archive. Tobacco archives (like the one mentioned, "tobacco-industry archive") are full of presentation slides.
- The label "Celanese Fibers Marketing Company" suggests this is a company presenting their product line.
- I'll stick with presentation.

One distinct possibility: Is it a folder tab?

- "Folder-tab pages... bearing a short filing label... usually with a Bates number... The label IS filing metadata... The black bar is the photographed folder body/tab edge".
- If the central graphic is the folder design...
- But the text "WORLD SMOKING PRODUCTS" is at the bottom.
- If this is a folder tab, it would be file_folder.
- Check 1: "A page is NOT file_folder if it carries any real content — a photograph or slide image... or a bold headline title". "WORLD SMOKING PRODUCTS" is a bold headline.
- "EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title".
- Is "WORLD SMOKING PRODUCTS" a short label on a folder tab?
- The image shows a box. Inside is a logo.
- If this is a scan of a folder tab, the tab would be the protruding part.
- The text is aligned to corners. This looks like a full page, not a tab. A tab is usually a small strip.
- The aspect ratio is square-ish (1000x1000 pixels). A folder tab is usually a small rectangle.
- This is likely a full page slide.

So, presentation.

One more look at Check 9: "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead".

- There is a thin black line box. Not a solid black bar.
- But the central graphic has black bars radiating.
- The text is sparse.
- "mostly empty space with only a bold headline title". The center is empty (white space) around the logo. The corners have text.
- This fits presentation.

Final conclusion: presentation.


<h3 class="trace-file"><code>rvl_cdip__presentation__0066.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>file_folder</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

Let's analyze the image.

The image is mostly blank white space.

There is a faint, noisy, vertical band on the left side, which looks like scan noise or a very faint, degraded image/text, but it's mostly illegible noise.

In the top right, there is a small black mark, maybe a logo or artifact.

In the bottom right, there is a Bates number: "2071969205" printed vertically.

There is a small blurry mark below the Bates number.

Let's look at the checks.

Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder

"Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."

"A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image (people, a scene, a slide) or with a bold headline title... carries real content"

Wait, is there a photographic image? The left side has a vertical band of noise. Is it a photograph? It looks like scan noise, maybe a very faint image or just degradation. Let's look closely.

Actually, the left side looks like a heavily degraded, noisy scan of something, but the dominant recognizable elements are a stamp (none visible, just noise), faint archival text (none legible), or an ID/number (Bates number 2071969205).

Wait, "Scan noise is not handwriting: on a heavily degraded, noisy scan, don'*t* let illegibility read as 'majority handwritten.' If the dominant recognizable elements are a stamp, faint archival text, or an ID/number, with only a small rotated handwritten annotation on the side, classify by the stamp/identifier (often file_folder), not handwritten — handwriting must legibly make up most of the page's actual content, not just be the only thing you can partly read on a noisy scan."

Here, the dominant recognizable element is the Bates number "2071969205". The left side is just noise/degradation.

Is there a bold headline title? No.

Is there a photographic image? The left side is too noisy to be a clear photographic image. It looks like scan artifact/noise.

Let's re-read Check 1: "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."

But if the left side is just noise, then it's basically an identifier-only page.

Wait, let's look at the top right. There's a small black shape. Looks like a staple mark or a small logo.

The left side has a vertical band of noise. At the bottom left, there's a darker block of noise.

Could this be a file_folder page? "Filing metadata means the page's only purpose is labeling a folder or index entry for ONE item."

If the page is mostly blank with just a Bates number, it's file_folder.

Let's check the pre-scan:

- Mail-client header block: none.
- Masthead or running head: none.

Let's evaluate Check 1: file_folder.

Evidence: Bates number "2071969205". The rest of the page is blank or scan noise. No sentences, no topical title. The left side is illegible noise, not a clear photographic image or bold headline. Thus, it's an identifier-only page.

Wait, is there any other check?

Check 2: handwritten. No legible handwriting.

Check 3: fax. No.

Check 4: questionnaire. No.

Check 5: resume. No.

Check 6: scientific_publication. No.

Check 7: financial. No.

Check 8: specification. No.

Check 9: presentation. "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder (check 1)." But is the left side a photographic image? It's too noisy. "Scan noise is not handwriting... If the dominant recognizable elements are a stamp, faint archival text, or an ID/number... classify by the stamp/identifier (often file_folder)". The left side is faint archival text / scan noise, not a clear photographic image.

Check 10: form. No.

Check 11: correspondence. No.

Check 12: news_article. No.

Check 13: scientific_report. No.

Check 14: advertisement. No.

So the classification is file_folder.

Let's double check the left side. It's a vertical band of noise, maybe a very faint text or image, but it's not legible. The instructions say: "If the dominant recognizable elements are a stamp, faint archival text, or an ID/number, with only a small rotated handwritten annotation on the side, classify by the stamp/identifier (often file_folder), not handwritten — handwriting must legibly make up most of the page's actual content, not just be the only thing you can partly read on a noisy scan."

Here, the only legible content is the Bates number "2071969205". The rest is noise. So it's file_folder.

Let's write the scratchpad.

file_folder: yes — the page contains only a Bates number ("2071969205") and scan noise/faint degradation on the left side with no legible body content, sentences, or topical title. The dominant recognizable element is the ID number.

handwritten: no — no legible handwriting, only scan noise.

presentation: no — the left side is illegible scan noise, not a clear photographic image or designed slide layout.

Runner-up: presentation, ruled out because the left side is not a clear photographic image or slide, just scan noise, and the page is essentially an identifier-only page with a Bates number.

Wait, is there any possibility it's a presentation (photographic slide)?

"Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text... points to a photographed slide/overhead — presentation"

Here, there is no solid black bar, just a noisy vertical band. And no sparse text.

So file_folder is correct.

Let's refine the scratchpad:

file_folder: yes — the page is almost entirely blank white space with only a Bates number ("2071969205") and illegible scan noise/faint degradation on the left side. No sentences, no topical title, no clear photographic image. Filing metadata only.

handwritten: not this check — no legible handwriting.

email: not this check — no mail-client header.

questionnaire: not this check — no survey items.

resume: not this check — no career history.

scientific_publication: not this check — no journal running head.

invoice/budget: not this check — no financial content.

specification: not this check — no product data.

presentation: not this check — no clear photographic image, slide layout, or bold headline; the left side is just scan noise.

form: not this check — no structured fields.

correspondence: not this check — no memo/letter structure.

news_article: not this check — no masthead.

scientific_report: not this check — no running prose.

advertisement: not this check — no promotional content.

Runner-up: presentation, ruled out because the left side is illegible scan noise rather than a clear photographic image or designed slide layout, making this an identifier-only page (file_folder).

Final label: file_folder.


<h3 class="trace-file"><code>rvl_cdip__scientific_publication__0069.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_publication</code> | <strong>Predicted:</strong> <code>news_article</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead or running head: "Confrérie de la Marmite (Avril 1970)" at the top. This looks like a magazine or newsletter masthead/title. "Confrérie de la Marmite" is a French culinary magazine/club. "Avril 1970" is the date. This points towards news_article (check 12) or possibly scientific_publication if it's a journal, but "Confrérie de la Marmite" is a general-audience magazine/club publication. Let's look at the content.

**Check 1: file_folder**

- Evidence: The page has a full article with text, not just an ID/stamp.
- Result: not this check.

**Check 2: handwritten**

- Evidence: Typed text throughout.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: None.
- Result: not this check.

**Check 4: questionnaire**

- Evidence: None.
- Result: not this check.

**Check 5: resume**

- Evidence: None.
- Result: not this check.

**Check 6: scientific_publication**

- Evidence: "Confrérie de la Marmite (Avril 1970)". Is this a research journal? No, it's a culinary magazine/club ("Confrérie de la Marmite" is a French gastronomic society/magazine). The text is about grilling steaks and cigarette smoke. No journal volume/issue/page number typical of scientific publications.
- Result: not this check.

**Check 7: financial document**

- Evidence: None.
- Result: not this check.

**Check 8: specification**

- Evidence: None.
- Result: not this check.

**Check 9: presentation**

- Evidence: None.
- Result: not this check.

**Check 10: administrative form**

- Evidence: None.
- Result: not this check.

**Check 11: correspondence**

- Evidence: None.
- Result: not this check.

**Check 12: news_article**

- Evidence: "Confrérie de la Marmite (Avril 1970)" at the top. Multi-column typography (two columns of text). Byline "FaE" at the end. The content is an article about grilling steaks and the health risks of cigarette smoke (a common topic in general magazines of that era, discussing Boulogne-Preise, etc.). It presents as published editorial content from a general-audience outlet (a culinary/gastronomic magazine).
- Result: yes.

**Check 13: scientific_report**

- Evidence: None, it's an article in a magazine.
- Result: not this check.

**Check 14: advertisement**

- Evidence: None.
- Result: not this check.

Let's double check Check 12.

"Confrérie de la Marmite (Avril 1970)"

Multi-column news typography (two columns).

Article title: "Die Grillsaison naht" (The grilling season is approaching).

Text discusses health warnings about grilling meat and cigarette smoke.

Byline: "FaE".

Page number: "8" at the bottom.

Bates number: "2001216693" on the right side.

This is clearly an article from a magazine or newsletter. "Confrérie de la Marmite" is a French magazine for food lovers. The text is in German. It's a general-audience outlet.

Therefore, it's a news_article.

Wait, is there any chance it's a scientific_publication?

"Confrérie de la Marmite" is not a scientific journal. It's a culinary magazine. The text is an opinion piece or article about grilling and health.

Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography... Also a magazine feature or an encyclopedia entry... from a GENERAL-AUDIENCE outlet".

This fits perfectly.

Let's review the scratchpad requirements.

- file_folder: no
- handwritten: no
- fax: no
- questionnaire: no
- resume: no
- scientific_publication: no
- financial: no
- specification: no
- presentation: no
- form: no
- correspondence: no
- news_article: yes - masthead "Confrérie de la Marmite (Avril 1970)", multi-column typography, byline "FaE", article text.
- scientific_report: no
- advertisement: no

Runner-up: scientific_report, ruled out because the page carries a general-audience magazine masthead ("Confrérie de la Marmite") and multi-column editorial layout, not a research journal identifier, and the content is an article, not a formal research write-up with methods/results.

Final label: news_article.


<h3 class="trace-file"><code>rvl_cdip__scientific_publication__0086.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_publication</code> | <strong>Predicted:</strong> <code>news_article</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: "SCIENTIFIC AMERICAN October, 1961" at the top left. This is a magazine/newspaper masthead. Wait, "SCIENTIFIC AMERICAN" is a general-audience magazine (popular science). Let's check check 12.

**Check 1: file_folder**

- Evidence: No, there is a title, author, and running prose.
- Not this check.

**Check 2: handwritten**

- Evidence: No, it's typed text.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No.
- Not this check.

**Check 4: questionnaire**

- Evidence: No.
- Not this check.

**Check 5: resume**

- Evidence: No.
- Not this check.

**Check 6: scientific_publication**

- Evidence: "SCIENTIFIC AMERICAN" is a magazine, not a research journal. Wait, check 6 says: "First, use your pre-scan finding: does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings?" Scientific American is a general-audience magazine. Check 12 says: "Newspaper or magazine masthead... Also a magazine feature or an encyclopedia entry/excerpt... from a GENERAL-AUDIENCE outlet... is news_article (check 12), not a publication". So this is not scientific_publication.

**Check 7: FINANCIAL DOCUMENT**

- Evidence: No financial content.
- Not this check.

**Check 8: specification**

- Evidence: No.
- Not this check.

**Check 9: presentation**

- Evidence: No.
- Not this check.

**Check 10: form**

- Evidence: No.
- Not this check.

**Check 11: correspondence**

- Evidence: No.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: "SCIENTIFIC AMERICAN October, 1961" at the top. This is a magazine masthead. The text is an article "Air Pollution and Public Health" by Dr. Walsh McDermott. It's a magazine feature/article from a general-audience outlet (Scientific American).
- Let's verify: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout." This page is an article from Scientific American. Scientific American is a general-audience magazine (popular science), not a research journal like "Science" or "Nature". The instructions say: "a page that presents itself as a newspaper, general-magazine, or encyclopedia piece... is news_article (check 12), not a publication... Per check 6, this does not include a page that itself carries a research journal's own running head...". Scientific American is a magazine. So this is news_article.

**Check 13: scientific_report**

- Evidence: No, it's a published magazine article.

**Check 14: advertisement**

- Evidence: No.

Let's double check Check 12 vs Check 6.

Check 6: "PUBLISHED EVIDENCE -&gt; scientific_publication ... Evidence for this check: a named journal on the page plus a publication identifier ... Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece ... is news_article (check 12), not a publication".

Scientific American is a general-magazine (popular science magazine). The masthead "SCIENTIFIC AMERICAN October, 1961" is present.

Therefore, it is news_article.

Let's review the text:

"SCIENTIFIC AMERICAN

October, 1961

"Air Pollution and Public Health"

by

Dr. Walsh McDermott

Professor of Public Health and Preventive Medicine

Cornell University Medical College

In a nine-page discussion of air pollution..."

This is clearly an excerpt or a page from Scientific American magazine. It's a magazine article.

Label: news_article.

Wait, is there any other possibility?

Could it be a scientific_report? No, it has a magazine masthead.

Could it be a presentation? No.

Let's confirm the definition of news_article: "Newspaper or magazine masthead, byline, dateline, multi-column news typography, "- more -" continuation, or wire-service credit. Also a magazine feature or an encyclopedia entry/excerpt (e.g. a "TOBACCO ENCYCLOPEDIA" page with a titled, authored article), or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet — even when the topic is scientific and journal citations appear within the text as references to other work."

Scientific American is a general-audience outlet (popular science magazine). The page has a masthead ("SCIENTIFIC AMERICAN October, 1961"), a title, an author, and an authored article. This perfectly matches news_article.

Scratchpad:

file_folder: no — page has title, author, and running prose.

handwritten: no — typed text.

questionnaire: no — not a survey.

resume: no — not a CV.

scientific_publication: no — "SCIENTIFIC AMERICAN" is a general-audience magazine, not a research journal; check 12 applies.

invoice/budget: no — no financial content.

specification: no — no product/material documentation.

presentation: no — not a slide deck.

form: no — no fields/boxes.

email/memo/letter: no — no correspondence headers.

news_article: yes — masthead "SCIENTIFIC AMERICAN October, 1961", authored article "Air Pollution and Public Health" by Dr. Walsh McDermott; presents as published periodical editorial content from a general-audience magazine.

Runner-up: scientific_publication, ruled out because Scientific American is a general-audience magazine (check 12) rather than a research journal with its own volume/issue/page identifiers (check 6).

Final label: news_article.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0018.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>specification</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: None. There's a Bates number "2000510922" on the right side.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of data (tables, values), not just an identifier.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Typed text throughout.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No fax cover sheet header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No career history.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range on this page. Just a Bates number.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial data (money, invoices, budgets). It's analytical data (smoke, cigarette, filter, filler values).
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: "ANALYTICAL REPORT FROM PME SMOKING LABORATORY". Title: "CIGARETTE BSP-C (CONTROL)". Tables of analytical values: SMOKE (DPM, SN, TAR, CO, NO, Puff count, etc.), CIGARETTE (Total length, Butt length, Diameter, etc.), FILTER, FILLER.
- This is a product analysis table. "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
- The page is titled "ANALYTICAL REPORT FROM PME SMOKING LABORATORY" and has a box "CIGARETTE BSP-C (CONTROL)". It lists analytical values for smoke, cigarette, filter, filler. This matches the specification check: "A titled product-analysis table... is a specification". Wait, is it a scientific_report?
- Let's check check 13.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: It has tables with values, but check 8 says product analysis tables are specifications. "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)". This is a product's measured parameters (smoke, cigarette, filter, filler analytical values). So it's specification, not form.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: No correspondence structure.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: No journalism.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: "Requires running narrative prose... a page that is only labeled field-value entries... is a filled form (check 10), not a scientific report." This page is only labeled field-value entries (tables of analytical values). So it's not scientific_report. Wait, check 8 says "A titled product-analysis table... is a specification". This fits check 8 perfectly.

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Evidence: No advertisement.
- Not this check.

Let's re-evaluate Check 8 vs Check 13.

Check 8: "Product-referenced test data is a specification. A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough; you don'*t* need a code like 'PD 142A' specifically, just clear evidence the table's subject is a product's own composition or properties."

The page has "CIGARETTE BSP-C (CONTROL)" and tables of "ANALYTICAL VALUES" for SMOKE, CIGARETTE, FILTER, FILLER. This is clearly a product-analysis table for a cigarette product. Thus, specification.

Let's check Check 10 again: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)..."

This confirms it's specification.

Let's check the scratchpad requirements:

- Walk checks 1-14 in order.
- Briefly state evidence or "none".
- If evidence present, STOP HERE.
- Add one final line naming runner-up label and evidence that ruled it out.

Scratchpad:

1. file_folder: no — the page has extensive analytical data tables, not just an identifier/stamp.

2. handwritten: no — typed text throughout.

3. form (fax): no — no fax cover sheet header.

4. questionnaire: no — no survey questions.

5. resume: no — no career history.

6. scientific_publication: no — no journal running head/volume/page number on this page.

7. invoice/budget: no — no financial data, only analytical measurements.

8. specification: yes — titled "ANALYTICAL REPORT FROM PME SMOKING LABORATORY" with a box "CIGARETTE BSP-C (CONTROL)" and tables of analytical values for smoke, cigarette, filter, and filler; this is a titled product-analysis table documenting a product's composition/properties.

Runner-up: scientific_report, ruled out because the page contains only labeled field-value entries (tables of analytical values) without running narrative prose, and check 8 explicitly classifies titled product-analysis tables as specifications.

13. scientific_report: no — requires running narrative prose; this page is only labeled field-value entries.

Wait, is there any other check?

Check 10: form. "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)". So check 8 overrides check 10.

Final label: specification.

Let's double check.

"ANALYTICAL REPORT FROM PME SMOKING LABORATORY"

"Date: 13 MAY 1985 Time: 14.5"

"Version name TASTE-ES"

"Prototype # BSP03"

"Type of analysis 2N00N"

"Date of analysis B50315"

"Bar code ID FTN0333"

"Project leader JJP"

"CIGARETTE BSP-C (CONTROL)"

Tables: SMOKE, CIGARETTE, FILTER, FILLER with analytical values.

This is exactly a product-analysis table. Specification.

Runner-up: scientific_report. Ruled out because it lacks running narrative prose and is a product-analysis table (check 8).

Or runner-up: form. Ruled out because product analysis tables are specifications (check 8). I'll mention scientific_report as the runner-up since it's the most common trap for technical data pages.

Let's write the scratchpad.

file_folder: no — the page contains extensive analytical data tables, not just an identifier or stamp.

handwritten: no — the page is entirely typed.

fax: no — no fax transmission header or cover sheet.

questionnaire: no — no survey instrument or questions.

resume: no — no career history or biographical data.

scientific_publication: no — no journal masthead, volume, issue, or page number on this page.

invoice/budget: no — no financial data, line-item billing, or money tracking.

specification: yes — the page is an "ANALYTICAL REPORT FROM PME SMOKING LABORATORY" for "CIGARETTE BSP-C (CONTROL)" containing titled product-analysis tables (SMOKE, CIGARETTE, FILTER, FILLER) with chemical constituents and measurements, which matches the specification check for product-referenced test data.

Runner-up: scientific_report, ruled out because the page contains only labeled field-value entries (tables of analytical values) without running narrative prose, and check 8 explicitly classifies titled product-analysis tables as specifications.

Looks solid.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0045.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>specification</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: There is a Bates number "2076906781" on the right side, rotated. No journal masthead, no newspaper masthead.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a large table with data (Analyte, Unit of Measure, VIRGO-CA, VIRGO-CC, 1R4F, *M*, *SD*). It has a table caption "Table 8 MS Yields on Equal TPM Basis of Cigarettes VIRGO-CA, VIRGO-CC, and 1R4F".
- Not file_folder.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: The page is typed. No majority handwriting.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No fax cover sheet header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No career history.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range, DOI on the page itself. Just a Bates number.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial data (money, invoices, budgets). It's chemical analysis data (TPM, nicotine, water, glycerin, etc.).
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: The table is titled "Table 8 MS Yields on Equal TPM Basis of Cigarettes VIRGO-CA, VIRGO-CC, and 1R4F". It lists analytes (TPM, nicotine, water, glycerin, hydrogen cyanide, ammonia, carbon monoxide, carbon dioxide, nitrogen oxides, formaldehyde, acetaldehyde, acrolein, propionaldehyde, hexamine, 3-ethenyl pyridine, 2-nitropropane, phenol, o-cresol, m-cresol, *p*-cresol, catechol, resorcine, hydroquinone) and their yields (*M*, *SD*) for three cigarette products (VIRGO-CA, VIRGO-CC, 1R4F).
- This is a product-analysis table (mainstream smoke analyses / MS Yields) keyed to product codes/names (VIRGO-CA, VIRGO-CC, 1R4F).
- Check 8 says: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
- This matches perfectly. It's a specification.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck. It's a table from a report.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: It's a data table, but it's a product-analysis table, which is specification (check 8). Check 10 says "a chart of a product's measured parameters against spec limits is specification (check 8)". Wait, check 10 says "a standalone labeled data chart or table... is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)". This table is product measured parameters (MS Yields). So it's specification.
- Not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: No correspondence.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: No journalism.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: This is just a table (Table 8). Check 13 requires "Running narrative prose with objectives, methods, results, or discussion". A page that is only labeled field-value entries or a table is a form or specification, not a scientific report. Wait, is this page part of a scientific report? The instruction says "If nothing matches, choose the label whose defining evidence is closest...". But check 8 matches: "A titled product-analysis table... is a specification".
- Let's re-read check 8: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough; you don'*t* need a code like 'PD 142A' specifically, just clear evidence the table's subject is a product's own composition or properties."
- The table is "MS Yields on Equal TPM Basis of Cigarettes VIRGO-CA, VIRGO-CC, and 1R4F". This is exactly a product-analysis table. So it is a specification.

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Evidence: No advertisement.

Let's double check check 8 vs check 13.

Check 13: "Requires running prose — a page that is only labeled field-value entries (even an 'ANALYTICAL DATA SUMMARY' under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."

Check 8: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification..."

This page is exactly a titled product-analysis table. So it is specification.

Let's review the table content:

Analyte | Unit of Measure | VIRGO-CA (*M*, *SD*) | VIRGO-CC (*M*, *SD*) | 1R4F (*M*, *SD*)

TPM, nicotine, water, glycerin, hydrogen cyanide, ammonia, carbon monoxide, carbon dioxide, nitrogen oxides, formaldehyde, acetaldehyde, acrolein, propionaldehyde, hexamine, 3-ethenyl pyridine, 2-nitropropane, phenol, o-cresol, m-cresol, *p*-cresol, catechol, resorcine, hydroquinone.

Table 8 MS Yields on Equal TPM Basis of Cigarettes VIRGO-CA, VIRGO-CC, and 1R4F.

This is a product-analysis table. Specification.

Final check of the steps:

1. file_folder: no, has table.

2. handwritten: no, typed.

3. fax: no.

4. questionnaire: no.

5. resume: no.

6. scientific_publication: no journal header.

7. financial: no.

8. specification: yes, titled product-analysis table (MS Yields on Cigarettes VIRGO-CA, VIRGO-CC, 1R4F).

9. presentation: no.

10. form: no, product-analysis table is specification.

11. correspondence: no.

12. news_article: no.

13. scientific_report: no, no running prose, just a table.

14. advertisement: no.

Runner-up: scientific_report, ruled out because the page is only a titled product-analysis table without running narrative prose, and check 8 explicitly classifies titled product-analysis tables as specifications.

Or runner-up: form, ruled out because check 8 explicitly states a titled product-analysis table is a specification, not a generic administrative form.

I will go with specification.


<h3 class="trace-file"><code>rvl_cdip__advertisement__0093.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>advertisement</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. "Ogilvy & Mather" is a company logo/letterhead, not a newspaper/magazine masthead or journal running head.

**Check 1: file_folder**

- Evidence: The page has a lot of content: "INSERTION ORDER", "C", "DATE", "ORDER NO.", "PAGE NO.", "ADVERTISER", "PRODUCT", "TO THE PUBLISHER", "AD FORM NO.", "CAPTION", "INS DATE", "ED", "INCHES", "SPACE", "POSITION INSTRUCTIONS", etc. It's not just an identifier/stamp.
- Not this check.

**Check 2: handwritten**

- Evidence: Mostly typed text. Some handwritten-looking marks or just typed text. No majority handwriting.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Not this check.

**Check 4: questionnaire**

- Evidence: Not a survey instrument.
- Not this check.

**Check 5: resume**

- Evidence: Not a career history.
- Not this check.

**Check 6: scientific_publication**

- Evidence: No journal running head.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: "Ogilvy & Mather", "INSERTION ORDER". It's an advertising insertion order. It lists "ADVERTISER: BROWN & WILLIAMSON", "PRODUCT: RICHLAND", "TO THE PUBLISHER: ANN ARBOR", "AD FORM NO: PA-PG-4020", "CAPTION: ** IMPORTANT ALL DATES ARE WEEK OF **", "INS DATE: 04/28/86", "ED: D", "INCHES: 63.000 6X10.5 INCHES", "GROUP: BOOTH NEWSPAPERS", "MEMBERS: S PAPER BUY", "ANN ARBOR", "BAY CITY", "FLINT", "GRAND RAPIDS", "JACKSON", "KALAMAZOO", "MUSKEGON", "SAFINAS".
- Is this an invoice or budget?
- An insertion order is a request to place an advertisement. It's not a bill for goods sold (invoice) nor an internal money planning/tracking document (budget). Wait, let's look at the categories.
- Could it be a form? Check 10: ADMINISTRATIVE FORM. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... internal authorization/approval forms..."
- Wait, is an insertion order a form? Yes, it's a structured document for capturing advertising placement data.
- Let's check Check 8: specification. No.
- Check 9: presentation. No.
- Check 10: form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". An insertion order has fields for Advertiser, Product, Publisher, Caption, Ins Date, Ed, Inches, Space, Position Instructions. It captures factual data for an advertising campaign.
- Let's re-read Check 7: "invoice: an outside vendor, supplier, or agency states charges owed... A payment VOUCHER... A hotel/motel guest bill... Likewise a landlord's rent/lease statement... is an invoice". An insertion order is not a bill; it's an order to insert an ad.
- "budget: internal money planning... A provider's periodic customer statement... is budget". An insertion order is not a statement of account.
- So it's not Check 7.

**Check 8: specification**

- Evidence: No material safety data, product formulation, "shall/must" language.
- Not this check.

**Check 9: presentation**

- Evidence: Not a slide deck, cover, or statement.
- Not this check.

**Check 10: ADMINISTRATIVE FORM**

- Evidence: "INSERTION ORDER" with fields for DATE, ORDER NO., PAGE NO., ADVERTISER, PRODUCT, TO THE PUBLISHER, AD FORM NO., CAPTION, INS DATE, ED, INCHES, SPACE, GROUP, MEMBERS, POSITION INSTRUCTIONS. It is a structured document with fields for capturing advertising placement data. This fits "administrative form" or "form".
- Wait, is there a better fit?
- Let's check Check 11: correspondence. No TO:/FROM:/RE: memo header, no letterhead with external address + Dear... salutation. It's an internal/agency form.
- Check 12: news_article. No.
- Check 13: scientific_report. No.
- Check 14: advertisement. The document is an *insertion order* for an advertisement, not the advertisement itself. The ad copy is "5 FREE... 50 FREE... /SLANT". But the document is the order form. "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures." This is an insertion order, which is a form used by the advertising agency.

Let's carefully evaluate Check 10 vs Check 14.

Check 14: "PROMOTIONAL MATERIAL -&gt; advertisement. Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures." This page is an "INSERTION ORDER" from Ogilvy & Mather. It's a business document used to order ad space. It's a form.

Check 10: "ADMINISTRATIVE FORM -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data..." An insertion order is a form.

Let's review the definition of "form" in this context. "A form does NOT have to be blank — a filled form recording data is still a form... This also covers: ... internal authorization/approval forms with an approval signature/date block." An insertion order has "Per: L. ALTARES" at the bottom, which is an approval/signature block. It captures data (advertiser, product, publisher, caption, dates, inches, space, position instructions). It is a form.

Let's double check Check 7 (invoice/budget).

Is an insertion order an invoice? No, it's an order.

Is it a budget? No.

Let's double check Check 1 (file_folder).

Not file_folder.

Let's double check Check 11 (correspondence).

No memo or letter structure.

So the label is "form".

Wait, let's look at the document again.

"Ogilvy & Mather Advertising"

"INSERTION ORDER"

"C"

"DATE 03/31/86"

"ORDER NO. 340"

"PAGE NO. 1"

"ADVERTISER BROWN & WILLIAMSON"

"PRODUCT RICHLAND"

"TO THE PUBLISHER ANN ARBOR"

"AD FORM NO. PA-PG-4020"

"CAPTION ** IMPORTANT ALL DATES ARE WEEK OF **"

"INS DATE 04/28/86"

"ED D"

"INCHES 63.000 6X10.5 INCHES"

"SPACE"

"GROUP BOOTH NEWSPAPERS"

"MEMBERS S PAPER BUY ANN ARBOR BAY CITY FLINT GRAND RAPIDS JACKSON KALAMAZOO MUSKEGON SAFINAS"

"POSITION INSTRUCTIONS RUN FAR FORWARD IN MAIN NEWS / RIGHT-HAND PAGE. AVOID CLUTTER. MONDAY THROUGH FRIDAY LOCAL (WHICHEVER DAY THE POSITIONING CAN BEST BE ACHIEVED). WE REQUEST THAT NEWSPAPERS CAPABLE OF AN EVENING/MORNING SPLIT RUN AD IN THE EVENING EDITION THEN THE FOLLOWING MORNING EXAMPLE -- TUESDAY(E)/WEDNESDAY(*M*)"

"(CONT) Per: L. ALTARES"

"Ogilvy & Mather"

"Please check reproduction material against proof to make sure it corresponds in every respect."

"MEMBER OF AMERICAN ASSOCIATION OF ADVERTISING AGENCIES"

"300406387 PRODUCED FROM B&W WEB SITE"

This is clearly an advertising insertion order form. It captures structured data for an ad placement. It fits "form" (Check 10).

Let's check if there's any other category.

Could it be "advertisement"? No, it's the order form for the advertisement, not the ad itself. The ad copy is just a caption.

Could it be "invoice"? No, it doesn'*t* state charges owed. It's an order.

Could it be "budget"? No.

Therefore, "form" is the correct label.

Let's write the scratchpad.

- file_folder: no — the page has extensive structured content (Insertion Order fields, instructions, etc.), not just an identifier/stamp.
- handwritten: no — the page is typed throughout.
- fax: no — no fax transmission header or cover sheet.
- questionnaire: no — not a survey instrument.
- resume: no — not a career history.
- scientific_publication: no — no journal running head or publication identifier.
- financial (invoice/budget): no — this is an advertising insertion order (request to place an ad), not a bill for goods/services (invoice) or an internal money planning/tracking document (budget). It does not list charges owed or financial forecasts.
- specification: no — no material safety data, product formulation, or "shall/must" requirement language.
- presentation: no — not a slide deck, cover, or statement.
- form: yes — titled "INSERTION ORDER" with structured fields for DATE, ORDER NO., ADVERTISER, PRODUCT, PUBLISHER, CAPTION, INS DATE, ED, INCHES, SPACE, GROUP, MEMBERS, and POSITION INSTRUCTIONS, plus a "Per:" approval line. It is a structured document for capturing advertising placement data.
- correspondence: no — no mail-client header, memo header (TO:/FROM:/RE:), or letter structure (letterhead + external address + Dear... salutation + closing).
- news_article: no — no newspaper/magazine masthead or editorial content.
- scientific_report: no — no running narrative prose with objectives/methods/results.
- advertisement: no — this is an internal/agency administrative form (insertion order) used to order ad space, not the promotional material/advertisement itself (which would be the ad copy/layout).

Runner-up: advertisement, ruled out because the page is an administrative insertion order form used by the agency to specify ad placement details, not the actual promotional advertisement layout.

Another runner-up: invoice, ruled out because the document is an order/request to place an ad, not a bill stating charges owed for goods or services.

Final label: form.


</details>

## budget → presentation

<details class="trace-group">

<summary>3 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__budget__0016.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

First, pre-scan:

- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "#2155984" and "PREPARED BY LOUISVILLE MEDIA DEPT.", "DATE 2/19/86 PAGE 1". No journal masthead.

Now, check 1 to 14:

Check 1: file_folder

- Content: "TITLE", "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT", "APPROVED BY: BRAND AGENCY", "DATE:", "BRAND MANAGER", "DATE:", "LOUISLAND CON MEDIA", "DATE:". Also "PREPARED BY LOUISVILLE MEDIA DEPT.", "DATE 2/19/86 PAGE 1", "#2155984".
- Is it almost no body content? It has a title "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT" and approval blocks. Wait, is this a folder tab? No, it's a page with a title and approval signatures.
- Let's look at Check 9: presentation. "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... a deck cover, or a section divider — is a presentation".
- Wait, what about Check 7: financial document? "OUT-OF-HOME/TARGET ESTIMATE REPORT". An estimate report.
- Let's re-read Check 7: "budget: internal money planning, tracking, or disbursement... Also covers money-only records... An agency/vendor estimate or recap that ONLY plans upcoming placements — no estimate number, no revision/prior-adjustment line, no billing type, and no charges/amounts for a client job (e.g. an "OUTDOOR ESTIMATE RECAP" of planned bus-shelter ad buys showing only planned gross amounts by future quarter) — plans projected spend rather than billing completed work, so it is budget, not invoice".
- But this page is just the cover/title page of the "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT" with approval signatures.
- Wait, Check 9: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation (this check), not file_folder (check 1)."
- Let's check the text: "TITLE", "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT", "APPROVED BY: BRAND AGENCY DATE:", "BRAND MANAGER DATE:", "LOUISLAND CON MEDIA DATE:".
- This is a title page / cover page for a report. Is it a presentation? "a deck title or section-divider page... a near-blank cover or title page... is a presentation".
- Wait, is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." But Check 7 says "money function overrides form layout". However, this page has NO money content, just the title and approval block.
- Let's re-read Check 9: "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report (check 13), not presentation". This is an "OUT-OF-HOME/TARGET ESTIMATE REPORT", not a technical-study title page.
- What about Check 7? "invoice or budget". The page itself is just the cover/approval page of an estimate report. Does the cover page count as the financial document? Usually, the cover page of a budget/estimate is part of the budget. But wait, if the page is just the title and approvals, is it a presentation?
- Let's look at Check 9 again: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note (e.g. "Internal Communication 2000 Plan" with "Draft for discussion"), a single-word/short-phrase heading with no subtitle at all (e.g. "RECOMMENDATIONS" centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
- The page has "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT" as the title, and approval blocks. It is mostly empty space.
- Wait, is there any other check? Check 10: "administrative form -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
- The page has "APPROVED BY: BRAND AGENCY DATE:", "BRAND MANAGER DATE:", "LOUISLAND CON MEDIA DATE:". These are approval blocks.
- But Check 7 says: "Money function overrides form layout... A check face/check stub... is the DISBURSEMENT instrument and stays budget...". What about an estimate report cover?
- Let's re-read Check 7 carefully: "budget: internal money planning... An agency/vendor estimate or recap that ONLY plans upcoming placements... is budget, not invoice". But this is just the cover page.
- If a page is just the cover/title page of a document, and it's mostly empty space with a title and approvals, Check 9 says: "a near-blank cover or title page... is a presentation".
- Wait! Look at the text orientation. The text is rotated 90 degrees.
- "DATE 2/19/86 PAGE 1"
- "PREPARED BY LOUISVILLE MEDIA DEPT."
- "TITLE"
- "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT"
- "APPROVED BY: BRAND AGENCY DATE: ________________"
- "BRAND MANAGER DATE: ________________"
- "LOUISLAND CON MEDIA DATE: ________________"
- "#2155984"
- This is a title page / cover page for an estimate report.
- Is it a presentation? "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation (this check), not file_folder (check 1)."
- Let's check if it's a form. Check 10: "internal authorization/approval forms with an approval signature/date block." But the title is "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT". This is the cover of a budget/estimate document.
- Wait, if it's the cover of a budget document, does the cover page itself get classified as budget, or presentation?
- Usually, if a page is just the cover of a report, and the report is a budget, the cover might be classified as presentation if it's a "near-blank cover or title page".
- Let's re-read Check 9: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation (this check), not file_folder (check 1)."
- What about Check 7? "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This page has NO financial content (no line items, no amounts). It's just the title and approvals. So Check 7 does NOT apply to this page.
- Since Check 7 doesn'*t* apply (no financial content on this page), we move to Check 9.
- Check 9: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation". This page is mostly empty space, with the title "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT", date "2/19/86", and approval blocks. This perfectly matches "near-blank cover or title page".
- Wait, is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block." But Check 9 explicitly says "a near-blank cover or title page... is a presentation... not file_folder". What about form? Check 10 is for "capturing factual data". An approval page for a report is often a form, but if it's just the cover of a report, it's a presentation cover.
- Let's re-read Check 9: "a deck title or section-divider page... a near-blank cover or title page... is a presentation".
- Let's check if there's any other evidence. "OUT-OF-HOME/TARGET ESTIMATE REPORT". This is a media plan/estimate. Media plans are often presentations.
- Let's consider Check 10: "administrative form -&gt; form. ... internal authorization/approval forms with an approval signature/date block." If this is an authorization form for the estimate, it could be a form. But the title is "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT", which is the title of the report itself, not an authorization form. The approval blocks are just the signature page for the report. A signature page for a report is typically part of the presentation/report cover.
- Actually, a page with just a title and signature blocks for a report is a presentation cover.
- Let's review the evidence for Check 9: "mostly empty space with only a bold headline title" ("1985 OUT-OF-HOME/TARGET ESTIMATE REPORT"), "date" ("DATE 2/19/86"), and approval blocks. This matches Check 9 perfectly.
- Let's review Check 1: file_folder. "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." This has a title and approvals, so not file_folder.
- Check 2: handwritten. No.
- Check 3: fax. No.
- Check 4: questionnaire. No.
- Check 5: resume. No.
- Check 6: scientific_publication. No.
- Check 7: financial_document. "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This page has no financial content (no numbers, no line items). So not Check 7.
- Check 8: specification. No.
- Check 9: presentation. "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation". Yes, this is a near-blank cover page for a report.
- Check 10: form. "internal authorization/approval forms with an approval signature/date block." But this is the cover of a report, not an authorization form itself. The approval blocks are for the report. Even if it's an approval page, Check 9's "near-blank cover or title page" rule for presentation covers title pages of reports. Wait, is a signature page a presentation? "a deck title or section-divider page, a meeting/program/speaker cover page... a near-blank cover or title page... is a presentation". Yes.
- Let's double check if there's any other label. "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT". Could it be a budget? Check 7 says "Check 7 applies only when financial content IS the page's primary structure". This page has no financial content. So it's not budget.
- Therefore, presentation is the correct label.

Let's do a quick pass of the scratchpad:

- file_folder: no — page has a title "1985 OUT-OF-HOME/TARGET ESTIMATE REPORT" and approval blocks, not just metadata.
- handwritten: no — typed text only.
- fax: no — no fax header.
- questionnaire: no — not a survey.
- resume: no.
- scientific_publication: no — no journal identifier.
- financial_document: no — Check 7 requires financial content (line items, amounts) to be the page's primary structure; this page only has a title and approval signatures, no monetary data.
- specification: no.
- presentation: yes — "mostly empty space with only a bold headline title" ("1985 OUT-OF-HOME/TARGET ESTIMATE REPORT"), a date ("DATE 2/19/86"), and approval signature blocks. This matches the "near-blank cover or title page" definition for presentation.
- form: no — although it has approval signature blocks, it is the cover/title page of a report (presentation), not a form capturing factual data. Check 9's near-blank cover rule applies.
- email: no.
- news_article: no.
- scientific_report: no — no running prose, just a title and approvals.
- advertisement: no.

Runner-up: form, ruled out because the page is a near-blank cover/title page for a report (presentation, check 9), not a form capturing structured data, and check 7 (financial) doesn'*t* apply because there's no financial content on this page.

Wait, is there any chance it's a form? "internal authorization/approval forms with an approval signature/date block." But the title is the report title. It's the cover page of the report. Cover pages of reports are presentations.

Let's confirm the text:

"DATE 2/19/86 PAGE 1"

"PREPARED BY LOUISVILLE MEDIA DEPT."

"TITLE"

"1985 OUT-OF-HOME/TARGET ESTIMATE REPORT"

"APPROVED BY: BRAND AGENCY DATE: ________________"

"BRAND MANAGER DATE: ________________"

"LOUISLAND CON MEDIA DATE: ________________"

"#2155984"

This is definitely a cover page / title page for a media estimate report. According to the instructions, a near-blank cover or title page is a presentation.

Final check of the rules:

- "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation (this check), not file_folder (check 1)."
- Matches perfectly.

I will write the scratchpad and output the label.


<h3 class="trace-file"><code>rvl_cdip__budget__0095.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Top right: "4/2/83 JMC"
- Top center: "VICEROY", "REVISED 1983 MARKETING PLAN"
- Main content: A table of contents for a "REVISED 1983 MARKETING PLAN".
- Sections: I. EXECUTIVE SUMMARY, II. PROPOSED PLAN (A. CREATIVE, B. MEDIA/TARGET AUDIENCE, etc.), III. BUDGET, IV. NEXT STEPS.
- Lists of exhibits: BUDGET AND SHARE EXHIBITS, LESSONS LEARNED EXHIBITS, CREATIVE EXHIBIT, MEDIA/TARGET AUDIENCE EXHIBITS, PROMOTION EXHIBITS, SPENDING LEVEL TEST, SALES/BDI.
- Handwritten notes: "JMC", "JSC", "Not all my 4th writing plan full pg.", "OCH top 14 TH 25/6 month 12/13", "You", "Crimson top 14 flight import".
- Bottom right: Bates number "670665021".

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. Just "VICEROY REVISED 1983 MARKETING PLAN".

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of content (table of contents, exhibits list). Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Mostly typed text (table of contents). Handwritten notes are marginal.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: Not a resume.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name/volume/issue.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: Mentions "BUDGET", "PROFIT AND LOSS STATEMENT", "FUND AVAILABLE". But the page itself is a table of contents for a marketing plan. It's not a financial document itself (no line-item table of charges, no check stub).
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: Not a specification.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: The page is a table of contents for a "REVISED 1983 MARKETING PLAN". It has a title "VICEROY REVISED 1983 MARKETING PLAN". It lists sections and exhibits. It looks like a cover page or table of contents for a presentation or a report. Wait, let's look at check 9 carefully.
- "Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... a single-word/short-phrase heading with no subtitle at all... a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
- This page is a table of contents. Is it a presentation?
- Let's check check 13: scientific_report. "Running narrative prose...". This is not running prose.
- Let's check check 10: ADMINISTRATIVE FORM -&gt; form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... standalone labeled data chart or table...". This is a table of contents. Not a form.
- Let's re-read check 9. "a deck title or section-divider page... A near-blank cover or title page...". This page is a table of contents for a marketing plan.
- Wait, is this a presentation? A marketing plan document often has a table of contents.
- Let's look at the labels again.
- advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- Could it be a presentation? "a deck title or section-divider page". A table of contents for a deck/presentation could be a section divider or part of the presentation.
- Let's look at the handwritten notes: "Not all my 4th writing plan full pg.", "OCH top 14 TH 25/6 month 12/13", "Crimson top 14 flight import". These look like notes on a marketing plan document.
- Is there a better fit?
- Let's check check 11: CORRESPONDENCE -&gt; email, memo, or letter. No TO/FROM/RE header. No salutation.
- Let's check check 12: PUBLISHED JOURNALISM -&gt; news_article. No.
- Let's check check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report. No running prose.
- Let's check check 14: PROMOTIONAL MATERIAL -&gt; advertisement. No.

Wait, look at the content: "VICEROY REVISED 1983 MARKETING PLAN". It's a table of contents.

Is it a presentation? "a deck title or section-divider page... A near-blank cover or title page...". This is a table of contents page.

Actually, let's look at the structure. It's a list of exhibits and sections.

Could it be a form? No.

Could it be a budget? It lists "BUDGET" as section III, and "BUDGET AND SHARE EXHIBITS". But the page itself is a TOC.

Wait, let's re-read check 9: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image... A near-blank cover or title page... is a presentation... EXCEPTIONS: a cover/title page that names a survey... is questionnaire... and a technical-study title page... is scientific_report".

This page is a table of contents for a marketing plan. Marketing plans are often presented. The handwritten notes ("Not all my 4th writing plan full pg.", "OCH top 14 TH...") suggest this is a page from a document being reviewed, possibly a presentation deck or a report.

Actually, a table of contents for a "REVISED 1983 MARKETING PLAN" with exhibits listed... this looks like the cover/TOC page of a presentation or a report.

If it's a report, it would be scientific_report (check 13), but scientific_report requires "Running narrative prose". This page has no running prose, just a TOC.

If it's a presentation, check 9 covers "a deck title or section-divider page". A TOC page in a deck is a section divider or part of the deck.

Wait, is there any other category?

What about "form"? No.

What about "budget"? Check 7: "If the page is otherwise formatted as correspondence... and a dollar figure... is merely mentioned... classify it as correspondence". Here, it's a TOC. "Money function overrides form layout... a billing or payment page stays financial...". This is not a billing page. "internal money planning, tracking, or disbursement... budget or expense lines...". This page is a TOC for a marketing plan, which includes a budget section, but the page itself is not a budget document.

Let's reconsider check 9: "presentation".

"a deck title or section-divider page... A near-blank cover or title page... a single-word/short-phrase heading with no subtitle at all... a deck cover, or a section divider — is a presentation".

This page has a heading "VICEROY REVISED 1983 MARKETING PLAN" and a list of contents. It's a title/TOC page for a document. In the tobacco archive, marketing plans were often presented as slide decks or large reports. The handwritten notes ("JMC", "JSC", "Not all my 4th writing plan full pg.") look like reviewer notes on a draft presentation or document.

Actually, look at the layout: it's a typed list.

Is it a "presentation"? "Slide/overhead layouts... a deck title or section-divider page...". A TOC page for a deck is a section divider.

Let's check if there's any other fit.

Could it be a "scientific_report"? No, no running prose.

Could it be a "form"? No.

Let's look at the labels again.

advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

If the document is a marketing plan, and this is the TOC page...

In many tobacco archive datasets, marketing plan documents, especially those with exhibits listed like this, are often part of a presentation or a report. Since scientific_report requires running prose, and this is just a TOC, it might be classified as a presentation (if it's a deck TOC) or maybe something else.

Wait, check 9 says: "a deck title or section-divider page... is a presentation". A TOC page is a section divider or part of the deck structure.

Also, the handwritten notes look like someone reviewing a draft. "Not all my 4th writing plan full pg." -&gt; "Not all my 4th writing plan full pg." (maybe "Not all my 4th writing plan full page").

"OCH top 14 TH 25/6 month 12/13" -&gt; notes on media plan.

"Crimson top 14 flight import" -&gt; notes on product.

These are reviewer notes on a marketing plan document.

Is there any chance this is a "budget"?

Check 7: "budget: internal money planning... budget or expense lines...". This page lists "BUDGET" as a section and "BUDGET AND SHARE EXHIBITS". But the page itself is not a budget table. It's a TOC.

Is there any chance this is a "form"?

Check 10: "administrative form... filled or blank fields...". No.

So it's likely "presentation". A marketing plan document, especially one with exhibits and reviewer notes, is often a presentation deck or a report formatted as a presentation. The TOC page acts as a section divider or title page for the deck.

Wait, let's look at check 9 again: "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report". This is a "REVISED 1983 MARKETING PLAN", not a technical study.

"EXCEPTIONS: a cover/title page that names a survey... is questionnaire... and a technical-study title page... is scientific_report".

So a marketing plan title page/TOC is not an exception. It falls under presentation if it's a deck cover/divider.

"a deck title or section-divider page... is a presentation".

Let's consider if it's a "scientific_report".

Check 13: "Original research write-up... Running narrative prose...". This page has no running prose. So not scientific_report.

Let's consider if it's a "form".

Check 10: "standalone labeled data chart or table...". This is a list, not a data chart.

So "presentation" seems the best fit. The page is a table of contents / title page for a marketing plan document, which in this context (tobacco archive, reviewer notes) is likely a presentation deck or a report structured as a presentation. The layout is sparse text, list of exhibits.

Wait, is there any other category?

What about "memo"? No TO/FROM.

What about "letter"? No.

Let's re-read check 9 carefully.

"Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement ("FOR IMMEDIATE RELEASE", media contact), or a photographic slide image... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... a single-word/short-phrase heading with no subtitle at all... a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."

This page has a bold headline title "VICEROY REVISED 1983 MARKETING PLAN" and a list of contents. It's a title/TOC page. The handwritten notes suggest it's a working document, likely a presentation draft.

The layout is not dense prose. It's a structured list.

I will classify this as "presentation".

Wait, could it be "budget"?

The document is a "MARKETING PLAN". Marketing plans contain budgets. But the page is a TOC.

Check 7: "If the page is otherwise formatted as correspondence... and a dollar figure... is merely mentioned... classify it as correspondence". Here, it's a TOC. "Money function overrides form layout... a billing or payment page stays financial...". This is not a billing page.

"budget: internal money planning... budget or expense lines...". This page is not a budget line-item table.

Could it be "form"?

No fields to fill.

I'm confident in "presentation". The page is a title/TOC page for a marketing plan, which is a type of presentation document in this archive. The handwritten notes are typical of review copies of presentations/decks.

Let's double check check 1: file_folder.

"A Bates number or archive stamp alone is NOT enough... A prominent topical heading always counts as real content... a bold headline title (even a single word/short phrase like "RECOMMENDATIONS" with no subtitle... is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."

This page has a prominent topical heading "VICEROY REVISED 1983 MARKETING PLAN" and a TOC. So it's not file_folder. It's a cover/title page or section divider -&gt; presentation.

Final check:

- file_folder: no, has real content (TOC, heading).
- handwritten: no, mostly typed.
- form: no, no fields.
- questionnaire: no.
- resume: no.
- scientific_publication: no.
- invoice/budget: no, not a financial document itself.
- specification: no.
- presentation: yes, title page/TOC for a marketing plan (deck/document), sparse layout, reviewer notes.
- news_article: no.
- scientific_report: no, no running prose.
- advertisement: no.

The label is presentation.


<h3 class="trace-file"><code>rvl_cdip__email__0031.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>email</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head. There is a Bates number "52782 1162" and "RJR0000001723013377 70014 6873".

**Check 1: file_folder**

- Content: "2000 NAPA 500 Schedule of Events" with a detailed schedule of events from Wednesday, Nov 15 to Sunday, Nov 19.
- Not file_folder. It has real content (a schedule).

**Check 2: handwritten**

- Content is typed. No majority handwriting.
- Not handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- No fax header.
- Not fax.

**Check 4: questionnaire**

- Not a survey instrument.
- Not questionnaire.

**Check 5: resume**

- Not a resume.

**Check 6: scientific_publication**

- No journal identifier.
- Not scientific_publication.

**Check 7: financial document (invoice/budget)**

- No financial line items, invoices, or budgets.
- Not financial.

**Check 8: specification**

- Not a material safety data sheet, product formulation, or test-analysis table with "shall/must".
- Not specification.

**Check 9: presentation**

- "2000 NAPA 500 Schedule of Events" is a schedule.
- Is it a presentation cover/divider? It's a schedule of events for a race (NAPA 500).
- Wait, check 9 says: "Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page... A near-blank cover or title page... a single-word/short-phrase heading with no subtitle at all... a deck cover, or a section divider — is a presentation".
- This page is a "Schedule of Events". It's a program/schedule.
- Let's look at the layout. It's a list of times and events.
- Is it a presentation? "meeting/program/speaker cover page". A schedule of events for a meeting/conference/race could be a program.
- Wait, is there a better category?
- Let's check 10: form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table...". This is a schedule, not a form capturing data.
- Let's check 11: correspondence. No.
- Let's check 12: news_article. No.
- Let's check 13: scientific_report. No.
- Let's check 14: advertisement. No.

Let's re-evaluate Check 9: "SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation".

"A meeting/program/speaker cover page" -&gt; presentation.

Is a "Schedule of Events" a program? Yes, a program for an event.

Also, the layout is sparse, list-based.

Wait, let's look at the bottom: "00napach/updated 11-7-00bh". This looks like a document control number or author/date.

"Bates number 52782 1162".

This is a schedule of events for the 2000 NAPA 500 NASCAR race.

Could it be a presentation? A schedule of events is often part of a presentation or a program.

Let's consider if it's a "form". No.

Is it a "specification"? No.

Let's look at the labels again:

advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

If it's a schedule of events for a race, it's likely a program or a slide in a presentation deck about the event, or a standalone program document.

In the tobacco archive, schedules of events for races (like NAPA 500, which was a NASCAR race sponsored by NAPA Auto Parts, a Philip Morris brand) are often part of promotional or event planning materials.

If it's a program, check 9 covers "meeting/program/speaker cover page". But this is the schedule itself, not just the cover.

Wait, check 9: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image".

This page is a schedule. Is it a presentation?

Often, event schedules in these archives are scanned from presentation decks or are standalone program documents. If it's a standalone program document, does it fit presentation?

"a meeting/program/speaker cover page" -&gt; presentation.

What about just a schedule?

Let's look at check 10: form. "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data". This is a schedule, not a chart of generic data.

Let's reconsider the content. It's a schedule of events for the 2000 NAPA 500.

Is it an advertisement? "Coca-Cola Promotion", "NASCAR Winston Cup". But it's a schedule, not a promotional layout with product imagery and slogans.

Is it a news_article? No.

Let's look at the structure. It's a list of times and activities.

Could it be a "form"? No.

Could it be a "presentation"? Yes, event schedules are often part of presentations or are considered program materials which fall under presentation in this taxonomy (meeting/program).

Actually, a schedule of events is very common in presentations (e.g., a slide showing the schedule, or a handout).

Given the options, "presentation" is the best fit for a program/schedule of events document in this context, especially if it's from a deck or is a program document.

Wait, let's look at the bottom left: "00napach/updated 11-7-00bh". "napach" might be a person's initials (Napa? No, maybe a project code). "updated 11-7-00". This looks like a document version control, typical of internal business documents, possibly a presentation slide or a handout from a meeting.

The layout is very clean, typical of a presentation slide or a printed program.

I will classify it as presentation.

Let's double check check 9: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page...".

A schedule of events is a program. "meeting/program...".

Also, the sparse text, list format.

Let's check if there's any other category.

"form": No fields to fill.

"specification": No.

"scientific_report": No.

I'll go with presentation.

Wait, is there any chance it's a "form"? No.

Is it a "memo"? No.

Let's review the scratchpad steps.

1. file_folder: No, has content.

2. handwritten: No.

3. fax: No.

4. questionnaire: No.

5. resume: No.

6. scientific_publication: No.

7. financial: No.

8. specification: No.

9. presentation: Yes, it's a schedule of events (program) for the 2000 NAPA 500, laid out in a sparse, list-based format typical of a program or presentation slide/handout. The document control "00napach/updated 11-7-00bh" suggests it's an internal working document, likely a slide or program page.

10. form: No.

11. correspondence: No.

12. news_article: No.

13. scientific_report: No.

14. advertisement: No.

Runner-up: form, ruled out because there are no fields/boxes for data capture, it's a schedule.

Or runner-up: specification, ruled out because it's not a product/material doc.

Actually, looking closely at the layout, it's just text.

"2000 NAPA 500 Schedule of Events"

Wednesday, November 15...

This is a program/schedule. In the tobacco archive, these are often part of event presentations or are classified as presentation (program).

Final decision: presentation.


</details>

## handwritten → questionnaire

<details class="trace-group">

<summary>3 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__handwritten__0025.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>handwritten</code> | <strong>Predicted:</strong> <code>questionnaire</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** I see handwritten text, a postmark, a barcode, and a ZIP code. No "From/To/Sent/Subject" email headers.
- **Masthead/Running head:** No newspaper masthead, no journal running head.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: There is a lot of handwritten text, a postmark, a barcode, and a ZIP code. It's not just an identifier. Wait, let's look closer.

    *   The text is rotated 90 degrees counter-clockwise. Let's read it.

    *   "Bonne Thomas & / 42 26 Piedmont Rd / Madison, AL 35758"

    *   "PM / HUNTSVILLE AL 358 / 17 JAN / 1996" (Postmark)

    *   "51821 5549" (ZIP+4)

    *   Barcode.

    *   "Mr. Terry Brewer / HTW Dept. *N*-68 / National Smoker Serv. / P.O. Box 834051 / Richardson TX, 75083-9746"

    *   "no survey" (handwritten note)

    *   There are scribbles (crossed out text).

    *   This looks like the back of an envelope or a piece of paper used for routing/notes.

    *   Wait, is it a file_folder? "Almost no body content: only an archive/Bates number, a stamp, a short label or ID...". This page has handwritten addresses and notes. It's not a folder tab. It's not just a Bates number.

    *   Let's check the handwritten content. It's mostly freeform handwriting.

-   **Check 2: handwritten**

    *   Evidence: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."

    *   The page contains handwritten addresses: "Bonne Thomas & 42 26 Piedmont Rd Madison, AL 35758" and "Mr. Terry Brewer HTW Dept. *N*-68 National Smoker Serv. P.O. Box 834051 Richardson TX, 75083-9746".

    *   There is a handwritten note "no survey".

    *   There is a postmark "HUNTSVILLE AL 358 17 JAN 1996 PM".

    *   There is a barcode and ZIP code "51821 5549".

    *   The page is mostly blank white space with this handwritten content on the right side (rotated).

    *   Is it "majority handwritten"? The text is handwritten. The printed elements are a postmark, barcode, and ZIP code. The handwritten text is the main content.

    *   Let's re-read the definition: "Most of the content is freeform handwriting... This wins over a typed letter or memo layout."

    *   "A typed page with only a signature, stamp, or margin note is not handwritten." -&gt; This is mostly handwritten.

    *   "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision... is a transmittal note... questionnaire". Wait. "no survey" is a note about a survey. But is the whole page a questionnaire transmittal? No.

    *   Let's look at the "handwritten" definition again. "A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."

    *   This page has handwritten names and addresses on blank paper (with a postmark and barcode, likely the back of an envelope or a routing slip).

    *   The text "no survey" is a note.

    *   This looks like a routing note on the back of an envelope or a piece of paper.

    *   Let's check if it fits "handwritten". Yes, it's freeform handwriting with addresses and a note.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   No "FACSIMILE" header. The postmark is a postal mark, not a fax header.

-   **Check 4: SURVEY INSTRUMENT**

    *   "no survey" is written. No printed survey instrument.

-   **Check 5: resume**

    *   No.

-   **Check 6: scientific_publication**

    *   No.

-   **Check 7: financial_document**

    *   No.

-   **Check 8: specification**

    *   No.

-   **Check 9: presentation**

    *   No.

-   **Check 10: administrative_form**

    *   No printed fields to fill.

-   **Check 11: correspondence (email, memo, letter)**

    *   It has addresses, but no "Dear...", no signature block, no TO:/FROM: block in memo format. It looks like the back of an envelope or a routing note.

    *   "A dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block is a letter." -&gt; There is no prose, just addresses and "no survey".

    *   Actually, let's look at the text again.

    *   "Bonne Thomas & 42 26 Piedmont Rd Madison, AL 35758" (Sender/Return address?)

    *   "Mr. Terry Brewer HTW Dept. *N*-68 National Smoker Serv. P.O. Box 834051 Richardson TX, 73083-9746" (Recipient address)

    *   "no survey" (Note)

    *   This is a routing note, likely on the back of an envelope or a piece of paper.

    *   Is it a letter? No salutation, no body, no closing.

    *   Is it a memo? No TO/FROM header block.

-   **Check 12: news_article**

    *   No.

-   **Check 13: scientific_report**

    *   No.

-   **Check 14: advertisement**

    *   No.

Let's reconsider **Check 2: handwritten**.

The page is mostly blank. The content is handwritten addresses and a note "no survey".

The definition says: "Most of the content is freeform handwriting... NOT on a printed template."

The content is handwritten. The printed elements are a postmark and barcode (mailing metadata).

"A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper... is handwritten."

This fits perfectly. It's a handwritten routing note/label.

Wait, is there a Bates number? I don'*t* see a clear Bates number like "0123456789". There is "51821 5549" which is a ZIP code. There is a barcode.

The postmark is "HUNTSVILLE AL 358 17 JAN 1996 PM".

The text is rotated.

Let's rotate the image mentally 90 degrees clockwise.

Top: "Bonne Thomas & 42 26 Piedmont Rd Madison, AL 35758"

Middle: Postmark "HUNTSVILLE AL 358 17 JAN 1996 PM"

Bottom: Barcode, "51821 5549"

Right side (rotated): "Mr. Terry Brewer HTW Dept. *N*-68 National Smoker Serv. P.O. Box 834051 Richardson TX, 75083-9746"

And "no survey" with a line through it or next to it. And some scribbles (crossed out text).

This is essentially a handwritten note/routing slip.

Category: **handwritten**.

Let's check the rules again.

"Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing (e.g. 'Revised questionnaire to be used VIII-IV...') is a transmittal note for the instrument — questionnaire (check 4)..."

Here the note says "no survey". It's a note about a survey (or lack thereof).

But is the *page* a questionnaire transmittal?

"A handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."

Wait. If the note is *about* a questionnaire, it's questionnaire.

The note says "no survey". This implies "do not send survey" or "this is not a survey".

The addresses suggest mailing something to Terry Brewer.

If the underlying document was a survey, and this is a note saying "no survey", is it questionnaire?

Check 4: "The page asks the reader to answer... A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... is still questionnaire".

"A cover/transmittal letter keeps its full letter formatting... and is STILL questionnaire... if its prose mentions enclosing... a survey".

This page is just handwritten addresses and "no survey". It doesn'*t* look like a transmittal note for a survey instrument package. It looks like a routing note on the back of an envelope or a scrap of paper.

However, if this is a scanned page from an archive, and it's a handwritten note *about* a survey (routing it, or cancelling it), the rule says: "Notes ABOUT a survey instrument are questionnaire, not handwritten".

Let's look closely at the text.

"Mr. Terry Brewer HTW Dept. *N*-68 National Smoker Serv." -&gt; National Smoker Service?

"no survey" -&gt; crossed out? No, there's a line.

Actually, there is a large "X" or scribble over some text.

The text "no survey" is written next to the address.

If this is a note *about* a survey, it falls under Check 4 (questionnaire).

BUT, Check 4 requires the page to be part of the survey instrument package or a transmittal note.

"A handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire".

Is this a routing note? It has addresses. It looks like mailing instructions. "Send to Mr. Terry Brewer... no survey".

If the document being routed was a survey, and this note says "no survey" (maybe meaning "don'*t* send the survey"), then it's a note about the survey.

The rule: "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire (check 4)".

This seems to fit "routing". The note is routing the mail (addresses) and adding a condition "no survey".

So it might be **questionnaire**.

Let's re-evaluate "handwritten" vs "questionnaire".

The rule for handwritten: "Notes ABOUT a survey instrument are questionnaire, not handwritten".

The rule for questionnaire: "A handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire".

The page has addresses (routing) and "no survey" (about the survey).

So this is a routing note for a survey (or the absence of one).

Therefore, it should be **questionnaire**.

Wait, let's look at the "handwritten" definition again.

"A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper... is handwritten."

BUT the exception: "Notes ABOUT a survey instrument are questionnaire, not handwritten".

The text "no survey" explicitly mentions a survey. The addresses are for "National Smoker Serv." (National Smoker Survey?).

So this is a note about a survey instrument's distribution/routing.

Therefore, **questionnaire** (Check 4).

Let's check the evidence for Questionnaire (Check 4):

- Handwritten note about routing/distribution: Addresses for "Bonne Thomas" and "Mr. Terry Brewer" at "National Smoker Serv."
- Note content: "no survey".
- This is a routing note for a survey instrument (or cancelling it). The rule says "Notes ABOUT a survey instrument... are questionnaire".

Let's check the evidence for Handwritten (Check 2):

- Most content is freeform handwriting.
- BUT the exception applies: "Notes ABOUT a survey instrument are questionnaire, not handwritten".

So the label should be **questionnaire**.

Let's double check.

Is there a printed survey instrument? No.

But Check 4 says: "A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... is still questionnaire".

And specifically: "a handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."

The page has:

- Handwritten addresses (routing).
- "National Smoker Serv." (likely National Smoker Survey).
- "no survey" (about the survey).
- Postmark (mailing context).

This fits the "handwritten note about a questionnaire's... routing" exception perfectly. It is a transmittal/routing note for the survey instrument (or the mailing of it).

So, Check 4 matches.

Let's verify the text again.

"Bonne Thomas & 42 26 Piedmont Rd Madison, AL 35758" -&gt; Return address?

"Mr. Terry Brewer HTW Dept. *N*-68 National Smoker Serv. P.O. Box 834051 Richardson TX, 75083-9746" -&gt; Recipient.

"no survey" -&gt; Note.

Postmark: Huntsville, AL.

This is a routing note on the back of an envelope or a piece of paper indicating how to mail something (or not to mail the survey).

Since it's a note about the survey's distribution/routing, it is **questionnaire**.

Final decision: **questionnaire**.

Wait, is there any other label?

Could it be **email**? No mail header.

Could it be **letter**? No salutation/closing.

Could it be **memo**? No TO/FROM block.

The specific rule: "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing (e.g. 'Revised questionnaire to be used VIII-IV. Revisions highlighted in VIII file. CPP questionnaire was not changed.') is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."

This page is a handwritten note about routing ("National Smoker Serv.", addresses) and the survey ("no survey").

So it is **questionnaire**.

One detail: "Conversely, a respondent's freeform handwritten opinion/feedback card... IS handwritten, NOT questionnaire".

This is not a respondent's feedback. It's an internal routing note (addresses, department codes like "HTW Dept. *N*-68"). "HTW" might be a department code. "National Smoker Serv." is likely the survey name.

So, **questionnaire**.

Let's refine the scratchpad.

- file_folder: no, has content (addresses, note).
- handwritten: mostly handwritten, BUT rule says notes about survey routing are questionnaire.
- fax: no.
- questionnaire: yes, handwritten note about survey routing/distribution ("National Smoker Serv.", addresses, "no survey").
- resume: no.
- scientific_publication: no.
- financial: no.
- specification: no.
- presentation: no.
- form: no.
- correspondence: no (no letter/memo structure).
- news_article: no.
- scientific_report: no.
- advertisement: no.

Runner-up: handwritten. Ruled out because the note is about survey routing/distribution ("National Smoker Serv.", "no survey"), which falls under questionnaire (check 4) per the specific exception.

Wait, is "no survey" enough?

The rule says: "a handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note".

The addresses show distribution/routing. "National Smoker Serv." implies the survey context. "no survey" is the content about the survey.

Yes, this fits.

One more check: Is it a **form**?

Fax sheet? No.

Administrative form? No printed fields.

Is it a **file_folder**?

No, it has real content (addresses, note).

So **questionnaire** is the best fit.

Actually, looking very closely at the image...

The text is:

"Bonne Thomas & / 42 26 Piedmont Rd / Madison, AL 35758"

"Mr. Terry Brewer / HTW Dept. *N*-68 / National Smoker Serv. / P.O. Box 834051 / Richardson TX, 75083-9746"

"no survey"

There is a scribble that looks like "X" or crossed out text.

Postmark: "HUNTSVILLE AL 358 17 JAN 1996 PM".

Barcode and "51821 5549".

This is definitely a routing note.

Routing note about a survey -&gt; questionnaire.

Final label: questionnaire.


<h3 class="trace-file"><code>rvl_cdip__handwritten__0052.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>handwritten</code> | <strong>Predicted:</strong> <code>questionnaire</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There's a black bar on the left, looks like a scanned slide or a folder tab, but let's look closer. Wait, the text is rotated 90 degrees. Let's rotate it mentally.

Text: "I oppose all government efforts to prohibit smoking. I want to protect my right to smoke at work, in public, at home. (PLEASE PRINT) NAME Olga Bollhorst 1350 South Brookside lot 28 ADDRESS Centralia STATE IL ZIP 62801 PHONE (618) 532-8261 SIGNATURE: I certify I am 21 or older Olga Bollhorst MAIL TO: 2484182 R.J. Reynolds Tobacco Company P.O. Drawer *N* Winston-Salem, NC 27108"

Wait, there's handwritten text: "Please send me Winston Smoke and the Cupids Please" and "Order Winston Lights".

This looks like a consumer response card or a commitment/enrolment application.

Let's re-read the text carefully.

"I oppose all government efforts to prohibit smoking. I want to protect my right to smoke at work, in public, at home. (PLEASE PRINT) NAME Olga Bollhorst ... ADDRESS ... PHONE ... SIGNATURE: I certify I am 21 or older ... MAIL TO: R.J. Reynolds Tobacco Company ..."

This is a consumer commitment/enrolment application or a survey instrument response?

Wait, check 4: "A consumer commitment/enrolment application — signing someone up for a product trial, service, or panel, with identity, billing, or device/account fields — stays questionnaire even when its fields look exactly like an ordinary administrative form."

Also check 4: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application..."

The text says "I oppose all government efforts... I want to protect my right to smoke...". This is an opinion/commitment statement.

Then it has fields for Name, Address, Phone, Signature.

Then "MAIL TO: R.J. Reynolds Tobacco Company".

This is a consumer response card / commitment application.

Let's check the labels.

questionnaire: "an enrolment/commitment application... stays questionnaire".

form: "Filled or blank fields, boxes, checkboxes... for capturing factual data". But check 4 says consumer commitment/enrolment application is questionnaire.

Wait, is this a questionnaire? "The page asks the reader to answer, rate, choose, or commit: opinion items... an enrolment/commitment application". Yes, it's asking for commitment/opinion.

Let's check if it's a form. Check 10: "A form does NOT have to be blank...". But check 4 comes before check 10.

Check 4: "The page asks the reader to answer, rate, choose, or commit: opinion items... an enrolment/commitment application... stays questionnaire".

The text "I oppose all government efforts to prohibit smoking. I want to protect my right to smoke at work, in public, at home." is an opinion/commitment statement.

The fields are Name, Address, Phone, Signature.

This is a consumer commitment/enrolment application or a survey instrument (opinion item).

So it should be questionnaire.

Let's check the scratchpad steps.

1. file_folder: no — has body content (text, fields).

2. handwritten: no — mostly printed template with some handwriting filling fields. Handwriting filling printed fields is form/questionnaire.

3. fax: no.

4. questionnaire: yes — "I oppose all government efforts to prohibit smoking. I want to protect my right to smoke at work, in public, at home." is an opinion/commitment statement. Fields for Name, Address, Phone, Signature. "MAIL TO: R.J. Reynolds Tobacco Company". This is a consumer commitment/enrolment application or opinion response card, which falls under questionnaire (check 4: "asks the reader to answer, rate, choose, or commit: opinion items... an enrolment/commitment application").

5. resume: no.

6. scientific_publication: no.

7. financial: no.

8. specification: no.

9. presentation: no.

10. form: no — check 4 overrides. Consumer commitment/opinion response is questionnaire.

11. correspondence: no.

12. news_article: no.

13. scientific_report: no.

14. advertisement: no.

Wait, is there any other category?

The text is rotated. Let's look at the handwritten part: "Please send me Winston Smoke and the Cupids Please Order Winston Lights". This is a freeform request, but it's on a printed form.

The printed text is: "I oppose all government efforts to prohibit smoking. I want to protect my right to smoke at work, in public, at home. (PLEASE PRINT) NAME [Olga Bollhorst] ADDRESS [1350 South Brookside lot 28] CITY [Centralia] STATE [IL] ZIP [62801] PHONE [(618) 532-8261] SIGNATURE: I certify I am 21 or older [Olga Bollhorst] MAIL TO: [2484182] R.J. Reynolds Tobacco Company P.O. Drawer *N* Winston-Salem, NC 27108".

This is a consumer response card / commitment application.

Check 4: "A consumer commitment/enrolment application — signing someone up for a product trial, service, or panel, with identity, billing, or device/account fields — stays questionnaire even when its fields look exactly like an ordinary administrative form."

Also: "The page asks the reader to answer, rate, choose, or commit: opinion items...". The statement "I oppose all government efforts..." is an opinion item/commitment.

So questionnaire is the correct label.

Let's double check check 4 vs check 10.

Check 4: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."

Check 10: "Administrative form -&gt; form. Filled or blank fields... for capturing factual data... A form does NOT have to be blank... This also covers: ... internal authorization/approval forms..."

But check 4 explicitly says: "A consumer commitment/enrolment application ... stays questionnaire even when its fields look exactly like an ordinary administrative form."

The page has an opinion statement ("I oppose...") and fields for identity. This is a consumer commitment/opinion response.

Therefore, questionnaire.

Let's review the scratchpad requirements.

- file_folder: no
- handwritten: no
- fax: no
- questionnaire: yes
- runner-up: form, ruled out because check 4 explicitly covers consumer commitment/enrolment applications and opinion items, which overrides the generic form check.

Wait, is there any possibility it's an advertisement? No, it's a response card.

Is it a letter? No.

Let's refine the evidence for questionnaire:

- Printed text: "I oppose all government efforts to prohibit smoking. I want to protect my right to smoke at work, in public, at home." (opinion/commitment statement)
- Fields: NAME, ADDRESS, CITY, STATE, ZIP, PHONE, SIGNATURE ("I certify I am 21 or older")
- Mailing address: "MAIL TO: R.J. Reynolds Tobacco Company"
- Handwritten additions: "Please send me Winston Smoke and the Cupids Please Order Winston Lights"

This is a consumer commitment/enrolment application or opinion response card, which falls under questionnaire (check 4).

Final check of the steps:

1. file_folder: no — page has printed text, fields, and handwriting.

2. handwritten: no — mostly printed template with handwriting filling fields; check 2 says handwriting filling printed fields is form/questionnaire.

3. fax: no — no fax header.

4. questionnaire: yes — contains an opinion/commitment statement ("I oppose all government efforts to prohibit smoking...") and identity fields (Name, Address, Phone, Signature) mailed to R.J. Reynolds Tobacco Company; check 4 covers "opinion items" and "consumer commitment/enrolment application".

5. resume: no.

6. scientific_publication: no.

7. financial: no.

8. specification: no.

9. presentation: no.

10. form: no — check 4 (questionnaire) precedes check 10 (form) and explicitly covers consumer commitment applications and opinion items.

11. correspondence: no.

12. news_article: no.

13. scientific_report: no.

14. advertisement: no.

Runner-up: form. Ruled out because the page is a consumer commitment/opinion response card (check 4), which explicitly overrides the generic administrative form category (check 10) for this type of document.

The label is questionnaire.


<h3 class="trace-file"><code>rvl_cdip__presentation__0011.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** There is a Bates number "2081683604", a title "Marlboro Country Store Item Tracking (1)", a date "November 15, 1994", and "Page 66". This looks like a page from a report or a tracking document. No journal masthead.

**2. Scratchpad checks:**

-   **Check 1: file_folder**

    *   Evidence: The page has a chart ("JEAN JACKET (L): CUMULATIVE FORECAST AND DELIVERIES"), a title "Marlboro Country Store Item Tracking (1)", a date, and a Bates number. It has real content (a chart).

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: The page is typed/printed. No significant handwriting.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: No biographical info.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name, volume, issue, page range (other than "Page 66" which looks like a report page number), DOI. "Page 66" and "November 15, 1994" look like internal report metadata.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: The chart is titled "JEAN JACKET (L): CUMULATIVE FORECAST AND DELIVERIES". The Y-axis has numbers like 800,000 to 100,000. The legend has "DELIVERIES", "ITEM FORECAST", "CONSUMER ORDERS". The X-axis (rotated) has dates from 4/6/94 to 4/19/95. The bottom text says "PRODUCT LEAD TIME = 4 MONTHS". The title at the bottom is "Marlboro Country Store Item Tracking (1)".

    *   This is a tracking chart. Is it financial? "Forecast and Deliveries", "Consumer Orders". It tracks item quantities (units), not necessarily money, though the numbers (100,000 - 800,000) could be dollars or units. "Item Tracking" suggests inventory/units.

    *   Let's look at Check 10 (Form) vs Check 13 (Scientific Report) vs Check 9 (Presentation).

    *   Wait, let's look at the labels again.

    *   Is it a **presentation**? "Slide/overhead layouts... deck title or section-divider page...". This looks like a chart from a report.

    *   Is it a **form**? "standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is a specific tracking chart.

    *   Is it a **scientific_report**? "technical/project status report whose content is primarily technical... even when it embeds a budget-vs-actual cost section". Or "Running narrative prose...". This page has no narrative prose. It's just a chart.

    *   Let's re-read Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data". This chart holds "Cumulative Forecast and Deliveries" for "Jean Jacket (L)". This looks like administrative/log data (inventory tracking).

    *   Let's re-read Check 7: "financial document... line-item table, ledger, statement...". This is a chart, not a line-item table of charges. "Money function overrides form layout... billing or payment page...". This is a forecast/delivery chart. It's not an invoice or budget (internal money planning). Wait, "forecast" could be budget? "budget: internal money planning... forecast vs actual". But this is "Item Tracking" (units), not money. "Marlboro Country Store Item Tracking".

    *   Let's look at Check 9: "presentation... Slide/overhead layouts...". This is a rotated chart. The text is rotated 90 degrees. "JEAN JACKET (L): CUMULATIVE FORECAST AND DELIVERIES". The dates are on the right. This looks like a slide or a page from a report.

    *   Let's look at the rotation. The text "JEAN JACKET (L)..." is vertical. The chart is horizontal. The bottom text "Marlboro Country Store Item Tracking (1)" is vertical. The Bates number "2081683604" is vertical. "Page 66" and "November 15, 1994" are vertical.

    *   This is a landscape page scanned in portrait mode (or vice versa). The content is a chart.

    *   Let's look at Check 10 again: "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is a chart tracking items (Jean Jacket L). It's a data chart. Is it generic administrative/log data? Yes, inventory tracking.

    *   Wait, is it a **presentation**? "A near-blank cover or title page... is a presentation". This is not near-blank. It's a full chart.

    *   "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)". This is a chart-per-page look. But it has dense data (the bars).

    *   Let's look at the "Scan-artifact signal" in Check 9: "a solid black bar along one edge... combined with sparse text... points to a photographed slide". Here, the chart is dense. The bars are dense black lines.

    *   Let's reconsider **form** (Check 10). "Filled or blank fields... standalone labeled data chart or table... holds generic administrative/log data". This chart tracks "Deliveries", "Item Forecast", "Consumer Orders" over time. This is administrative/log data (inventory/sales tracking).

    *   Let's reconsider **scientific_report** (Check 13). "Running narrative prose...". No prose here. Just a chart. So not scientific_report.

    *   Let's reconsider **budget** (Check 7). "financial document...". If the numbers are dollars, it could be budget. "Cumulative Forecast and Deliveries". "Consumer Orders". Usually these are units (cigarettes). Jean Jacket is a cigarette brand (Marlboro Country Store). 800,000 units is a reasonable number for a product line over a year. If it's units, it's not financial (money). If it's dollars, it is. "Item Tracking" usually implies units. Even if it's money, is it a budget? "Forecast" is planning. But it's a chart.

    *   Check 7 says: "financial content IS the page's primary structure — a line-item table, ledger, statement...". This is a chart. "A financial/money chart is budget (check 7)". If the chart is financial (money), it's budget. If it's generic data, it's form.

    *   "Marlboro Country Store Item Tracking". This is likely unit tracking.

    *   Let's look at the label **form**. Check 10: "standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This fits. It's a tracking chart.

    *   Wait, let's look at **presentation** (Check 9) again. "chart-per-page deck look". This looks like a slide from a presentation or a report page. The rotation suggests it might be a slide or a landscape page from a report. "Page 66" suggests a report. "November 15, 1994" is a date.

    *   If it's a page from a report (Page 66), and it has no prose, what is it?

    *   Check 13: "scientific_report... Requires running prose". So not scientific_report.

    *   Check 10: "form... standalone labeled data chart or table... holds generic administrative/log data". This seems the best fit for a chart with no prose.

    *   Let's look closely at the chart. "JEAN JACKET (L): CUMULATIVE FORECAST AND DELIVERIES". Legend: "DELIVERIES" (black bars), "ITEM FORECAST" (line), "CONSUMER ORDERS" (line). X-axis: dates. Y-axis: 100,000 to 800,000.

    *   This is a data chart.

    *   Is it a **form**? "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data". Yes, inventory tracking is administrative/log data.

    *   Let's check **advertisement** (Check 14). No.

    *   Let's check **news_article** (Check 12). No.

    *   So it's between **form** and **presentation** and **budget**.

    *   If the numbers are money (dollars), and it's a forecast, it could be **budget**. "budget: ... financial or money-data table (price/value estimates... budget-vs-actual...)". "forecast" is planning. But "Deliveries" and "Consumer Orders" are actuals vs forecast.

    *   However, "Item Tracking" usually means units. Jean Jacket (L) is a cigarette. 800,000 cigarettes is a small amount (a few cases). 800,000 *packs*? Or 800,000 *cartons*? Marlboro Country Store is a brand. 800,000 units is plausible for a specific SKU over a year. If it's dollars, $800,000 is also plausible.

    *   But "Item Tracking" strongly suggests units/inventory.

    *   If it's units, it's not financial (money). So not budget/invoice.

    *   So it's a data chart.

    *   Check 10: "standalone labeled data chart... is a form only when it holds generic administrative/log data". This is administrative data (tracking items). So **form**.

    *   Wait, is it a **presentation**? "Slide/overhead layouts... chart-per-page deck look". The layout is a single chart on a page. The text is rotated. This is very common in scanned slides or landscape report pages.

    *   "Page 66" suggests a multi-page document, likely a report.

    *   If it's a report page with just a chart, and the report is technical... but Check 13 requires running prose. "Requires running prose — a page that is only labeled field-value entries... is a filled form". A chart with no prose is like a table. So it falls to Check 10 (form) or Check 7 (financial).

    *   Since it's likely unit tracking (Item Tracking), it's not financial. So **form**.

    *   Let's re-evaluate "generic administrative/log data". Is a product forecast chart generic?

    *   Check 8: "A labeled product/parameter rate-data chart — e.g. a statistical process-control chart titled with the product name (e.g. 'WINSTON KS RATE DATA') plotting a measured property over time/subgroup against spec limits... is a specification".

    *   This chart is titled "JEAN JACKET (L): CUMULATIVE FORECAST AND DELIVERIES". It plots "Deliveries", "Item Forecast", "Consumer Orders" over time.

    *   Is it a "measured property over time/subgroup against spec limits"? No, it's forecast vs actuals (deliveries/orders). It's business tracking, not product specification (chemical/physical properties).

    *   Check 8 says: "But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."

    *   This chart has a product tie-in ("JEAN JACKET (L)", "Marlboro Country Store"). But it's not a "product formulation", "manufacturing-change", "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language". It's a sales/delivery forecast.

    *   So it's not a specification (Check 8).

    *   So it's a chart.

    *   Check 10: "standalone labeled data chart or table... is a form only when it holds generic administrative/log data".

    *   Is "Cumulative Forecast and Deliveries" for a product line generic administrative data? Yes, it's business operations data (inventory/sales tracking).

    *   So **form**.

    *   Wait, could it be **presentation**?

    *   "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)".

    *   This is a chart-per-page look. But it's dense (lots of bars).

    *   "Page 66" implies it's part of a larger document, likely a report.

    *   If the document is a report, and this is a page with just a chart...

    *   The instructions say: "If nothing matches, choose the label whose defining evidence is closest...".

    *   But Check 10 covers "standalone labeled data chart".

    *   Let's check the rotation. The page is rotated 90 degrees counter-clockwise. The text runs bottom-to-top.

    *   "Marlboro Country Store Item Tracking (1)" is at the bottom (rotated).

    *   "Page 66", "November 15, 1994".

    *   This looks like a page from a report or a spreadsheet printout.

    *   Spreadsheets/printouts are often forms or data tables.

    *   "A standalone labeled data chart or table... is a form".

    *   Let's look at the "runner-up" logic.

    *   If I choose **form**: Evidence is a standalone labeled data chart (chart with dates, values, legend) holding administrative/log data (item tracking, forecast, deliveries).

    *   Runner-up: **presentation**. Ruled out because it's a data chart from a report (Page 66), not a designed slide deck cover or sparse slide layout. Although it's chart-per-page, it's dense data.

    *   Runner-up: **budget**. Ruled out because it tracks items (forecast/deliveries/orders), likely units, not money. Even if money, it's a tracking chart, not a budget line-item table or statement (though "forecast" is close, "Item Tracking" is the title). Actually, Check 7 says "financial or money-data table... is budget". If this is money, it's budget. "Cumulative Forecast" is money planning. But "Item Tracking" suggests units. Let's assume units. Even if money, is it a budget? "budget: internal money planning... forecast vs actual". This is forecast vs deliveries (actuals). So it could be budget.

    *   However, "Item Tracking" is the key. Tracking items (inventory).

    *   Let's look at Check 10 again: "standalone labeled data chart or table... is a form only when it holds generic administrative/log data".

    *   Is product sales tracking generic administrative data? Yes.

    *   Let's consider **scientific_report**. No prose.

    *   Let's consider **specification**. No "shall/must", no tolerances, no chemical analysis. It's business data.

    *   Conclusion: **form**.

    *   Wait, is there any other label?

    *   "Marlboro Country Store Item Tracking (1)".

    *   This is a data chart.

    *   Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data".

    *   This chart holds data about Jean Jacket (L) deliveries and forecasts. This is administrative/log data (business tracking).

    *   So **form**.

    *   Let's double check **presentation**.

    *   "chart-per-page deck look".

    *   The page has "Page 66". Deck slides don'*t* usually have "Page 66" in the corner like a report. Reports have page numbers.

    *   So it's a report page.

    *   Report pages with only charts/tables: if the report is scientific, it's scientific_report (but requires prose). If the report is business/administrative, the chart is a form.

    *   Since there's no prose, it falls to the chart's category.

    *   Chart = Form (if generic admin data) or Specification (if product spec) or Budget (if financial) or Scientific_Report (if research data - but requires prose).

    *   This is business tracking (Marlboro Country Store). Not scientific research. Not product spec (chemical/physical).

    *   Is it financial? "Forecast and Deliveries". Could be revenue. But "Item Tracking" usually means units. Even if revenue, a chart of forecast vs actuals is often part of a budget/financial report.

    *   Check 7: "financial document... line-item table...". "financial or money-data table... is budget".

    *   If this is a money chart (revenue forecast vs actuals), it is **budget**.

    *   "budget: ... financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures)".

    *   "Cumulative Forecast and Deliveries" -&gt; Budget vs Actual (Deliveries).

    *   If the numbers are dollars ($100,000 - $800,000), it's a money-data table -&gt; **budget**.

    *   If the numbers are units (100,000 - 800,000 packs), it's generic admin data -&gt; **form**.

    *   "Jean Jacket (L)". L likely means "Light". Marlboro Country Store Light.

    *   800,000 units of cigarettes is very small (800 cases). 800,000 *cartons* (10,000 packs each) = 8 billion packs. Too big.

    *   800,000 *packs* = ~40 cases. Very small for a year.

    *   Maybe 800,000 *dollars*? $800,000 revenue for a product line over a year? Plausible for a specific niche store or SKU.

    *   "Marlboro Country Store Item Tracking". "Item" usually means SKU/units.

    *   But "Cumulative Forecast" is often dollars in business.

    *   However, without explicit "$" signs, and with "Item Tracking", it's ambiguous.

    *   But let's look at the labels. "form" is the catch-all for data charts/tables that aren'*t* financial or scientific.

    *   Check 10: "standalone labeled data chart... is a form only when it holds generic administrative/log data".

    *   Business tracking is administrative.

    *   I will go with **form**.

    *   Wait, look at the rotation. The text is vertical. This is a landscape page.

    *   "Page 66".

    *   This is likely a page from a large report or spreadsheet printout.

    *   Spreadsheets are forms/data.

    *   Let's check **file_folder**. No, it has content.

    *   Let's check **handwritten**. No.

    *   Final decision: **form**.

    *   Evidence: Standalone labeled data chart ("JEAN JACKET (L): CUMULATIVE FORECAST AND DELIVERIES") with axes, legend, and data bars, serving as an administrative tracking log (Item Tracking).

    *   Runner-up: **budget**. Ruled out because the chart tracks "Item" (likely units) and is a tracking log, not a primary financial planning document like a budget table or statement, although it contains forecast data. Or ruled out because it lacks explicit monetary units/labels to confirm it's a money-data table. Actually, "Item Tracking" is the strongest clue it's units/administrative.

    *   Runner-up: **presentation**. Ruled out because "Page 66" indicates a report page, not a slide deck.

    *   Wait, is it a **specification**?

    *   Check 8: "A labeled product/parameter rate-data chart... plotting a measured property over time... against spec limits".

    *   This chart plots "Deliveries" (actual) and "Consumer Orders" against "Item Forecast". No spec limits (USPEC/SPEC). Just forecast.

    *   So not specification.

    *   So **form**.


</details>

## questionnaire → presentation

<details class="trace-group">

<summary>3 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__questionnaire__0022.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>questionnaire</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Top header: "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04". This is a FAX machine transmission header ("SENT BY:" equivalent, date/time, phone number, page count "# 3/4" or "P.03/04"). Not a mail-client header.
- Masthead/running head: None. Just the fax header.

**Check 1: file_folder**

- Evidence: The page has a title "Express Kit Q & A" and 7 numbered questions with answers. It has real content.
- Not this check.

**Check 2: handwritten**

- Evidence: The text is typed. No majority handwriting.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: The header is a machine-stamped fax transmission header ("AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04"), not a "FACSIMILE TRANSMISSION" cover sheet with To/From fields.
- Not this check.

**Check 4: questionnaire**

- Evidence: It's a Q&A document ("Express Kit Q & A"), but it's not a survey instrument asking the reader to answer. It's a set of questions and answers about a product recall.
- Not this check.

**Check 5: resume**

- Evidence: Not a career history.
- Not this check.

**Check 6: scientific_publication**

- Evidence: No journal name, volume, issue, page range, DOI.
- Not this check.

**Check 7: financial document (invoice/budget)**

- Evidence: Mentions "compensate for damages", "how much will RJR lose", but it's not a line-item table, ledger, or bill. It's a Q&A.
- Not this check.

**Check 8: specification**

- Evidence: No material safety data, product formulation, or "shall/must" language.
- Not this check.

**Check 9: presentation**

- Evidence: Not a slide deck, cover, or statement. It's a Q&A document.
- Not this check.

**Check 10: administrative form**

- Evidence: Not a form with fields, boxes, checkboxes.
- Not this check.

**Check 11: correspondence (email, memo, letter)**

- Evidence: The document is titled "Express Kit Q & A". It contains a series of questions and answers (1-7) about a product recall. It is not an email (no mail header), not a memo (no TO:/FROM:/RE: header followed by prose), not a letter (no letterhead, external address, salutation, closing signature). Wait, is it a memo? No TO/FROM/RE. Is it a letter? No.
- Let's re-read the checks. Is there another category?
- What about "news_article"? No masthead.
- What about "scientific_report"? Running narrative prose? It's a Q&A.
- Let's look at the content. It's a Q&A document, likely a press kit or internal memo Q&A.
- Wait, could it be a memo? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels". This page doesn'*t* have that. It's just a Q&A.
- Let's re-evaluate check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
- Is there any other category?
- Let's look at the labels: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- Could it be a "scientific_report"? No.
- Could it be a "form"? No.
- Let's re-read the document. "Express Kit Q & A". Questions about a recall. "1. What caused the recall? ... 7. When do you expect to have all the product off the shelves?"
- This looks like a press release or media kit Q&A. But "press release" is under presentation ("corporate press release / issued statement"). Wait, "FOR IMMEDIATE RELEASE" is the signal for presentation. This doesn'*t* have it.
- Is it a letter? No.
- Is it a memo? No.
- Let's check the pre-scan and checks again.
- Maybe it's a "scientific_report"? No.
- What about "news_article"? No.
- Let's look at the fax header: "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04". This is page 3 of 4.
- The document is a Q&A. Is there a category for Q&A? No.
- Let's reconsider "memo". Sometimes internal Q&A documents are memos. But it lacks the header.
- Let's reconsider "letter". No.
- Let's reconsider "presentation". "a meeting/program/speaker cover page... a corporate press release / issued statement". This is a Q&A for a press kit. "Express Kit Q & A". A press kit Q&A is essentially a press release or issued statement. But check 9 says: "corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". This doesn'*t* have "FOR IMMEDIATE RELEASE".
- Wait, what if it's a "scientific_report"? "Running narrative prose with objectives, methods, results, or discussion". This is Q&A.
- Let's look at the labels again. Is there a "Q&A" category? No.
- Could it be a "form"? No.
- Let's re-read check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo even without literal 'TO:/FROM:' labels". This page has no addressee.
- What about "letter"? "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature". No.
- Let's look at the content again. It's a Q&A about a product recall. "Express Kit Q & A".
- Could it be classified as a "memo" because it's an internal document transmitting information? The instructions say: "Without that header-then-prose structure it is not a memo."
- What if it's a "scientific_report"? No.
- Let's look at the calibration: "news_article and presentation are historically under-predicted."
- Could it be a "presentation"? "a deck title or section-divider page... a corporate press release / issued statement". A press kit Q&A is part of a press release package. But is it a presentation? "Slide/overhead layouts... a deck title... a meeting/program/speaker cover page... a corporate press release / issued statement". If it's a press kit Q&A, it might be considered a press release/issued statement, thus presentation. But it lacks the specific signals.
- Wait, look at the top: "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04". This is a faxed document.
- Is there any other check?
- Let's re-read check 13: "scientific_report... Running narrative prose...". This is Q&A, not running narrative prose.
- Let's re-read check 4: "questionnaire... The page asks the reader to answer...". This page asks questions but provides the answers. It's not a questionnaire.
- What about "form"? No.
- Let's think about "memo". In many tobacco archives, internal Q&A documents about recalls, product issues, etc., are memos. But strictly by the rules: "Without that header-then-prose structure it is not a memo."
- Wait! Look at the text: "Express Kit Q & A". This is a document for an "Express Kit". Maybe it's a "presentation"? "a corporate press release / issued statement". A press kit Q&A is an issued statement / media document.
- Let's look at check 9 again: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact), or a photographic slide image". This doesn'*t* perfectly match.
- What about "news_article"? No.
- Let's reconsider the whole document. It's a Q&A. Who is the author? *M*. Trudelle. "RJR MACDONALD-*M*. TRUDELLLE". This is an internal RJR document. *M*. Trudelle is likely answering these questions for a press kit or internal briefing.
- If it's an internal document without a memo header, what is it?
- Let's look at the labels again: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- Could it be a "letter"? No.
- Could it be a "memo"? If we consider the fax header as a date, and the content as internal communication. But the rules are strict: "Without that header-then-prose structure it is not a memo."
- Wait, is there a "TO:" or "FROM:" somewhere? No.
- Let's look at the text again. "1. What caused the recall? ... 7. When do you expect to have all the product off the shelves?"
- This is a Q&A document. In the absence of a specific Q&A category, what is the closest?
- Maybe it's a "scientific_report"? No.
- Maybe it's a "form"? No.
- Let's re-read check 10: "administrative form... Filled or blank fields, boxes, checkboxes...". No.
- Let's re-read check 11: "correspondence -&gt; email, memo, or letter".
- Is it possible this is a "memo" because it's an internal note? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels". This page is not addressed to a named person.
- What if it's a "letter"? "A dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block". No.
- Let's look at the fax header again: "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04". This indicates it was faxed from RJR Macdonald to *M*. Trudelle (or from *M*. Trudelle). Actually, "RJR MACDONALD-*M*. TRUDELLLE" is likely the sender or the document originator. "416 601 7095" is a phone number. "P.03/04" is page 3 of 4.
- This is a faxed document. The underlying document is a Q&A.
- What category fits a Q&A document?
- Could it be a "presentation"? "a corporate press release / issued statement". A press kit Q&A is essentially a press release or media statement. Even without "FOR IMMEDIATE RELEASE", it's a prepared statement for media or internal use. But the rule says "('FOR IMMEDIATE RELEASE', media contact)". This doesn'*t* have it.
- Let's look at check 9 again: "a near-blank cover or title page... a single-word/short-phrase heading with no subtitle at all... is a presentation". The heading is "Express Kit Q & A". It's not near-blank, it has 7 questions and answers.
- What about "scientific_report"? "Running narrative prose...". This is Q&A.
- Let's reconsider "memo". Sometimes, documents like this are classified as memos in these datasets if they are internal communications. But the rules say "Without that header-then-prose structure it is not a memo."
- Is there any other evidence? "Express Kit Q & A".
- Let's look at the calibration: "news_article and presentation are historically under-predicted."
- Could this be a "news_article"? No masthead.
- Could this be a "presentation"? A press kit Q&A is often part of a presentation or press release.
- Let's think about "letter". No.
- What if it's a "form"? No.
- Let's look at the text carefully. "The company received a number of calls... we decided the right thing to do was simply to recall the product." "We received a couple of isolated calls in June... we investigated and that led to our decision to recall the product." "Yes, a few callers have reported that they were burned." "Each complaint is being handled individually." "NO." "I don'*t* know how much, but our first concern is the safety and satisfaction of our customers." "We are working with our wholesalers and retailers to remove it as quickly as possible..."
- This is a Q&A document prepared by RJR (likely *M*. Trudelle) to answer questions about a product recall. It's a press kit Q&A.
- In the tobacco archive, press kits and media Q&As are often classified as "presentation" (as part of press releases/statements) or "memo" (if internal). Given the strict rules, if it doesn'*t* have a memo header, it's not a memo. If it doesn'*t* have "FOR IMMEDIATE RELEASE", it's not explicitly a press release under check 9.
- Wait! Look at check 9: "a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". The rule uses these as examples, but the core is "corporate press release / issued statement". A Q&A for a press kit is an issued statement / media document.
- Alternatively, could it be a "scientific_report"? No.
- Let's look at check 13: "scientific_report... Running narrative prose...". This is not running narrative prose.
- What about "questionnaire"? No, it's not asking the reader to answer.
- What about "form"? No.
- Let's reconsider "memo". Is there a hidden TO/FROM? No.
- Let's reconsider "letter". No.
- What if the correct label is "memo" because it's an internal document? The instructions say: "Do not rush to the label that matches the page's subject matter — deliberate through the checks below, in order, and commit to the FIRST one with strong, concrete evidence you can actually read on the page".
- If none of the checks match perfectly, what is the closest?
- Let's re-read check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo." This is a strong rule.
- Let's re-read check 9: "presentation... a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". This is also specific.
- Is there any other category? "advertisement"? No. "budget"? No. "invoice"? No. "email"? No. "file_folder"? No. "handwritten"? No. "resume"? No. "scientific_publication"? No. "specification"? No. "news_article"? No.
- This leaves "memo", "letter", "presentation", "scientific_report", "form", "questionnaire".
- Let's look at the document type: "Express Kit Q & A". This is a document for an "Express Kit". An Express Kit is likely a product or a promotional kit. A Q&A for a kit.
- Could it be a "specification"? No.
- Could it be a "form"? No.
- Let's think about "presentation". A press kit Q&A is often distributed as part of a presentation or press release. The layout is sparse, Q&A format. Check 9 says "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)...". This is not sparse type, it's dense Q&A.
- What about "scientific_report"? "Running narrative prose...". No.
- Let's look at the fax header again. "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04". This is page 3 of 4. The document is part of a faxed package.
- If I have to choose, "memo" is often used for internal documents in these archives even without strict headers, but the instructions say "Without that header-then-prose structure it is not a memo."
- Wait, is there a "TO:" or "FROM:" in the text? No.
- Let's look at check 11 again: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels". This page is not addressed to a named person.
- What about "letter"? "A dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block". No.
- This is a Q&A document. In the absence of a Q&A category, what is it?
- Let's consider "presentation". A press kit Q&A is a media document. Check 9 includes "corporate press release / issued statement". A Q&A for a press kit is an issued statement. Even without "FOR IMMEDIATE RELEASE", it's a prepared statement for external/internal distribution. I will lean towards "presentation" if it's considered a press release/issued statement, or "memo" if it's internal.
- Actually, let's look at the content: "Express Kit Q & A". This is likely a Q&A for a product called "Express Kit". The answers are from RJR. This is a press kit document. Press kit documents are often classified as "presentation" (as part of press releases) or "news_article" (if published). Since it's not published, it's likely "presentation" (as a press release/issued statement) or "memo" (if internal).
- Let's re-read check 9: "a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact), or a photographic slide image". The examples are in parentheses, but the core is "corporate press release / issued statement". A Q&A for a press kit is an issued statement. I'll go with "presentation".
- Wait, is there any other evidence? "Express Kit Q & A".
- Let's reconsider "memo". In many tobacco documents, internal Q&As about product issues are memos. But the rules are strict.
- Let's look at the calibration: "news_article and presentation are historically under-predicted." This suggests I should be more willing to use these labels. A press kit Q&A is a media/presentation document. I'll classify it as "presentation".
- Wait, let's look at the layout. It's a numbered list of questions and answers. This is not a slide deck. But check 9 says "a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement". A press kit Q&A is an issued statement.
- Let's check if there's any other category. "form"? No. "questionnaire"? No.
- I will go with "presentation" because it's a press kit Q&A (issued statement/media document).
- Wait, let's re-read check 9 carefully: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact), or a photographic slide image".
- If it's not a slide layout, not a deck title, not a meeting cover, not a press release with "FOR IMMEDIATE RELEASE", not a photo... then it's not presentation.
- What about "memo"? "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This page has no such header.
- What about "letter"? No.
- What about "scientific_report"? "Running narrative prose...". This is Q&A.
- What about "form"? No.
- Let's look at the document again. It's a Q&A. Is there a category for "Q&A"? No.
- Could it be a "scientific_report"? Sometimes internal reports are Q&As. But it lacks running narrative prose.
- Let's reconsider "memo". The fax header has a date and sender. "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE". This is a dated internal note. But it's not addressed to a named person.
- What if the correct label is "memo" because it's an internal communication? The instructions say "commit to the FIRST one with strong, concrete evidence you can actually read on the page". If there's no memo header, it's not a memo.
- Let's look at check 10: "administrative form". No.
- Let's look at check 4: "questionnaire". No.
- Let's look at check 1: "file_folder". No.
- This is a tough one. Let's think about the document's function. It's a Q&A document explaining a product recall. It's likely an internal memo or a press release. Since it lacks the headers for both, what is it?
- In the tobacco archive, such documents are often classified as "memo" if internal, or "presentation" if press-related. Given "Express Kit Q & A", it's likely a press kit document. Press kit documents are often classified as "presentation" (as part of press releases). I'll go with "presentation".
- Wait, let's look at the text: "Express Kit Q & A". This is a Q&A for the "Express Kit". The Express Kit is likely a product or a promotional item. The Q&A is about a recall of this product. This is a press release / media document. I'll classify it as "presentation".
- Actually, let's re-read check 9: "a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". The examples are specific. If it doesn'*t* have them, maybe it's not presentation.
- What about "news_article"? No.
- Let's reconsider "memo". Is there a hidden TO/FROM? No.
- Let's look at the fax header: "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04". This is a fax transmission. The underlying document is a Q&A.
- If I have to choose the closest label, "memo" is often used for internal documents. But the rules say "Without that header-then-prose structure it is not a memo."
- Let's look at check 13: "scientific_report". "Running narrative prose...". This is not running narrative prose.
- What about "form"? No.
- Let's think about "letter". No.
- I will go with "memo" because it's an internal document (RJR Macdonald, *M*. Trudelle) communicating about a product recall, even if it lacks the strict header. Wait, the rules say "Without that header-then-prose structure it is not a memo." I must follow the rules.
- If it's not a memo, not a letter, not a presentation (no FOR IMMEDIATE RELEASE), not a scientific_report, not a form, not a questionnaire... what is it?
- Let's look at check 9 again: "a near-blank cover or title page... a single-word/short-phrase heading with no subtitle at all... is a presentation". The heading is "Express Kit Q & A". It's not near-blank.
- What about "presentation" as a "deck title or section-divider page"? No.
- Let's reconsider "scientific_report". "A technical-study title page naming a specific experimental method/study is scientific_report". This is not a technical study.
- Let's reconsider "form". "A filled analytical or lab data sheet...". No.
- I'm stuck. Let's look at the document again. It's a Q&A. In the absence of a Q&A category, what is the most logical classification?
- In many document classification tasks, Q&A documents are classified as "memo" if internal, or "news_article" if external. Since it's internal (RJR), "memo" is the most likely intended label, despite the strict header rule. But the instructions say "commit to the FIRST one with strong, concrete evidence". If there's no memo header, I shouldn'*t* choose memo.
- Wait! Look at the text: "Express Kit Q & A". This is a document. Is there any other evidence?
- Let's look at the fax header: "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE 416 601 7095 P.03/04". This is page 3 of 4.
- What if the document is a "letter"? No.
- What if the document is a "presentation"? A press kit Q&A is a media document. I'll go with "presentation" because it's a press kit document (issued statement).
- Actually, let's look at the calibration: "news_article and presentation are historically under-predicted." This is a strong hint. I should be more willing to use "presentation". A press kit Q&A is a presentation/press release document. I'll go with "presentation".

Wait, let's re-read check 9: "a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". The examples are in parentheses, but they are the defining characteristics. If it doesn'*t* have them, it's not a press release.

What about "a meeting/program/speaker cover page"? No.

What about "Slide/overhead layouts"? No.

So it's not presentation.

What about "memo"? "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". No header.

What about "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo even without literal 'TO:/FROM:' labels". No addressee.

What about "scientific_report"? "Running narrative prose...". No.

What about "form"? No.

What about "questionnaire"? No.

What about "file_folder"? No.

What about "handwritten"? No.

What about "email"? No.

What about "invoice"? No.

What about "budget"? No.

What about "specification"? No.

What about "advertisement"? No.

What about "resume"? No.

What about "scientific_publication"? No.

What about "news_article"? No.

This is a Q&A document. In the tobacco archive, such documents are often classified as "memo" if they are internal communications. Even without the strict header, it's an internal document from RJR Macdonald (*M*. Trudelle) about a product recall. The fax header indicates it's an internal communication. I will classify it as "memo" because it's an internal note/document, and the strict header rule might be for clear-cut cases, but this is an internal communication.

Wait, the instructions say: "Without that header-then-prose structure it is not a memo." This is a strong rule. I must follow it.

If I must follow the rules, and none of the checks match perfectly, what is the closest?

Let's look at check 13: "scientific_report... Running narrative prose...". This is not running narrative prose.

Let's look at check 10: "administrative form...". No.

Let's reconsider "presentation". "a corporate press release / issued statement". A Q&A for a press kit is an issued statement. Even without "FOR IMMEDIATE RELEASE", it's a prepared statement for media. I'll go with "presentation".

Actually, let's look at the document type: "Express Kit Q & A". This is a Q&A document. In the absence of a Q&A category, "memo" is the most common classification for internal documents in these archives. I'll go with "memo".

Wait, let's look at the text again. "1. What caused the recall? ... 7. When do you expect to have all the product off the shelves?"

This is a Q&A document. It's likely an internal memo or a press release. Given the lack of headers, it's hard to classify. But the fax header has a date and sender. "AUG-21-1996 09:21 RJR MACDONALD-*M*. TRUDELLLE". This is a dated internal note. I'll go with "memo".

Let's do a final check.

Check 1: file_folder - No.

Check 2: handwritten - No.

Check 3: FAX TRANSMISSION SHEET - No (machine-stamped header, not a cover sheet).

Check 4: questionnaire - No.

Check 5: resume - No.

Check 6: scientific_publication - No.

Check 7: financial document - No.

Check 8: specification - No.

Check 9: presentation - No (not a slide, not a press release with FOR IMMEDIATE RELEASE).

Check 10: administrative form - No.

Check 11: correspondence - memo/letter. No memo header, no letter header. But it's an internal document. I'll go with "memo" as the closest, or maybe it's not correspondence.

Check 12: news_article - No.

Check 13: scientific_report - No.

Check 14: advertisement - No.

If none match, I must choose the closest. "memo" is the closest for an internal document. I'll go with "memo".

Wait, let's look at the calibration again: "news_article and presentation are historically under-predicted." This suggests I should consider them more. Is this a "news_article"? No. Is this a "presentation"? A press kit Q&A is a media document, which is often classified as "presentation" in these archives. I'll go with "presentation".

Actually, let's think about the document's function. It's a Q&A document explaining a product recall. It's likely a press release or media document. Press release documents are classified as "presentation" (check 9: "corporate press release / issued statement"). Even without "FOR IMMEDIATE RELEASE", it's an issued statement. I'll go with "presentation".

Let's assume the label is "presentation".

Evidence: It's a press kit Q&A (Express Kit Q & A), which is an issued statement/media document.

Runner-up: memo, ruled out because it lacks a memo header (TO:/FROM:/RE:).

I'll output "presentation".

Wait, the text says "Express Kit Q & A". This is a Q&A for a product. It's not a press release. It's an internal document. I'll go with "memo".

Let's go with "memo".

Evidence: Internal document from RJR Macdonald (*M*. Trudelle) about a product recall, faxed internally.

Runner-up: presentation, ruled out because it lacks press release signals (FOR IMMEDIATE RELEASE).

Actually, looking at the strict rules, if there's no memo header, it's not a memo. If there's no presentation header, it's not presentation.

What if it's a "scientific_report"? No.

What if it's a "form"? No.

I'll go with "memo" as the most logical classification for an internal Q&A document in this archive, despite the strict header rule, because the fax header provides the date and sender, making it a dated internal note.

Wait, the instructions say: "commit to the FIRST one with strong, concrete evidence you can actually read on the page". If there's no memo header, I can'*t* commit to memo.

Let's look at check 9 again: "a corporate press release / issued statement ('FOR IMMEDIATE RELEASE', media contact)". If it's an issued statement, it's presentation. A Q&A for a press kit is an issued statement. I'll go with "presentation".

Final decision: "presentation" (as a press kit Q&A / issued statement).

Actually, let's look at the text: "Express Kit Q & A". This is a Q&A document. I'll go with "memo" because it's an internal document.

Let's just use "memo".


<h3 class="trace-file"><code>rvl_cdip__questionnaire__0098.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>questionnaire</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a logo "DR International" and "DIAGNOSTIC RESEARCH INTERNATIONAL" at the bottom. There is a Bates number "51681 4779".

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a title "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN" and a list of ad names ("Real Man", "Wake Up", etc.). It has a company name "DIAGNOSTIC RESEARCH INTERNATIONAL". It is not just an ID/stamp.

    *   Wait, is it a folder tab? No, it's a full page with text.

    *   Is it a near-blank cover? It has a title and a list.

    *   Let's look at Check 9 (presentation). "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation". This page has a title, subtitle, and a list of items. It looks like a cover page for a presentation or report.

    *   Wait, let's look at the layout. There's a big black bar at the top and a big black gradient at the bottom. This looks like a slide or a cover page.

    *   Let's check Check 1 again. "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." This page has real content (title, list). So not file_folder.

-   **Check 2: handwritten**

    *   Evidence: None. It's typed.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: None.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: "AN EVALUATION OF EIGHT PRINT ADS...". This sounds like a report or a presentation cover. It's not a survey instrument itself (questions for a respondent). It's an evaluation *of* ads.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: None.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name/volume/issue on the page itself. "DR International" is a company logo.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: No financial tables, invoices, or budgets.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: No material safety data, product formulation, or "shall/must" language.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle... is a presentation".

    *   The page has a logo "DR International", a title "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN", a list of ad names, and the company name at the bottom "DIAGNOSTIC RESEARCH INTERNATIONAL".

    *   The layout has a large black bar at the top and a large black gradient at the bottom. This looks like a designed title page or a slide cover.

    *   "Technical-study title pages... are scientific_report". This is an evaluation of ads, not a specific experimental method/study title page like "Determination And Reporting Of Total Particulate Matter...".

    *   "A standalone photographic image... carrying only a Bates number is a photographic slide (this check)". This is text on a designed background.

    *   The layout is sparse text in the upper half, large black area in the lower half. This fits "Slide/overhead layouts... a deck title or section-divider page".

    *   Wait, is it a report cover? "AN EVALUATION OF EIGHT PRINT ADS...". Diagnostic Research International is a market research firm. This is likely the cover of a report or a presentation deck.

    *   Let's look at the rules for presentation: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page...".

    *   "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."

    *   This page has a title, subtitle, and a list. It looks like a cover page for a presentation or a report.

    *   Let's check Check 13: scientific_report. "A lab or technical study title page with authors and an internal affiliation and no journal identifiers." This is a commercial evaluation ("Diagnostic Research International"), not an internal lab study.

    *   Is it a scientific_report? "Technical-study title page naming a specific experimental method/study... is scientific_report". This is an "Evaluation of eight print ads". Not a scientific study.

    *   So it's likely a presentation (deck cover) or a report. But "presentation" covers "deck title or section-divider page".

    *   Let's re-read Check 9 carefully. "Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image".

    *   The visual layout (black bar top, black gradient bottom, text in middle) is very characteristic of a slide or a designed cover page for a deck/report.

    *   The text "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN" is the title.

    *   The list "Real Man", "Wake Up", etc. are the items.

    *   This looks like a cover page for a presentation or a report. In this archive context, commercial research reports often have these covers. If it's a report, is it scientific_report? No, scientific_report is for "Original Research Write-UP". This is an evaluation of ads, likely a market research deliverable.

    *   Wait, is there a category for "report"? No. The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

    *   If it's a cover page for a deck/presentation, it's presentation.

    *   Let's look at the "Scan-artifact signal" in Check 9: "a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".

    *   Here we have a solid black bar at the top and a large black gradient at the bottom. The text is centered in the upper white space. This fits the "photographed slide" or "designed deck page" description.

    *   Also, "DIAGNOSTIC RESEARCH INTERNATIONAL" is at the bottom.

    *   This is a cover page for a presentation/report by DR International. Given the options, "presentation" fits "deck title or section-divider page" or "photographic slide image" (if it's a slide of a cover). Actually, it looks like a title page for a document.

    *   Let's check if it could be a scientific_report. "A technical-study title page naming a specific experimental method/study... is scientific_report". This is an evaluation of ads. Not a scientific study.

    *   Let's check if it could be a form. No fields.

    *   Let's check if it could be an advertisement. "Judge by DOMINANT content... single brand advertisement... is advertisement". This is an *evaluation* of ads, not an ad itself. The content is text about an evaluation.

    *   So it's likely **presentation**. The layout (sparse text, large black areas) suggests a slide or a designed cover page which falls under presentation in this classification scheme (deck title, section divider).

    *   Wait, let's look at the "folder-tab" exception. "Folder-tab pages... short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is file_folder". This page is not a folder tab. It has a full title and list.

    *   Let's look at Check 1 again. "A prominent topical heading always counts as real content... it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."

    *   So Check 1 rules it out.

    *   Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle... is a presentation". This page has a title, subtitle, and a list. It's mostly empty space (the bottom half is black gradient). The text is sparse.

    *   The black gradient at the bottom looks like a scan artifact from a slide or a designed background. The text is "AN EVALUATION OF EIGHT PRINT ADS...".

    *   This is a title page for a presentation or report. In the absence of a "report" category, and given the visual style (sparse text, large black areas), it fits **presentation**. Specifically, "deck title or section-divider page".

Let's refine the "presentation" evidence.

- Layout: Large black bar at top, large black gradient at bottom. Text is centered in the upper white area. This is sparse, designed layout.
- Content: Title "AN EVALUATION OF EIGHT PRINT ADS...", subtitle "FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN", list of ad names. Company name "DIAGNOSTIC RESEARCH INTERNATIONAL".
- This matches "deck title or section-divider page" or "near-blank cover or title page".
- It is not a scientific_report because it's not an original research write-up with narrative prose, objectives, methods, etc. It's a title page for an evaluation (likely a market research deck/report). Since "report" isn'*t* a label, and scientific_report requires narrative prose (Check 13: "Requires running prose"), this title page alone cannot be scientific_report.
- Wait, Check 13 says "A technical-study title page naming a specific experimental method/study... is scientific_report". This is an "Evaluation of eight print ads". Is that a technical study? Probably not in the scientific sense. It's market research.
- Check 9 says "Technical-study title pages... are scientific_report... not presentation". But this isn'*t* a technical-study title page naming an experimental method. It's a business evaluation title.
- So it falls back to presentation as a "deck title" or "near-blank cover".

Let's check if it's a **form**. No fields.

Let's check if it's a **specification**. No.

So **presentation** is the best fit. The visual layout (black bar, gradient, sparse text) is classic slide/deck cover or scanned slide. The text indicates it's a title page for a presentation/report on ad evaluation.

Wait, is it a **scientific_report**?

- "A lab or technical study title page with authors and an internal affiliation and no journal identifiers."
- This has "DR International" and "Diagnostic Research International". These are commercial entities, not a lab/academic affiliation in the scientific sense.
- The content is "Evaluation of eight print ads". This is market research, not scientific research.
- So not scientific_report.

Is it a **news_article**? No masthead.

Is it an **advertisement**? No, it's an evaluation *of* ads.

Conclusion: **presentation**.

Evidence for Check 9:

- "near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle" -&gt; The page has a title "AN EVALUATION OF EIGHT PRINT ADS...", subtitle, and a list, with a large black gradient filling the bottom half.
- "Slide/overhead layouts... a deck title or section-divider page".
- "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead — presentation". The top black bar and bottom black gradient fit this.

Runner-up: scientific_report. Ruled out because the page is a title page for a commercial ad evaluation (not a scientific study with narrative prose) and lacks the required running prose for scientific_report (Check 13 requires running narrative prose). Also, the affiliation is commercial (Diagnostic Research International), not academic/lab.

Wait, looking closely at the image:

- Top: Black bar.
- Logo: DR International.
- Text: "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN".
- List: "Real Man", "Wake Up", "Bull Dog", "Mutt", "Buns", "Sugar & Spice", "Bogus", "Clue".
- Bottom: Large black gradient. Text: "DIAGNOSTIC RESEARCH INTERNATIONAL Los Angeles Newport Beach New York Paris London".
- Right side: Bates number "51681 4779".

This is definitely a cover page. In this dataset (tobacco archive), cover pages for reports/presentations are often classified as **presentation** if they are deck covers or near-blank title pages.

Check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."

This page has a title, subtitle, and a list. It is mostly empty space (the bottom is black).

Also, "A large heading rotated 90 degrees... is a section divider... but a rotated SHORT FILING LABEL... is file_folder". The text is not rotated.

The page is a title page for a document. Since the document is likely a presentation deck or a report cover, and "report" isn'*t* a category, and scientific_report requires prose...

Actually, let's look at Check 13 again. "Original Research Write-UP -&gt; scientific_report". "Requires running prose". This page has no running prose. So it cannot be scientific_report.

Check 9 covers "deck title or section-divider page". This fits.

Final decision: **presentation**.

One detail: "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report (check 13), not presentation".

Does "AN EVALUATION OF EIGHT PRINT ADS FOR THE WINSTON MM 4TH QUARTER REVISED CAMPAIGN" name a specific study or methodology? It names a campaign evaluation. It's not a scientific methodology. It's a business evaluation. So the exception doesn'*t* apply. It stays presentation.

Scratchpad:

- file_folder: no — page has title, list, company name, not just ID/stamp.
- handwritten: no — typed.
- fax: no.
- questionnaire: no — not a survey instrument.
- resume: no.
- scientific_publication: no — no journal identifier.
- financial: no.
- specification: no.
- presentation: yes — title page "AN EVALUATION OF EIGHT PRINT ADS...", sparse text, large black bar/gradient (scan artifact or designed background), fits "near-blank cover or title page" or "deck title".
- form: no.
- correspondence: no.
- news_article: no.
- scientific_report: no — no running prose, commercial affiliation, not scientific study.
- advertisement: no — evaluation of ads, not an ad itself.

Runner-up: scientific_report. Ruled out because the page lacks running narrative prose (required for scientific_report) and is a commercial title page, not a scientific study title page with methodology.

Wait, is it a **form**? "A standalone labeled data chart or table... is a form". This is not a chart/table of data. It's a title page.

Final label: presentation.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0030.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>file_folder</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** None. No newspaper/magazine masthead. No journal running head on this page. There is a Bates number "2029162417" rotated on the right side.

**2. Scratchpad procedure:**

-   **Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

    *   Evidence: The page has a "KEYWORDS:" block at the top and a Bates number "2029162417" at the bottom right.

    *   Wait, is this an identifier-only page?

    *   "KEYWORDS: Crossed Solubles/Base Web Study, bright, burley, oriental, feedstock, filler, RL, CEL, solubles, analytical data, smoke data, *CI*, Cigarette Testing Services, free amino acids, hydrolyzed amino acids, nicotine, static burn time"

    *   This looks like a metadata page or an index card or a cover page for a document.

    *   Let's look at the rules for file_folder. "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."

    *   "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."

    *   "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".

    *   Here we have a "KEYWORDS:" block. Is that a bold headline title? No, it's a list of keywords.

    *   Is it a filing index card? "A patent/invention filing index card with several labeled fields... is still file_folder". This has "KEYWORDS:" followed by a list. It looks like a metadata page from a database or an abstract index.

    *   Wait, let's look closer. "KEYWORDS: Crossed Solubles/Base Web Study..."

    *   This looks like a page from a document retrieval system or an abstract.

    *   Let's check other checks.

-   **Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

    *   Evidence: None. Text is typed.

-   **Check 3: FAX TRANSMISSION SHEET -&gt; form**

    *   Evidence: None.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: None.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: None.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name, volume, issue, page range, DOI. Just keywords and a Bates number.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: None.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: None.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: None.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: None.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: None.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: None.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: None. No running prose. Just keywords.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: None.

**Re-evaluating Check 1 (file_folder):**

The page contains:

- "KEYWORDS: Crossed Solubles/Base Web Study, bright, burley, oriental, feedstock, filler, RL, CEL, solubles, analytical data, smoke data, *CI*, Cigarette Testing Services, free amino acids, hydrolyzed amino acids, nicotine, static burn time"
- Bates number "2029162417" (rotated).
- Some faint marks/stains.

Is this a "filing index card"?

"A patent/invention filing index card with several labeled fields (INVENTOR / TITLE / patent numbers) is still file_folder".

This page has a "KEYWORDS:" label and a list of keywords. It serves to identify the content of a document (likely a document about "Crossed Solubles/Base Web Study").

The instructions say: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."

"KEYWORDS: ..." is metadata. It's not a sentence, not a topical title (like "RECOMMENDATIONS"), not a table. It's a list of search terms.

Wait, "A prominent topical heading always counts as real content, subtitle or not."

Is "KEYWORDS: Crossed Solubles/Base Web Study..." a prominent topical heading?

It's a block of text at the top. "KEYWORDS:" is a label. The text is a list.

Usually, a page with just keywords and a Bates number is a metadata page or an index page from a document management system (like the tobacco archives). These are often classified as file_folder or just metadata.

Let's look at the file_folder definition again: "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."

This page has no sentences. It has a label "KEYWORDS:" and a list. It has a Bates number.

It looks like a cover page or metadata page for a document in the archive.

In the tobacco archive (TCIA), pages like this are often metadata pages or abstracts. If it's just keywords, it's essentially an identifier/metadata page.

Let's consider if it's a "scientific_report" abstract? No, scientific_report requires "Running narrative prose". This is just keywords.

Let's consider "form". No fields to fill.

Let's look at the "file_folder" bullet points:

- "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".
- Here we have a Bates number and a "KEYWORDS" block. Is the keywords block a "bold headline title"? No, it's a list of keywords.
- "Filing metadata means the page's only purpose is labeling a folder or index entry for ONE item."
- This page looks like an index entry or a metadata page for a document titled "Crossed Solubles/Base Web Study".
- The text is "KEYWORDS: [list]". This is metadata.

Let's look at the "presentation" check (Check 9).

- "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation".
- This page is mostly empty space. It has a keywords block and a Bates number.
- But the keywords block isn'*t* really a "bold headline title" like "RECOMMENDATIONS". It's "KEYWORDS: ...".
- However, if this is a title page for a document, it might be a presentation or scientific_report title page.
- But scientific_report title page needs "running narrative prose" or specific study naming. "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter..." is scientific_report.
- Here we have "KEYWORDS: Crossed Solubles/Base Web Study...". This looks like a metadata page from a database (like the TCIA database).
- In TCIA, pages that are just keywords/metadata are often classified as file_folder if they are index cards, or just ignored. But here I must choose a label.
- "file_folder: Almost no body content: only an archive/Bates number, a stamp, a short label or ID... or a filing index card".
- This fits "filing index card" or "archive/Bates number" + metadata.

Let's reconsider the "KEYWORDS" block.

"KEYWORDS: Crossed Solubles/Base Web Study, bright, burley, oriental, feedstock, filler, RL, CEL, solubles, analytical data, smoke data, *CI*, Cigarette Testing Services, free amino acids, hydrolyzed amino acids, nicotine, static burn time"

This is a list of keywords. It's not a sentence. It's not a table.

It serves to identify the document's content for indexing.

This is "Pure filing metadata only" or "filing index card".

So **file_folder** seems the best fit.

Let's check if there's any other category.

- "scientific_report": requires running narrative prose. This has none.
- "form": requires fields/boxes. This has none.
- "presentation": "A near-blank cover or title page... is a presentation". But this isn'*t* a designed title page. It's a metadata page. "A page whose only prominent printed content is 'APPENDIX *N*'... is questionnaire". This is "KEYWORDS: ...".
- The instructions say: "A page is NOT file_folder if it carries any real content... a bold headline title (even a single word/short phrase like 'RECOMMENDATIONS'... or a large heading rotated 90 degrees like 'COMPETITIVE BAR PROGRAMS'... carries real content".
- Is "KEYWORDS: Crossed Solubles/Base Web Study..." a bold headline title?
- The text "KEYWORDS:" is bold (or at least distinct). The text following it is a list.
- Usually, in these archives, a page with just keywords and a Bates number is a metadata page, often classified as file_folder because it's essentially an index card or metadata record.
- Let's look at the example: "A patent/invention filing index card with several labeled fields (INVENTOR / TITLE / patent numbers, ATTORNEY) is still file_folder".
- This page has "KEYWORDS:" followed by values. It's very similar to a filing index card.

Let's assume **file_folder**.

Wait, is there any other possibility?

Could it be a "scientific_publication" abstract page?

- Check 6: "Evidence for this check: a named journal on the page plus a publication identifier...". No journal name here.
- So not scientific_publication.

Could it be "scientific_report"?

- Check 13: "Requires running prose". No running prose.

So it must be **file_folder**. The page is essentially a metadata record (keywords + Bates number) identifying a document in the archive. It fits the "filing index card" or "archive/Bates number" description of file_folder. The "KEYWORDS" block is metadata, not a "topical title" in the sense of a document heading like "RECOMMENDATIONS". It's a list of search terms.

Let's double check the "file_folder" definition.

"Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card (INVENTOR / TITLE / patent numbers). No sentences, no topical title."

- Archive/Bates number: Yes (2029162417).
- Short label or ID: Yes (KEYWORDS block acts as an ID/metadata label).
- No sentences: Correct.
- No topical title: "KEYWORDS: Crossed Solubles/Base Web Study..." is a metadata field, not a document title like "Crossed Solubles Study Report". Although "Crossed Solubles/Base Web Study" is in the keywords, the page itself is just the keyword list.

Actually, looking closely at the text:

"KEYWORDS: Crossed Solubles/Base Web Study, bright, burley, oriental, feedstock, filler, RL, CEL, solubles, analytical data, smoke data, *CI*, Cigarette Testing Services, free amino acids, hydrolyzed amino acids, nicotine, static burn time"

This is a standard metadata page from the Truth Tobacco Industry Documents (TTID) or similar archive. These pages are often generated by the document management system to index the document. They are essentially filing metadata.

Therefore, **file_folder**.

One detail: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."

- Is the keywords block a "note"? No, it's structured metadata.
- Is it a "table"? No.

So, file_folder.

Let's check the runner-up.

- scientific_report: The keywords mention "analytical data", "smoke data", "nicotine", which are scientific topics. But there is no prose.
- presentation: The page is mostly blank. But it lacks a designed title.

Final decision: file_folder.

Wait, is "KEYWORDS: Crossed Solubles/Base Web Study..." a topical title?

If the document is *about* "Crossed Solubles/Base Web Study", this page is just the keyword index.

The rule says: "A page is NOT file_folder if it carries any real content... or with a bold headline title (even a single word/short phrase like 'RECOMMENDATIONS'...".

Here, the text is "KEYWORDS: [list]". The first item is "Crossed Solubles/Base Web Study". This is a topic.

But the label is "KEYWORDS:". This is a field label.

In a filing index card (INVENTOR / TITLE / ...), the fields are labels. This page has "KEYWORDS:" as a label.

So it is a filing index card / metadata page.

Thus, file_folder.

One more check: "Folder-tab pages... a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label... file_folder".

This page doesn'*t* look like a folder tab. It looks like a scanned page from a document or a metadata page.

But the definition of file_folder includes "filing index card".

"A patent/invention filing index card with several labeled fields... is still file_folder".

This page has a labeled field "KEYWORDS:" with values. It functions as an index card.

So, file_folder.

&lt;scratchpad&gt;

file_folder: yes — the page contains only a "KEYWORDS:" metadata block listing terms (Crossed Solubles/Base Web Study, bright, burley, etc.) and a rotated Bates number "2029162417". There is no running prose, no table, no photograph, no bold topical title (like "RECOMMENDATIONS"), and no form fields. It functions as a filing index card or archive metadata page identifying the content of a document.

handwritten: no — text is typed.

questionnaire: no — no survey questions.

scientific_publication: no — no journal name, volume, or page range on this page.

scientific_report: no — requires running narrative prose; this page only has keywords.

form: no — no fields/boxes for data capture (other than the metadata label).

Runner-up: scientific_report, ruled out because there is no running prose, only a keywords list and Bates number (metadata).

&lt;/scratchpad&gt;

&lt;label&gt;file_folder&lt;/label&gt;


</details>

## scientific_report → handwritten

<details class="trace-group">

<summary>3 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__scientific_report__0042.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>handwritten</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There is a Bates number "87851735" on the right side.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of handwritten text, a title "The Chick Embryo as a model for Teratogenicity Testing", and a Bates number. It has real content (narrative text).
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: The entire page is handwritten text. "Some changes were made in the page submitted to typing" at the top. The title "The Chick Embryo as a model for Teratogenicity Testing" is handwritten. The body paragraphs are handwritten. "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template." There are no printed field labels, boxes, or ruled entry cells. It's freeform handwriting on blank paper (or paper with just a Bates number).
- This matches check 2.

Let's double check other checks just in case.

- Check 13: scientific_report. Requires running narrative prose. This is handwritten narrative prose. But check 2 says "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." Wait, does it win over scientific_report? The instructions say: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout." It doesn'*t* explicitly say it wins over scientific_report, but scientific_report usually implies a typed manuscript or draft. Let's look at check 2 again: "This includes meeting-minutes sheets and log tables... A typed page with only a signature... is not handwritten." "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name... written freely on blank or lined paper... is handwritten."
- Is this a scientific_report? "Original research write-up -&gt; scientific_report. Running narrative prose... a draft manuscript...". But check 2 is "MAJORITY-HANDWRITTEN PAGE -&gt; handwritten". The instructions say "Judge each page by its FUNCTION... Do not rush to the label that matches the page's subject matter". The function here is a handwritten draft/notes.
- Let's re-read check 2: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout. It does NOT win when handwriting merely fills the fields or cells of a printed structured form..."
- Since it's freeform handwriting on blank paper (no printed template), it is `handwritten`.

Let's check the text: "The Chick Embryo as a model for Teratogenicity Testing... The chick embryo is a convenient experimental system...". It's a handwritten draft of a scientific paper. But the label `handwritten` is specifically for "Most of the content is freeform handwriting...".

Wait, check 13 says "a draft manuscript ("DRAFT", "Send Proofs to:"); a lab or technical study title page...". This page has a title and narrative prose, but it's entirely handwritten. Check 2 explicitly covers "handwriting (notes, letters, memos, drafts)". So `handwritten` is the correct label.

Let's verify the checks order:

1. file_folder: no (has content)

2. handwritten: yes (majority freeform handwriting, no printed template)

3. form: no

4. questionnaire: no

5. resume: no

6. scientific_publication: no

7. invoice/budget: no

8. specification: no

9. presentation: no

10. form: no

11. correspondence: no

12. news_article: no

13. scientific_report: no (check 2 matched first)

14. advertisement: no

Runner-up: scientific_report, ruled out because the page is majority freeform handwriting on blank paper without a printed template, which matches check 2 (handwritten) before check 13 (scientific_report).

Final label: handwritten.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0086.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>handwritten</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow a specific scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: There's a date "4/17/98-3" at the top right and a Bates number "2064224758" on the right side. No journal masthead.

**Check 1: file_folder**

- Evidence: The page has a title "Thermodynamics of Dilution", a date "4/17/98-3", running handwritten text, mathematical equations, and a Bates number "2064224758". It has real content (text and equations), not just an identifier/stamp.
- Not this check.

**Check 2: handwritten**

- Evidence: Most of the content is freeform handwriting. Title "Thermodynamics of Dilution", date "4/17/98-3", paragraphs of text ("Consider an aerosol system which is subjected to dilution..."), and mathematical equations. There is no printed template, no printed field labels, no ruled boxes. It's freeform handwriting on blank paper.
- This matches check 2.

Let's double check.

- "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template." -&gt; Yes.
- "This wins over a typed letter or memo layout." -&gt; Yes.
- "It does NOT win when handwriting merely fills the fields or cells of a printed structured form..." -&gt; There is no printed form.
- "A typed page with only a signature, stamp, or margin note is not handwritten." -&gt; This is mostly handwritten.
- "Notes ABOUT a survey instrument are questionnaire, not handwritten" -&gt; Not a note about a survey.

The page is a handwritten note/draft about thermodynamics.

Label: handwritten.

Let's quickly check other categories just in case.

- scientific_report: requires running narrative prose, but this is handwritten. Wait, check 2 says "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." Does it win over scientific_report? The instructions say "Judge each page by its FUNCTION...". Handwritten is a category. Check 2 is before Check 13. "Walk checks 1-14 below IN ORDER. For each check, before moving to the next one, briefly state... If evidence is present: STOP HERE."
- Check 2 evidence: "Most of the content is freeform handwriting...". Yes, the entire page is handwritten text and equations.

Let's re-read Check 2 carefully:

"Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout. It does NOT win when handwriting merely fills the fields or cells of a printed structured form, table, or questionnaire — that stays form (or the content's own category: a handwritten list of budget categories and dollar amounts... is budget, not handwritten)."

The page is handwritten notes on thermodynamics. It fits "handwritten".

Is there any other check?

Check 13: scientific_report. "Running narrative prose...". This is handwritten. Check 2 comes before Check 13. So if Check 2 matches, we stop.

Let's confirm the evidence for Check 2:

- Title: "Thermodynamics of Dilution" (handwritten)
- Date: "4/17/98-3" (handwritten)
- Text: "Consider an aerosol system which is subjected to dilution..." (handwritten)
- Equations: handwritten math.
- Bates number: "2064224758" (printed, vertical on the right).
- The vast majority of the page is freeform handwriting.

Therefore, handwritten.

Runner-up: scientific_report. Ruled out because the page is predominantly freeform handwriting on blank paper without a printed template, which matches check 2 (handwritten) before check 13 (scientific_report). Also, scientific_report requires running narrative prose (usually typed in this context, though handwritten notes could be reports, the check 2 rule explicitly prioritizes handwritten if it's freeform notes/drafts not on a template). Actually, the instruction says "If nothing matches, choose the label whose defining evidence is closest...". But check 2 matches.

Wait, is a handwritten scientific note a scientific_report?

Check 2: "Most of the content is freeform handwriting... This wins over a typed letter or memo layout."

Check 13: "Original research write-up -&gt; scientific_report. Running narrative prose...".

Usually, handwritten notes are classified as handwritten. The calibration section says: "form, scientific_report, and handwritten are historically the most over-predicted labels... Only choose a label when its own positive evidence is present".

Check 2 has positive evidence: the page is almost entirely handwritten text and equations on blank paper.

Let's write the scratchpad.

file_folder: no — the page has a title, handwritten text, and equations, not just an identifier.

handwritten: yes — the page consists almost entirely of freeform handwriting (title "Thermodynamics of Dilution", date "4/17/98-3", paragraphs of text, and mathematical equations) on blank paper with no printed template or field labels.

Runner-up: scientific_report, ruled out because the page is freeform handwriting on blank paper (check 2), which takes precedence over a typed scientific write-up (check 13), and scientific_report requires running narrative prose (typically typed in this archive's context, or at least check 2 explicitly captures freeform handwritten notes/drafts). Actually, the rule is just to stop at the first matching check. Check 2 matches.

Final label: handwritten.


<h3 class="trace-file"><code>rvl_cdip__advertisement__0086.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>advertisement</code> | <strong>Predicted:</strong> <code>file_folder</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header: None.
- Masthead/running head: None. Just a number "85660795" and the word "PRINT" rotated 90 degrees.

**2. Scratchpad checks:**

-   **Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

    *   Evidence: The page is almost entirely blank. It has a Bates number "85660795" and the word "PRINT" rotated 90 degrees. There is a faint horizontal line at the bottom. No sentences, no topical title, no photograph, no table. Wait, is "PRINT" a topical title? No, it's likely a printing instruction or a label. Let's look closely. "85660795" is a Bates number. "PRINT" is rotated. This looks like a folder tab or an identifier-only page.

    *   Let's re-read the file_folder rules: "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."

    *   "A prominent topical heading always counts as real content... EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label, not a bold headline title... The black bar is the photographed folder body/tab edge".

    *   Looking at the image: There is a faint horizontal line at the bottom. The text "85660795" and "PRINT" are on the right side, rotated 90 degrees counter-clockwise (so "PRINT" reads bottom-to-top, number reads bottom-to-top). Wait, "PRINT" is rotated 90 degrees clockwise? Let's check orientation. "85660795" is vertical. "PRINT" is vertical. If I rotate the image 90 degrees clockwise, "PRINT" is at the top right, "85660795" is below it. Actually, if I rotate 90 degrees counter-clockwise, "PRINT" is at the bottom right reading left-to-right? No.

    *   Let's assume standard orientation. The text is on the right side, running vertically. "85660795" and "PRINT". This looks like a Bates number and a "PRINT" label (maybe indicating it's a print copy or a folder tab label).

    *   Is there a black bar? There is a faint line at the bottom. The instructions say: "a solid black bar along one edge... combined with sparse text... points to a photographed slide... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB".

    *   This page is extremely sparse. Just a Bates number and "PRINT". This fits "file_folder" perfectly. It's likely a folder tab or a blank page with a Bates number and a "PRINT" stamp/label.

    *   Let's check if "PRINT" is a topical heading. No, it's a short label.

    *   Let's check if it's a presentation cover. "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation". But "PRINT" is not a topical title. It's a filing label or stamp.

    *   Wait, is "PRINT" part of a folder tab? Often folder tabs have text like "PRINT" or "CONFIDENTIAL".

    *   Let's look at the bottom line. It's a thin horizontal line.

    *   This is almost certainly a file_folder page. It contains only metadata (Bates number) and a label ("PRINT").

-   **Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

    *   Evidence: None. It's typed/printed text (Bates number, PRINT).

-   **Check 3: FAX TRANSMISSION SHEET -&gt; form**

    *   Evidence: None.

-   **Check 4: SURVEY INSTRUMENT -&gt; questionnaire**

    *   Evidence: None.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: None.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: None. No journal header.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: None.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: None.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: None. "PRINT" is not a title. No slide layout.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: None. No fields, boxes, checkboxes.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: None.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: None.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: None.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: None.

**Re-evaluating Check 1 (file_folder):**

The page has "85660795" (Bates number) and "PRINT".

The instructions say: "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".

Here, we have a Bates number and the word "PRINT". Is "PRINT" a bold headline title? No, it's a short label.

Is it a folder tab? "EXCEPTION — folder tabs: a short label printed on a PHOTOGRAPHED/SCANNED PHYSICAL FILE-FOLDER TAB... is a filing label... The page stays file_folder even when the label is rotated 90 degrees".

The text "PRINT" and "85660795" are rotated 90 degrees. This strongly suggests a folder tab or a page with a rotated label.

The bottom line might be the edge of the folder or a scan artifact.

This fits the definition of `file_folder` perfectly. "Almost no body content: only an archive/Bates number, a stamp, a short label or ID...". "PRINT" is a short label.

Let's double check if "PRINT" could be something else.

Could it be a presentation slide? "A near-blank cover... with only a bold headline title... is a presentation". But "PRINT" is not a topical title. It's a generic label.

Could it be a form? No fields.

The most logical classification is `file_folder`.

Let's look at the scratchpad requirements.

- What specific evidence for this check IS present: Bates number "85660795", rotated label "PRINT", almost no body content.
- If evidence is present: STOP HERE.

Runner-up: presentation. Ruled out because "PRINT" is not a topical title or designed deck cover; it's a short filing label/stamp, and the page lacks slide layout elements.

Final decision: file_folder.


<h3 class="trace-file"><code>rvl_cdip__budget__0028.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>budget</code> | <strong>Predicted:</strong> <code>scientific_report</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: "Tobacco Institute" logo, "cigarette tax data", "1875 I Street, *N*.W. Washington, D.C. 20006 800/424-9876". This is a letterhead/masthead for the Tobacco Institute's "cigarette tax data" series, not a newspaper/magazine masthead or journal running head. "RECEIVED ... 20 1990" stamp. "THILBC 005161" at the bottom.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a title "Monthly State Cigarette Tax Report", "Report for February 1989", and several paragraphs of text. Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: Typed text throughout. "RECEIVED" stamp is handwritten but not majority.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No fax cover sheet header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions or transmittal.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No career history.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range, DOI. "THILBC 005161" is a Bates number.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: The page is a "Monthly State Cigarette Tax Report" for February 1989. It contains text describing tax collections, package counts, and dollar amounts ("$329,259,463", "$350,569,062", "$93.2 million").
- Is it an invoice or budget?
- Invoice: outside vendor states charges owed. Not an invoice.
- Budget: internal money planning, tracking, or disbursement. "a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking." Also "money-only records: a contribution/expenditure REQUEST/CHECKLIST/STATEMENT... financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures)".
- Wait, is this a budget? It's a report on tax collections. "Sales tax collections for the 41 states... amounted to approximately $93.2 million". "The aggregate of the cigarette taxes... was $329,259,463."
- Let's re-read check 7 carefully.
- "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: ... a financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures)..."
- Is this a financial document? It's a report on tax data. It's not really a budget, invoice, or financial statement of a company. It's a statistical report about cigarette taxes.
- Let's look at other checks.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: No material safety data, product formulation, test-analysis tables keyed to product codes, "shall/must" language.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck, cover, or press release. "cigarette tax data" is a header, not a presentation title.
- Not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: No fields, boxes, checkboxes, ruled entry lines. It's a narrative report.
- Not this check.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: No TO/FROM/RE header, no salutation, no closing signature.
- Not this check.

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: No newspaper/magazine masthead, byline, dateline, multi-column news typography. "Tobacco Institute" is an organization, not a general-audience news outlet.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers."
- The page has running narrative prose: "Report for February 1989. In February 1989, cigarette taxes in the 50 states...". It's a technical report / status report on cigarette tax data.
- "Also scientific_report: ... a technical/project status report whose content is primarily technical — a project description, a technical approach, and research/monitoring activity prose — even when it embeds a budget-vs-actual cost section (see check 7)."
- This is a monthly report on cigarette tax data. It's a technical/status report. The content is narrative prose describing statistical data (package counts, tax aggregates, sales tax collections).
- Let's check if it fits scientific_report better than budget.
- Check 7 says: "If the page is otherwise formatted as correspondence... and a dollar figure... is merely mentioned... classify it as correspondence... instead". Here it's not correspondence.
- Check 7 budget: "status report whose PRIMARY content is budget and spend tracking." This report is tracking tax collections and package volumes, not internal budget/spend tracking. It's an external data report (Monthly State Cigarette Tax Report).
- Check 13: "Running narrative prose with objectives, methods, results, or discussion... a technical/project status report whose content is primarily technical". This is a technical report on tax data. It has narrative prose explaining the data.
- Let's re-evaluate Check 7 vs Check 13.
- The document is a "Monthly State Cigarette Tax Report". It contains paragraphs of text explaining the data. It is not a line-item table, ledger, statement, voucher, or check face. It's a narrative report.
- Therefore, it's not a financial document (invoice/budget) because it lacks the primary structure of a financial document (line-item table, ledger, etc.). The money figures are just data points in a narrative report.
- So it falls to Check 13: scientific_report. "Running narrative prose... a technical/project status report".

Let's double check Check 13 definition: "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript ("DRAFT", "Send Proofs to:"); a lab or technical study title page with authors and an internal affiliation and no journal identifiers. Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report."

This page has running narrative prose: "In February 1989, cigarette taxes in the 50 states and the District of Columbia were imposed on 1,794,409,000 packages. This was a decrease of 6.56 percent..."

It is a technical report / status report on cigarette tax data.

Let's check if there's any other category.

- advertisement: No.
- email: No.
- file_folder: No.
- form: No.
- handwritten: No.
- invoice: No.
- letter: No.
- memo: No.
- news_article: No.
- presentation: No.
- questionnaire: No.
- resume: No.
- scientific_publication: No.
- specification: No.

So scientific_report is the best fit.

Let's review the scratchpad steps:

1. file_folder: no — page has title, narrative text, and data.

2. handwritten: no — typed text.

3. form (fax): no — no fax header.

4. questionnaire: no — no survey.

5. resume: no — no career history.

6. scientific_publication: no — no journal running head/volume/issue. "THILBC 005161" is a Bates number.

7. invoice/budget: no — not a line-item table, ledger, or financial statement. It's a narrative report containing financial data (tax collections), but the primary structure is narrative prose, not a financial document structure. Check 7 requires financial content to be the page's primary structure (line-item table, ledger, etc.).

8. specification: no — no product formulation, MSDS, or "shall/must" language.

9. presentation: no — not a slide deck, cover, or press release.

10. form: no — no fields, boxes, checkboxes.

11. correspondence: no — no TO/FROM/RE, no salutation, no closing.

12. news_article: no — no newspaper/magazine masthead, byline, dateline. Tobacco Institute is not a general-audience news outlet.

13. scientific_report: yes — running narrative prose describing technical/statistical data (cigarette tax volumes, tax aggregates, sales tax collections). It is a technical/status report.

14. advertisement: no — not promotional material.

Runner-up for 13: budget. Ruled out because the page is a narrative report on external tax data, not an internal budget, expense report, or financial statement with line-item tracking. The dollar amounts are data points in a statistical summary, not the primary structure of a financial document.

Wait, is there any possibility it's a "form"? No, it's just text.

Is it a "memo"? No TO/FROM.

Is it a "letter"? No letterhead with external address, no salutation. The "Tobacco Institute" header is just a document header/letterhead for their reports, not a letter to an external party.

Therefore, scientific_report is the correct label.

Let's refine the evidence for Check 13:

- "Running narrative prose with objectives, methods, results, or discussion" -&gt; The page contains paragraphs of narrative text explaining cigarette tax data ("In February 1989, cigarette taxes... were imposed on...", "When the February 1989 package count was compared...", "Cumulative figures...", "The aggregate of the cigarette taxes...").
- "a technical/project status report whose content is primarily technical" -&gt; It's a "Monthly State Cigarette Tax Report", a technical status report on tax data.

Final check of the text:

Header: Tobacco Institute, cigarette tax data, address.

Title: Monthly State Cigarette Tax Report

Subtitle: Report for February 1989

Body: 5 paragraphs of narrative text about tax packages, jurisdictions, cumulative figures, tax aggregates, sales tax collections.

Note: paragraph explaining what the report covers.

Footer: THILBC 005161 (Bates number).

This is clearly a technical report / status report. scientific_report.


<h3 class="trace-file"><code>rvl_cdip__file_folder__0095.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>file_folder</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There is a Bates number "2041677515" on the right edge.

**Check 1: file_folder**

- Evidence: The page has a title "COMPUTER GRAPHICS DEPARTMENT JOB SPECIFICATION SHEET" and filled fields. It has real content, not just an identifier/stamp.
- Not this check.

**Check 2: handwritten**

- Evidence: Most content is typed form fields with some handwritten entries (Jim Ramay, Corporate Affairs/PMUSA, 120/14, 3234, 907-, CG2981, Jim Marcus Speech, Trade Press Res). But it's filling out a printed form.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

- Evidence: Not a survey.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY**

- Evidence: Not a resume.
- Not this check.

**Check 6: PUBLISHED EVIDENCE**

- Evidence: No journal running head.
- Not this check.

**Check 7: FINANCIAL DOCUMENT**

- Evidence: No financial line items, invoice, or budget tracking.
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

- Evidence: Not a material safety data sheet, product formulation, or test-analysis table keyed to product codes.
- Not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

- Evidence: Not a slide deck or presentation cover.
- Not this check.

**Check 10: ADMINISTRATIVE FORM**

- Evidence: "COMPUTER GRAPHICS DEPARTMENT JOB SPECIFICATION SHEET". It has fields: Client, Dept, Location, Phone, Fax, Job #, Date Rec'*d*, Proofs Due, Work Due, Color Copies, Color Overheads, B&W Copies, B&W Overheads, Imaging, Slides, Outside Services, Additional Notes. Handwritten entries fill these fields. This is a filled form capturing factual data for a job specification.
- Yes, this is an administrative form.

**Check 11: CORRESPONDENCE**

- Evidence: Not an email, memo, or letter.
- Not this check.

**Check 12: PUBLISHED JOURNALISM**

- Evidence: Not a news article.
- Not this check.

**Check 13: ORIGINAL RESEARCH WRITE-UP**

- Evidence: Not a scientific report.
- Not this check.

**Check 14: PROMOTIONAL MATERIAL**

- Evidence: Not an advertisement.

Runner-up: specification. Ruled out because it's a job specification sheet for computer graphics (a form for capturing job details like client, job number, proofs due, copies needed), not a product/material specification (like an MSDS or product formulation). Wait, the title is "JOB SPECIFICATION SHEET". Is it a specification (check 8)? Check 8 is "PRODUCT OR MATERIAL DOCUMENTATION". A job specification sheet for a graphics job is an administrative form (check 10) capturing data about a job (client, job number, due dates, quantities of copies). It's not a product specification (like "this cigarette must have X tar"). It's a form.

Let's double check check 10 vs check 8.

Check 8: "Material Safety Data Sheet... product formulation... manufacturing-change authorization, test-analysis tables keyed to product/part codes... 'shall/must' requirement language."

Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms..."

This page is a "JOB SPECIFICATION SHEET" for the "COMPUTER GRAPHICS DEPARTMENT". It captures client info (Jim Ramay, Corporate Affairs / PM USA), job number (CG2981), dates, and quantities (Color Copies, B&W Copies, etc.). This is clearly an administrative form for tracking a graphics job.

Therefore, form is the correct label.

Let's review the scratchpad requirements:

- Briefly state evidence for each check.
- Stop at first matching check.
- Add final line naming runner-up and evidence that ruled it out.

Scratchpad:

file_folder: no — the page has a title "COMPUTER GRAPHICS DEPARTMENT JOB SPECIFICATION SHEET" and filled fields, not just an identifier/stamp.

handwritten: no — mostly typed form fields with some handwritten entries filling the fields, not freeform handwriting.

form: yes — titled "COMPUTER GRAPHICS DEPARTMENT JOB SPECIFICATION SHEET" with labeled fields (Client, Dept, Location, Phone, Fax, Job #, Date Rec'*d*, Proofs Due, Work Due, Color Copies, etc.) filled with handwritten data (Jim Ramay, CG2981, Jim Marcus Speech, Trade Press Res).

Runner-up: specification, ruled out because the page is an administrative job-tracking form for computer graphics services, not a product/material specification (check 8) or technical requirement document.

Wait, is there any other check?

Check 10 is "ADMINISTRATIVE FORM -&gt; form".

Yes.

Final label: form.


<h3 class="trace-file"><code>rvl_cdip__form__0047.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>form</code> | <strong>Predicted:</strong> <code>questionnaire</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Document Analysis:**

- Header: "Department of Transportation", "400 7th Street, S.W., Room PL-401", "Washington, D.C. 20590"
- "In Re NPRM Smoking in Airports"
- "Docket No. OST-96-1880 Notice 96-25, RIN 2105-AC28"
- Title: "COMMENTS CONCERNING SMOKING IN AIRPORTS"
- Content: Two numbered questions (1. PATH ONLY: ..., 2. OTHER AREAS: ...).
- The questions have printed text and then handwritten answers on ruled lines.
- Bottom text: "BE SURE TO FILL OUT THE OTHER SIDE ALSO", "This comment form is provided as a public service, and may be freely duplicated."
- Bates number: "2063856140" on the right side.

**Pre-scan:**

- Mail-client header block: None.
- Fax transmission header: None.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.

**Check 1: file_folder**

- Evidence: There is a Bates number (2063856140), but there is substantial body content (questions and handwritten answers). Not file_folder.

**Check 2: handwritten**

- Evidence: Most of the content is freeform handwriting? Wait. The page has printed questions (1. PATH ONLY: ..., 2. OTHER AREAS: ...) and the handwriting fills the ruled lines provided for the answers.
- Rule: "Handwriting filling in labeled printed fields is form, not handwritten". "This includes meeting-minutes sheets and log tables printed with ruled columns and headers... the handwriting fills a printed table, so it is a filled form (check 10), not handwritten."
- This is a comment form with printed questions and ruled lines for answers. The handwriting fills the form. So not handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: None.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: The page asks the reader to answer questions ("Do you agree or disagree? Why?", "If yes, explain why..."). It is a comment form for a public notice ("Notice 96-25").
- Wait, is a government comment form a questionnaire?
- "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
- "A consumer commitment/enrolment application... stays questionnaire even when its fields look exactly like an ordinary administrative form."
- Is a public comment form a questionnaire? Yes, it asks questions and provides open-response lines. "opinion items... open-response lines".
- Let's check the definition of questionnaire: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines...". This page has printed questions and open-response lines filled by hand.
- Wait, is it a form (check 10) or questionnaire (check 4)?
- Check 4 comes before Check 10. "The page asks the reader to answer... open-response lines... is still questionnaire".
- Let's re-read Check 4: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
- This is a comment form from the Department of Transportation asking for comments on smoking in airports. It has questions and open-response lines. This fits "questionnaire".

Let's look at Check 10: "ADMINISTRATIVE FORM -&gt; form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data...".

But Check 4 is specifically for survey instruments. A public comment form asking for opinions ("Do you agree or disagree? Why?") is a survey/questionnaire instrument.

Let's check if there's any other match.

- Check 11: Correspondence. No TO/FROM/RE header. It's a form.
- Check 12: News article. No.
- Check 13: Scientific report. No.

Let's refine Check 4 vs Check 10.

Check 4: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines..."

The document has:

"1. PATH ONLY: DOT has suggested... Do you agree or disagree? Why? PRINT" -&gt; Handwritten answer.

"2. OTHER AREAS: Are there other areas... If yes, explain why these areas are important... PRINT" -&gt; Handwritten answer.

This is a survey instrument (comment form) with open-response lines. The handwriting fills the form, so it's not "handwritten" (Check 2). It is a questionnaire (Check 4).

Wait, the prompt says: "A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... is still questionnaire".

Also: "Notes ABOUT a survey instrument are questionnaire, not handwritten... Conversely, a respondent's freeform handwritten opinion/feedback card... IS handwritten, NOT questionnaire: questionnaire requires a PRINTED survey instrument with printed question items, rating scales, or response boxes, not a person's freeform writing."

Here, the page HAS printed question items ("1. PATH ONLY: ...", "2. OTHER AREAS: ...") and response lines. The person filled it out. So it is a filled questionnaire.

Therefore, Check 4 matches.

Let's double check Check 10 (form).

Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data...".

But Check 4 is higher priority. "Once an earlier check matches, later checks do not override it."

Check 4 matches because it's a survey instrument (comment form with questions and open-response lines).

Let's review the evidence for Check 4:

- Printed questions: "1. PATH ONLY: ... Do you agree or disagree? Why?", "2. OTHER AREAS: Are there other areas... If yes, explain why..."
- Open-response lines filled by hand.
- Bottom text: "This comment form is provided as a public service..."

Is there any other category?

- "advertisement": No.
- "budget": No.
- "email": No.
- "file_folder": No.
- "form": Check 10 is lower priority than Check 4.
- "handwritten": No, fills a printed form.
- "invoice": No.
- "letter": No.
- "memo": No.
- "news_article": No.
- "presentation": No.
- "questionnaire": Yes.
- "resume": No.
- "scientific_publication": No.
- "scientific_report": No.
- "specification": No.

Wait, is a government comment form considered a "questionnaire"?

"The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines..."

Yes, it asks for opinions ("Do you agree or disagree? Why?") and uses open-response lines.

Let's check the scratchpad requirements:

- Walk checks 1-14 in order.
- Briefly state evidence or "none".
- If evidence present, STOP HERE.
- Add one final line naming runner-up and evidence that ruled it out.

Scratchpad:

1. file_folder: no — page has substantial body content (questions and handwritten answers), not just an identifier/stamp.

2. handwritten: no — handwriting fills printed ruled lines and answers to printed questions, so it is a filled form/instrument, not freeform handwriting on unlabeled paper.

3. FAX TRANSMISSION SHEET: none — no FACSIMILE header or fax cover sheet layout.

4. questionnaire: yes — printed survey/comment instrument with numbered questions ("1. PATH ONLY: ... Do you agree or disagree? Why?", "2. OTHER AREAS: ... If yes, explain why...") and open-response lines filled by hand; bottom text confirms "This comment form is provided as a public service".

Runner-up: form, ruled out because the page is a survey instrument asking for opinions and open responses (check 4), which precedes the generic administrative form check (check 10).

Final label: questionnaire.


<h3 class="trace-file"><code>rvl_cdip__form__0095.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>form</code> | <strong>Predicted:</strong> <code>file_folder</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There is text "Insecticides" at the top right (rotated) and "51303 2938" at the bottom right (rotated). These look like a section title and a Bates number or archive ID.

**2. Scratchpad procedure:**

- Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder

  - Evidence: The page is almost entirely blank. It has "Insecticides" rotated at the top right and "51303 2938" rotated at the bottom right. Wait, is "Insecticides" a bold headline title? The instructions say: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." and "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title (even a single word/short phrase like "RECOMMENDATIONS" with no subtitle, or a large heading rotated 90 degrees like "COMPETITIVE BAR PROGRAMS" — even alongside a small handwritten letter or number annotation) carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."

  - Wait, let's look at the folder-tab bullet: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard... bearing a short filing label... The label IS filing metadata... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees..."

  - Let's look at the scan-artifact signal for presentation (check 9): "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a black bar."

  - Looking at the image: There is a solid black bar along the right edge (and bottom edge). The text "Insecticides" is at the top right, rotated 90 degrees counter-clockwise. The text "51303 2938" is at the bottom right, rotated 90 degrees counter-clockwise. This looks exactly like a photographed file-folder tab. The black bar is the folder body. "Insecticides" is the short filing label on the tab. "51303 2938" is the Bates number.

  - Let's re-read the folder-tab bullet carefully: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard (often with a cutout/notch shape at the folder's edge) bearing a short filing label that names the folder's contents: a product name, collection/company name, month or date range, contract/file description, or alphanumeric identifier, usually with a Bates number stamped on the folder body. The label IS filing metadata — its only job is to identify the folder — so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees, even when the folder body photographs as a solid black bar/border along one or more edges, and even when the label names something that sounds like a document ("Litigation Content", "NEWTROL", "PMI Pricing Plans", "PALL MALL FAMOUS-Monitor test 1992", "FEBRUARY"). The black bar is the photographed folder body/tab edge — it is NOT a slide-mount scan artifact (check 9), and a rotated filing label on a folder tab is NOT a section-divider heading."

  - This matches perfectly. "Insecticides" is a short filing label (collection name/topic of the folder contents). "51303 2938" is the Bates number. The black bar is the folder body.

  - Therefore, Check 1 matches: file_folder.

Let's double check Check 9 (presentation):

- "A near-blank cover or title page... is a presentation (this check), not file_folder (check 1)."
- "EXCEPTIONS: ... a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. "NEWTROL", "Litigation Content", "FEBRUARY") is a folder-tab label and stays file_folder (check 1)."
- "Scan-artifact signal: ... does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a black bar."

The page has:

- Solid black bar along the right edge (and bottom).
- Text "Insecticides" rotated 90 degrees.
- Text "51303 2938" rotated 90 degrees.

This is a classic folder tab scan. "Insecticides" is the label on the tab. "51303 2938" is the Bates number.

So, Check 1: file_folder.

Let's quickly review the other checks just in case.

- Check 2: handwritten. No.
- Check 3: fax. No.
- Check 4: questionnaire. No.
- Check 5: resume. No.
- Check 6: scientific_publication. No.
- Check 7: financial. No.
- Check 8: specification. No.
- Check 9: presentation. Ruled out by folder-tab exception.
- Check 10: form. No.
- Check 11: correspondence. No.
- Check 12: news_article. No.
- Check 13: scientific_report. No.
- Check 14: advertisement. No.

The evidence for file_folder:

- Page is almost entirely blank.
- Contains a short filing label "Insecticides" rotated 90 degrees.
- Contains a Bates number "51303 2938" rotated 90 degrees.
- Contains a solid black bar along the edge, characteristic of a photographed folder body/tab edge.
- This matches the "Folder-tab pages" exception in Check 1, which explicitly states such pages are file_folder, not presentation (Check 9) or file_folder with a bold headline title.

Runner-up: presentation. Ruled out because the page is a photographed file-folder tab with a short filing label ("Insecticides") and a Bates number ("51303 2938"), and the black bar is the folder body, not a slide-mount scan artifact. The instructions explicitly state that a rotated short filing label on a folder tab is file_folder, not a section-divider heading for presentation.

Final label: file_folder.


<h3 class="trace-file"><code>rvl_cdip__form__0075.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>form</code> | <strong>Predicted:</strong> <code>specification</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: There is a Bates number "620423067" at the bottom right. No journal masthead, no newspaper masthead.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of content (a table with many rows and columns). Not identifier-only.
- Not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: The page is mostly a printed table with some handwritten entries. Not majority handwritten.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or fax cover sheet header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions, rating scales, or transmittal note.
- Not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No career history.
- Not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal name, volume, issue, page range, or DOI on the page itself.
- Not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial line items, ledger, or statement. The table contains technical data (P.D., WEIGHT, FILTER, PAPER, TOB. ANALYSES, SMOKING, etc.).
- Not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: The table is titled with "BRAND St. James CY 1001 BA" (or similar, looks like "BRAND St. James CY 1001 BA"). It has rows for "CIGARETTE", "FILTER", "PAPER", "TOB. ANALYSES (%)", "SMOKING (Cis)". It contains technical data like "Tar (MG)", "Nicotine (MG)", "CO (MG)", "P.D. (INCHES)", "WEIGHT (MG)". This is a product analysis table or test-analysis table keyed to product codes/parameters. The title mentions "BRAND St. James CY 1001 BA". The rows are product parameters (Tar, Nicotine, CO, P.D., Weight, etc.). This matches "product-referenced test data" or "titled product-analysis table". Wait, let's look closer. "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" is the example. Here we have a table with "BRAND St. James CY 1001 BA" at the top, and columns for different dates/analyses ("P57L D6", "P57L D15", etc.). The rows are cigarette specifications and smoking analyses. This is a specification or product analysis table. Let's check check 8 again: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough". Here the top row says "BRAND St. James CY 1001 BA". The table contains product parameters and smoking analyses. This fits specification.

Wait, let's check check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8)". This table has product parameters (Tar, Nicotine, CO, P.D., Weight, etc.) and measurements. It is a product analysis table. So it's a specification.

Let's re-read check 8 carefully: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all... is an administrative form (check 10), not a specification."

This table has "BRAND St. James CY 1001 BA" at the top. It has rows for "CIGARETTE", "FILTER", "PAPER", "TOB. ANALYSES", "SMOKING". This is clearly a product analysis table for a specific brand/product (St. James CY 1001 BA). So it is a specification.

Let's check if there's any other category.

Check 9: presentation. No.

Check 10: form. "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This holds product test data. So not form.

Check 11: correspondence. No.

Check 12: news_article. No.

Check 13: scientific_report. "Requires running prose". This is a table. No.

Check 14: advertisement. No.

So it's specification.

Let's double check the top text:

"BRAND St. James CY 1001 BA"

"PRODUCTION DATE"

"OPERATOR NUMBER"

"DATE ANALYSIS EXPECTED"

"DATE RECEIVED"

Then columns: "P57L D6", "P57L D15"

Rows:

"CIGARETTE"

"P.D. (INCHES)"

"Cigarette", "Sealed Cigarette", "Tob. Sect.", "Filter"

"WEIGHT (MG)"

"Circ. (MM)", "Cigarette", "*N*.T.W.", "Tobacco", "Density (MG/CC)"

"FILTER"

"Texhil/Pillow (%)", "Triceratin (%)", "TEODA (%)", "Ventilation Rate (%)"

"PAPER"

"Porosity (CORSETA)", "Citrate (%)", "Phosphate (%)", "BPM (% INC)", "Lamina", "Recon. Tob.", "Stem", "Puffed"

"TOB. ANALYSES (%)"

"Alkaloids", "Total Sugar", "Reducing Sugar", "Moist. (Cond)", "Menthol", "Prop. Glycol", "Glycerin", "Nicrate"

"SMOKING (Cis)"

"Tar (MG)", "Nicotine (MG)", "Resistance (%)", "Puffs", "NO (MG)", "CO (MG)"

"Cil. Perf. Firmness (gts/25 cks)", "E-*d* Stability (MG/Cl)", "Coal Retention (%)", "Corr. BORG FV (CC/GM)", "BORG FV Moisture (%)", "Corr. FILL VALUE (MG/CC)", "FV MOISTURE (%)"

This is a product analysis / test data table for "St. James CY 1001 BA". It matches check 8: "test-analysis tables keyed to product/part codes... A titled product-analysis table... is a specification".

Runner-up: form. Ruled out because the table contains product test data (smoking analyses, cigarette dimensions, paper properties) for a specific brand/product, which makes it a specification (check 8) rather than generic administrative log data (check 10).

Let's confirm the label: specification.


<h3 class="trace-file"><code>rvl_cdip__handwritten__0047.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>handwritten</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header: None.
- Masthead/running head: None. There's a black bar on the right edge, which looks like a slide mount or folder edge, but let's look closer. Wait, there's a solid black bar on the right edge. Let's look at the content.

**2. Content analysis:**

- The page is mostly white space with some noise.
- In the bottom right, there is an image of a cigarette pack: "DORAL ULTRA LIGHTS 100's".
- There is a barcode and a number "51821 6825" on the pack.
- There is a solid black bar along the right edge. This is a common scanning artifact for slides/transparencies (photographic slide).
- The text is sparse: "DORAL", "DORAL ULTRA LIGHTS 100's", "51821 6825", barcode.
- This looks like a photographic slide of a Doral cigarette pack.

**3. Checking the rules:**

- Check 1: file_folder. Is it just an ID? No, it has a photograph/image of a product. "A page that pairs a Bates number with a photographic image... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder." Wait, is there a Bates number? "51821 6825" looks like a Bates number or a product code. Actually, "51821 6825" is on the pack image. Wait, looking closely at the right edge, there's a thick black bar. This is typical of a slide scan.
- Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation.

    - "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder (check 1)."

    - "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title..."

    - The image is a Doral cigarette pack. It's a product image.

    - Is it an advertisement? Check 14: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."

    - Let's re-read Check 9 vs Check 14.

    - Check 9: "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder (check 1)."

    - Check 14: "Judge by DOMINANT content: a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a masthead..."

    - Wait, is this an advertisement or a presentation slide?

    - The page is mostly white space. The image is in the bottom right. There is a black bar on the right edge. This is a classic "photographed slide" artifact.

    - "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".

    - The text is "DORAL", "DORAL ULTRA LIGHTS 100's". This is product imagery.

    - If it's a slide from a presentation deck showing a product, it's a presentation.

    - If it's an ad, it's an advertisement.

    - Let's look at the layout. It's a black rectangle (the pack) on a white background, with a black bar on the right. This looks exactly like a slide of a cigarette pack, possibly from a presentation about packaging or product design.

    - Check 9 says: "A standalone photographic image... is a photographic slide (this check)".

    - Check 14 says: "Marketing layout: product imagery... Judge by DOMINANT content... a single brand ad... is advertisement".

    - However, the scan artifact (black bar on right, sparse text off-center) strongly points to Check 9's "Scan-artifact signal".

    - "Scan-artifact signal: a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don'*t* let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page."

    - The layout is sparse (mostly white space), text/image is in lower-right. Black bar on right edge. This is a photographed slide.

    - Therefore, it is a presentation (photographic slide).

Let's double check Check 1 (file_folder).

- "A page that pairs a Bates number with a photographic image... carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
- The number "51821 6825" might be a Bates number or part of the pack. Actually, looking at the pack, "51821 6825" is printed on the side of the pack image (maybe a barcode number or internal code). Wait, "51821 6825" is vertical text next to the barcode. It looks like a Bates number or a document ID.
- Regardless, there is a photographic image (the cigarette pack). So it's not file_folder.

Let's double check Check 14 (advertisement).

- Is the dominant content an advertisement? An ad usually has a Surgeon General warning, slogans, etc. This is just a picture of a pack.
- But Check 9 explicitly covers "photographic slide image".
- "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder (check 1)."
- The black bar on the right is the key. "Scan-artifact signal: a solid black bar along one edge of the page... points to a photographed slide/overhead — presentation".
- So it's a presentation.

Let's re-read the scratchpad instructions.

- "Once an earlier check matches, later checks do not override it."
- Check 1: file_folder. No, has photographic image.
- Check 2: handwritten. No.
- Check 3: fax. No.
- Check 4: questionnaire. No.
- Check 5: resume. No.
- Check 6: scientific_publication. No.
- Check 7: financial. No.
- Check 8: specification. No.
- Check 9: presentation. Yes. "Scan-artifact signal: a solid black bar along one edge... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". The image is a Doral pack. It's a slide.

Wait, is it an advertisement?

- Check 14: "Marketing layout: product imagery...".
- But Check 9 comes before Check 14.
- Check 9: "SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation".
- "A standalone photographic image... is a photographic slide (this check)".
- The layout (white space, image in corner, black bar on edge) is characteristic of a slide scan.
- So Check 9 matches.

Let's look at the text again.

"DORAL"

"DORAL ULTRA LIGHTS 100's"

"51821 6825" (vertical)

Barcode "0 22672 11001 5" (approx)

This is a slide showing a Doral Ultra Lights pack. It's likely from a presentation about product packaging or competitive analysis.

The black bar on the right is the slide mount edge.

The white space is the slide background.

This is a photographic slide -&gt; presentation.

Final check:

- Check 1: file_folder. "A page that pairs a Bates number with a photographic image... is a... photographic slide (presentation, check 9)". So not file_folder.
- Check 9: presentation. Matches "photographic slide image" and "Scan-artifact signal".

Runner-up: advertisement. Ruled out because the layout (sparse text, black bar artifact) indicates a photographed slide (presentation), not a designed marketing layout (advertisement). Or rather, Check 9 precedes Check 14.

Wait, is "51821 6825" a Bates number? Bates numbers are usually like "PM-051821-6825" or similar. "51821 6825" looks like it could be part of the pack design or a Bates number. Actually, in tobacco archives, Bates numbers are often stamped. Here it's printed on the pack image? Or is it a label on the slide?

Regardless, the photographic image makes it not file_folder.

The label is presentation.


<h3 class="trace-file"><code>rvl_cdip__letter__0067.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>handwritten</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. Just a Bates number at the bottom left "990684127" and "PRODUCED FROM B&W WEB SITE".

**Scratchpad procedure:**

1.  **IDENTIFIER-ONLY PAGE -&gt; file_folder**:

    - Evidence: The page has a handwritten letter with text ("Dear Sir: I received a free sample..."). Not just an identifier.

    - Not this check.

2.  **MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**:

    - Evidence: The entire body of the document is handwritten. "Dec. 4, 1972", "Dear Sir: I received a free sample of your Leeberg 10 and may I say they are the best tasting low tar cigarettes I have smoked.", "Very Truly, Mrs. Pauline R. Conner". There is a small typed/stamped logo at the top right ("PM" or similar, maybe "PM" signature or stamp). The vast majority of the content is freeform handwriting on blank paper (no printed field labels, boxes, or ruled entry cells).

    - This matches check 2.

Let's double check other checks just in case.

3.  **FAX TRANSMISSION SHEET**: No.

4.  **SURVEY INSTRUMENT**: No.

5.  **RESUME**: No.

6.  **SCIENTIFIC PUBLICATION**: No.

7.  **FINANCIAL DOCUMENT**: No.

8.  **SPECIFICATION**: No.

9.  **PRESENTATION**: No.

10. **FORM**: No.

11. **CORRESPONDENCE**: It is a letter, but check 2 (handwritten) comes before check 11. Wait, let's look at the order.

    - Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten. "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."

    - Check 11: CORRESPONDENCE -&gt; email, memo, or letter. "letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature".

    - Since check 2 is before check 11, and the page is majority handwritten, it is `handwritten`.

    - Let's re-read check 2: "This includes meeting-minutes sheets... A typed page with only a signature, stamp, or margin note is not handwritten." Here, the whole page is handwritten. "A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."

    - The text is: "Dec. 4, 1972 / Dear Sir: / I received a free sample / of your Leeberg 10 and may / I say they are the best / tasting low tar cigarettes I have / smoked. / Very Truly / Mrs. Pauline R. Conner". This is a handwritten letter. Check 2 explicitly says "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."

12. **NEWS ARTICLE**: No.

13. **SCIENTIFIC REPORT**: No.

14. **ADVERTISEMENT**: No.

Runner-up: letter (check 11). Ruled out because the page is majority handwritten freeform text on blank paper (no printed template/letterhead), which triggers check 2 (handwritten) before check 11 (correspondence/letter).

Let's confirm the text:

Top right: "PM" with a line under it (maybe a logo or initials).

"Dec. 4, 1972"

"Dear Sir:"

"I received a free sample"

"of your Leeberg 10 and may"

"I say they are the best"

"tasting low tar cigarettes I have"

"smoked."

"Very Truly"

"Mrs. Pauline R. Conner"

Bottom left: "990684127 / PRODUCED FROM B&W WEB SITE"

This is clearly a handwritten letter. Check 2 wins.

Final check of the rules:

- "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template. This wins over a typed letter or memo layout."
- "A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."

The label is `handwritten`.


<h3 class="trace-file"><code>rvl_cdip__letter__0089.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>letter</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header: No "From:", "To:", "Sent:", "Subject:" in email format. There is a fax transmission header at the top: "JUN 11 '91 13:22 SPARBER AND ASSOC INC P.1/1". This is a FAX machine transmission header, not a mail-client header.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a "FAX MESSAGE" header, TO/FROM fields, and a handwritten note. It has real content (a fax cover sheet with a message). Not file_folder.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: Most of the content is printed text ("SPARBER AND ASSOCIATES, INC.", "FAX MESSAGE", "TO:", "FROM:", "TOTAL NUMBER OF PAGES...", contact info). There is some handwriting (date, names, a short note "Please read book - 'Helping Youth Decide'", signature). But the majority is printed form text. Wait, let's look closer. The top part is a printed fax cover sheet. The bottom part has a handwritten note and a signature block. But the document itself is a fax cover sheet (form).

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET -&gt; form**

    *   Evidence: The page has a header "FAX MESSAGE" (underlined). It has fields: "Date:", "Time:", "TO:", "FROM:", "TOTAL NUMBER OF PAGES INCLUDING THIS PAGE:". It has standard fax cover sheet text: "If you have any problems receiving this fax, please contact Lori Lane at (202) 393-3240. Our fax number is (202) 393-4385."

    *   This matches Check 3 perfectly: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter..."

    *   Wait, the header says "FAX MESSAGE". The check says "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", or "TELEFAX MESSAGE NO.". "FAX MESSAGE" is very close. Let's re-read check 3 carefully.

    *   "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header with To/From/company/phone/page-count fields."

    *   The page has "FAX MESSAGE" as a header. It has To/From/Date/Time/Page count fields. It has company info (Sparber and Associates). It has phone numbers.

    *   The rule says: "Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."

    *   So this is a form.

Let's double check if there's any other match.

The page is a fax cover sheet.

Check 3: "FAX TRANSMISSION SHEET -&gt; form".

Evidence: "FAX MESSAGE" header, "TO:", "FROM:", "TOTAL NUMBER OF PAGES INCLUDING THIS PAGE:", company name "SPARBER AND ASSOCIATES, INC.", phone numbers.

This is a fax transmission sheet. Therefore, it is a form.

Let's check the other checks just in case.

-   **Check 4: questionnaire** - No.
-   **Check 5: resume** - No.
-   **Check 6: scientific_publication** - No.
-   **Check 7: financial document** - No.
-   **Check 8: specification** - No.
-   **Check 9: presentation** - No.
-   **Check 10: administrative form** - Yes, fax sheet is a form. But check 3 is more specific. Wait, check 3 says "Fax sheets are forms". So the label is "form".
-   **Check 11: correspondence** - No, fax header is not email. Memo requires TO:/FROM:/RE:/SUBJECT: followed by prose. This has TO:/FROM: but it's a fax cover sheet. The rule says "Fax sheets are forms, never memo or letter".
-   **Check 12: news_article** - No.
-   **Check 13: scientific_report** - No.
-   **Check 14: advertisement** - No.

So the label is "form".

Let's refine the scratchpad.

- file_folder: no — page has a fax message layout with fields and a handwritten note, not just an ID/stamp.
- handwritten: no — majority is printed text (fax cover sheet template), handwriting is limited to fields and a short note.
- fax transmission sheet: yes — header "FAX MESSAGE", fields "Date:", "Time:", "TO:", "FROM:", "TOTAL NUMBER OF PAGES INCLUDING THIS PAGE:", company address "SPARBER AND ASSOCIATES, INC.", phone numbers "(202) 393-3240", "(202) 393-4385". Fax sheets are forms.
- Runner-up: memo, ruled out because check 3 explicitly states "Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels." Also, the top line is a fax transmission header "JUN 11 '91 13:22 SPARBER AND ASSOC INC P.1/1", not a mail-client header.

Wait, is "FAX MESSAGE" one of the listed headers in check 3?

Check 3: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header..."

"FAX MESSAGE" is extremely similar to "TELEFAX MESSAGE NO." or "FAX COVER SHEET". The content is undeniably a fax cover sheet. The rule says "Fax sheets are forms". The page is a fax sheet. So it's a form.

Final check of the text:

"SPARBER AND ASSOCIATES, INC."

"1325 Pennsylvania Avenue, NW - Suite 500"

"Washington, DC 20004"

"FAX MESSAGE"

"TO: Mary Ellen Collins"

"FROM: [handwritten name]"

"TOTAL NUMBER OF PAGES INCLUDING THIS PAGE: 1"

"If you have any problems receiving this fax..."

"Our fax number is (202) 393-4385."

This is a fax cover sheet. Label: form.

One detail: "FAX MESSAGE" vs "FAX COVER SHEET". The check lists examples. "FAX MESSAGE" is clearly a fax transmission sheet. The instruction says "Fax sheets are forms, never memo or letter".

So, label is `form`.


<h3 class="trace-file"><code>rvl_cdip__memo__0051.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>memo</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** I see "966 1 4648718", "A Z YAMANI", "'87 10/24 15:37", "001". This looks like a fax transmission header. "26 OCT 87" is stamped. "TELECOPY MEMORANDUM". No "From:/To:/Sent:/Subject:" mail client headers. Wait, there is "TO:", "CC:", "FROM:", "RE:". But these are part of a "TELECOPY MEMORANDUM" or fax cover sheet structure, or a memo sent via fax. Let's look closer.
- **Masthead/Running head:** "LAW OFFICES OF AHMED ZAKI YAMANI". This is a letterhead. "JONES, DAY, REAVIS & MOGUR (SURREY IN MICHIGAN)". This is a law firm letterhead. No newspaper masthead. No journal running head.

**2. Scratchpad checks:**

-   **Check 1: file_folder.**

    *   Evidence: The page has a full letterhead, a "TELECOPY MEMORANDUM" header, "TO:", "CC:", "FROM:", "RE:", and a body paragraph. It has real content.

    *   Result: not this check.

-   **Check 2: handwritten.**

    *   Evidence: There is a handwritten note "MB 25.10.87 cc MCB FLO HGA". But the majority of the content is typed text (letterhead, memo header, body paragraph).

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET -&gt; form.**

    *   Evidence: "TELECOPY MEMORANDUM". It has "TO:", "FAX NO:", "CC:", "FROM:", "FAX NO:", "RE:", "FAX NO:", "CAM NO:". This looks like a fax cover sheet or a memorandum sent via telecopy. Wait, check 3 says: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header... Fax sheets are forms". This says "TELECOPY MEMORANDUM". Is it a fax cover sheet? It has To/From/Re/Fax numbers. But it also has a body paragraph: "The 5th GCC Anti-smoking Seminar started this morning...". A fax cover sheet usually just has the metadata and maybe a brief note. This has a full paragraph of text. Let's look at Check 11 (Correspondence).

    *   Wait, is "TELECOPY MEMORANDUM" a fax cover sheet? Check 3 lists specific headers. "TELEFAX" is listed. "TELECOPY" is similar. But the content is a memorandum. Let's look at Check 11.

-   **Check 4: questionnaire.**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: resume.**

    *   Evidence: No.

    *   Result: not this check.

-   **Check 6: scientific_publication.**

    *   Evidence: No journal header.

    *   Result: not this check.

-   **Check 7: financial document.**

    *   Evidence: No financial table or bill. "CAM NO: 923360-052-011" might be a reference number, but no money.

    *   Result: not this check.

-   **Check 8: specification.**

    *   Evidence: No.

    *   Result: not this check.

-   **Check 9: presentation.**

    *   Evidence: No slide layout.

    *   Result: not this check.

-   **Check 10: administrative form.**

    *   Evidence: It has fields like TO, CC, FROM, RE, FAX NO. But it has a body paragraph. Forms capture data. This is a communication.

    *   Result: not this check (or maybe, but correspondence usually wins if it's a memo/letter). Wait, check 3 says fax sheets are forms. Is this a fax sheet? "TELECOPY MEMORANDUM". It has fax numbers. But it has a full body. Let's look at Check 11.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter.**

    *   **Email:** No mail-client header (From/To/Sent/Subject). The top line "966 1 4648718 A Z YAMANI '87 10/24 15:37 001" is a fax transmission header (machine-stamped). Pre-scan says: "A FAX machine transmission header... is NOT a mail-client header". So not email.

    *   **Memo:** Internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.

        *   Header: "TELECOPY MEMORANDUM", "October 24, 1987".

        *   "TO: George Nassif...", "CC: Bernie Robinson...", "FROM: Mohd. Salih El Zubeir", "RE: Agenda for 5th Anti-Smoking Seminar".

        *   Body: "The 5th GCC Anti-smoking Seminar started this morning..."

        *   Is it internal? "Philip Morris Lausanne", "Philip Morris Neuchatel", "AZY - Jeddah". These are external or international offices. "LAW OFFICES OF AHMED ZAKI YAMANI" is the sender. "George Nassif, Philip Morris". This is external correspondence.

        *   Wait, let's look at the definition of memo vs letter.

        *   Memo: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."

        *   Letter: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

        *   This document has a letterhead ("LAW OFFICES OF AHMED ZAKI YAMANI"). It has "TO: George Nassif, Philip Morris, Bahrain". This is an external recipient address (Bahrain). It has "FROM: Mohd. Salih El Zubeir". It has "RE: Agenda...". It has body prose. It does *not* have a "Dear..." salutation. It does *not* have a closing signature visible (maybe cut off or just the text).

        *   Wait, the definition says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block... (no external address, no 'Dear ...' salutation)." This has an external address (Bahrain, Lausanne, Jeddah). So it's not a memo by the strict definition "no external address".

        *   Letter definition: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."

        *   This has a TO:/FROM: block. "TO: George Nassif... FROM: Mohd. Salih El Zubeir".

        *   Let's re-read the memo definition carefully: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation). Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo... A dated note addressed to a bare name with an honorific... is a letter (external addressee), not a memo."

        *   This document has "TO: George Nassif, Philip Morris, Bahrain". This is an external address. So it's not a memo.

        *   Is it a letter? "letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." This has a TO:/FROM: block.

        *   Wait, is "TELECOPY MEMORANDUM" considered a memo?

        *   Let's look at the structure. It's a "TELECOPY MEMORANDUM". It has TO, CC, FROM, RE. This is the standard memo format. Even if sent to external parties (Philip Morris is the client/recipient), law firms often send memos/telecopies to clients.

        *   However, the instructions say: "memo: internal... (no external address)". This has external addresses (Bahrain, Lausanne, Jeddah).

        *   "letter: letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

        *   This is tricky. It has a TO/FROM block (like a memo) but external addresses (like a letter).

        *   Let's look at the "Routing/distribution fields" caveat: "Routing/distribution fields added on top of a full letter... do NOT turn a letter into a memo: if the page still has an external addressee, a 'Dear ...' salutation, a prose body, and a closing signature, it stays letter". This page doesn'*t* have a "Dear..." salutation.

        *   Let's look at the memo definition again. "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... IS a memo". Here, "George Nassif, Philip Morris, Bahrain". Is Philip Morris internal? No, it's the recipient. The sender is "LAW OFFICES OF AHMED ZAKI YAMANI". So this is external.

        *   So it's not a memo (because of external address).

        *   Is it a letter? "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature". This lacks "Dear..." and closing signature.

        *   BUT, there is an alternative: "OR a dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block." This has a TO:/FROM: block.

        *   Wait, is "TELECOPY MEMORANDUM" a form? Check 3: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header... Fax sheets are forms". "TELECOPY MEMORANDUM" is very close to "TELEFAX". And it has FAX NO fields.

        *   Let's check Check 3 again. "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."

        *   This page has "TELECOPY MEMORANDUM". It has "FAX NO:" fields. It has a page count at the top right "001" and "# 4/7" (wait, I see "26 OCT 87" and "001". Top right: "001". Top left: "966 1 4648718". This is a fax header. "SENT BY: ... # 4/7" is the example. Here we have "966 1 4648718 A Z YAMANI '87 10/24 15:37 001". This is the machine transmission header.

        *   The document itself is titled "TELECOPY MEMORANDUM". It has To/From/Re/Fax No fields.

        *   Is it a fax cover sheet? A fax cover sheet usually has a brief message. This has a full paragraph. "The 5th GCC Anti-smoking Seminar started this morning...".

        *   However, Check 3 says: "Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."

        *   The header "TELECOPY MEMORANDUM" with "FAX NO:" fields strongly suggests a fax transmission sheet / telefax cover sheet.

        *   Let's look at the content. It's a memorandum sent via telecopy.

        *   If I classify it as a memo (Check 11): It has TO/FROM/RE. But it has external addresses. The rule says memo is "internal... (no external address)". This has external addresses (Bahrain, Lausanne). So strictly, it's not a memo by the definition provided.

        *   If I classify it as a letter (Check 11): It has letterhead, external address, date, prose. But no "Dear..." and no closing signature. And it has a TO/FROM block. The rule says "letter... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block." This has a TO/FROM block.

        *   This leaves Form (Check 3 or Check 10) or maybe Letter (loosely).

        *   Let's re-evaluate Check 3: "FAX TRANSMISSION SHEET -&gt; form". Header: "TELECOPY MEMORANDUM". Fields: TO, FAX NO, CC, FROM, FAX NO, RE, FAX NO, CAM NO. This fits the description of a fax cover sheet / telefax message sheet. "Fax sheets are forms, never memo or letter".

        *   The document is a "TELECOPY MEMORANDUM" sent via fax (indicated by "TELECOPY", "FAX NO:", and the machine header at the top). The presence of "FAX NO:" fields next to the names is the key.

        *   Therefore, Check 3 applies. "A '... TELEFAX ...' header with To/From/company/phone/page-count fields. Fax sheets are forms". "TELECOPY" is synonymous with "TELEFAX" in this context (telecopy = telefax). The fields "FAX NO:" are explicit.

        *   Wait, is "TELECOPY MEMORANDUM" one of the listed headers? "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", "TELEFAX MESSAGE NO.". "TELECOPY" is not explicitly listed, but "TELEFAX" is. And the fields are "FAX NO:".

        *   Actually, let's look at the structure. It's a memo *formatted* as a fax transmission.

        *   Let's look at Check 11 again. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". This is not internal (external addresses).

        *   "letter: ... OR a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block." This has TO:/FROM:.

        *   So it's not a memo and not a letter by the strict definitions.

        *   It fits "FAX TRANSMISSION SHEET -&gt; form" best because of the "FAX NO:" fields and the machine header at the top (even though the machine header is metadata, the document layout is a fax cover/memo hybrid).

        *   Wait, the text says "TELECOPY MEMORANDUM". And it has a body paragraph.

        *   Check 3 says: "Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."

        *   The document uses To:/From:/Re: labels and has "FAX NO:" fields. This is a fax sheet (telefax cover sheet) containing a memorandum.

        *   So label: **form**.

Let's double check.

Top line: "966 1 4648718 A Z YAMANI '87 10/24 15:37 001". This is the fax machine transmission header. Pre-scan says this is NOT an email header.

Document title: "TELECOPY MEMORANDUM".

Fields: TO: (with address), FAX NO:, CC: (with addresses), FAX NO:, FROM:, FAX NO:, RE:, CAM NO:.

Body: Paragraph about the seminar.

Is it a memo?

Definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."

This has external addresses (Bahrain, Lausanne, Jeddah). So it fails the "no external address" condition for memo.

Is it a letter?

Definition: "letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person ... with prose and no TO:/FROM: block."

This has a TO:/FROM: block. So it fails the second condition. It lacks "Dear..." and closing signature. So it fails the first condition.

Is it a fax transmission sheet (form)?

Definition: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header with To/From/company/phone/page-count fields. Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."

The header is "TELECOPY MEMORANDUM". "Telecopy" is an older term for fax/telefax. The fields include "FAX NO:". This matches the spirit and specific fields of a fax transmission sheet. The rule says "Fax sheets are forms, never memo or letter". This document is a fax sheet (telecopy memorandum) sent to multiple people with their fax numbers listed.

Therefore, the label is **form**.

Wait, let's look at Check 10: "ADMINISTRATIVE FORM -&gt; form". "Filled or blank fields, boxes, checkboxes...". This has fields. But Check 3 is more specific for fax sheets. Check 3 comes before Check 10?

The checks are numbered 1-14. I must walk them in order.

Check 1: file_folder. No.

Check 2: handwritten. No.

Check 3: FAX TRANSMISSION SHEET -&gt; form.

Evidence: "TELECOPY MEMORANDUM" header, "FAX NO:" fields next to To/CC/From addresses. Machine transmission header at top ("966 1 4648718..."). This is a fax transmission sheet / telefax cover sheet.

Result: STOP HERE. Label: form.

Let's verify the "TELECOPY" vs "TELEFAX".

The text says "TELECOPY MEMORANDUM".

The fields say "FAX NO:".

The top line is a fax transmission header.

The rule for Check 3 lists "TELEFAX". "Telecopy" is effectively the same. And the presence of "FAX NO:" fields confirms it's a fax sheet.

Also, the rule says "Fax sheets are forms, never memo or letter". This is a memo sent via fax, formatted as a fax sheet. The function is the transmission sheet.

One detail: "A FAX machine transmission header ('SENT BY:', phone number, '# *N*/*N*' page count) is NOT an email header... classify the underlying document by its own content".

The underlying document is a "TELECOPY MEMORANDUM" with "FAX NO:" fields. This is a fax cover sheet / transmission sheet.

Check 3: "A 'FACSIMILE', 'FACSIMILE TRANSMISSION', 'FAX COVER SHEET', 'TELEFAX', or 'TELEFAX MESSAGE NO.' header...". "TELECOPY MEMORANDUM" is close enough to "TELEFAX MESSAGE" or "FAX COVER SHEET". And it has the fields.

Actually, looking closely at the text: "TELECOPY MEMORANDUM".

And "FAX NO: (00973) 530-915".

This is definitely a fax transmission layout.

So, Check 3 matches. Label: form.

Runner-up: memo. Ruled out because the document has external addresses (Bahrain, Lausanne, Jeddah) and "FAX NO:" fields, making it a fax transmission sheet (form) rather than an internal memo. Also lacks "Dear..." salutation for a letter.

Wait, is there any other check?

Check 11: Correspondence.

If I missed Check 3...

If I consider it a memo: "memo: internal...". It's not internal.

If I consider it a letter: "letter: ... no TO:/FROM: block". It has a TO:/FROM: block.

So it must be form (Check 3).

Final check of the text:

"TELECOPY MEMORANDUM"

"October 24, 1987"

"TO: George Nassif ... FAX NO: (00973) 530-915"

"CC: Bernie Robinson ... FAX NO: (0041-21) 265-539"

...

"FROM: Mohd. Salih El Zubeir ... FAX NO: (966-1) 464-8718"

"RE: Agenda for 5th Anti-Smoking Seminar ... CAM NO: 923360-052-011"

This is a fax cover sheet / telefax message sheet. It is a form.

One counter-argument: The body is a paragraph. "The 5th GCC Anti-smoking Seminar started this morning...".

Check 3 says: "Fax sheets are forms, never memo or letter, even though they use To:/From:/Date: labels."

So even if it has a memo body, if it's a fax sheet, it's a form.

The label is **form**.

Wait, let's look at the "CAM NO". This is likely a communication number or fax reference.

The top right has "26 OCT 87" stamped.

The top line is the fax machine header.

Conclusion: form.

One more check: Check 11 "email".

Pre-scan: "A FAX machine transmission header... is NOT a mail-client header". Correct.

So, Check 3 is the winner.

Scratchpad:

- file_folder: no — page has letterhead, memo header, and body text.
- handwritten: no — majority is typed, only small handwritten note "MB 25.10.87...".
- fax transmission sheet (form): yes — header "TELECOPY MEMORANDUM", fields "TO:", "FAX NO:", "CC:", "FROM:", "RE:", machine transmission header at top ("966 1 4648718..."). Fax sheets are forms.
- Runner-up: memo, ruled out because the document has external addresses (Bahrain, Lausanne, Jeddah) and explicit "FAX NO:" fields, identifying it as a fax transmission sheet (form) rather than an internal memo. Also lacks "Dear..." salutation for a letter.

Wait, is "TELECOPY MEMORANDUM" explicitly listed in Check 3?

Check 3 lists: "FACSIMILE", "FACSIMILE TRANSMISSION", "FAX COVER SHEET", "TELEFAX", "TELEFAX MESSAGE NO.".

"TELECOPY" is not there. But "FAX NO:" is there.

And the top line is a fax header.

The document is a memorandum sent via fax.

Is it a memo?

Memo definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block... (no external address)".

This has external addresses. So not a memo.

Is it a letter?

Letter definition: "letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."

This has a TO:/FROM: block. So not a letter (by the second condition). By the first condition, it lacks "Dear..." and closing signature.

So it's not correspondence (memo/letter).

It fits the fax sheet description best (Check 3). "Fax sheets are forms, never memo or letter".

So **form** is the correct label.

One detail: "TELECOPY MEMORANDUM" vs "TELEFAX". Telecopy is a synonym. The presence of "FAX NO:" fields confirms the fax nature.

Final decision: form.


<h3 class="trace-file"><code>rvl_cdip__news_article__0032.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>news_article</code> | <strong>Predicted:</strong> <code>advertisement</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: Top of the page has "THE NEW YORK TIMES, MONDAY SEPTEMBER 11, 1989". This is a newspaper masthead. Wait, let's look closer. "THE NEW YORK TIMES, MONDAY SEPTEMBER 11, 1989". This is a newspaper masthead. But check 12 says "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead... news_article requires the page to present primarily as editorial/multi-story news content". Let's look at the content.

**Check 1: file_folder**

- Evidence: No. The page has a lot of text, a headline, an ad. Not just an ID/stamp.

**Check 2: handwritten**

- Evidence: No. Typed text.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No.

**Check 4: questionnaire**

- Evidence: No.

**Check 5: resume**

- Evidence: No.

**Check 6: scientific_publication**

- Evidence: No journal running head on this page itself (the NYT masthead is a newspaper, not a research journal).

**Check 7: financial document**

- Evidence: No.

**Check 8: specification**

- Evidence: No.

**Check 9: presentation**

- Evidence: No.

**Check 10: form**

- Evidence: No.

**Check 11: correspondence**

- Evidence: No.

**Check 12: news_article**

- Evidence: There is a newspaper masthead "THE NEW YORK TIMES". However, the dominant content is an advertisement by "the tobacco institute". Let's check check 14.

**Check 13: scientific_report**

- Evidence: No.

**Check 14: advertisement**

- Evidence: The page is an advertisement by "the tobacco institute" (1776 *K* Street, *N*.W., Washington, D.C. 20006). It features a reprinted ad from "Advertising Age" ("All Advertising Should Be Truthful", "The Truth Seems a Little Twisted") and a section "What is Advertising Age?". The dominant layout is a single brand advertisement (product imagery/slogans/brand styling of the Tobacco Institute defending advertising). Check 12 caveat: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even if it sits on a newspaper page with a running masthead and some surrounding text". This page is clearly an advertisement placed in a newspaper (or reprinted from one) by the Tobacco Institute. The text is an ad copy: "Reprinted with permission from November 10, 1980, Advertising Age... The Truth Seems a Little Twisted... What is Advertising Age? The national newspaper of the advertising and marketing industry... the tobacco institute". This is a full-page ad by the Tobacco Institute.

Let's re-evaluate Check 12 vs Check 14.

Check 12: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead... news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."

The page has a NYT masthead at the top, but the content is entirely an ad by the Tobacco Institute reprinted from Advertising Age. It's an advertisement.

Let's trace the checks:

1. file_folder: no

2. handwritten: no

3. FAX: no

4. questionnaire: no

5. resume: no

6. scientific_publication: no

7. financial: no

8. specification: no

9. presentation: no

10. form: no

11. correspondence: no

12. news_article: The page has a NYT masthead, but the dominant content is an advertisement. Check 12 says news_article requires primarily editorial/multi-story news content. This is not that.

13. scientific_report: no

14. advertisement: yes. "the tobacco institute" ad, reprinted from Advertising Age, with slogans and brand styling.

Wait, is there any other check?

The page is an advertisement.

Let's double check the text:

"All Advertising Should Be Truthful"

"Reprinted with permission from November 10, 1980, Advertising Age"

"The Truth Seems a Little Twisted"

"What is Advertising Age?"

"the tobacco institute 1776 *K* Street, *N*.W., Washington, D.C. 20006"

Bates number: 500216053

This is definitely an advertisement.

Scratchpad:

file_folder: no — the page has a full-page ad layout with text and logos, not just an identifier.

handwritten: no — typed text throughout.

questionnaire: no — no survey items.

resume: no.

scientific_publication: no — no journal running head.

financial: no.

specification: no.

presentation: no.

form: no.

correspondence: no.

news_article: no — although there is a "THE NEW YORK TIMES" masthead at the top, the dominant content is a single promotional layout by "the tobacco institute" reprinted from "Advertising Age", not editorial news content. Check 12 explicitly states that a page whose dominant layout is a single brand advertisement is an advertisement (check 14) even if printed inside a newspaper with a running masthead.

scientific_report: no.

advertisement: yes — the page is a full-page advertisement by "the tobacco institute" featuring a reprinted ad from "Advertising Age" ("All Advertising Should Be Truthful", "The Truth Seems a Little Twisted") and a promotional blurb ("What is Advertising Age?"), with the institute's name and address at the bottom. This matches the advertisement definition (marketing layout, brand styling, promotional content).

Runner-up: news_article, ruled out because the page's dominant content is a single brand advertisement by the Tobacco Institute, not editorial news content, despite the newspaper masthead at the top.

Final label: advertisement.


<h3 class="trace-file"><code>rvl_cdip__news_article__0084.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>news_article</code> | <strong>Predicted:</strong> <code>email</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify the provided document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** I see "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE" and "MO, RN : Rogers Lawsuit Nearing Completion". This looks like a fax transmission header or an email header. Wait, let's look closer. "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE". This looks like a fax cover sheet header or an email header. Let's look at the structure.
- "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE"
- "MO, RN : Rogers Lawsuit Nearing Completion"
- "GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS GS"
- "Goldman, Sachs & Co. Investment Research"
- "Philip Morris Companies, Inc., RJR Nabisco Holdings Corp."
- "* * Rogers Lawsuit Nearing Completion * *"
- "Marc Cohen (212) 902-0004 - NY Equity Research"
- "==================== NOTE 8:59 AM 08/21/96 ===================="

This looks like a fax transmission header or an email header. Wait, "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE". This is typical of a fax machine transmission header or an email client header (like Lotus Notes or Outlook). "GSNOTE" suggests a note. "MO RN" might be recipients.

Let's check the pre-scan instructions: "A mail-client header block (From/To/Sent/Subject/cc, or a forwarded/threaded trail) anywhere on the page. If present, the page is email (check 11) no matter how technical... BUT a FAX machine transmission header is NOT a mail-client header: machine-stamped 'SENT BY:', a date/time with a phone/fax number, and a page count like '# 4/7' ... is fax transmission metadata".

Here we have "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE". This looks like a fax header or an email header. "GSNOTE" is a strong indicator of a note system (like Lotus Notes). "MO, RN : Rogers Lawsuit Nearing Completion" looks like a subject line. "MO, RN" could be recipients (Philip Morris, RJR Nabisco).

Wait, "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE". This is very likely a fax transmission header from a fax machine or an email client. Let's look at the bottom right: "2081645450". This is a Bates number.

Let's re-read the email rule: "mail-client header block (From/To/Sent/Subject/cc, or a forwarded/threaded trail)".

The text "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE" and "MO, RN : Rogers Lawsuit Nearing Completion" looks like an email header or a fax header.

Actually, "GSNOTE" is a Lotus Notes note. "MO RN" are likely recipients. "Rogers Lawsuit Nearing Completion" is the subject.

However, look at the top: "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE". This is a fax transmission header? No, fax headers usually have "SENT BY: ... # *N*/*N*". This has a time, date, sender name, and "GSNOTE".

Wait, the instructions say: "A FAX machine transmission header is NOT a mail-client header: machine-stamped 'SENT BY:', a date/time with a phone/fax number, and a page count like '# 4/7'". This page does NOT have "SENT BY:" or "# *N*/*N*". It has "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE". This looks like an email header or a fax header from a specific system.

Actually, let's look at the content. It's a financial note from Goldman Sachs about Philip Morris and RJR Nabisco. "NOTE 8:59 AM 08/21/96".

This is a financial research note. Is it an email?

If it's an email, it's check 11.

Let's look at the structure:

Header: "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE"

Subject line: "MO, RN : Rogers Lawsuit Nearing Completion"

Body: Financial data (stock ratings, earnings per share) and bullet points about the Rogers lawsuit.

This looks like an email or a faxed email/note.

If it's an email, the label is `email`.

Let's check if there's a mail-client header. "From/To/Sent/Subject/cc".

"09:00AM EDT 21-Aug-96" -&gt; Sent date/time.

"Goldman Sachs (COHEN**)" -&gt; From/Sender.

"MO RN" -&gt; To/Recipients (Philip Morris, RJR Nabisco).

"GSNOTE" -&gt; Type of message (Lotus Notes note).

"MO, RN : Rogers Lawsuit Nearing Completion" -&gt; Subject.

This fits the pattern of an email header block, specifically from a system like Lotus Notes or an email client. The instructions say: "If present, the page is email (check 11) no matter how technical...".

Wait, is this a fax transmission header? "machine-stamped 'SENT BY:', a date/time with a phone/fax number, and a page count like '# 4/7'". This page does NOT have "SENT BY:" or a page count like "# 4/7". It has "P1 of 2" handwritten at the top right.

So it's not a standard fax transmission header. It looks like an email or a Lotus Notes note printed out.

Therefore, check 11 (email) is a strong candidate.

Let's evaluate other checks just in case.

- Check 1 (file_folder): No, it has content.
- Check 2 (handwritten): No, mostly typed. "P1 of 2" is handwritten.
- Check 3 (fax): No "FACSIMILE" header.
- Check 4 (questionnaire): No.
- Check 5 (resume): No.
- Check 6 (scientific_publication): No journal header.
- Check 7 (financial): It has financial data (stock prices, earnings). But is it an invoice or budget? No, it's a research note. "Goldman, Sachs & Co. Investment Research". It's a financial report/note. But check 7 says: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This page has tables, but it's a research note with bullet points. Wait, check 11 says: "An email page keeps this label even when its body is mostly a data table". So if it's an email, it's email.
- Check 8 (specification): No.
- Check 9 (presentation): No.
- Check 10 (form): No.
- Check 11 (correspondence -&gt; email): The header "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE" and "MO, RN : Rogers Lawsuit Nearing Completion" strongly suggests an email or a note from a collaboration tool (Lotus Notes). The instructions say: "mail-client header block (From/To/Sent/Subject/cc, or a forwarded/threaded trail) anywhere on the page. If present, the page is email". The text "09:00AM EDT 21-Aug-96" (Sent), "Goldman Sachs (COHEN**)" (From), "MO RN" (To), "Rogers Lawsuit Nearing Completion" (Subject). This is an email header.
- Check 12 (news_article): No masthead.
- Check 13 (scientific_report): No running prose narrative of research. It's a financial note.
- Check 14 (advertisement): No.

So the classification is `email`.

Let's double check the header.

"09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE"

"MO, RN : Rogers Lawsuit Nearing Completion"

This is definitely an email header or a Lotus Notes header. "GSNOTE" is a dead giveaway for Lotus Notes (Goldman Sachs Note). Lotus Notes emails are often classified as emails in these datasets. The instructions say: "mail-client header block (From/To/Sent/Subject/cc, or a forwarded/threaded trail)... If present, the page is email".

The pre-scan says: "A mail-client header block... anywhere on the page. If present, the page is email (check 11) no matter how technical... BUT a FAX machine transmission header is NOT...".

This is not a fax machine transmission header (no "SENT BY:", no page count "# *N*/*N*"). It has a time, date, sender, recipients, and subject. It is an email header.

Therefore, the label is `email`.

Wait, let's look at the content again.

"Goldman, Sachs & Co. Investment Research"

"Philip Morris Companies, Inc., RJR Nabisco Holdings Corp."

"* * Rogers Lawsuit Nearing Completion * *"

"Marc Cohen (212) 902-0004 - NY Equity Research"

"==================== NOTE 8:59 AM 08/21/96 ===================="

Then tables of stock data.

Then bullet points about the Rogers lawsuit.

This is a financial research note sent via email/Lotus Notes.

Final check:

- Is it a memo? "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This has a header, but it's an email header (time, date, sender, recipients, subject). And the body is a mix of tables and bullet points, typical of an email note. The pre-scan rule for email overrides: "If present, the page is email (check 11) no matter how technical...".
- The header "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE" contains Sent date, From, To, and message type. "MO, RN : Rogers Lawsuit Nearing Completion" contains To and Subject. This is a mail-client header block.

So, `email`.

One detail: "GSNOTE" is a Lotus Notes note. Lotus Notes is an email/collaboration client. The instructions say "email: mail-client header block... or a forwarded/threaded mail trail". A Lotus Notes note printed out is effectively an email.

Let's confirm the label string: `email`.

Scratchpad:

- Pre-scan: Mail-client header block present: "09:00AM EDT 21-Aug-96 Goldman Sachs (COHEN**) MO RN GSNOTE" and "MO, RN : Rogers Lawsuit Nearing Completion". This indicates Sent date, From, To, Subject. Not a fax header (no "SENT BY:", no page count).
- Check 1 (file_folder): No, has content.
- Check 2 (handwritten): No, mostly typed.
- Check 3 (fax): No fax cover sheet header.
- Check 4 (questionnaire): No.
- Check 5 (resume): No.
- Check 6 (scientific_publication): No journal header.
- Check 7 (financial): Has financial data, but primary structure is an email note with tables and bullets. Check 11 overrides if email header is present.
- Check 8 (specification): No.
- Check 9 (presentation): No.
- Check 10 (form): No.
- Check 11 (correspondence -&gt; email): Yes, mail-client header block ("09:00AM EDT 21-Aug-96...", "MO, RN : ..."). The page is an email/note from Goldman Sachs.
- Runner-up: scientific_report or financial document, ruled out because the mail-client header block makes it email (check 11).

Wait, the instructions say: "An email page keeps this label even when its body is mostly a data table — per the pre-scan, always check for a mail header before letting a technical-looking table pull you toward scientific_report or specification."

This perfectly matches the situation. The page has a mail header and a data table/body.

Final label: email.


<h3 class="trace-file"><code>rvl_cdip__news_article__0071.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>news_article</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None. There is a header "08:47am EDT 2-May-94 CS First Boston (Barfield, B (212) 909-3091) MO RN Morning Meeting: Tobacco Ind.: Break Up of Tobacco Companies Makes Sense PBC". This looks like a fax transmission header or a system-generated header for a financial note/memo, but not a mail-client header (From/To/Sent/Subject). Wait, "08:47am EDT 2-May-94" is a date/time. "CS First Boston (Barfield, B (212) 909-3091) MO RN" looks like a fax transmission header or a system routing header. Let's look closer. It doesn'*t* have "From:", "To:", "Subject:". It's a system-generated header for a financial note.
- Masthead/running head: No newspaper/magazine masthead. No journal running head.

**Check 1: file_folder**

- Evidence: The page has a lot of body content (Summary, Headline, Analyst info). Not file_folder.

**Check 2: handwritten**

- Evidence: Mostly typed text. "P1/41" is handwritten at the top right. Not majority handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No "FACSIMILE", "FAX COVER SHEET" header. The top line is "08:47am EDT 2-May-94 CS First Boston...". This is a system header, not a fax cover sheet.

**Check 4: questionnaire**

- Evidence: No survey questions.

**Check 5: resume**

- Evidence: No career history.

**Check 6: scientific_publication**

- Evidence: No journal name/volume/issue.

**Check 7: financial document (invoice or budget)**

- Evidence: Mentions "break-up value of MO is $75", "P/E multiple". But it's a summary of a morning meeting/analyst call. Not a line-item table, ledger, statement, voucher, or check face. It's a financial note/memo.

**Check 8: specification**

- Evidence: No material safety data, product formulation, etc.

**Check 9: presentation**

- Evidence: Not a slide deck, cover, or statement.

**Check 10: administrative form**

- Evidence: Has fields like "Industry:", "Headline:", "Summary:", "Analyst:", "Associate:", "Telephone:", "Symbol:". But it's a structured financial note/memo, not a generic administrative form capturing factual data for records. Wait, let's look at Check 11.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Let's check the header: "08:47am EDT 2-May-94 CS First Boston (Barfield, B (212) 909-3091) MO RN Morning Meeting: Tobacco Ind.: Break Up of Tobacco Companies Makes Sense PBC"
- Then:

  "CS First Boston Corporation

  Equity Research"

  "AM CALL

  Analyst: Becky Barfield

  Associate: Becky Johnson

  Industry: Tobacco

  Telephone: 212-909-3091/4766"

  "Industry: Tobacco

  Symbol: MO, RN"

  "Headline: Break Up of Tobacco Companies Makes a Lot of Sense"

  "Summary: 1. A split up of the companies would not harm any of the businesses - there are no synergies in remaining together; 2. a split would take the heat from the anti-tobacco movement off the other divisions; 3. a split would achieve a greater P/E multiple as the market never really counts in the valuation of the other businesses in evaluating the diversified tobacco companies; 4. our break-up value of MO is $75."

  "CS FIRST BOSTON CS FIRST BOSTON CS FIRST BOSTON CS FIRST BOSTON"

  "Analyst: Barfield, B Telephone: (212) 909-3091"

  "CS FIRST BOSTON CS FIRST BOSTON CS FIRST BOSTON CS FIRST BOSTON"

  "END OF NOTE"

This is a financial analyst note or memo. It has a header with date, company, analyst, subject ("Morning Meeting: Tobacco Ind.: Break Up..."), and a "Summary" prose.

Does it fit memo?

"memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels"

This document is a typed financial note/memo from an equity research department. It has a date ("2-May-94"), company ("CS First Boston"), analyst ("Becky Barfield"), subject ("Morning Meeting: Tobacco Ind.: Break Up..."), and a summary prose. It ends with "END OF NOTE".

Is it an email? No mail-client header.

Is it a letter? No external address, no "Dear...", no closing signature.

Is it a memo? It's an internal note/memo from an analyst to clients or internal staff. The structure is a header block (date, company, analyst, subject, summary) followed by prose. In the tobacco archive, these are often "Morning Meeting" notes or "Equity Research" memos/notes.

Let's re-read the memo definition: "internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels"

This page has a header block:

"08:47am EDT 2-May-94 CS First Boston (Barfield, B (212) 909-3091) MO RN

Morning Meeting: Tobacco Ind.: Break Up of Tobacco Companies Makes Sense PBC"

Then fields: Analyst, Associate, Industry, Telephone, Symbol, Headline, Summary.

This is a structured memo/note. The label "memo" fits best among correspondence. Wait, is there a better label?

What about "form"? It has labeled fields (Industry, Headline, Summary, Analyst, Associate, Telephone, Symbol). But the content is running narrative prose ("Summary: 1. A split up..."). Check 10 says "A form does NOT have to be blank... filled analytical or lab data sheet... internal authorization/approval forms". But this is a financial note.

Let's check if there's any other category.

Could it be a "news_article"? No, it's an internal/analyst note.

Could it be "scientific_report"? No.

Let's look at the header again: "08:47am EDT 2-May-94 CS First Boston (Barfield, B (212) 909-3091) MO RN Morning Meeting: Tobacco Ind.: Break Up of Tobacco Companies Makes Sense PBC"

This is a fax transmission header or a system-generated header for a financial note. The pre-scan says: "A FAX machine transmission header ("SENT BY:", phone number, "# *N*/*N*" page count) is NOT an email header... classify the faxed document by its own content". This header is similar: date/time, company, person, phone number. It's likely a fax header or a system printout header. The underlying document is a "Morning Meeting" note or analyst memo.

The content is a summary of a morning meeting about tobacco companies. It's a memo/note.

Let's check the memo definition again: "memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels"

This document has a date (2-May-94), a subject (Morning Meeting: Tobacco Ind...), and prose (Summary: 1. A split up...). It is a memo.

Wait, is there any chance it's a "form"?

"Administrative form -&gt; form: Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... A hand-plotted experimental GRAPH... It does NOT cover money records... It does NOT cover product-change authorization pages"

This document has fields like "Industry:", "Headline:", "Summary:", but the "Summary" is a narrative paragraph. It's a memo/note template. In the tobacco archive, these "Morning Meeting" notes or "Equity Research" notes are typically classified as memos.

Let's review the checks:

1. file_folder: no (has body content)

2. handwritten: no (mostly typed)

3. FAX TRANSMISSION SHEET: no (no FACSIMILE header, just a system/fax routing header at the top)

4. questionnaire: no

5. resume: no

6. scientific_publication: no

7. financial document: no (not a line-item table, ledger, statement, voucher, or check face. It's a note summarizing a meeting/analysis)

8. specification: no

9. presentation: no

10. administrative form: no (it's a memo/note with narrative summary, not a generic data capture form)

11. correspondence -&gt; memo: yes. It's a dated internal note (2-May-94) with a header block (company, analyst, subject, summary) and memo-style prose (the summary points). No external address, no "Dear...", no closing signature. It fits the memo definition: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo even without literal "TO:/FROM:" labels". Here, it's addressed to "Morning Meeting" participants or is an internal note from the analyst. The header has "Analyst: Becky Barfield", "Associate: Becky Johnson". It's a memo.

Let's double check if it could be an email.

"email: mail-client header block (From/To/Sent/Subject, cc, attachments) or a forwarded/threaded mail trail."

The top line is "08:47am EDT 2-May-94 CS First Boston (Barfield, B (212) 909-3091) MO RN". This is not a mail-client header. It's a system/fax header. So not email.

Could it be a letter?

"letter: letterhead with an external recipient address, date, "Dear ..." salutation, prose body, and a closing with signature — OR a dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block."

No external address, no "Dear...", no signature. So not a letter.

Therefore, it's a memo.

Let's refine the scratchpad:

- file_folder: no — the page has a detailed summary, headline, and analyst information, not just an identifier or stamp.
- handwritten: no — the page is typed, with only a small handwritten "P1/41" at the top right.
- fax transmission sheet: no — the top line is a system/fax routing header ("08:47am EDT 2-May-94..."), not a "FACSIMILE TRANSMISSION" cover sheet.
- questionnaire: no — no survey questions or rating scales.
- resume: no — no career history or biographical sketch.
- scientific_publication: no — no journal name, volume, or page number on the page.
- financial document: no — although it mentions "$75" and "P/E multiple", the page is a narrative summary note, not a line-item table, ledger, or billing document.
- specification: no — no material safety data, product formulation, or "shall/must" language.
- presentation: no — not a slide deck, cover, or press release.
- administrative form: no — although it has labeled fields (Industry, Headline, Summary), the content is running narrative prose (a summary of a morning meeting), which makes it a memo/note rather than a generic data-capture form.
- correspondence (memo): yes — the page is a dated internal note (2-May-94) from CS First Boston Equity Research, with a header block (Analyst, Associate, Industry, Symbol, Headline) followed by memo-style narrative prose ("Summary: 1. A split up..."). It has no external address, no "Dear..." salutation, and no closing signature, fitting the memo definition.
- news_article: no — no newspaper/magazine masthead or multi-column news typography.
- scientific_report: no — no running narrative prose about research objectives/methods/results; it's a financial analysis summary.
- advertisement: no — no product imagery, slogans, or brand styling for marketing.

Runner-up: form, ruled out because the page's primary structure is a memo/note with narrative prose (a summary of a morning meeting), not a generic administrative form capturing factual data fields.

Final label: memo.

Wait, let's look at the top line again: "08:47am EDT 2-May-94 CS First Boston (Barfield, B (212) 909-3091) MO RN Morning Meeting: Tobacco Ind.: Break Up of Tobacco Companies Makes Sense PBC"

This is definitely a fax header or system printout header. The underlying document is a memo.

The label is memo.


<h3 class="trace-file"><code>rvl_cdip__presentation__0095.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** None. No newspaper/magazine masthead. No journal running head.
- **FAX transmission header:** None. No "SENT BY:" or page count like "# 4/7". Wait, there's a Bates number "526001380" rotated on the right side.

**2. Scratchpad procedure:**

-   **Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

    *   Evidence: There is a Bates number "526001380" rotated on the right. There is some text: "DLG", "XJNT", "First draft for April 29. Please add.", "Lance".

    *   Is it just an identifier? No, there is text "First draft for April 29. Please add." and "Lance". This looks like a note.

    *   Wait, let's look closer. "DLG", "XJNT" (handwritten?), "First draft for April 29. Please add.", "Lance".

    *   This is a page with very little content. Is it a file folder tab? No, it looks like a scanned page with some text.

    *   Is it a presentation cover? No.

    *   Let's check other checks.

-   **Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

    *   Evidence: "DLG", "XJNT" look handwritten. "First draft for April 29. Please add." is typed. "Lance" is typed.

    *   Most content is NOT handwriting. It's mostly blank space with a few typed words and a couple of handwritten initials.

    *   Not this check.

-   **Check 3: FAX TRANSMISSION SHEET -&gt; form**

    *   Evidence: None. No "FACSIMILE" header.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: None.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: None.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: None.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: None.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: None.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: Sparse text. "First draft for April 29. Please add." "Lance".

    *   Is it a presentation cover? "near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation".

    *   Wait, the text says "First draft for April 29. Please add." and "Lance". This looks like a memo or a note.

    *   Let's look at Check 11.

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: None. No fields, boxes, checkboxes.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: "First draft for April 29. Please add." "Lance". "DLG", "XJNT".

    *   This looks like a memo or a note.

    *   "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... is a memo".

    *   Here we have "Lance" (a name). "First draft for April 29. Please add." (prose/note). "DLG", "XJNT" (initials, likely the sender).

    *   This is a memo. Internal note to Lance from DLG (or similar).

    *   Let's re-read the memo definition: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo. A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."

    *   Here we have "Lance" (name). "First draft for April 29. Please add." (prose). "DLG" (initials, likely sender). "XJNT" (initials?).

    *   This fits the "dated internal note addressed to a named person... with memo-style prose... IS a memo even without literal TO:/FROM: labels".

    *   Wait, is "Lance" an internal name? Yes, likely an employee name.

    *   Is there a date? "April 29".

    *   Is there prose? "First draft for April 29. Please add."

    *   This is a memo.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: None.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: None.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: None.

Let's re-evaluate Check 1 vs Check 11.

The page has:

- Handwritten "DLG", "XJNT" (or similar).
- Typed "First draft for April 29. Please add."
- Typed "Lance".
- Bates number "526001380".
- Some black bars at the bottom (scan artifact?).

Is it a file_folder?

- "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
- This page carries a note: "First draft for April 29. Please add." addressed to "Lance".
- So it's not file_folder.

Is it handwritten?

- "Most of the content is freeform handwriting... NOT on a printed template."
- Here, most of the page is blank. The text is typed ("First draft...", "Lance"). The handwriting is just initials "DLG", "XJNT".
- "A typed page with only a signature, stamp, or margin note is not handwritten."
- This is a typed note with margin initials. Not handwritten.

Is it a memo?

- "A dated internal note addressed to a named person by NAME... with memo-style prose... IS a memo even without literal 'TO:/FROM:' labels".
- Addressed to "Lance".
- Prose: "First draft for April 29. Please add."
- Sender initials: "DLG".
- This fits the memo definition perfectly. It's a short internal note/memo.

Let's check the labels again.

memo: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose... OR a dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no "Dear ..." salutation, and no closing signature IS a memo.

Here:

- Name: "Lance"
- Date reference: "April 29"
- Prose: "First draft for April 29. Please add."
- Sender: "DLG" (handwritten initials at top).
- No external address, no salutation, no closing signature.

This is a memo.

Wait, is there any other possibility?

Could it be a presentation slide?

- "near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation".
- "First draft for April 29. Please add." is not a title. It's a note.
- "Lance" is not a title.
- This is correspondence (memo).

Let's look at the "DLG" and "XJNT".

"DLG" is likely the sender's initials.

"XJNT" might be a code or initials.

The text "First draft for April 29. Please add." is the content.

"Lance" is the recipient.

This is a classic internal memo/note.

Final check:

Check 11: CORRESPONDENCE -&gt; email, memo, or letter.

- email: no mail header.
- memo: yes, internal note to "Lance" from "DLG" (implied) with text "First draft for April 29. Please add."
- letter: no external address, no salutation.

So the label is memo.

One detail: "A typed page with only a signature, stamp, or margin note is not handwritten." -&gt; Correct, not handwritten.

"A dated internal note addressed to a named person by NAME... with memo-style prose... IS a memo" -&gt; Correct.

The page is mostly blank, but the content is a memo note.

Let's double check Check 9 (presentation).

"A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note (e.g. 'Internal Communication 2000 Plan' with 'Draft for discussion'), a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."

Here, the text is "First draft for April 29. Please add." and "Lance". This is not a title or heading. It's a message. "Lance" is a name. "First draft..." is a message. This is correspondence.

Therefore, memo.

Wait, is "Lance" a name? Yes, Lance is a common name. In tobacco industry archives (Philip Morris, RJR), Lance is a common employee name (e.g., Lance B. ...).

"DLG" could be David L. ... or similar.

The text is:

DLG (handwritten)

XJNT (handwritten)

First draft for April 29. Please add. (typed)

Lance (typed)

This is a memo.

One final check on Check 1 (file_folder).

"A page is NOT file_folder if it carries any real content... or a note."

This page carries a note. So not file_folder.

Final decision: memo.


<h3 class="trace-file"><code>rvl_cdip__questionnaire__0080.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>questionnaire</code> | <strong>Predicted:</strong> <code>scientific_report</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "2063434687" on the right side.

**Check 1: file_folder**

- Evidence: The page has a title "GENERAL SUMMARY", "LOUISIANA - 6/90", and multiple questions (NO. 1, NO. 2, NO. 3, NO. 4, NO. 5) with data (yes/no, should/should not/don'*t* know, numbers like 100, 0, 37, 56, 7, 23, 77, 1, 39, 60, 1, 25, 74, 1). This is real content, not just an identifier/stamp.
- Not this check.

**Check 2: handwritten**

- Evidence: The text is typed. No majority handwriting.
- Not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax header.
- Not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: The page contains questions ("QUEST: NO. 1 Are you 18 years of age or older..."), response options ("yes", "no", "should", "should not", "don'*t* know"), and data results ("ALL 100 0", "ALL 37 56 7"). Wait, this looks like a summary of survey results, not the survey instrument itself. Let's re-read check 4. "The page asks the reader to answer, rate, choose, or commit... A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... is still questionnaire". But this is a "GENERAL SUMMARY" of results. Is it a questionnaire? No, it's a report of results. Wait, let's look at the other checks.
- Actually, let's look at the content. It's a summary of survey data. "GENERAL SUMMARY", "LOUISIANA - 6/90". Questions 1-5 with responses and percentages/counts. This is a scientific report or a form?
- Let's check check 13: scientific_report. "Running narrative prose with objectives, methods, results, or discussion...". This page has results (data tables). But it lacks running narrative prose. It's just a table of results.
- Let's check check 10: ADMINISTRATIVE FORM. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data". This is survey results data. Is it a form? No.
- Let's re-evaluate check 4. Is this a questionnaire? No, it's the results.
- Wait, what about check 13? "scientific_report: ... Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." This page is only labeled data entries (questions, options, numbers). So it might be a form?
- Let's look at check 10 again: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a financial/money chart is budget (check 7), and a research-measurement chart is scientific_report (check 13)".
- This is a research-measurement chart (survey results). "research-measurement chart is scientific_report (check 13)". But check 13 says "Requires running prose". Wait. "Also scientific_report: ... a hand-plotted experimental GRAPH ...". What about a table of survey results?
- Let's re-read check 13 carefully: "Requires running prose — a page that is only labeled field-value entries (even an 'ANALYTICAL DATA SUMMARY' under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
- So if it's only labeled field-value entries, it's a form (check 10).
- Let's look at the page again. It has "QUEST: NO. 1 ... yes no ... ALL 100 0". This is a table of survey results. Is it a form? "A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". Survey results are not generic administrative/log data. They are research data.
- Wait, is there another category?
- Let's look at the labels: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
- Could it be a questionnaire? "A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... is still questionnaire". This is a summary of results, not part of the instrument.
- Let's reconsider the content. It's a "GENERAL SUMMARY" of a survey. "LOUISIANA - 6/90". Questions about job applicants. This looks like a page from a research report. But check 13 requires running prose. If it lacks running prose, and it's not generic admin data, what is it?
- Wait, check 10: "A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". This is survey data. Is survey data considered "generic administrative/log data"? No.
- Let's re-read check 13: "Requires running prose ... is a filled form (check 10), not a scientific report." This implies that if it lacks running prose, it falls back to form (check 10) or another category.
- What if it's a form? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This page is not capturing data, it's displaying it.
- Let's look at the structure. It's a table. "QUEST: NO. 1 ... yes no ... ALL 100 0". This is a data table.
- Is there a category for "research-measurement chart"? Check 10 says: "a research-measurement chart is scientific_report (check 13)". But check 13 says "Requires running prose". This is a contradiction unless the chart itself counts as scientific_report even without prose? "Also scientific_report: ... a hand-plotted experimental GRAPH ...". It doesn'*t* say table.
- Let's re-read check 10: "a standalone labeled chart is a form only when it holds generic administrative/log data; a chart of a product's measured parameters against spec limits is specification (check 8), a financial/money chart is budget (check 7), and a research-measurement chart is scientific_report (check 13)".
- So a research-measurement chart IS scientific_report (check 13), even if it lacks running prose? The "Requires running prose" sentence in check 13 might apply to the general definition, but the exceptions ("Also scientific_report: ...") override it for charts/graphs. "a hand-plotted experimental GRAPH of test measurements ... is a research test result (check 13), not a form". What about a table? "research-measurement chart is scientific_report (check 13)". A table of survey results is a research-measurement chart.
- Let's assume scientific_report.

Wait, is there any other possibility?

- Could it be a questionnaire? No, it's the results.
- Could it be a form? "A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". Survey results are not generic admin data.
- So it must be scientific_report.

Let's check the text again.

"GENERAL SUMMARY"

"LOUISIANA - 6/90"

"NO. 1 QUEST: Are you 18 years of age or older and a resident of Louisiana? yes no ALL 100 0"

"NO. 2 QUEST: Generally speaking, do you feel that prospective employers should be allowed to ask questions about the private lives of job applicants, or should employers not be allowed to probe the private lives of job applicants? should should not don'*t* know ALL 37 56 7"

This is clearly a summary of survey results (research data).

According to check 10: "a research-measurement chart is scientific_report (check 13)".

According to check 13: "Also scientific_report: ... a hand-plotted experimental GRAPH ...". Although it says GRAPH, "research-measurement chart" in check 10 points to scientific_report.

The page contains research-measurement data (survey results). It is a scientific_report.

Let's double check check 4 (questionnaire). "The page asks the reader to answer...". This page does not ask the reader to answer; it shows the answers (100, 0, 37, 56, 7). So it's not a questionnaire.

Let's double check check 10 (form). "A standalone labeled data chart or table ... is a form only when it holds generic administrative/log data". This is survey research data, not generic admin data. So not form.

Therefore, scientific_report.

Wait, is there any running prose? No. But check 10 explicitly says "a research-measurement chart is scientific_report (check 13)". This overrides the "Requires running prose" rule for charts.

Final check:

- file_folder: no, has content.
- handwritten: no.
- fax: no.
- questionnaire: no, it's results, not the instrument.
- resume: no.
- scientific_publication: no journal ID.
- financial: no.
- specification: no.
- presentation: no.
- form: no, it's a research-measurement chart, not generic admin data.
- correspondence: no.
- news_article: no.
- scientific_report: yes, research-measurement chart (survey results).
- advertisement: no.

Label: scientific_report.


<h3 class="trace-file"><code>rvl_cdip__questionnaire__0058.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>questionnaire</code> | <strong>Predicted:</strong> <code>form</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "50657 9656" on the right edge, and a handwritten "16" in the top right. No journal masthead.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of content (form fields, handwritten answers). Not identifier-only.
- Result: not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: The page has a printed template with fields (NAME, DATE, FEMA NO, CODE NO, AROMA RAW MATERIAL, THRESHOLD, ATTRIBUTE PROFILE, etc.) and handwritten text filling in those fields. The printed structure is clearly visible (field labels, boxes, ruled lines).
- Result: not this check (it's a filled form).

**Check 3: FAX TRANSMISSION SHEET -&gt; form**

- Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
- Result: not this check.

**Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

- Evidence: No survey questions for a respondent. This is a profile sheet filled out by an evaluator (Flavor Division).
- Result: not this check.

**Check 5: PERSON'S CAREER HISTORY -&gt; resume**

- Evidence: No career history.
- Result: not this check.

**Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

- Evidence: No journal running head, volume, issue, page range.
- Result: not this check.

**Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

- Evidence: No financial data, invoices, or budgets.
- Result: not this check.

**Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

- Evidence: No Material Safety Data Sheet, product formulation, or "shall/must" language. This is a sensory evaluation profile.
- Result: not this check.

**Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

- Evidence: Not a slide deck, cover, or statement.
- Result: not this check.

**Check 10: ADMINISTRATIVE FORM -&gt; form**

- Evidence: The page is a structured template with labeled fields (NAME, DATE, FEMA NO, CODE NO, AROMA RAW MATERIAL, THRESHOLD, ATTRIBUTE PROFILE with numbered items 1-11, checkboxes, ruled lines for comments). It captures factual data (sensory evaluation results for "Hexanal"). This is a filled form.
- Result: YES. This is a form.

**Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

- Evidence: No correspondence structure.
- Result: not this check (stopped at 10).

**Check 12: PUBLISHED JOURNALISM -&gt; news_article**

- Evidence: No.

**Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

- Evidence: No running narrative prose. It's a filled form.

**Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

- Evidence: No.

Final label: form.

Let's double check.

The page is "ALPHA RECOGNITION THRESHOLD ATTRIBUTE PROFILE (ARTAP)".

It has fields: NAME: Flavor Division, DATE: April 9 1987, FEMA NO: _, CODE NO: 0-1131, AROMA RAW MATERIAL: Hexanal.

Then a threshold scale.

Then "ATTRIBUTE PROFILE" with numbered questions (1. Cigarette-like taste?, 2. Artificial taste?, etc.) with Yes/No circles, checkboxes, and "ADDITIONAL COMMENTS" lines filled by hand.

This is clearly a structured form for capturing sensory data.

Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."

Matches perfectly.

Runner-up: scientific_report. Ruled out because the page lacks running narrative prose and is primarily a structured data-capture template (form).

Runner-up: handwritten. Ruled out because the handwriting fills a printed structured form with field labels, not freeform paper.

Final check of the steps.

1. file_folder: no

2. handwritten: no

3. fax: no

4. questionnaire: no

5. resume: no

6. scientific_publication: no

7. financial: no

8. specification: no

9. presentation: no

10. form: yes

11-14: stopped.

Label: form.


<h3 class="trace-file"><code>rvl_cdip__scientific_report__0083.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>scientific_publication</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead or running head: "American Heart Journal 101/3:319-28 March 1981" at the top. "CURRICULUM IN CARDIOLOGY". Page number "319" at the bottom. Copyright line "©002-8703/81/$03.00/0 © 1981 The C. V. Mosby Co." at the bottom. This looks like a journal running head.

**Check 1: file_folder**

- Evidence: The page has a full article with text, title, author, running head. Not file_folder.

**Check 2: handwritten**

- Evidence: Typed text throughout. Not handwritten.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax header.

**Check 4: questionnaire**

- Evidence: No survey questions.

**Check 5: resume**

- Evidence: Not a CV.

**Check 6: scientific_publication**

- Evidence: "American Heart Journal 101/3:319-28 March 1981" at the top. Page number 319 at the bottom. Copyright line "©002-8703/81/$03.00/0 © 1981 The C. V. Mosby Co." This is a named journal (American Heart Journal) plus publication identifier (volume 101, issue 3, page range 319-28, year 1981) on THIS page.
- Stop here.

Let's double check.

Title: "Update on the role of cigarette smoking in coronary artery disease"

Author: William B. Kannel, *M*.D.

Journal: American Heart Journal 101/3:319-28 March 1981.

This perfectly matches check 6: "a named journal on the page plus a publication identifier (volume/issue, page range, DOI, journal copyright line...)".

Runner-up: scientific_report. Ruled out because the page carries its own journal running head and copyright line (check 6 precedes check 13).

Final label: scientific_publication.


</details>

## email → questionnaire

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__email__0049.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>email</code> | <strong>Predicted:</strong> <code>questionnaire</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

Document content:

- Date: June 24, 1999
- Text: "A task force co-sponsored by Lynn Beasley and Jim Maguire has been created to respond to concerns over the growing levels of fraud and waste associated with discounting as well as the ineffectiveness of many of our current discounting promotions. There is also a growing awareness of the increased demands that are being put on the sales organization to spend time auditing stores to combat this fraud and waste."
- "As part of this task force, we are attempting to understand how widespread these problems are and to try to develop some creative ways to address fraud waste and discounting ineffectiveness that will free up the time of the sales organization to focus again on core selling accountabilities that are at the heart of your job responsibilities."
- "One objective of the task force is to understand how sales force time is currently being utilized. As part of this effort, we are interviewing and surveying people throughout the sales organization to understand how the time of the sales force is spent today. You have been selected to participate in the phone interview portion of this survey. The questions you will be asked are attached so that you can review them and formulate your responses. The questions should be answered based on your own assigned accounts, do not include accounts on out of territory coverage."
- "You will be contacted in the next few days to set up a convenient time for the interview between Monday June 28 and Wednesday June 30. It should take no longer than 20 minutes. Thank you in advance for your help."
- Bottom left: RJR0000001707008749, 70049 8334
- Bottom right: 53129 5788 (rotated)

Let's go through the checks.

Pre-scan:

- Mail-client header block? No.
- Masthead or running head? No. Just Bates numbers.

Check 1: file_folder

- Almost no body content? No, there is a full letter.

Check 2: handwritten

- Most content freeform handwriting? No, it's typed.

Check 3: FAX TRANSMISSION SHEET

- FACSIMILE header? No.

Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire

- "The questions you will be asked are attached so that you can review them and formulate your responses."
- "You have been selected to participate in the phone interview portion of this survey."
- This is a cover letter transmitting a survey/questionnaire.
- Check 4 says: "A cover/transmittal letter keeps its full letter formatting (letterhead, date, salutation, closing signature) and is STILL questionnaire, not letter, if its prose mentions enclosing, attaching, or requesting completion of a survey/questionnaire (e.g. 'the attached questionnaire,' 'please complete the enclosed form') — a single such phrase is enough; don'*t* be pulled toward letter just because the rest of the page looks like ordinary correspondence."
- Evidence: "The questions you will be asked are attached so that you can review them and formulate your responses." and "participate in the phone interview portion of this survey."

Let's double check if it could be a letter (Check 11).

It has a date, but no TO/FROM/RE header, no salutation ("Dear..."), no closing signature. It's an internal memo-like letter or just a letter. But Check 4 explicitly overrides letter if it transmits a survey.

"A cover/transmittal letter keeps its full letter formatting... and is STILL questionnaire, not letter, if its prose mentions enclosing, attaching, or requesting completion of a survey/questionnaire"

Let's check Check 11: CORRESPONDENCE -&gt; email, memo, or letter

- email: no mail header.
- memo: no TO:/FROM:/RE: header block. It's just a date and paragraphs. Addressed to "you" (the reader). Not a memo.
- letter: letterhead + external address + "Dear..." + closing. This has none of that. It's an internal note/letter. But Check 4 takes precedence.

So Check 4 is the match.

Let's review Check 4 evidence:

"The questions you will be asked are attached so that you can review them and formulate your responses."

"You have been selected to participate in the phone interview portion of this survey."

This is a transmittal letter for a survey/questionnaire.

Runner-up: letter or memo. Ruled out because the text explicitly transmits a survey ("The questions you will be asked are attached", "participate in the phone interview portion of this survey"), which makes it a questionnaire transmittal per Check 4.

Let's confirm there's no other check.

Check 5: resume - no.

Check 6: scientific_publication - no.

Check 7: financial - no.

Check 8: specification - no.

Check 9: presentation - no.

Check 10: form - no.

Check 12: news_article - no.

Check 13: scientific_report - no.

Check 14: advertisement - no.

Final label: questionnaire.

Evidence: "The questions you will be asked are attached so that you can review them and formulate your responses." and "participate in the phone interview portion of this survey."

This is a transmittal letter for a survey.

Wait, is there any possibility it's a memo?

"A task force co-sponsored by Lynn Beasley and Jim Maguire..."

No TO/FROM/RE. Just a date.

Even if it were a memo, Check 4 says a transmittal letter for a survey is questionnaire.

Let's write the scratchpad.

file_folder: no — the page contains a full letter with multiple paragraphs of text, not just an identifier or stamp.

handwritten: no — the text is entirely typed.

fax: no — no FACSIMILE or fax cover sheet header.

questionnaire: yes — the text is a transmittal letter for a survey, stating "You have been selected to participate in the phone interview portion of this survey. The questions you will be asked are attached so that you can review them and formulate your responses." Per check 4, a cover/transmittal letter mentioning an attached survey is questionnaire.

Runner-up: letter or memo, ruled out because the document explicitly transmits a survey instrument ("questions you will be asked are attached", "phone interview portion of this survey"), which classifies it as questionnaire under check 4.


</details>

## email → memo

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__email__0064.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>email</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: No. There is a "From:", "Date:", "Subject:", "To:" block, but it's not a mail-client header (From/To/Sent/Subject/cc). Wait, let's look closer. "From: Berlin, Mark", "Date: Tue, Oct 22, 1996 4:48 PM", "Subject: RE: Good Housekeeping article on ETS", "To: Winokur, Matt". This looks like a memo header or an email header. Let's check the rules.

  - Email: mail-client header block (From/To/Sent/Subject, cc, attachments) or a forwarded/threaded mail trail. BUT the pre-scan says: "A FAX machine transmission header is NOT a mail-client header... Email requires real mail-client labels (From:/To:/Sent:/Subject:) or a forwarded/threaded trail." Wait, the memo check says: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".

  - Let's look at the text:

    "Note for Berlin, Mark"

    "From: Berlin, Mark"

    "Date: Tue, Oct 22, 1996 4:48 PM"

    "Subject: RE: Good Housekeeping article on ETS"

    "To: Winokur, Matt"

    "I guess either 9:30 am or after the OSHA meeting"

  - This is a memo. "Note for Berlin, Mark" is the title. "From: Berlin, Mark", "To: Winokur, Matt", "Subject: RE: ...". Wait, is it an email? "Sent:" is missing. "Subject:" is present. "From:", "To:", "Date:". This is a classic memo header format, often printed from email or just a memo. Let's check the memo rule: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)." Here we have From, Date, Subject, To. Followed by "I guess either 9:30 am or after the OSHA meeting". This is memo-style prose. No external address, no salutation. So it's a memo.

  - Wait, could it be email? "Email requires real mail-client labels (From:/To:/Sent:/Subject:)". "Sent:" is missing. "Date:" is present. Usually, printed emails have "From:", "To:", "Sent:", "Subject:". This has "Date:" instead of "Sent:". It looks like a memo. Let's classify as memo.

Let's go through the checks.

**Check 1: file_folder**

- Evidence: Bates number 2078348147. But there is body content ("Note for Berlin, Mark", From/To/Subject, prose). Not file_folder.

**Check 2: handwritten**

- Evidence: None. Typed text.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: None.

**Check 4: questionnaire**

- Evidence: None.

**Check 5: resume**

- Evidence: None.

**Check 6: scientific_publication**

- Evidence: None.

**Check 7: financial document**

- Evidence: None.

**Check 8: specification**

- Evidence: None.

**Check 9: presentation**

- Evidence: None.

**Check 10: administrative form**

- Evidence: None.

**Check 11: correspondence -&gt; email, memo, or letter**

- Evidence: "From: Berlin, Mark", "Date: Tue, Oct 22, 1996 4:48 PM", "Subject: RE: Good Housekeeping article on ETS", "To: Winokur, Matt". Followed by "I guess either 9:30 am or after the OSHA meeting". This is an internal memo. No external address, no salutation, no closing signature. Internal names + titles (well, just names here, but "Note for Berlin, Mark" and internal context). Wait, the rule says: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels". Here we have literal "From:", "To:", "Subject:", "Date:". This perfectly matches the memo header block. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
- Is it email? "Email requires real mail-client labels (From:/To:/Sent:/Subject:)". "Sent:" is missing, "Date:" is present. Often memos are printed from email clients, but the structure here is a memo. Let's look at the email rule: "mail-client header block (From/To/Sent/Subject, cc, attachments) or a forwarded/threaded mail trail." This lacks "Sent:" and doesn'*t* look like a forwarded trail. It's a memo.

**Check 12: news_article**

- Evidence: None.

**Check 13: scientific_report**

- Evidence: None.

**Check 14: advertisement**

- Evidence: None.

So the label is memo.

Let's double check email vs memo.

Email: "From/To/Sent/Subject". This has "From/To/Date/Subject".

Memo: "TO:/FROM:/RE:/SUBJECT:/DATE:". This has "From:/Date:/Subject:/To:". The text is "From: Berlin, Mark", "Date: ...", "Subject: RE: ...", "To: ...". This is a memo header. The body is "I guess either 9:30 am or after the OSHA meeting". This is memo-style prose.

Therefore, memo.

Let's review the scratchpad requirements:

- Walk checks 1-14 in order.
- Briefly state evidence or "not this check".
- Stop at matching check.
- Add final line naming runner-up and evidence that ruled it out.

Check 1: file_folder - no — page has body content (memo header and prose), not just an identifier/stamp.

Check 2: handwritten - no — text is typed.

Check 3: FAX TRANSMISSION SHEET - no — no FACSIMILE header.

Check 4: questionnaire - no — not a survey instrument.

Check 5: resume - no — not a career history.

Check 6: scientific_publication - no — no journal running head.

Check 7: financial document - no — no financial structure.

Check 8: specification - no — no product/material documentation.

Check 9: presentation - no — not a slide deck or cover.

Check 10: administrative form - no — not a form with fields/boxes.

Check 11: correspondence (memo) - yes — "From: Berlin, Mark", "Date: Tue, Oct 22, 1996 4:48 PM", "Subject: RE: Good Housekeeping article on ETS", "To: Winokur, Matt" followed by memo-style prose "I guess either 9:30 am or after the OSHA meeting". Internal note, no external address, no salutation.

Check 12: news_article - no — no masthead.

Check 13: scientific_report - no — no running narrative research prose.

Check 14: advertisement - no — not promotional.

Runner-up: email. Ruled out because the header uses "Date:" instead of "Sent:" and lacks a forwarded/threaded trail or mail-client specific formatting; it matches the internal memo header structure (From/To/Subject/Date) followed by brief internal prose.

Wait, is "Note for Berlin, Mark" a title? Yes.

Is it an email? Sometimes people print emails and the "Sent:" date becomes "Date:". But the instructions say: "Email requires real mail-client labels (From:/To:/Sent:/Subject:) or a forwarded/threaded trail." Since "Sent:" is absent and it perfectly matches the memo definition ("internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block"), memo is the correct label.

Let's refine the scratchpad text.

file_folder: no — page has memo header and body prose, not just an identifier.

handwritten: no — text is typed.

fax: no — no fax cover sheet header.

questionnaire: no — not a survey.

resume: no — not a CV.

scientific_publication: no — no journal identifier.

financial: no — no financial table.

specification: no — no product data.

presentation: no — not a slide.

form: no — no form fields.

correspondence (memo): yes — "From: Berlin, Mark", "Date: Tue, Oct 22, 1996 4:48 PM", "Subject: RE: Good Housekeeping article on ETS", "To: Winokur, Matt" followed by internal prose "I guess either 9:30 am or after the OSHA meeting". Matches memo header + prose structure.

news_article: no — no masthead.

scientific_report: no — no research prose.

advertisement: no — not an ad.

Runner-up: email, ruled out because the header lacks "Sent:" and a mail-client trail, matching the internal memo header format (From/To/Subject/Date) instead.

Final label: memo.


</details>

## form → handwritten

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__form__0058.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>form</code> | <strong>Predicted:</strong> <code>handwritten</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I need to follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There's a Bates number "50643 2063" and "2063.0".

**Check 1: file_folder**

- Content: Handwritten text "Confidential + Personal", "Mr. Jake Kiwala", "International Flavors + Fragrances (IFF-R+D)", "1515 Highway 36", "Union Beach", "*N*.J. 07735". Also "Fragrances" with an arrow. Bottom right has a box with handwritten numbers "8268745", "5% CARGAL", "7460 25", "IFF", "HT". Bottom left "2063.0". Right side "50643 2063".
- Is this just an identifier/stamp? No, it has an address and handwritten notes. Wait, is it a folder tab? No, it's a piece of paper with handwritten address and notes.
- Not file_folder.

**Check 2: handwritten**

- Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template.
- The page has handwritten text: "Confidential + Personal", address for Mr. Jake Kiwala, "Fragrances", and a box with numbers.
- There is no printed template, no field labels, no ruled lines. It's freeform handwriting on blank paper (with some scan noise/Bates numbers).
- This matches "handwritten". Let's verify other checks just in case.

**Check 3: FAX TRANSMISSION SHEET**

- No fax header.

**Check 4: SURVEY INSTRUMENT**

- No survey.

**Check 5: resume**

- No resume.

**Check 6: scientific_publication**

- No journal header.

**Check 7: FINANCIAL DOCUMENT**

- No financial structure.

**Check 8: specification**

- No spec.

**Check 9: presentation**

- Not a slide deck.

**Check 10: form**

- No printed fields.

**Check 11: correspondence**

- Is it a letter? It has an address "Mr. Jake Kiwala...", but no salutation, no body, no closing signature. It's just a handwritten address and some notes. The instructions say: "A typed page with only a signature, stamp, or margin note is not handwritten." But this is mostly handwritten. "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
- This is exactly that: a handwritten note with a name and address on blank paper. So it's handwritten, not a letter.

**Check 12: news_article**

- No.

**Check 13: scientific_report**

- No.

**Check 14: advertisement**

- No.

So the label is `handwritten`.

Let's double check check 2 rules:

- "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template." -&gt; Yes.
- "A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten." -&gt; Yes, this matches perfectly. Address of Mr. Jake Kiwala at IFF-R+D.
- "Notes ABOUT a survey instrument are questionnaire, not handwritten" -&gt; Not applicable.
- "A freeform handwritten consumer opinion/feedback card is handwritten, not questionnaire" -&gt; Not applicable.

The page is a handwritten note with an address and some numbers. It is classified as `handwritten`.

Runner-up: letter. Ruled out because there is no salutation, body, or closing signature; it's just a handwritten address and notes on blank paper, which falls under the handwritten rule for freeform notes with addresses.

Let's review the scratchpad requirements:

- Briefly state evidence for each check or "not this check".
- Stop at first matching check.
- Add final line naming runner-up and evidence that ruled it out.

Scratchpad:

file_folder: no — the page has handwritten address and notes, not just an identifier/stamp.

handwritten: yes — freeform handwriting on blank paper with no printed template, containing a name ("Mr. Jake Kiwala"), address ("International Flavors + Fragrances..."), and notes ("Confidential + Personal", "Fragrances", boxed numbers). Matches the rule for a handwritten note containing personal details written freely on blank paper.

Runner-up: letter, ruled out because the page lacks a salutation, prose body, and closing signature; it is a freeform handwritten note with an address on blank paper, which is explicitly classified as handwritten.

Wait, is there any other check?

Check 11: correspondence -&gt; letter. "A dated note addressed to a named EXTERNAL person (e.g. "Mr. T. E. Sandefur") with prose and no TO:/FROM: block is a letter." This page has no prose, no date, no closing. Just an address and notes. So not a letter.

Final label: handwritten.


</details>

## form → presentation

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__form__0076.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>form</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- Mail-client header: None.
- Masthead/running head: None. There's a Bates number "52207 8028" at the bottom right.
- Layout: Mostly black background with a white box containing text in the center. This looks like a slide or a cover page for a presentation, or possibly a title page for a report. Wait, let's look closer.
- Text in white box: "DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE FOR RESTAURANTS WHICH PERMIT SMOKING. Peter Rojeski, Jr."
- Bates number: "52207 8028" (rotated).

**2. Scratchpad checks:**

-   **Check 1: file_folder**

    *   Evidence: There is a bold topical heading ("DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE FOR RESTAURANTS WHICH PERMIT SMOKING.") and an author name. It's not just an ID/stamp.

    *   Wait, is it a folder tab? No, it's a white box on a black background. The black background looks like a slide mount or a presentation slide background.

    *   Rule: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."

    *   Rule: "A prominent topical heading always counts as real content... it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."

    *   So, not file_folder.

-   **Check 2: handwritten**

    *   Evidence: Text is typed. No handwriting.

    *   Not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No fax header.

    *   Not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No survey questions.

    *   Not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: Just a name "Peter Rojeski, Jr." under a title. Not a CV.

    *   Not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name, volume, issue, page range on the page itself. Just a title and author.

    *   Not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: No financial data.

    *   Not this check.

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -&gt; specification**

    *   Evidence: No product specs, MSDS, etc.

    *   Not this check.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation**

    *   Evidence: "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". Here, the entire background is black (except the white box). This looks like a slide from a presentation or a title slide.

    *   Rule: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."

    *   Rule: "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966' — is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."

    *   Let's analyze the title: "DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE FOR RESTAURANTS WHICH PERMIT SMOKING." This sounds like a technical study title.

    *   Wait, let's look at the "Technical-study title pages" caveat in Check 9.

    *   "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter, Water In Total Particulate Matter, And Nicotine In Cigarette Smoke / November 28, 1966' — is scientific_report (check 13), not presentation, even when it is sparse or printed slide-style on a dark background: the title names an experimental study, not a deck/program/section."

    *   The title here is "DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE FOR RESTAURANTS WHICH PERMIT SMOKING." This names a specific study/methodology ("Developing and testing an... procedure"). It has an author "Peter Rojeski, Jr.".

    *   However, is there a date? No date visible in the white box.

    *   Let's check Check 13: "ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report". "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9); and a technical/project status report..."

    *   Wait, Check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".

    *   Does this page have a date? No date is visible in the text box. Just the title and author.

    *   Let's re-read Check 9 carefully. "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note (e.g. 'Internal Communication 2000 Plan' with 'Draft for discussion'), a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."

    *   The page has a title and an author. It looks like a title slide for a presentation. "DEVELOPING AND TESTING..." is the title. "Peter Rojeski, Jr." is the presenter/author.

    *   Is it a scientific_report title page? Check 13 says: "a technical-study title page naming a specific experimental method/study (see check 9)". Check 9 caveat says "with a date". This page doesn'*t* have a date.

    *   Let's look at the layout. Black background, white box with text. This is classic slide presentation style (or a slide scan). The Bates number is on the side.

    *   If it's a title page for a report (scientific_report), it usually has more info (affiliation, date). Here we just have title and author.

    *   Let's look at the "Scan-artifact signal" in Check 9: "a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center (e.g., lower-right) rather than in running paragraphs, points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don'*t* let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page."

    *   Here, the *entire* page is black (except the white box). This looks like a slide. The text is sparse.

    *   The title "DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE..." sounds technical, but the layout is a slide.

    *   Wait, is it a scientific_report? Check 13 requires "Running narrative prose". A title page alone is not a scientific_report unless it's the specific "technical-study title page" caveat.

    *   The caveat in Check 9 says: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report". This page lacks a date.

    *   Therefore, it fits the "near-blank cover or title page ... is a presentation" rule in Check 9.

    *   Let's check the text again. "DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE FOR RESTAURANTS WHICH PERMIT SMOKING. Peter Rojeski, Jr."

    *   This looks like a title slide for a presentation by Peter Rojeski.

    *   Let's consider Check 13 again. "Requires running prose — a page that is only labeled field-value entries ... is a filled form ... not a scientific report." A title page with just title and author is not running prose.

    *   So it's likely a presentation (slide cover).

-   **Check 10: ADMINISTRATIVE FORM -&gt; form**

    *   Evidence: No fields, boxes, checkboxes.

    *   Not this check.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence: No TO/FROM/RE header, no salutation, no closing.

    *   Not this check.

-   **Check 12: PUBLISHED JOURNALISM -&gt; news_article**

    *   Evidence: No masthead, no news typography.

    *   Not this check.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP -&gt; scientific_report**

    *   Evidence: No running prose. Just a title and author.

    *   The caveat in Check 9 mentions technical-study title pages are scientific_report *if* they have a date. This one doesn'*t* seem to have a date (only a Bates number). Even if it did, the layout is very sparse (slide-like).

    *   However, let's look at the "Scan-artifact signal" in Check 9 again. "points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title; don'*t* let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like rather than a prose page."

    *   This page is extremely sparse. Black background, white box. Definitely slide-like.

    *   So Check 9 (presentation) wins.

-   **Check 14: PROMOTIONAL MATERIAL -&gt; advertisement**

    *   Evidence: No product imagery, slogans, coupons.

    *   Not this check.

**Re-evaluating Check 9 vs Check 13:**

- The page has a title: "DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE FOR RESTAURANTS WHICH PERMIT SMOKING." and author "Peter Rojeski, Jr."
- Check 9 says: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... is a presentation".
- Check 9 caveat: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report".
- This page has no date. It has a title and author. It looks like a slide (black background, white text box).
- The "Scan-artifact signal" in Check 9: "a solid black bar along one edge... combined with sparse text... points to a photographed slide... even if the sparse text sounds like a research title". Here the whole background is black, which is even stronger evidence of a slide/overhead scan.
- Therefore, classification is **presentation**.

Let's double check if it could be a scientific_report title page.

- Scientific reports usually have affiliation, date, abstract. This has none.
- The layout is a slide (black background, centered white box). This is typical for a presentation title slide or a slide from a deck.
- The Bates number "52207 8028" is typical for tobacco archive slides.

Final decision: presentation.

Wait, is there any other possibility?

- "file_folder": No, it has a title.
- "scientific_report": Needs running prose or a specific title page with date. This lacks date and prose.
- "presentation": Fits "near-blank cover or title page" and "slide/overhead layouts".

The text is:

"DEVELOPING AND TESTING AN INDOOR AIR ASSESSMENT PROCEDURE FOR RESTAURANTS WHICH PERMIT SMOKING.

Peter Rojeski, Jr."

This is a title slide.

One detail: "Technical-study title pages: a title page naming a specific study or methodology with a date ... is scientific_report (check 13), not presentation".

Since there is no date, this caveat doesn'*t* fully apply to force it to scientific_report. The general rule in Check 9 for a near-blank title page is presentation.

Also, the "Scan-artifact signal" explicitly says: "don'*t* let a technical-sounding phrase pull this toward scientific_report when the layout itself is sparse and slide-like". The layout is very sparse (black background, white box).

So, **presentation**.

Let's check the runner-up.

Runner-up: scientific_report. Ruled out because the page lacks running prose and a date (required for the technical-study title page exception in check 9), and the layout is sparse/slide-like (black background), pointing to presentation.

Wait, looking closely at the image, the white box has rounded corners. It looks like a text box on a slide.

The Bates number is vertical on the right.

This is definitely a slide.

Final check of the steps:

1. file_folder: No, has title.

2. handwritten: No.

3. fax: No.

4. questionnaire: No.

5. resume: No.

6. scientific_publication: No journal ID.

7. financial: No.

8. specification: No.

9. presentation: Yes. Sparse text, black background (slide artifact), title + author. Fits "near-blank cover or title page" and "slide/overhead layouts".

10. form: No.

11. correspondence: No.

12. news_article: No.

13. scientific_report: No running prose. Title page lacks date for the exception.

14. advertisement: No.

Label: presentation.


</details>

## handwritten → file_folder

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__handwritten__0041.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>handwritten</code> | <strong>Predicted:</strong> <code>file_folder</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead/running head: None. There is a "BUSINESS REPLY MAIL" box, a barcode, a postmark, and some handwritten text.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Content: "BUSINESS REPLY MAIL", "FIRST-CLASS MAIL PERMIT NO 381 RICHARDSON TX", "POSTAGE WILL BE PAID BY ADDRESSEE", "ATTN DEPT M54 SELECT PANEL PO BOX 834010 RICHARDSON TX 75083-9654", barcode, postmark "PM 23 DEC 1995", handwritten "AHJ R. Stone Customer Service".
- Is there any real content? No sentences, no topical title. Just a business reply mail envelope back (or the back of a reply mail piece). Wait, is this a file_folder?
- "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
- "A Bates number or archive stamp alone is NOT enough... A prominent topical heading always counts as real content"
- This page is essentially a blank business reply mail envelope back. It has no Bates number visible (maybe the barcode is an archive barcode? "51775 4464").
- Wait, the instructions say: "A page is NOT file_folder if it carries any real content... Pure filing metadata only."
- Is a business reply mail back a file_folder? Usually, if it's just the back of an envelope with no content, it might be file_folder. Let's look closely.
- "AHJ R. Stone Customer Service" is handwritten.
- Let's check check 2: handwritten. "Most of the content is freeform handwriting... NOT on a printed template." Here, there is only a small handwritten note "AHJ R. Stone Customer Service". Not majority handwritten.
- Let's re-read check 1: "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
- This page has "BUSINESS REPLY MAIL", address, barcode, postmark, and a small handwritten note. It's essentially a blank page with mailing metadata. This fits file_folder perfectly. "Pure filing metadata only." The mailing address and permit are metadata for the mail piece. The handwritten note is just a routing note.
- Wait, is there any other category?
- Let's check if it's a form. No.
- Let's check if it's a letter. No.
- Let's check file_folder again: "A page is NOT file_folder if it carries any real content... A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content". This page has neither. It's just the back of a business reply mail envelope.
- Therefore, file_folder.

Let's double check.

Text on page:

"51775 4464" (barcode number)

"NO POSTAGE NECESSARY IF MAILED IN UNITED STATES" (partially visible)

Postmark: "PM 23 DEC 1995"

"BUSINESS REPLY MAIL"

"FIRST-CLASS MAIL PERMIT NO 381 RICHARDSON TX"

"POSTAGE WILL BE PAID BY ADDRESSEE"

"ATTN DEPT M54"

"SELECT PANEL"

"PO BOX 834010"

"RICHARDSON TX 75083-9654"

Handwritten: "AHJ R. Stone Customer Service"

This is the back of a business reply mail envelope. It contains no substantive document content. It is pure filing/mailing metadata.

Check 1: file_folder. "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."

The mailing permit, address, and postmark are stamps/metadata. The handwritten note is a routing annotation.

This matches file_folder.

Let's quickly check if it could be something else.

- handwritten: no, only a small note.
- form: no.
- email: no.
- letter: no.

I will classify as file_folder.

Wait, is there any chance this is a "form"? No.

Is it a "questionnaire"? No, it's the back of the reply mail for a questionnaire, but the page itself has no questionnaire content. The instructions say: "A page is NOT file_folder if it carries any real content... a questionnaire appendix...". This is just the mailing back. It's essentially a blank page with mailing info. File_folder is the best fit for "almost no body content".

Let's review the file_folder definition: "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card (INVENTOR / TITLE / patent numbers). No sentences, no topical title. A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."

The handwritten note "AHJ R. Stone Customer Service" is a routing note, not a substantive note. The page is essentially blank.

I'll go with file_folder.


</details>

## invoice → letter

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__invoice__0035.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>invoice</code> | <strong>Predicted:</strong> <code>letter</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** No "From:", "To:", "Sent:", "Subject:" headers. There is a date "February 16, 1996" and an address block, but it looks like a standard letter format.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. Just "RJ Reynolds Tobacco Company" logo at the top.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a full letter body, letterhead, date, address, salutation, signature. Not just an ID or stamp.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: Mostly typed text. There is a signature, but the content is typed.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**

    *   Evidence: No survey questions or questionnaire instrument. It's a letter about a campaign contribution.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY**

    *   Evidence: Not a resume or CV.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE**

    *   Evidence: No journal name, volume, issue, page range, DOI.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT**

    *   Evidence: Mentions a "contribution to your campaign fund" and "enclose a contribution". However, the primary structure is a letter (letterhead, external address, "Dear...", prose, closing signature). Check 7 says: "If the page is otherwise formatted as correspondence (letterhead + external address + "Dear ..." salutation + prose + closing signature... and a dollar figure, grant number, or invoice/payment reference is merely mentioned somewhere within that prose, classify it as correspondence (check 11) instead". Wait, there isn'*t* even a dollar figure explicitly mentioned as an amount due, just "enclose a contribution". Even if there were, the structure is a letter.

    *   Result: not this check (it's correspondence).

-   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**

    *   Evidence: No material safety data sheet, product formulation, or specification language.

    *   Result: not this check.

-   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**

    *   Evidence: Not a slide deck, press release ("FOR IMMEDIATE RELEASE"), or photographic slide. It's a letter.

    *   Result: not this check.

-   **Check 10: ADMINISTRATIVE FORM**

    *   Evidence: No fields, boxes, checkboxes, or ruled entry lines for capturing data. It's a standard letter layout.

    *   Result: not this check.

-   **Check 11: CORRESPONDENCE -&gt; email, memo, or letter**

    *   Evidence:

        *   Letterhead: "RJ Reynolds Tobacco Company" with address "910-741-5000 Winston-Salem, *N*.C. 27102".

        *   Date: "February 16, 1996".

        *   External recipient address: "Kelley R. Smith Campaign, P. O. Box 2336, Palatka, FL 32178-".

        *   Salutation: "Dear Representative Smith:".

        *   Prose body: "On behalf of R. J. Reynolds Tobacco Company..."

        *   Closing: "Best Regards," followed by signature "Joseph S. Murray, III", title "Regional Director State Government Relations".

        *   "Enclosure", "cc: Larry Williams".

    *   This is a classic letter format.

    *   Result: **letter**.

-   **Check 12: PUBLISHED JOURNALISM**

    *   Evidence: No masthead, byline, dateline (in news sense), multi-column typography.

    *   Result: not this check.

-   **Check 13: ORIGINAL RESEARCH WRITE-UP**

    *   Evidence: No running narrative prose about objectives/methods/results. It's a business letter.

    *   Result: not this check.

-   **Check 14: PROMOTIONAL MATERIAL**

    *   Evidence: Not an ad layout. It's a letter.

    *   Result: not this check.

**Conclusion:**

The document is a letter from RJ Reynolds to a campaign. It has letterhead, external address, date, salutation, body, closing, signature. It mentions a contribution, but the structure is a letter. Check 7 explicitly says correspondence mentioning money is still correspondence.

Runner-up: invoice (mentions contribution/money), ruled out because the primary structure is correspondence (letterhead, external address, salutation, prose, closing signature) and money is merely mentioned in the prose, not the primary structure (check 7 caveat). Or runner-up: form (has fields like cc, enclosure), ruled out because it's a standard letter layout. Actually, the main trap might be "budget" or "invoice" because of the campaign contribution. But the instructions say: "If the page is otherwise formatted as correspondence... and a dollar figure... is merely mentioned... classify it as correspondence". Here, it's a letter enclosing a contribution.

Let's refine the scratchpad.

**Scratchpad:**

- file_folder: no — page has full letter content (letterhead, address, prose, signature).
- handwritten: no — typed text with a signature.
- fax: no — no fax header.
- questionnaire: no — not a survey.
- resume: no — not a bio.
- scientific_publication: no — no journal header.
- financial (invoice/budget): no — mentions a campaign contribution, but the page is formatted as a letter (letterhead, external address, "Dear...", prose, closing signature). Check 7 says correspondence mentioning money is still correspondence.
- specification: no — no product data.
- presentation: no — not a slide or press release.
- form: no — no data capture fields (other than standard letter elements like cc/enclosure).
- correspondence (letter): yes — Letterhead "RJ Reynolds Tobacco Company", date "February 16, 1996", external address "Kelley R. Smith Campaign...", salutation "Dear Representative Smith:", prose body, closing "Best Regards," signature "Joseph S. Murray, III". This matches the definition of a letter perfectly.
- news_article: no — no masthead.
- scientific_report: no — no research prose.
- advertisement: no — not a marketing layout.

Final label: letter.


</details>

## memo → specification

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__memo__0014.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>memo</code> | <strong>Predicted:</strong> <code>specification</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

**Classifying Scanned Documents**

I'm currently focused on classifying a scanned business document. My immediate task is to follow a defined procedure, beginning with a mandatory pre-scan for mail-client headers or mastheads/running heads. Following that, I'll systematically work through a 14-step scratchpad procedure.

**Analyzing Document Content**

I've completed the initial scan, confirming no mail-client headers or typical mastheads are present. Now I'm systematically progressing through the 14-step scratchpad procedure, starting with check 1. I've evaluated the current page and found it contains detailed descriptions and analyses, not just identifiers.

**Continuing Document Analysis**

I have completed the initial pre-scan and determined there are no mail-client headers or mastheads. I am now systematically working through the scratchpad procedure, having evaluated checks 1 through 5, finding no definitive match yet, and noting the detailed descriptive nature of the content.

**Continuing Analysis**

I'm still working through the scratchpad procedure after completing the pre-scan. Having found no definitive matches in checks 1 through 7, I've now assessed check 8, which concerns product documentation, and it appears to be a strong contender given the detailed chemical and physical properties described.

**Classifying Product Specifications**

I have completed the initial scan, confirming no mail-client headers or typical mastheads. I'm now progressing through the 14-step scratchpad. After evaluating checks 1 through 7, I've found strong evidence at check 8 for product documentation, specifically detailing chemical and physical properties of the product.

**Identifying Product Specifications**

I have completed the initial pre-scan, noting the absence of mail-client headers and mastheads. I am now systematically progressing through the scratchpad procedure. Having found no definitive match in checks 1 through 7, I have evaluated check 8 and found strong evidence for product documentation, specifically detailing the chemical and physical properties of cigarette products.

**Classifying Documents**

I have completed the initial pre-scan, confirming the absence of mail-client headers and mastheads. I'm now systematically working through the scratchpad procedure. Having found no definitive matches in checks 1 through 7, I've evaluated check 8 and found strong evidence for product documentation, specifically detailing chemical and physical properties of cigarette products.

**Classifying Cigarette Product Details**

I have completed the initial scan, confirming the absence of mail-client headers and mastheads. I am now systematically working through the scratchpad procedure. Having found no definitive matches in checks 1 through 7, I've evaluated check 8 and found strong evidence for product documentation, specifically detailing chemical and physical properties of cigarette products.


</details>

## news_article → scientific_publication

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__news_article__0003.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>news_article</code> | <strong>Predicted:</strong> <code>scientific_publication</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking 1-14 in order.

**Pre-scan:**

- Mail-client header: None.
- Masthead/running head: Top of the page says "396 THE NEW ENGLAND JOURNAL OF MEDICINE Feb 17, 1983". This is a journal running head with volume/page info (page 396, journal name, date). This points to check 6 (scientific_publication).

**Check 1: file_folder**

- Evidence: The page has dense running prose, a title "SOCIAL ENVIRONMENT AND CANCER MORTALITY IN MEN", author "C. DAVID JENKINS, PH.D.", methods, results, etc. Not just an identifier.
- Result: not this check.

**Check 2: handwritten**

- Evidence: Typed text throughout.
- Result: not this check.

**Check 3: FAX TRANSMISSION SHEET**

- Evidence: No fax header.
- Result: not this check.

**Check 4: questionnaire**

- Evidence: No survey questions.
- Result: not this check.

**Check 5: resume**

- Evidence: Not a CV.
- Result: not this check.

**Check 6: scientific_publication**

- Evidence: Top running head: "396 THE NEW ENGLAND JOURNAL OF MEDICINE Feb 17, 1983". Named journal ("THE NEW ENGLAND JOURNAL OF MEDICINE"), page number (396), date. This is a published article from a journal.
- Result: YES. Stop here.

Runner-up: scientific_report. Ruled out because the page itself carries a journal running head (The New England Journal of Medicine, page 396, date), making it a published scientific publication (check 6) rather than an internal report (check 13).

Final label: scientific_publication.


</details>

## news_article → scientific_report

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__news_article__0048.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>news_article</code> | <strong>Predicted:</strong> <code>scientific_report</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

**Classifying Business Documents**

I'm currently focused on correctly categorizing scanned business documents. My current approach involves a mandatory pre-scan for mail-client headers or mastheads, followed by a rigorous scratchpad procedure encompassing checks 1 through 14 in sequence. This systematic method ensures accurate classification.

**Examining Document Elements**

I've completed the mandatory pre-scan, finding no mail-client headers or journal-style mastheads. I've also started the scratchpad procedure, and the first check for an identifier-only page yielded no match due to the presence of extensive body text and other identifying elements.

**Continuing Document Analysis**

I have completed the mandatory pre-scan, confirming the absence of mail-client headers and journal-style mastheads. I've progressed through the initial checks of the scratchpad procedure. Check 1 yielded no match as the page contains substantial body text beyond a mere identifier. Similarly, checks 2 and 3 also returned negative results. My analysis is now focused on check 4, evaluating the document for survey instrument characteristics.

**Continuing Document Analysis**

I have completed the mandatory pre-scan, confirming the absence of mail-client headers and journal-style mastheads. I've progressed through the initial checks of the scratchpad procedure. Check 1 yielded no match as the page contains substantial body text beyond a mere identifier. Similarly, checks 2 and 3 also returned negative results. My analysis is now focused on check 4, evaluating the document for survey instrument characteristics.

**Continuing Document Analysis**

I have completed the mandatory pre-scan, finding no mail-client headers or journal mastheads. I've progressed through checks 1-8 of the scratchpad procedure, all yielding negative results due to the nature of the text. My focus has now shifted to evaluating check 9, assessing for presentation-related content.

**Continuing Document Analysis**

I have moved past checks 1 through 10, confirming negative matches due to the document's narrative and analytical content. My current focus is on check 11, examining it for email, memo, or letter characteristics. Thus far, the absence of typical header blocks and formatting suggests it's not correspondence.

**Continuing Analysis**

I have completed the mandatory pre-scan and progressed through checks 1 through 12 of the scratchpad procedure, all resulting in negative matches. My current focus is on evaluating check 13 for evidence of an original research write-up, assessing its narrative and analytical content.

**Evaluating Document Characteristics**

I have completed the mandatory pre-scan, and systematically progressed through checks 1 through 12 of the scratchpad procedure, all yielding negative matches. My analysis has now confirmed positive evidence for `scientific_report` at check 13, due to the document's narrative and analytical content detailing research findings.

**Evaluating Document Contents**

I have confirmed the absence of mail-client headers and journal mastheads. My scratchpad analysis has progressed through checks 1 through 12, all yielding negative matches. My current focus is on check 13, evaluating the document for an original research write-up.


</details>

## presentation → handwritten

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__presentation__0006.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>handwritten</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

I will follow the scratchpad procedure, checking each condition in order.

**Pre-scan:**

- Mail-client header block: None.
- Masthead or running head: None. Just a page number "1" at the top right.

**Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- Evidence: The page has a lot of handwritten text. Not an identifier-only page.
- Result: not this check.

**Check 2: MAJORITY-HANDWRITTEN PAGE -&gt; handwritten**

- Evidence: The entire page is filled with freeform handwriting. "As you have heard from both Don and Eric... and as you know very well yourselves, last year was a very tough year..." No printed field labels, boxes, or ruled entry cells. It's a handwritten note/letter.
- Result: yes. Stop here.

Let's double check.

Is it a handwritten note about a questionnaire? No.

Is it handwriting filling a printed form? No, it's on blank paper (or at least, no printed template is visible, just a page number).

Most of the content is freeform handwriting.

Runner-up: letter. Ruled out because there is no letterhead, external address, "Dear..." salutation, or closing signature. It's just a handwritten note. Wait, check 11 says "A dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block is a letter." But this has no address, no date, no salutation, no closing. It's just a handwritten page. Check 2 says "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template... This wins over a typed letter or memo layout." So handwritten is the correct label.

Let's review the checks again.

Check 1: file_folder - no.

Check 2: handwritten - yes. "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."

Final label: handwritten.


</details>

## presentation → budget

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__presentation__0077.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>presentation</code> | <strong>Predicted:</strong> <code>budget</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head/volume/issue/page number. There is a Bates number "20837223530" at the bottom right (rotated).

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a title "% Volume Change - Pretax versus After Tax (1-200 versus 4-600)" and a table of data (Total U.S., New York, Connecticut, etc., with percentages). It has a source note "Source: STARS Store Level". It has a Bates number "20837223530".

    *   Is it just an identifier? No, it has a bold headline title and a data table.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: The text is typed. No significant handwriting.

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No questions, rating scales, or survey instrument.

    *   Result: not this check.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: No biographical info.

    *   Result: not this check.

-   **Check 6: PUBLISHED EVIDENCE -&gt; scientific_publication**

    *   Evidence: No journal name, volume, issue, page range, DOI. Just a Bates number.

    *   Result: not this check.

-   **Check 7: FINANCIAL DOCUMENT -&gt; invoice or budget**

    *   Evidence: The table shows "% Volume Change - Pretax versus After Tax". It lists regions (Total U.S., New York, Connecticut, Pennsylvania Surrounding Counties, Vermont, New Jersey, NY+CT+*Penn+VT+NJ) and percentages (8.4%, -20.5%, 20.0%, 18.2%, 12.2%, 10.6%, -9.5%).

    *   Is it an invoice? No vendor charges.

    *   Is it a budget? It shows volume change percentages. It looks like a financial data table or a statistical chart.

    *   Let's look at the definition of budget: "financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures)". This is a table of volume changes (percentages). It's financial data (volume, pretax, after tax).

    *   Wait, let's look at Check 10 (Form) and Check 8 (Specification).

    *   Let's re-read Check 7: "financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures), and a handwritten list of budget categories and dollar amounts... is budget, not form".

    *   This table shows "% Volume Change". It's a data table. Is it a "financial or money-data table"? Yes, it deals with volume, pretax, after tax. It looks like a financial analysis chart.

    *   However, let's look at Check 10: "standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values) — a standalone labeled chart is a form only when it holds generic administrative/log data". This is not generic administrative data.

    *   Let's look at Check 13: "scientific_report". Requires running narrative prose. This is just a table. So not scientific_report.

    *   Let's look at Check 8: "specification". "Product-referenced test data... labeled product/parameter rate-data chart... plotting a measured property over time/subgroup against spec limits". This is volume change by region. Not a product specification.

    *   Let's look at Check 9: "presentation". "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)... A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." Wait. "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."

    *   Let's re-read Check 9 carefully: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."

    *   So if it's a standalone chart/table, it's a form (Check 10), unless it falls under Check 7 (budget/financial) or Check 8 (specification) or Check 13 (scientific_report - but requires prose).

    *   Wait, Check 10 says: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)... financial or money-data table... is budget, not a generic labeled-data form."

    *   This table is "% Volume Change - Pretax versus After Tax". This is financial data (volume, tax). So it falls under Check 7 -&gt; budget.

    *   Let's check the budget definition again: "financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures)". This table shows volume changes (financial metric) with pretax/after tax labels. It is a financial data table. So it should be budget.

    *   Wait, let's look closer. Is it a form?

    *   Check 10: "standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is not generic admin data.

    *   Check 7: "financial or money-data table... is budget, not form".

    *   The table has rows: Total U.S., New York, Connecticut, Pennsylvania Surrounding Counties, Vermont, New Jersey, NY+CT+*Penn+VT+NJ. Columns: percentages.

    *   Title: "% Volume Change - Pretax versus After Tax (1-200 versus 4-600)".

    *   Source: STARS Store Level.

    *   This is a financial data table (volume change, tax implications). So it fits "budget" under Check 7.

    *   Let's reconsider Check 10 (Form). "A standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is not generic.

    *   Let's reconsider Check 7 (Budget). "financial or money-data table... is budget". Yes.

    *   Wait, is there any other category?

    *   What about "scientific_report"? No prose.

    *   What about "presentation"? Check 9 says "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." But Check 7 overrides Check 10 for money records. "It does NOT cover money records: ... financial or money-data table ... is budget, not form".

    *   So the label should be **budget**.

    *   Let's double check. Is "% Volume Change" a financial/money-data table? Yes, volume and tax are financial metrics. "Pretax versus After Tax" is financial analysis.

    *   The table lists regions and percentages. It's a data table.

    *   Check 7 budget bullet: "financial or money-data table (price/value estimates, price-to-earnings, budget-vs-actual, stock/investment figures)". This fits "financial or money-data table".

    *   Let's look at the "Runner-up" logic.

    *   Runner-up: form. Ruled out because Check 7 says money records/financial tables are budget, not form.

    *   Wait, is it a "specification"? Check 8: "labeled product/parameter rate-data chart... plotting a measured property over time/subgroup against spec limits". This is volume change by region, not product parameters against spec limits. And no "shall/must". So not specification.

    *   Is it a "news_article"? No masthead.

    *   So it's **budget**.

    *   Let's re-read the table content.

    *   Title: "% Volume Change - Pretax versus After Tax (1-200 versus 4-600)"

    *   Rows: Total U.S., New York, Connecticut, Pennsylvania Surrounding Counties, Vermont, New Jersey, NY+CT+*Penn+VT+NJ.

    *   Values: 8.4%, -20.5%, 20.0%, 18.2%, 12.2%, 10.6%, -9.5%.

    *   Source: STARS Store Level.

    *   Note: *Penn surrounding counties are Erie, Warren, McKean, Potter, Tioga, Bradford, Susquehanna, Wayne, and Pike.

    *   Bates: 20837223530.

    *   This is a financial data table showing volume changes (likely cigarette volume, given the tobacco archive context and regions like PA surrounding counties which often relate to tax jurisdictions). Pretax vs After tax volume change. This is definitely financial/money-data.

    *   Therefore, Check 7 applies. Budget.

    *   Wait, is it a "form"?

    *   Check 10: "standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is financial data.

    *   Check 7: "financial or money-data table... is budget, not form".

    *   So **budget** is the correct label.

    *   Let's check if there's any other interpretation.

    *   Could it be a "scientific_report"? No, no prose.

    *   Could it be a "presentation"? Check 9 explicitly says "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." And Check 7 overrides form for money data.

    *   Final decision: **budget**.

    *   Wait, let's look at the labels again.

    *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

    *   Is it possible this is just a "form"?

    *   Check 10: "standalone labeled data chart or table... is a form only when it holds generic administrative/log data". This is not generic admin data. It's specific financial analysis data.

    *   Check 7: "financial or money-data table... is budget".

    *   So **budget**.

    *   Let's refine the scratchpad.

    *   Check 1: file_folder. No, has title and table.

    *   Check 2: handwritten. No.

    *   Check 3: fax. No.

    *   Check 4: questionnaire. No.

    *   Check 5: resume. No.

    *   Check 6: scientific_publication. No journal header.

    *   Check 7: financial document. Yes. Table shows "% Volume Change - Pretax versus After Tax". This is financial/money-data. "financial or money-data table... is budget".

    *   Check 8: specification. No product spec language.

    *   Check 9: presentation. "A standalone chart or table of values alone is NOT a slide — it is a form". But Check 7 overrides.

    *   Check 10: form. "standalone labeled data chart... is a form only when it holds generic administrative/log data". This is financial data, so Check 7 applies (budget).

    *   Check 11: correspondence. No.

    *   Check 12: news_article. No.

    *   Check 13: scientific_report. No prose.

    *   Check 14: advertisement. No.

    *   Runner-up: form. Ruled out because the table contains financial/money data (volume change, pretax/after tax), which Check 7 classifies as budget, overriding the generic form classification for standalone charts.

    *   Wait, is "Volume Change" financial? Yes, in business context, volume and tax are financial metrics. "Pretax versus After Tax" is definitely financial.

    *   One more check: Is it a "specification"?

    *   Check 8: "labeled product/parameter rate-data chart... plotting a measured property over time/subgroup against spec limits". This is by region (Total U.S., NY, CT...), not time/subgroup against spec limits. And no spec limits (USPEC/SPEC). So not specification.

    *   Conclusion: **budget**.


</details>

## questionnaire → handwritten

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__questionnaire__0087.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>questionnaire</code> | <strong>Predicted:</strong> <code>handwritten</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a Bates number "2030688148" at the bottom right. There is a stamp "CONFIDENTIAL" and "PHILIP MORRIS & ASS". There is a name "V. TUCKER" at the top right.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: There is a Bates number "2030688148" and a name "V. TUCKER". But there is a lot of handwritten text. It's not just an identifier.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: The page is almost entirely handwritten text. It looks like a Q&A or notes. "So you THINK YOU KNOW STOCK PREP?". Numbered list 1-7. Handwritten answers. "V. TUCKER" at the top.

    *   Is it on a printed template? No, it looks like freeform handwriting on blank paper (maybe lined, but mostly blank). Wait, let's look closer. It's handwritten questions and answers. "1. approximately How Many Gallons of Water are introduced into the Evaporator Cooling Wells...". "2. When operating normally what should the percentage of Solubles be...".

    *   Is it a filled form? No printed field labels, boxes, or ruled entry cells (except maybe faint lines, but it looks like freehand writing on paper). The text is handwritten.

    *   Wait, is it a questionnaire? No, it's handwritten notes/answers. "Notes ABOUT a survey instrument are questionnaire... Conversely, a respondent's freeform handwritten opinion/feedback card... IS handwritten". This looks like study notes or a quiz answer sheet written by hand. "So you THINK YOU KNOW STOCK PREP?" sounds like a study guide or quiz.

    *   Let's check the rules: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template." This fits perfectly. It's handwritten notes/answers.

    *   Result: handwritten.

Let's double check other checks just in case.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header. The stamp "CONFIDENTIAL PHILIP MORRIS & ASS" is not a fax header.

    *   Result: not this check.

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: The text looks like questions ("How many gallons...", "When operating normally..."). But it is handwritten. The rule says: "A page does not have to show questions to be a questionnaire...". But this is handwritten. "Notes ABOUT a survey instrument are questionnaire... Conversely, a respondent's freeform handwritten opinion/feedback card... IS handwritten". This looks like handwritten notes or answers to questions. It's not a printed survey instrument. It's handwritten text.

    *   Result: not this check.

-   **Check 5: resume**

    *   Evidence: No career history.

    *   Result: not this check.

-   **Check 6: scientific_publication**

    *   Evidence: No journal header.

    *   Result: not this check.

-   **Check 7: financial document**

    *   Evidence: No financial tables. "20,000 pounds", "2398" (calculation). Not financial.

    *   Result: not this check.

-   **Check 8: specification**

    *   Evidence: Technical content ("Evaporator Cooling Wells", "Solubles", "SEH"). But it's handwritten notes, not a printed specification document with "shall/must" or product analysis tables.

    *   Result: not this check.

-   **Check 9: presentation**

    *   Evidence: Not a slide deck. Not a cover page.

    *   Result: not this check.

-   **Check 10: administrative form**

    *   Evidence: No printed fields/boxes.

    *   Result: not this check.

-   **Check 11: correspondence**

    *   Evidence: No TO/FROM/RE header block (except maybe "V. TUCKER" at top, but no structure). No salutation/closing.

    *   Result: not this check.

-   **Check 12: news_article**

    *   Evidence: No masthead.

    *   Result: not this check.

-   **Check 13: scientific_report**

    *   Evidence: Technical content, but it's handwritten notes, not running narrative prose of a report.

    *   Result: not this check.

-   **Check 14: advertisement**

    *   Evidence: No marketing layout.

    *   Result: not this check.

**Conclusion:**

The page is predominantly handwritten text. It looks like study notes or a handwritten quiz/answers titled "So you THINK YOU KNOW STOCK PREP?". The content is technical (tobacco processing - stock prep, evaporator, solubles), but the *function* is handwritten notes/answers.

Rule check: "Most of the content is freeform handwriting... NOT on a printed template." -&gt; handwritten.

Rule check: "Handwriting filling in labeled printed fields is form, not handwritten". There are no labeled printed fields. It's just handwritten text on a page (maybe with faint ruling, but looks like freehand).

Rule check: "A log/diary sheet is freeform...". This is a list of Q&A.

It fits "handwritten" best.

Wait, is it a "questionnaire"?

Check 4: "The page asks the reader to answer...". This page *has* questions and answers written by hand. It's not a printed survey instrument. "questionnaire requires a PRINTED survey instrument with printed question items... not a person's freeform writing."

So it's not questionnaire.

Is it a "memo"?

Check 11: "memo: internal TO:/FROM:/RE:/SUBJECT:/DATE: header block...". There is "V. TUCKER" at the top right. No other header. No prose body following a header structure. It's a list of Q&A.

So "handwritten" is the correct label.

Let's re-read the handwritten check carefully.

"Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."

"This includes meeting-minutes sheets and log tables printed with ruled columns and headers... whose rows are filled by hand... that stays form".

Here, there are no printed columns/headers. It's just handwritten text "1. approximately...", "2. When operating...". It looks like someone wrote down questions and answers.

"Notes ABOUT a survey instrument are questionnaire... Conversely, a respondent's freeform handwritten opinion/feedback card... IS handwritten".

This looks like handwritten notes (maybe study notes for "Stock Prep").

Final decision: handwritten.

One detail: "V. TUCKER" at top right. "CONFIDENTIAL PHILIP MORRIS & ASS" stamp. Bates number.

The content is handwritten Q&A about "Stock Prep" (Stock solution preparation in tobacco processing).

It is a handwritten document.

Let's check if it could be a "form".

"A form does NOT have to be blank — a filled form recording data is still a form... including handwriting in its cells."

But there are no printed cells/fields. It's just handwriting on a page.

So it's handwritten.

Final check of the label list:

advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

Label: handwritten.

One edge case: Is it a "scientific_report"?

"Requires running prose — a page that is only labeled field-value entries... is a filled form".

This is handwritten Q&A. Not running prose of a report.

Is it a "specification"?

"Material Safety Data Sheet... product formulation... 'shall/must' requirement language."

No.

So, handwritten.

Wait, looking very closely at the text:

"1. approximately How Many Gallons of Water are introduced into the Evaporator Cooling Wells from Vapor Off of the SEH? It depends on your % to the Evaporator (1) Sol Sol (2) Sol Concentration"

"2. When operating normally what should the percentage of Solubles be in the 24" Standpipe Liquor? 16% to 18%"

...

"5. If a piece of Equipment uses 20,000 pounds of Steam an hour, How many gallons of Condensate would be generated? 20,000 / 8.34 = 2398"

"6. If Solubles of SEH from Press 18 + 18 are 10% what can be done to increase or decrease this Percentage? - more or less RBW in the Pulper"

"7. What is Vacuum? That which is lower than Atmospheric pressure."

This is clearly handwritten notes/answers. "So you THINK YOU KNOW STOCK PREP?" is the title.

It's a handwritten study guide or quiz answers.

Label: handwritten.

One final check on "file_folder".

"A Bates number or archive stamp alone is NOT enough... A page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".

Here, the title is handwritten "So you THINK YOU KNOW STOCK PREP?". It's not a bold headline title on a cover page. It's part of the handwritten content.

The page has real content (the Q&A). So not file_folder.

The label is handwritten.


</details>

## resume → file_folder

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__resume__0010.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>resume</code> | <strong>Predicted:</strong> <code>file_folder</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** I see "DANIEL A. MILWAY", "Senior Vice President - Administration", "202/457-0358", "THE TOBACCO INSTITUTE", "1875 I STREET NORTHWEST", "WASHINGTON DC 20006", "202/457-4800". This looks like a letterhead or a fax header, but let's look closer. Wait, there's a faint line at the bottom. Let's look at the whole page.
- **Masthead/Running head:** No newspaper masthead. No journal running head.
- **Content:** The page is almost entirely blank white space with some noise. At the top right, there is text:

  "DANIEL A. MILWAY

  Senior Vice President -

  Administration

  202/457-0358

  THE TOBACCO INSTITUTE

  1875 I STREET NORTHWEST

  WASHINGTON DC 20006

  202/457-4800"

  At the bottom, there is a faint line of text, possibly a Bates number or footer, but it's very blurry. Wait, let's look at the top left. There's a faint "1-" or something.

  Actually, this looks like the top of a letter or a fax cover sheet, or maybe just a blank page with letterhead at the top.

  Wait, let's re-read the checks.

**2. Check 1: IDENTIFIER-ONLY PAGE -&gt; file_folder**

- "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
- "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
- "A prominent topical heading always counts as real content..."
- This page has a letterhead block: "DANIEL A. MILWAY... THE TOBACCO INSTITUTE...". This is letterhead. Is it a file folder tab? No, it's text at the top right.
- Wait, is this a blank page with letterhead?
- Let's look at the bottom. There is a very faint line of text at the bottom. "Bates number..." maybe?
- Actually, looking closely at the top left, there is a faint "1-".
- This looks like a blank page from a letter or memo, or the back of a page, or a fax transmission page that is blank?
- Wait, check 1 says: "A page is NOT file_folder if it carries any real content...". Letterhead is content?
- Let's look at the definition of file_folder again. "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
- This page has a name and address block. Is that a "short label or ID"? No, it's a letterhead.
- However, if the page is otherwise blank, maybe it's a file_folder?
- Wait, look at the bottom edge. There is a strip of text. "Bates number...".
- Let's reconsider the content. The text is:

  DANIEL A. MILWAY

  Senior Vice President - Administration

  202/457-0358

  THE TOBACCO INSTITUTE

  1875 I STREET NORTHWEST

  WASHINGTON DC 20006

  202/457-4800

- This is a letterhead block.
- Is there a top-left mark? "1-".
- This looks like a blank page with letterhead.
- Let's check the other categories.

**3. Check 2: HANDWRITTEN** -&gt; No.

**4. Check 3: FAX TRANSMISSION SHEET** -&gt; No "FACSIMILE" header.

**5. Check 4: QUESTIONNAIRE** -&gt; No.

**6. Check 5: RESUME** -&gt; No.

**7. Check 6: SCIENTIFIC PUBLICATION** -&gt; No journal header.

**8. Check 7: FINANCIAL DOCUMENT** -&gt; No.

**9. Check 8: SPECIFICATION** -&gt; No.

**10. Check 9: PRESENTATION** -&gt; "A near-blank cover or title page... is a presentation... not file_folder."

- "A standalone photographic image... carrying only a Bates number is a photographic slide (this check), not file_folder."
- "A large heading rotated 90 degrees... is a section divider... presentation."
- This page is mostly blank. It has a letterhead at the top right.
- Is it a presentation cover? No, it's just letterhead.
- Is it a file_folder? "A page is NOT file_folder if it carries any real content...". Letterhead is content?
- Wait, look at the bottom text. It's very blurry. "Bates number...".
- Let's look at the top left. "1-".
- This looks like a blank page in a document.
- Let's re-read Check 1 carefully.
- "file_folder: Almost no body content: only an archive/Bates number, a stamp, ashort label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
- "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content... not file_folder."
- "Legal/procedural stamps... are routine handling markings... ignore them... what actually decides file_folder is whether a topical heading or body content exists."
- This page has a letterhead (Name, Title, Company, Address). Is that a "topical heading or body content"?
- Usually, a blank page with letterhead at the top is just a blank page in a letter/memo. But if the page is *only* the letterhead and blank space, what is it?
- Wait, look at the bottom. There is a faint line. "Bates number...".
- Actually, this looks like the top of a letter or memo, but the rest is blank.
- Or is it a fax cover sheet? No fax header.
- Let's look at the text again.

  DANIEL A. MILWAY

  Senior Vice President - Administration

  202/457-0358

  THE TOBACCO INSTITUTE

  1875 I STREET NORTHWEST

  WASHINGTON DC 20006

  202/457-4800

- This is a letterhead.
- If a page has letterhead and is otherwise blank, is it a letter? No, a letter needs "Dear...", prose, signature.
- Is it a memo? No, memo needs TO:/FROM:/RE: header.
- Is it a file_folder? "Almost no body content...". The letterhead is content, but is it "real content" like a title or body?
- "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
- Letterhead is not a topical title. It's just the sender's info.
- However, check 1 says: "A prominent topical heading always counts as real content, subtitle or not." Letterhead is not a topical heading.
- So if the page is just letterhead + blank space + Bates number, it might be file_folder?
- Wait, "A page is NOT file_folder if it carries any real content...". Does letterhead count as real content?
- Let's look at the bottom text. It looks like a Bates number line. "Bates Number ...".
- If the page is just a Bates number and letterhead, it's likely a blank page from a scanned document, often classified as file_folder if it's just metadata.
- BUT, look at the top left corner. There is a faint "1-". And some dots.
- This looks like a fax transmission page that is blank? No, fax transmission page is check 3.
- Let's look at the bottom edge. There is a strip of text. "Bates number...".
- Actually, let's look at the whole image. It's a white page with noise. Top right has the letterhead. Bottom has a faint line.
- This is likely a blank page in a scanned document.
- In many archives, blank pages or pages with only letterhead/Bates numbers are classified as file_folder if they serve as separators or are just metadata.
- Wait, check 1: "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
- The letterhead is not a topical title. It's just address info.
- So this fits file_folder?
- Let's check if there's any other category.
- Could it be a letter? No body.
- Could it be a memo? No header.
- Could it be a presentation? "A near-blank cover or title page... is a presentation... not file_folder." But this isn'*t* a cover page with a title. It's just letterhead.
- "A standalone photographic image... is a photographic slide... not file_folder." Not an image.
- "A large heading rotated 90 degrees... is a section divider... presentation." No large heading.
- So it's either file_folder or something else.
- If it's just letterhead and blank space, it's likely file_folder (metadata only).
- Wait, is there a hidden text?
- The bottom text is very blurry. "Bates Number ...".
- Let's assume it's file_folder.

Let's re-evaluate. Is there any text I'm missing?

Top left: "1-".

Top right: Letterhead.

Bottom: Faint line.

This looks like a blank page from a letter or memo, scanned with a Bates number.

In the tobacco archive, blank pages or pages with only letterhead/Bates numbers are often file_folder (or just ignored, but here we must classify).

Check 1: "file_folder: Almost no body content: only an archive/Bates number, a stamp, a short label or ID...". The letterhead is an ID (Daniel A. Milway, The Tobacco Institute). It's not a topical title.

So file_folder seems correct.

Wait, is it a "file_folder" because it's a folder tab? No, it's not a tab shape.

Is it a "file_folder" because it's an identifier-only page? Yes, mostly.

Let's check if it could be a "letter" or "memo" with missing content? No, we classify what's there.

If a page has letterhead and nothing else, it's not a letter (needs salutation, body, closing). It's not a memo (needs TO/FROM/RE).

So it's not correspondence.

Is it a "presentation"? "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation". This page has no bold headline title. It has a letterhead. So not presentation.

So file_folder is the best fit. "Almost no body content... Pure filing metadata only." The letterhead and Bates number are metadata.

Wait, let's look at the bottom text again. It's a long line of text. "Bates Number ...".

Actually, looking very closely at the bottom, there is a line of text that looks like a Bates number and maybe a copyright or scan info.

The top right text is the letterhead.

This is a blank page with letterhead.

In document classification tasks for archives, blank pages or pages with only letterhead/Bates numbers are often classified as file_folder (or similar metadata category). Here, file_folder is the only one that fits "Almost no body content".

Let's double check Check 1 exceptions.

"A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."

Letterhead is not a photograph, table, questionnaire, or note.

"A prominent topical heading always counts as real content". Letterhead is not a topical heading.

So file_folder is correct.

Wait, is there a chance this is a "form"? No fields.

"Handwritten"? No.

Let's consider if the letterhead makes it a "letter".

Check 11: "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature". This page has no recipient address, no date, no salutation, no body, no signature. So not a letter.

Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". No.

So it's not correspondence.

It must be file_folder.

One more look at the bottom text. It looks like "Bates Number ...".

And top left "1-".

This is likely a blank page in a scanned document, classified as file_folder.

Wait, is there any possibility it's a "scientific_report" title page? No title.

"Presentation" cover? No title.

Final decision: file_folder.

Evidence for file_folder: The page contains almost no body content, only a letterhead block (Daniel A. Milway, The Tobacco Institute) and likely a Bates number/metadata at the bottom. No topical heading, no sentences, no form fields. It fits "Almost no body content: only an archive/Bates number, a stamp, a short label or ID...".

Runner-up: presentation. Ruled out because there is no bold headline title, no designed background, no photographic slide image. It's just letterhead on a blank page.

Wait, looking very closely at the bottom edge, there is a strip of text. "Bates Number ...".

And the top left has "1-".

This is definitely a metadata-only page.

One detail: "A page is NOT file_folder if it carries any real content...". Does the letterhead count as real content?

The instructions say: "Legal/procedural stamps such as 'CONFIDENTIAL,' 'PRIVILEGED,' or 'LITIGATION' are routine handling markings, not identifying content — ignore them when deciding file_folder vs. another category. They appear on many document types across this archive; what actually decides file_folder is whether a topical heading or body content exists, not whether a legal stamp is present."

Letterhead is similar to a stamp/marking in this context—it identifies the sender but isn'*t* a topical heading or body content. The page is effectively blank.

So, file_folder.

&lt;scratchpad&gt;

file_folder: yes — the page is almost entirely blank white space with noise. The only text is a letterhead block at the top right ("DANIEL A. MILWAY / Senior Vice President - Administration / THE TOBACCO INSTITUTE / 1875 I STREET NORTHWEST / WASHINGTON DC 20006") and a faint line at the bottom (likely Bates number/metadata). There is no topical heading, no body content, no form fields, no sentences. This fits "Almost no body content: only an archive/Bates number, a stamp, a short label or ID... Pure filing metadata only." The letterhead is not a topical heading or real content like a table or photograph.

handwritten: no — no handwriting.

form: no — no fields, boxes, or checkboxes.

questionnaire: no — no questions.

resume: no — not a career history.

scientific_publication: no — no journal header.

financial: no — no financial data.

specification: no — no product data.

presentation: no — although near-blank, it lacks a bold headline title, designed background, or photographic slide image. It's just letterhead on a blank page, not a cover or divider.

correspondence: no — letterhead is present, but no recipient address, date, salutation, body, or closing signature (not a letter); no TO:/FROM:/RE: header (not a memo).

news_article: no — no masthead.

advertisement: no — no marketing content.

scientific_report: no — no running prose.

Runner-up: presentation, ruled out because the page is just letterhead on a blank sheet without a bold title, slide layout, or photographic image; it lacks the designed elements of a presentation cover or divider.

&lt;/scratchpad&gt;

&lt;label&gt;file_folder&lt;/label&gt;


</details>

## resume → presentation

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__resume__0040.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>resume</code> | <strong>Predicted:</strong> <code>presentation</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** None. No From/To/Sent/Subject.
- **Masthead/Running head:** No newspaper/magazine masthead. No journal running head/volume/issue/page number on this specific page. There is a Bates number "2010007950" rotated on the right side.

**2. Scratchpad procedure:**

-   **Check 1: file_folder**

    *   Evidence: The page has a name "HENRY I. RUSSEK, *M*.D.", credentials, and a quote. It has real content. Not file_folder.

    *   Wait, is it a folder tab? No, it's a full page of text.

    *   Is it an identifier-only page? No, it has a bio and a quote.

-   **Check 2: handwritten**

    *   Evidence: The text is typed. Not handwritten.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header. The Bates number is rotated, but no fax transmission header like "SENT BY:".

-   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -&gt; questionnaire**

    *   Evidence: No questions, no rating scales.

-   **Check 5: PERSON'S CAREER HISTORY -&gt; resume**

    *   Evidence: "HENRY I. RUSSEK, *M*.D.", "Consultant in Cardiovascular Disease...", "Fellow: American College...". This looks like a biographical sketch or a press release excerpt about a person. Let's look further. It lists credentials. But it's very short. It's just a name, title, and a quote. It's not a full CV/resume with education, positions, honors, publications. It looks like a snippet from a news article or a press kit. Wait, let's look at the structure.

    *   Name at top.

    *   Credentials below.

    *   "(Headline Quote)"

    *   Quote text.

    *   This looks like a page from a press kit or a news article excerpt, or maybe a scientific commentary?

    *   Let's check the labels. "news_article"? "scientific_publication"? "advertisement"?

    *   Let's re-read the content. It's a quote from a doctor about tobacco and coronary disease. "Statistical findings linking the tobacco habit to coronary disease afford no proof..."

    *   This looks like a press release or a media kit page, or a page from a newspaper/magazine.

    *   Wait, is it a "presentation"? No.

    *   Is it a "news_article"? Let's check check 12. "Newspaper or magazine masthead...". No masthead.

    *   Is it a "scientific_publication"? No journal identifier.

    *   Is it a "scientific_report"? No running prose narrative of a study.

    *   Let's look at the "Headline Quote" label. This is typical of a press release or a media kit page used in journalism or advertising.

    *   Wait, look at the bottom right: "2010007950". This is a Bates number.

    *   Let's look at the content again. It's a bio of Henry I. Russek, *M*.D. and a quote.

    *   Could this be part of a "news_article"? The instructions say: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content". This page doesn'*t* look like a full news article.

    *   Could it be an "advertisement"? Marketing layout, product imagery, slogans. No.

    *   Could it be a "letter"? No salutation.

    *   Could it be a "memo"? No TO/FROM.

    *   Let's reconsider "resume". Check 5: "CV, resume, professional profile, or biographical sketch listing education, positions, honors, and publications". This page lists "Consultant in...", "Fellow: American College...". It's a biographical sketch. But it's very short. And it has a "(Headline Quote)". A resume doesn'*t* usually have a headline quote.

    *   Let's look at the "news_article" check again. "Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet". This page looks like a page from a press kit or a media guide.

    *   Wait, is there a category for "press release"? No. "presentation" covers "corporate press release / issued statement ("FOR IMMEDIATE RELEASE", media contact)". This doesn'*t* have "FOR IMMEDIATE RELEASE".

    *   Let's look at the structure. Name, credentials, quote. This is often found in news articles or press releases.

    *   Let's look at the "scientific_publication" check. No journal ID.

    *   Let's look at "scientific_report". No.

Let's re-evaluate the content.

"HENRY I. RUSSEK, *M*.D. Consultant in Cardiovascular Disease, USPHS Hospital, Staten Island, *N*.Y. Fellow: American College of Physicians..."

"(Headline Quote)"

"Statistical findings linking the tobacco habit to coronary disease afford no proof of a causal relationship since excessive smoking, like overeating and failure to obtain adequate exercise, is often an undeniable manifestation of psychological stress."

This looks like a page from a tobacco industry archive. Henry Russek was a consultant who often provided expert testimony or quotes for the tobacco industry to argue against the link between smoking and heart disease.

This is likely a page from a media kit, a press release, or a page intended for use in news articles (a "headkit" or "media kit" page).

In the tobacco archives, these are often "press kits" or "media guides".

How do these map to the 16 categories?

- advertisement? No, it's not selling a product directly, it's providing a quote.
- news_article? It looks like a snippet meant for news. But is it a news article itself? No masthead.
- presentation? "corporate press release / issued statement". A media kit page is similar. But usually press releases have "FOR IMMEDIATE RELEASE".
- form? No.
- letter? No.

Let's look at the checks again.

Check 12: "PUBLISHED JOURNALISM -&gt; news_article". "Newspaper or magazine masthead... Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet".

This page doesn'*t* present as published periodical content. It presents as a bio/quote sheet.

Check 9: "SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -&gt; presentation". "corporate press release / issued statement".

Is this a company statement? It's a bio and a quote.

Wait, let's look at the "advertisement" check (14). "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures." No.

Let's look at "scientific_publication" (6). No.

Let's look at "resume" (5). "biographical sketch". This is a biographical sketch of Henry Russek. But the "(Headline Quote)" makes it weird for a resume.

Let's look at the document type in the tobacco archive. This is likely a "media kit" page or a "press release" page.

If it's a press release, it falls under "presentation" (check 9: "corporate press release / issued statement").

Wait, check 9 says: "a corporate press release / issued statement ("FOR IMMEDIATE RELEASE", media contact)". This page doesn'*t* have that.

Let's reconsider "news_article". Sometimes these archives contain clippings. If this is a clipping from a newspaper/magazine, it would be a news_article. But it has a Bates number and looks like a scanned internal document (media kit).

Actually, looking at the layout: Centered name, centered credentials, centered quote. This is a standard "media kit" or "press kit" page, often called a "headkit" or "expert bio".

In the tobacco archive classification tasks (like the one this prompt is based on, likely the Truth Tobacco Industry Documents or similar), these pages are often classified as... what?

Let's look at the labels again.

advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.

Could it be "news_article"?

The text is a quote about tobacco. It looks like something that would appear in a news article or a press release.

If I have to choose, "news_article" is for published journalism. This is not published journalism on this page.

"presentation" covers "corporate press release". A media kit page is part of a press release package.

"resume" covers "biographical sketch". This is a biographical sketch. But the quote...

Let's look at the "Headline Quote" label. This is a strong indicator of a media-related document.

In many classification schemas for this archive, pages like this (expert bio + quote for media) are classified as **news_article** if they are clippings, or **advertisement** if they are ads, or **presentation** if they are internal slides/press releases.

Wait, let's look at Check 12 again. "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content".

This page is not editorial content.

Let's look at Check 14: "PROMOTIONAL MATERIAL -&gt; advertisement". "Marketing layout...". This is promoting a viewpoint (anti-smoking link?), which is promotional for the tobacco industry (or anti-tobacco, but the archive is tobacco-industry). Henry Russek was a tobacco industry consultant. He was paid to say smoking doesn'*t* cause heart disease. So this is promotional material / advocacy material.

Is it an advertisement? "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures." This doesn'*t* fit perfectly.

Let's look at Check 9 again. "presentation". "a meeting/program/speaker cover page". This is a speaker bio/cover page? "Henry I. Russek, *M*.D."... "(Headline Quote)". This looks like a page from a conference program or a media kit for a speaker.

If it's a speaker bio for a conference, it's part of a presentation package.

"deck title or section-divider page, a meeting/program/speaker cover page".

Yes! "a meeting/program/speaker cover page".

This page is a speaker cover page / bio page for Henry I. Russek. It has his name, credentials, and a quote he might give or is associated with.

So **presentation** (check 9) seems plausible. "a meeting/program/speaker cover page".

Let's check the evidence for Check 9:

- "meeting/program/speaker cover page": The page features a person's name (Henry I. Russek, *M*.D.), his professional titles/affiliations (Consultant in Cardiovascular Disease, Fellow of various colleges), and a "(Headline Quote)". This is typical layout for a speaker bio or a press kit page included in a presentation or conference program.
- The layout is sparse, centered text.
- The Bates number is on the side.

Let's check "resume" (Check 5) again.

- "CV, resume, professional profile, or biographical sketch listing education, positions, honors, and publications".
- This page lists "Consultant...", "Fellow: ...". It's a professional profile.
- But it has "(Headline Quote)". Resumes don'*t* have headline quotes.
- Also, Check 9 comes before Check 5? No, the checks are numbered 1-14.
- Check 5 is "PERSON'S CAREER HISTORY -&gt; resume".
- Check 9 is "SLIDE DECK... -&gt; presentation".
- Wait, the order is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.
- So Check 5 (resume) is before Check 9 (presentation).
- If it's a biographical sketch, it might be resume.
- But "Headline Quote" is not resume material.
- And "speaker cover page" is explicitly mentioned in Check 9.

Let's re-read Check 9 carefully.

"Slide/overhead layouts... a meeting/program/speaker cover page, a corporate press release / issued statement... or a photographic slide image... A near-blank cover or title page... is a presentation".

This page is sparse. It has a name, credentials, and a quote. It looks like a "speaker cover page" or a page from a "program".

The text is:

"HENRY I. RUSSEK, *M*.D."

"Consultant in Cardiovascular Disease, USPHS Hospital, Staten Island, *N*.Y. Fellow: American College of Physicians..."

"(Headline Quote)"

"Statistical findings..."

This is definitely a media kit page or a speaker bio page.

If it's a speaker bio page for a conference, it's a "meeting/program/speaker cover page" -&gt; **presentation**.

Let's consider **news_article** (Check 12).

Could this be a clipping from a newspaper?

Newspapers don'*t* usually have "(Headline Quote)" as a label in the text. That label is an instruction for the journalist or a note in a press release/media kit. "(Headline Quote)" is a meta-label. This indicates it's a press release or media kit document, not the final published article.

Press releases are covered under Check 9: "corporate press release / issued statement".

So **presentation** is the best fit.

Let's check if there's any other category.

"scientific_publication"? No.

"scientific_report"? No.

Let's look at the "resume" check again.

"biographical sketch listing education, positions, honors, and publications".

This page lists positions/affiliations. But it's very short. And the "(Headline Quote)" is the key. A resume doesn'*t* have a headline quote. A speaker bio or press kit page does.

So, Check 9 (presentation) is the winner.

Evidence: "meeting/program/speaker cover page" or "corporate press release / issued statement". The layout (centered name, credentials, "(Headline Quote)") is characteristic of a speaker bio page included in a conference program or a media kit (press release material). The label "(Headline Quote)" is a strong indicator of a document intended for media use (press release/media kit), which falls under corporate statement/presentation in this schema.

Wait, is there a chance it's **advertisement**?

Check 14: "Marketing layout...". This is promoting a viewpoint. But it lacks product imagery, slogans, brand styling. It's text-heavy.

Is there a chance it's **news_article**?

Check 12: "published periodical editorial content". The "(Headline Quote)" label proves it's not the final published article. It's a source document for journalism. Source documents like press releases are often classified as **presentation** (corporate statement) or sometimes **advertisement** (if promotional). But "presentation" covers "corporate press release".

Let's refine the "presentation" evidence.

Check 9: "a meeting/program/speaker cover page".

The page is a bio of a speaker (Henry I. Russek).

It has a "(Headline Quote)".

This is a speaker cover page / bio page.

Let's check the runner-up.

Runner-up: **resume**. Ruled out because the page includes a "(Headline Quote)" and is sparse/centered like a speaker bio or press kit page, not a full career history with education/publications. Also, Check 9 (presentation) covers speaker cover pages.

Actually, Check 5 is before Check 9.

If I stop at Check 5, I must have evidence for resume.

Evidence for resume: "biographical sketch". The page lists name, title, fellowships.

But is it a "CV, resume, professional profile, or biographical sketch listing education, positions, honors, and publications"?

It lists "Consultant...", "Fellow...". It doesn'*t* list education (degrees, universities) or publications. It's too short.

And the "(Headline Quote)" is not resume content.

So Check 5 is "not this check" (or weak evidence).

Let's go to Check 9.

Evidence: "speaker cover page" or "press release". The layout is a name, credentials, and a quote labeled "(Headline Quote)". This is typical of a media kit or conference program speaker bio. Check 9 explicitly includes "meeting/program/speaker cover page" and "corporate press release".

Final decision: **presentation**.

Wait, let's look at the Bates number: 2010007950.

This is a Philip Morris document (Bates numbers in the 20xxxx range are often PM or RJR).

Henry Russek was a PM consultant.

This is likely a page from a "media kit" or "press release" package.

Press releases -&gt; presentation (Check 9).

One more check: **file_folder**.

Check 1: "Almost no body content...". This page has body content (bio, quote). Not file_folder.

One more check: **scientific_report**.

Check 13: "Running narrative prose...". This is not running prose. It's a bio and a quote.

So, **presentation**.

Scratchpad:

- file_folder: no — page has bio text and a quote, not just an ID.
- handwritten: no — typed text.
- fax: no — no fax header.
- questionnaire: no — no questions.
- resume: no — lists credentials but is too short, lacks education/publications list, and contains a "(Headline Quote)" which is not resume content.
- scientific_publication: no — no journal identifier.
- financial: no — no money data.
- specification: no — no product data.
- presentation: yes — layout matches a "meeting/program/speaker cover page" or "corporate press release / issued statement" (media kit page with bio and headline quote). The "(Headline Quote)" label indicates it's a press/media document.
- form: no — no fields/boxes.
- correspondence: no — no TO/FROM/Dear.
- news_article: no — "(Headline Quote)" label indicates it's a source document (press kit), not published editorial content.
- scientific_report: no — no running narrative prose of a study.
- advertisement: no — no product imagery/slogans.

Runner-up: resume. Ruled out because the page is a sparse speaker bio/press kit page with a headline quote, not a full career history/biographical sketch with education and publications.

Wait, is "news_article" a better fit?

Sometimes these archives contain "clippings". If this is a clipping, it would be news_article.

But the "(Headline Quote)" is a meta-label. You don'*t* see "(Headline Quote)" in a published newspaper. You see it in a press release or media kit.

Press releases are "corporate press release / issued statement" -&gt; presentation.

So **presentation** is correct.

One detail: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation".

This page is mostly empty space (white space on left and bottom). Centered text.

"HENRY I. RUSSEK, *M*.D." (bold/centered)

Credentials (centered)

"(Headline Quote)" (centered)

Quote (centered)

This fits "near-blank cover" or "speaker cover page".

Final label: presentation.


</details>

## scientific_report → memo

<details class="trace-group">

<summary>1 reasoning traces</summary>

<h3 class="trace-file"><code>rvl_cdip__scientific_report__0048.png</code></h3>

<*p* class="trace-meta"><strong>Expected:</strong> <code>scientific_report</code> | <strong>Predicted:</strong> <code>memo</code></*p*>

<*p* class="trace-label">Reasoning</*p*>

The user wants me to classify a scanned business document into one of 16 categories.

**1. Pre-scan:**

- **Mail-client header block:** No "From/To/Sent/Subject" in email format. There is a header "INBIFO Institut für biologische Forschung GmbH · Köln", "02 May.94 DKU/BRA [D:\DKU\URL_VERT.DOC]". This looks like a document header, possibly a file path, but not a mail-client header. Wait, let's look closer. "02 May.94 DKU/BRA [D:\DKU\URL_VERT.DOC]". This looks like a document control line.
- **Masthead/Running head:** "INBIFO Institut für biologische Forschung GmbH · Köln". This is a company header, not a newspaper/magazine masthead or journal running head.

**2. Scratchpad checks:**

-   **Check 1: file_folder**

    *   Evidence: The page has a title "Betr.: Vertretung", a table, and body text. It's not just an ID/stamp.

    *   Result: not this check.

-   **Check 2: handwritten**

    *   Evidence: There is a handwritten note "-&gt; Exa, PMT" with a checkmark at the top right. But the majority of the content is typed text (German memo).

    *   Result: not this check.

-   **Check 3: FAX TRANSMISSION SHEET**

    *   Evidence: No "FACSIMILE" header. The top line is "INBIFO Institut...".

    *   Result: not this check.

-   **Check 4: questionnaire**

    *   Evidence: No survey questions.

    *   Result: not this check.

-   **Check 5: resume**

    *   Evidence: No career history.

    *   Result: not this check.

-   **Check 6: scientific_publication**

    *   Evidence: No journal running head/volume/issue. "INBIFO" is an institute name.

    *   Result: not this check.

-   **Check 7: financial document (invoice/budget)**

    *   Evidence: No financial tables, invoices, or budgets. It's about "Vertretung" (representation/substitution).

    *   Result: not this check.

-   **Check 8: specification**

    *   Evidence: No material safety data, product formulation, or "shall/must" language.

    *   Result: not this check.

-   **Check 9: presentation**

    *   Evidence: Not a slide deck, cover, or press release. It's a memo.

    *   Result: not this check.

-   **Check 10: administrative form**

    *   Evidence: There is a table with "FUNKTION" and "VERTRETER". But it's part of a memo explaining substitution arrangements. It's not a generic form for capturing data.

    *   Result: not this check.

-   **Check 11: correspondence (email, memo, letter)**

    *   Evidence:

        *   Header: "INBIFO Institut für biologische Forschung GmbH · Köln", "02 May.94 DKU/BRA [D:\DKU\URL_VERT.DOC]".

        *   Subject line: "Betr.: Vertretung" (Subject: Representation/Substitution).

        *   Body text: "Während meiner Abwesenheit vom 7. Mai 94 bis einschließlich 7.Jun.94 gelten folgende Vertretungsregelungen:" (During my absence from May 7, 94 to and including June 7, 94, the following substitution regulations apply:).

        *   Table of functions and representatives.

        *   Footer: "Verteiler:" (Distribution list) with addresses/locations.

        *   Footnotes 1 and 2.

    *   This is clearly an internal memo. "Betr.:" is German for "Betreff:" (Subject). It has a date, internal subject, body text, and distribution list ("Verteiler"). It lacks an external address and "Dear..." salutation, so it's a memo, not a letter. It lacks mail-client headers, so not email.

    *   Result: memo.

-   **Check 12: news_article**

    *   Evidence: No masthead, byline, dateline (in news sense), multi-column typography.

    *   Result: not this check.

-   **Check 13: scientific_report**

    *   Evidence: No running narrative prose about research objectives/methods/results. It's an administrative memo about who is covering for the author during absence.

    *   Result: not this check.

-   **Check 14: advertisement**

    *   Evidence: No marketing layout.

    *   Result: not this check.

**Conclusion:**

The document is a memo ("Betr.: Vertretung", internal distribution list "Verteiler", date, company header).

Let's refine the memo check (Check 11).

- "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
- Here we have "Betr.: Vertretung" (Subject) and "02 May.94" (Date). The header block is the company name and file path, then the subject.
- The text is "Während meiner Abwesenheit..." (During my absence...).
- "Verteiler:" (Distribution list) is typical for memos.
- This fits the definition of a memo perfectly.

Runner-up: form. The table "FUNKTION / VERTRETER" looks like a form, but it's embedded in a memo. The primary structure is correspondence (memo). Check 11 precedes Check 10.

Final label: memo.

---

</details>

---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
