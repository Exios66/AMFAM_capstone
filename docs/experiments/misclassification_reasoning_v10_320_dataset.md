# Misclassification Reasoning — v10_320_dataset

**Overall Accuracy:** 85.3% (272/319)  
**Total Errors:** 47  
**Unique Confused Pairs:** 24

## letter → memo (5 errors)

### `rvl_cdip__letter__0002.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** I see "RJR Interoffice Memorandum", "Subject:", "To:", "From:", "cc:". This looks like a memo header, not an email header (From/To/Sent/Subject). Wait, let's look closer. "RJR Interoffice Memorandum" is a header. "Subject:", "To:", "From:", "cc:". This is a standard memo format. No "Sent:" field typical of email. No "From: user@domain". It's a memo.
> - **Masthead/Running head:** No newspaper masthead. No journal running head. There is a date "MAR 27 1987" at the top right. There is a Bates number "50811 2328" on the right side.
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder.**
>     *   Evidence: The page has a full memo body, subject line, to/from fields, and handwritten notes. It has real content.
>     *   Result: not this check.
> 
> *   **Check 2: handwritten.**
>     *   Evidence: There is a large block of handwritten text at the bottom right ("3/30 / For the long term..."). However, the majority of the page is typed text (the memo body). The handwritten part is an annotation/note on the memo.
>     *   Result: not this check. (Handwriting fills a margin/annotation on a typed memo, it doesn't make the page "majority handwritten" in the sense of a freeform note on blank paper. Wait, let's check the rule: "Most of the content is freeform handwriting... NOT on a printed template." Here, the main content is the typed memo. The handwriting is a note *on* the memo. "A typed page with only a signature, stamp, or margin note is not handwritten." This fits.)
> 
> *   **Check 3: FAX TRANSMISSION SHEET.**
>     *   Evidence: No "FACSIMILE" header. The date "MAR 27 1987" is stamped, likely a received stamp or just a date stamp. No fax cover sheet layout.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL.**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY.**
>     *   Evidence: No CV/resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE.**
>     *   Evidence: No journal name, volume, issue, page range on this page.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT.**
>     *   Evidence: No line-item table, ledger, invoice, or budget. Mentions "Kydex(R) plastic sheets", toxicity data. No money.
>     *   Result: not this check.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION.**
>     *   Evidence: Discusses Kydex(R) plastic sheets, toxicity, polyacrylic-polyvinyl chloride polymer. But it's a memo *about* the material, not a Material Safety Data Sheet or a specification document defining the product's composition/properties with approval blocks (though it has an approval mention "Scientific Affairs has reviewed and approved..."). Wait, let's look at Check 8 vs Check 11.
>     *   Check 8: "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... 'shall/must' language." This page is a memo discussing toxicity. It's not a specification document itself. It's a memo *about* a material.
>     *   Result: not this check (yet, let's look at correspondence).
> 
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT.**
>     *   Evidence: Not a slide deck. Not a press release.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM.**
>     *   Evidence: It has "To:", "From:", "Subject:", "cc:". These are memo fields, not a generic form for capturing data. It's a standard memo layout.
>     *   Result: not this check.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter.**
>     *   Evidence:
>         *   Header: "RJR Interoffice Memorandum".
>         *   Fields: "Subject: Use of KYDEX(R) For A Waste Tub Stand", "March 26, 1987", "To: Mr. Bill Hunt", "From: Dr. Rob Harrington".
>         *   Body: Running prose about Kydex toxicity.
>         *   Closing: Signature (looks like "Rob"), initials "RH/Ige".
>         *   "cc: Dr. A. W. Hayes...".
>     *   This is clearly a memo. Internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed by memo-style prose.
>     *   Result: **memo**.
> 
> *   **Check 12: PUBLISHED JOURNALISM.**
>     *   Evidence: No masthead.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP.**
>     *   Evidence: It contains scientific text (toxicity data), but the structure is a memo (TO/FROM/SUBJECT). Check 11 (Correspondence) comes before Check 13? Wait, let's check the order.
>     *   Checks order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.
>     *   Check 11 is "CORRESPONDENCE -> email, memo, or letter".
>     *   The page has a memo header ("RJR Interoffice Memorandum", "To:", "From:", "Subject:"). This matches Check 11 perfectly.
>     *   Even though the content is scientific (toxicity of Kydex), the *function* is a memo. "Judge each page by its FUNCTION... a page full of technical data can still be a form, and a page about money can still be a form — but a bill is a bill even when it is printed on a form." Wait, "a page full of technical data can still be a form". Here, a page full of technical data is a memo.
>     *   Check 11 says: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose...". This page has exactly that. "RJR Interoffice Memorandum" is the header. "Subject:", "To:", "From:".
>     *   So it's a memo.
> 
> *   **Check 14: PROMOTIONAL MATERIAL.**
>     *   Evidence: No.
> 
> **Conclusion:**
> The document is an "RJR Interoffice Memorandum". It has To/From/Subject/Date. It is a memo.
> The handwritten note at the bottom is a margin note/annotation ("3/30 / For the long term..."). This doesn't make it handwritten (Check 2).
> The content is technical (toxicity of Kydex), but the format is a memo.
> 
> Let's double check Check 8 (Specification).
> "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... 'shall/must' language."
> This page is a memo *reviewing* the use of a material. "Scientific Affairs has reviewed and approved the use of Kydex(R)... Below is the evaluation of Kydex(R)." It's a memo transmitting an evaluation. The evaluation itself is text. It's not a specification document (which would define the product properties with "shall/must"). It's a memo *about* the material.
> Actually, let's look at the content. It describes the polymer composition and toxicity. But the layout is a memo.
> Check 11 (Correspondence) is before Check 8 (Specification) and Check 13 (Scientific Report).
> Wait, the order is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14.
> So Check 11 (Memo) stops the process.
> 
> Evidence for Memo (Check 11):
> - "RJR Interoffice Memorandum" header.
> - "Subject: Use of KYDEX(R)..."
> - "To: Mr. Bill Hunt"
> - "From: Dr. Rob Harrington"
> - "March 26, 1987"
> - Prose body.
> - Signature and initials "RH/Ige".
> - "cc:" list.
> 
> This is a classic memo.
> 
> Runner-up: scientific_report. Ruled out because the page has a clear memo header structure (TO/FROM/SUBJECT) and is an internal interoffice memorandum, which takes precedence as correspondence (Check 11) over a research write-up (Check 13), even though the content is technical/scientific. The function is internal communication/approval.
> 
> Wait, is there any email header? "From: Dr. Rob Harrington". No "Sent:", no email address. It's a typed memo (faxed perhaps, given the date stamp "MAR 27 1987" and the fax-like quality, but the content is a memo). The pre-scan says: "A FAX machine transmission header... is NOT a mail-client header... classify the underlying document by its own content (a faxed memo is a memo)". The date stamp "MAR 27 1987" looks like a received stamp or just a date. The document itself is titled "RJR Interoffice Memorandum". So it's a memo.
> 
> Final label: memo.

---

### `rvl_cdip__letter__0007.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None. There is a date "June 17, 1971", "Mr. J. H. Sherrill, Jr.", "Re: VANTAGE MENTHOL (HIRD # 71-0197)". No From/To/Sent/Subject mail client headers.
> - Masthead/running head: None. Just a Bates number "50030 0163" at the bottom right.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a date, recipient name, subject line, and several paragraphs of text. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: The text is typewritten. There is a small handwritten "Bill" at the top right and a circle around "MENTHOL (HIRD # 71-0197)". Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey instrument or transmittal note.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a resume.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal masthead, volume, issue, page range.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: Mentions "national print advertising", "outdoor advertising", but no line-item table, ledger, or financial structure. It's a report of data.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No Material Safety Data Sheet, formulation, or "shall/must" language.
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck, cover, or press release.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: No fields, boxes, checkboxes, or ruled entry lines for capturing data.
> - Not this check.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - Evidence:
>   - Date: "June 17, 1971"
>   - Recipient: "Mr. J. H. Sherrill, Jr."
>   - Subject: "Re: VANTAGE MENTHOL (HIRD # 71-0197)"
>   - Body: "This reports data from the VANTAGE Menthol CAS by billboard and non-billboard cities. BACKGROUND: ... DISCUSSION: ..."
>   - Sender: "Joseph Ottaviani, Marketing Research Department"
>   - Initials: "JO;sp"
>   - "Attachments"
>   - This is an internal memo. It has a date, internal recipient (Mr. J. H. Sherrill, Jr.), internal subject line ("Re:"), internal sender (Joseph Ottaviani, Marketing Research Department), and memo-style prose (BACKGROUND, DISCUSSION). No external address, no "Dear ..." salutation, no closing signature. It fits the memo definition perfectly: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo". Wait, it doesn't have literal "TO:/FROM:" labels, but it has "Mr. J. H. Sherrill, Jr." and "Re:" and the sender's name/title at the bottom. The instructions say: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels". This matches perfectly.
> - This is a memo.
> 
> **Check 12: PUBLISHED JOURNALISM -> news_article**
> - Evidence: No masthead, byline, dateline, multi-column typography.
> - Not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - Evidence: It's a memo reporting data, not a scientific write-up with objectives, methods, results, discussion in a research context. It's internal business correspondence.
> - Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
> - Evidence: Not an ad.
> - Not this check.
> 
> Final label: memo.
> 
> Let's double check.
> Date: June 17, 1971
> To: Mr. J. H. Sherrill, Jr.
> Re: VANTAGE MENTHOL (HIRD # 71-0197)
> Body paragraphs: BACKGROUND, DISCUSSION.
> From: Joseph Ottaviani, Marketing Research Department.
> Initials: JO;sp
> Attachments.
> 
> This is a classic internal memo.
> 
> Runner-up: letter. Ruled out because there is no external recipient address, no "Dear ..." salutation, and no closing signature. It's an internal note to a named person by name + department (implied internal). Actually, it just says "Mr. J. H. Sherrill, Jr." and the sender is "Joseph Ottaviani, Marketing Research Department". This is internal correspondence.
> 
> Wait, is there any chance it's a scientific_report? "This reports data from the VANTAGE Menthol CAS...". CAS = Consumer Awareness Survey? "BACKGROUND: VANTAGE Menthol went 'down-the-street' on May 3, 1971...". "DISCUSSION: Through the first six weeks...". It's a business memo reporting survey results. Not a scientific report.
> 
> Label: memo.

---

### `rvl_cdip__letter__0008.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** I see "TO:", "FROM:", "SUBJECT:", "April 16, 1993". This looks like a memo header. Let's check if it's an email. "TO: Mr. E. C. Leary", "FROM: G. R. Davis", "SUBJECT: March CAMEL Cash Tracking Results". No "Sent:", "Cc:", "Subject:" in email format (though Subject is there). Wait, email headers usually have "From:", "To:", "Sent:", "Subject:". This looks like a standard memo header. Let's look closer. "TO:", "FROM:", "SUBJECT:". This is a classic memo header.
> - **Masthead/Running head:** No newspaper/magazine masthead. No journal running head. There is a Bates number "93-13104" rotated on the left and "51969 5114" on the right. Top right has "24R2".
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a date, TO/FROM/SUBJECT headers, and several paragraphs of text ("Attached are the results...", "KEY FINDINGS:", bullet points). It has real content.
>     *   Result: not this check.
> 
> *   **Check 2: handwritten**
>     *   Evidence: There is a handwritten "24R2" at the top right and a rotated handwritten "93-13104" (looks like a Bates number, actually printed but rotated? No, "93-13104" looks like a handwritten annotation or a rotated stamp. Wait, "93-13104" is a Bates number, usually stamped. "24R2" is handwritten. But the majority of the content is typed text.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. The "SENT BY:" header is not present.
>     *   Result: not this check.
> 
> *   **Check 4: questionnaire**
>     *   Evidence: No survey questions, rating scales, or survey transmittal.
>     *   Result: not this check.
> 
> *   **Check 5: resume**
>     *   Evidence: No career history.
>     *   Result: not this check.
> 
> *   **Check 6: scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range on the page itself.
>     *   Result: not this check.
> 
> *   **Check 7: financial document (invoice/budget)**
>     *   Evidence: Mentions "March CAMEL Cash Tracking Results", "participation rate", "share of smoker results". No line-item table of charges, no invoice header, no budget table. It's a report of results.
>     *   Result: not this check.
> 
> *   **Check 8: specification**
>     *   Evidence: No material safety data, product formulation, "shall/must" language.
>     *   Result: not this check.
> 
> *   **Check 9: presentation**
>     *   Evidence: Not a slide deck, not a press release ("FOR IMMEDIATE RELEASE"), not a speech text. It's a memo.
>     *   Result: not this check.
> 
> *   **Check 10: administrative form**
>     *   Evidence: No filled fields, boxes, checkboxes for capturing data. It's a narrative document.
>     *   Result: not this check.
> 
> *   **Check 11: correspondence (email, memo, letter)**
>     *   Evidence:
>         *   Header: "TO: Mr. E. C. Leary", "FROM: G. R. Davis", "SUBJECT: March CAMEL Cash Tracking Results (BIAD #93-13104)", Date: "April 16, 1993".
>         *   Body: "Attached are the results...", "KEY FINDINGS:", bullet points with analysis.
>         *   Structure: Internal memo header (TO/FROM/SUBJECT/DATE) followed by memo-style prose. No external address, no "Dear...", no closing signature (though memos often don't have signatures, just the FROM line).
>         *   This fits the definition of a **memo**: internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose.
>     *   Result: **memo**.
> 
> *   **Check 12: news_article**
>     *   Evidence: No masthead, byline, dateline (other than the memo date), multi-column typography.
>     *   Result: not this check.
> 
> *   **Check 13: scientific_report**
>     *   Evidence: It has "KEY FINDINGS" and analysis, but the primary structure is a memo (TO/FROM/SUBJECT). Check 11 (correspondence/memo) takes precedence if the structure is a memo header + prose. Wait, let's check the precedence.
>     *   The instructions say: "Walk checks 1-14 below IN ORDER."
>     *   Check 11 is before Check 13.
>     *   Check 11 matches: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
>     *   The page has "TO:", "FROM:", "SUBJECT:", and a date "April 16, 1993". The body is prose discussing results.
>     *   Is it a scientific report? It discusses "CAMEL Cash Tracker Tag-on", "participation rate", "volatility". It looks like a business report/memo. But the *structure* is a memo.
>     *   Rule: "Once an earlier check matches, later checks do not override it."
>     *   Check 11 matches memo.
> 
> *   **Check 14: advertisement**
>     *   Evidence: No product imagery, slogans, coupons.
>     *   Result: not this check.
> 
> **Conclusion:**
> The document is a memo.
> Header: TO: Mr. E. C. Leary, FROM: G. R. Davis, SUBJECT: March CAMEL Cash Tracking Results. Date: April 16, 1993.
> Body: Prose discussing findings.
> This is a classic internal memo.
> 
> Let's double check Check 11 details.
> "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose (no external address, no 'Dear ...' salutation)."
> The page has:
> - Date: April 16, 1993
> - TO: Mr. E. C. Leary
> - FROM: G. R. Davis
> - SUBJECT: March CAMEL Cash Tracking Results
> - Body text starts immediately: "Attached are the results..."
> This is a perfect match for memo.
> 
> Runner-up: scientific_report. Ruled out because the page has a clear memo header (TO/FROM/SUBJECT) and follows memo structure (Check 11 precedes Check 13). Also, it's internal business correspondence about marketing results ("CAMEL Cash Tracking"), not an original research write-up with methods/results discussion in the scientific sense (though it has "findings", the format is a memo). Actually, even if it were a report, the memo header makes it a memo first. Wait, "A technical/project status report whose content is primarily technical... is scientific_report". But this is a memo *about* results. The structure is memo. Check 11 is before Check 13.
> 
> Final label: memo.

---

### `rvl_cdip__letter__0009.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> Let's look at the document.
> Header:
> RJR CONFIDENTIAL
> October 21, 1993
> TO: Mr. G. C. Pennell
> FROM: T. F. Witner
> SUBJECT: MAGNA Advertising Study Results
> 
> Body:
> "This provides you with key measures for the MAGNA Advertising Study..."
> Bullet points: "Recall/Impact Among Clutter Ads", "Key Measures"
> Tables with data (MAGNA, Bull Durham, Viceroy, DORAL, Pyramid, Bristol, Cambridge).
> Bates number: 51399 2876 (rotated on the right side).
> 
> Let's go through the checks.
> 
> Check 1: file_folder. No, it has a lot of body content, tables, prose.
> Check 2: handwritten. No, mostly typed. There's a small "can" or "cam" handwritten at the top right, but not majority.
> Check 3: FAX TRANSMISSION SHEET. No.
> Check 4: questionnaire. No.
> Check 5: resume. No.
> Check 6: scientific_publication. No journal running head.
> Check 7: financial document. No, it's advertising study results, not a bill or budget.
> Check 8: specification. No.
> Check 9: presentation. No, it's a memo with tables.
> Check 10: administrative form. No, it's a memo with data tables.
> Check 11: CORRESPONDENCE -> email, memo, or letter.
> It has:
> TO: Mr. G. C. Pennell
> FROM: T. F. Witner
> SUBJECT: MAGNA Advertising Study Results
> Date: October 21, 1993
> This is a classic memo header. Followed by prose.
> So it's a memo.
> 
> Let's double check.
> Is there an email header? No.
> Is it a letter? No external address, no "Dear ...", no closing signature.
> It's a memo.
> 
> Check 12: news_article. No.
> Check 13: scientific_report. No, it's a memo reporting on a study.
> Check 14: advertisement. No.
> 
> So the label is memo.
> 
> Let's write the scratchpad.
> Pre-scan:
> - Mail-client header: none. "TO:", "FROM:", "SUBJECT:" are memo headers, not email headers (From/To/Sent/Subject with email addresses, or forwarded trail). Wait, email headers are From/To/Sent/Subject. This has TO:/FROM:/SUBJECT:/DATE:. This is a memo header.
> - Masthead/running head: "RJR CONFIDENTIAL" at the top. Not a newspaper/magazine masthead. No journal running head.
> 
> Check 1: file_folder. Evidence: none. Page has extensive body content, tables, and prose. not this check.
> Check 2: handwritten. Evidence: none. Mostly typed text with a small handwritten annotation at the top right. not this check.
> Check 3: FAX TRANSMISSION SHEET. Evidence: none. not this check.
> Check 4: questionnaire. Evidence: none. not this check.
> Check 5: resume. Evidence: none. not this check.
> Check 6: scientific_publication. Evidence: none. No journal name/volume/issue/page number on the page itself. not this check.
> Check 7: financial document. Evidence: none. No line-item billing, ledger, or budget tracking. not this check.
> Check 8: specification. Evidence: none. No MSDS, product formulation, or "shall/must" language. not this check.
> Check 9: presentation. Evidence: none. Dense prose and tables, not sparse slide layout. not this check.
> Check 10: administrative form. Evidence: none. Not a structured form with fields/boxes for data capture. not this check.
> Check 11: CORRESPONDENCE -> memo. Evidence: "TO: Mr. G. C. Pennell", "FROM: T. F. Witner", "SUBJECT: MAGNA Advertising Study Results", "October 21, 1993", followed by memo-style prose. This is a memo.
> Stop here.
> 
> Runner-up: scientific_report, ruled out because the page has a memo header (TO:/FROM:/SUBJECT:) and is an internal transmittal of study results, not an original research write-up with running narrative prose as its primary structure (it's a memo summarizing results). Or maybe form, ruled out because it's a memo. Let's say scientific_report, ruled out because the primary structure is a memo header + prose summarizing a study, not an original research write-up.
> 
> Wait, is there any other check?
> Check 11 is memo.
> 
> Final label: memo.
> Let's review the memo definition: "internal "TO:/FROM:/RE:/SUBJECT:/DATE:" header block followed directly by memo-style prose (no external address, no "Dear ..." salutation)."
> Matches perfectly.
> 
> Scratchpad:
> file_folder: no — the page has extensive body content, tables, and prose, not just an identifier/stamp.
> handwritten: no — mostly typed text with a small handwritten annotation at the top right.
> fax: no — no FACSIMILE header or fax transmission sheet layout.
> questionnaire: no — does not ask the reader to answer or rate.
> resume: no — not a career history.
> scientific_publication: no — no journal running head, volume, or issue on the page.
> financial_document: no — no billing, ledger, or budget tracking structure.
> specification: no — no MSDS, product formulation, or requirement language.
> presentation: no — dense prose and tables, not sparse slide layout.
> form: no — not a structured form with fields/boxes for data capture.
> memo: yes — "TO: Mr. G. C. Pennell", "FROM: T. F. Witner", "SUBJECT: MAGNA Advertising Study Results", "October 21, 1993", followed by memo-style prose.
> news_article: no — no newspaper/magazine masthead or multi-column news typography.
> scientific_report: no — it is an internal memo summarizing study results, not an original research write-up.
> advertisement: no — not a marketing layout.
> 
> Runner-up: scientific_report, ruled out because the page's primary structure is a memo header (TO:/FROM:/SUBJECT:) followed by a summary of results, not an original research manuscript with objectives/methods/results prose.
> 
> Looks solid.
> I will output the scratchpad and the label.

---

### `rvl_cdip__letter__0010.png`
**Expected:** `letter` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow a specific scratchpad procedure, checking 1-14 in order.
> 
> **Document Analysis:**
> - Top right: "January 21, 1985"
> - Header block:
>   - TO: Mr. Alan R. Cox
>   - FROM: Susan C. Nassar
>   - SUBJECT: Marlboro Offensive--Idea Generation
> - Body text: "This summarizes what I would recommend as ideas for qualitative follow-up..."
> - Bottom right: "50461 4652" (Bates number)
> 
> **Pre-scan:**
> - Mail-client header block? No. "TO:", "FROM:", "SUBJECT:" are present, but this is a standard memo header, not an email client header (From:/To:/Sent:/Subject:/cc). Wait, let's check check 11. "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". This is a memo.
> - Masthead/running head? No.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: No, there is a full memo with body text.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: No, it's typed text.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No, it's a memo summarizing ideas.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal masthead or running head.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: No financial tables or billing.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No.
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: No.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: No.
> - Not this check.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - Evidence: "TO: Mr. Alan R. Cox", "FROM: Susan C. Nassar", "SUBJECT: Marlboro Offensive--Idea Generation", date "January 21, 1985". Followed by memo-style prose. This is a memo.
> - Stop here.
> 
> **Check 12-14:** Not evaluated.
> 
> Runner-up: letter. Ruled out because it lacks an external recipient address, "Dear..." salutation, and closing signature; it has an internal TO/FROM/SUBJECT header block.
> 
> Final label: memo.

---

## scientific_report → form (5 errors)

### `rvl_cdip__scientific_report__0008.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: "INBIFO Institut für biologische Forschung · Köln", "17.Okt.89 NDA/MWO QA3145.WM". This looks like an internal document header, not a journal masthead. "BLATT-NR.: 1 von 2". No journal name/volume/issue.
> 
> **Check 1: file_folder**
> - Evidence: Has a title "TITEL: Biological Activity of Formaldehyde and Acrolein...", a table, approval blocks. Not just an identifier.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed text, some handwritten signatures/dates ("21.Sep.89", "19.Okt.89"). Not majority handwritten.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Result: not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: Not a survey instrument.
> - Result: not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: Not a resume.
> - Result: not this check.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - Evidence: No journal name/volume/issue/page number on the page itself. "INBIFO Institut für biologische Forschung" is an institute, not a journal.
> - Result: not this check.
> 
> **Check 7: FINANCIAL DOCUMENT**
> - Evidence: No financial content (invoice, budget).
> - Result: not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
> - Evidence: Not a material safety data sheet, product formulation, or test-analysis table keyed to product codes with "shall/must". It's a QA review.
> - Result: not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
> - Evidence: Not a slide deck or press release.
> - Result: not this check.
> 
> **Check 10: ADMINISTRATIVE FORM**
> - Evidence: "ÜBERPRÜFUNG DURCH QA-UNIT" (Review by QA unit). Table with "ÜBERPRÜFTER PARAMETER" (Reviewed parameter) and "BEANSTANDUNG" (Objection/Comment). "STELLUNGNAHME" (Statement/Comment). "KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER: HHM". "VERTEILER: UHA, HHM, QA, RM-BRT". This is a QA/parameter review sheet or an internal authorization/approval form capturing factual data (parameters reviewed, objections, signatures).
> - Let's check the definition: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... a QA/parameter review sheet."
> - Yes, this is a QA review sheet / form.
> - Result: form.
> 
> **Check 11: CORRESPONDENCE**
> - Evidence: Not an email, memo, or letter. It's a form.
> - Result: not this check (stopped at 10).
> 
> **Check 12: PUBLISHED JOURNALISM**
> - Evidence: Not news.
> - Result: not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
> - Evidence: Not running narrative prose. It's a structured table with field labels.
> - Result: not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL**
> - Evidence: Not an ad.
> - Result: not this check.
> 
> Let's double check Check 10 vs Check 13.
> Check 13 requires "Running narrative prose with objectives, methods, results, or discussion". This page has a table with "ÜBERPRÜFTER PARAMETER" and "BEANSTANDUNG", and some text like "einige Unterschiede zwischen der Chronology des Integrating und der der Subprotocols". This is a QA review sheet. Check 10 explicitly mentions "a QA/parameter review sheet".
> Also, "internal authorization/approval forms with an approval signature/date block" are forms. This has "KENNTNISNAHME DURCH GM: UHA DATUM/ZN", "KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER: HHM".
> 
> So it's a form.
> 
> Let's review the evidence for Check 10:
> - "ÜBERPRÜFUNG DURCH QA-UNIT"
> - Table with headers "ÜBERPRÜFTER PARAMETER", "BEANSTANDUNG"
> - "STELLUNGNAHME" box
> - Approval/signature blocks: "KENNTNISNAHME DURCH GM: UHA", "KENNTNISNAHME/STELLUNGNAHME DURCH PROJEKTLEITER: HHM"
> - "VERTEILER: UHA, HHM, QA, RM-BRT"
> 
> This perfectly matches "administrative form" -> "form".
> 
> Runner-up: scientific_report. Ruled out because the page is a structured QA review sheet with labeled fields and a table, not running narrative prose (check 13 requires running prose, and check 10 explicitly covers QA/parameter review sheets).
> 
> Final label: form.

---

### `rvl_cdip__scientific_report__0011.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking each condition in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: There is a page number "17" at the bottom, and a Bates number "2074406831" rotated on the right side. No journal masthead.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a title "Exposure to Biological Contaminants...", PI info, contract details, budget numbers, report due dates, status. It has real content.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: The text is typed. There is no majority handwriting.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header. The Bates number is rotated, but no fax transmission header like "SENT BY:".
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions, rating scales, or transmittal note for a survey.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a CV or resume.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range (except page 17 at bottom, but no journal header), DOI, or copyright line belonging to a journal.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: The page contains a "Budget" line with amounts "$100,800", "$124,800", "$87,600". It has "Budget Amendment", report due dates, site visits, continuation approved, final report due, and "STATUS: MARCH, 1996".
> - Let's look closely at Check 7: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking."
> - Wait, is this a budget or a form? Or a scientific report?
> - Let's check Check 13: "ORIGINAL RESEARCH WRITE-UP -> scientific_report". "Also scientific_report: ... a technical/project status report whose content is primarily technical — a project description, a technical approach, and research/monitoring activity prose — even when it embeds a budget-vs-actual cost section (see check 7)."
> - The page has a paragraph: "The research team will investigate the role of mold and bacterial components in the development of respiratory allergy and asthma in a cohort of 800 high-risk children. Te investigators will look at the relationship between home characteristics and microbial exposure during the first year of life." This is technical/prose content.
> - Then it has contract details, budget numbers, report due dates, site visits, continuation approved, final report due. This looks like a project status report or a grant tracking sheet.
> - Wait, Check 10: "ADMINISTRATIVE FORM -> form". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application (research grant, employment, service request); a records-management inventory or log table... internal authorization/approval forms with an approval signature/date block."
> - This page has labeled fields: "Contract No.", "Contract Execution Date", "Contract End Date", "No Cost Extension", "Budget", "Budget Amendment", "Five month report due", "Five month report rec.", "Site visit (anticipated)", "Site visit (conducted)", "Ten month report due", "Ten month report rec.", "Continuation approved", "Final report due", "Final report rec.", "STATUS: MARCH, 1996".
> - Is it a form or a scientific_report?
> - Check 13 says: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
> - This page has a short paragraph of running prose at the top, but the majority of the page is labeled field-value entries (Contract No, dates, budget amounts, report due dates, site visits, status).
> - Wait, Check 7 says: "A technical/project status report whose content is primarily technical (project description, technical approach, research activity prose) is scientific_report (check 13), even if it embeds a budget-vs-actual COSTS section". But here, the budget is just a line item "$100,800 $124,800 $87,600". The primary content is the tracking of report due dates, site visits, and status.
> - Let's re-read Check 10: "A research grant application with structured section headings... stays form... Likewise, a QA/parameter review sheet... stays form". This looks like a grant tracking sheet or a project status form. It has fields for "Five month report due", "Five month report rec.", "Site visit", "Continuation approved", "Final report due", "STATUS". This is a form capturing factual data about the project's progress and budget.
> - Let's check Check 7 again: "budget: ... a status report whose PRIMARY content is budget and spend tracking." Here, the primary content is not just budget, it's project milestones (report due, site visit, continuation, final report).
> - Is it a form? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms". The page has ruled lines separating the fields. It's a structured data capture page for a grant/contract.
> - Let's look at the labels: form, scientific_report, budget.
> - The page has a title "Exposure to Biological Contaminants...", PI, a short description, then a table-like structure with Contract No, dates, Budget, report due dates, site visits, status.
> - This is a filled form (a grant tracking form or project status form). The fields are filled with typed text/numbers.
> - Let's check if it's a scientific_report. "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report." The page has a short paragraph, but the bulk is field-value entries. The paragraph is just the project description. The rest is a form tracking the contract.
> - Therefore, it's a form.
> 
> Let's double check Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application (research grant, employment, service request)... internal authorization/approval forms with an approval signature/date block."
> This page has ruled entry lines (horizontal lines separating the rows). It captures factual data: Contract No, dates, budget amounts, report due dates, site visit status, continuation status, final report status, overall status. This is a filled form.
> 
> Let's check if it could be budget. "budget: ... a status report whose PRIMARY content is budget and spend tracking." The primary content is not budget tracking, it's project milestone tracking (report due, site visit, continuation, final report). The budget is just one line.
> 
> Let's check if it could be scientific_report. "Requires running prose... a page that is only labeled field-value entries ... is a filled form". The page is mostly labeled field-value entries.
> 
> So the label is `form`.
> 
> Let's review the evidence for `form`:
> - Ruled entry lines separating fields.
> - Labeled fields: "Contract No.", "Contract Execution Date", "Contract End Date", "Budget", "Budget Amendment", "Five month report due", "Five month report rec.", "Site visit (anticipated)", "Site visit (conducted)", "Ten month report due", "Ten month report rec.", "Continuation approved", "Final report due", "Final report rec.", "STATUS:".
> - Filled with factual data (dates, amounts, "MARCH, 1996").
> 
> Runner-up: scientific_report. Ruled out because the page is primarily a structured set of labeled field-value entries with ruled lines for capturing project/budget tracking data, not running narrative prose (check 13 requires running prose, and explicitly states that pages with only labeled field-value entries are forms).
> Another runner-up: budget. Ruled out because the primary content is project milestone tracking (report due dates, site visits, continuation status), not primarily budget and spend tracking (check 7).
> 
> Wait, the prompt says: "A research grant application with structured section headings (e.g. Investigator, Objectives, Methods) that are field labels for the applicant to fill in — not continuous narrative sentences — stays form (this check), not scientific_report". This is a grant tracking form, which is similar.
> 
> Let's confirm the layout:
> Title: Exposure to Biological Contaminants...
> PI: Bert Brumkreef...
> Paragraph: The research team will investigate...
> Table/Form:
> Contract No. 96-02
> Contract Execution Date 3/1/96
> Contract End Date 3/1/97
> No Cost Extension
> Budget $100,800 $124,800 $87,600
> Budget Amendment
> [ruled line]
> Five month report due 8/1/96
> Five month report rec.
> [ruled line]
> Site visit (anticipated)
> Site visit (conducted)
> [ruled line]
> Ten month report due 1/1/97
> Ten month report rec.
> Continuation approved
> [ruled line]
> Final report due
> Final report rec.
> [ruled line]
> STATUS: MARCH, 1996
> 
> This is clearly a filled form (a contract/grant tracking form).
> 
> Final check of the steps:
> 1. file_folder: no, has content.
> 2. handwritten: no, typed.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. invoice/budget: no, not primarily financial structure, just a line item in a tracking form.
> 8. specification: no.
> 9. presentation: no.
> 10. form: yes, filled fields, ruled lines, capturing factual data.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no, lacks running prose, mostly field-value entries.
> 14. advertisement: no.
> 
> Label: form.

---

### `rvl_cdip__scientific_report__0012.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "2050056147" on the right side.
> 
> **Check 1: file_folder**
> - Evidence: The page has a lot of content: tables, headings like "B L PLANT ANALYTICAL SUMMARY SHEET", "BURLEY", "PRODUCTION DUST", "SLURRY", "FINISHED PRODUCT CHEMICAL ANALYSIS", "FINISHED PRODUCT % OV TARGET", "HOGSHEAD REPORT". It has filled data. Not file_folder.
> 
> **Check 2: handwritten**
> - Evidence: Most content is filled by hand, but it is filling in printed fields, boxes, and tables. The printed structure is dominant (labeled fields, boxes, ruled lines). Not handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or "FAX COVER SHEET" header. Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: Not a survey instrument. Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a resume. Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range, DOI, or copyright line belonging to a journal. Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: No financial line-item table, ledger, statement, voucher, or check face. The numbers are analytical data (averages, S.D., percentages, counts), not money. Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No Material Safety Data Sheet, product formulation, manufacturing-change authorization, or "shall/must" language. Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck, cover, or statement. Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: "B L PLANT ANALYTICAL SUMMARY SHEET". Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data. Tables with rows (C, A, B) and columns (AVERAGE / S.D., etc.). "FINISHED PRODUCT CHEMICAL ANALYSIS" with target values and shift averages. "HOGSHEAD REPORT" with gross, refeed, actual, out of spec & reason. This is a filled analytical or lab data sheet / QA/parameter review sheet / data capture form. "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) is a form". This matches perfectly.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - Evidence: No TO:/FROM:/RE: header, no salutation, no closing. Not this check.
> 
> **Check 12: PUBLISHED JOURNALISM -> news_article**
> - Evidence: No masthead, byline, dateline. Not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - Evidence: No running narrative prose. It's a structured data sheet. Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
> - Evidence: No marketing layout. Not this check.
> 
> Conclusion: Check 10 (form) is the correct match. The page is a filled analytical summary sheet with tables and fields for capturing factual data.
> 
> Runner-up: scientific_report, ruled out because the page lacks running narrative prose and is primarily a structured data capture sheet (form).
> 
> Let's double check check 10 description: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) is a form". The page is "B L PLANT ANALYTICAL SUMMARY SHEET" with filled tables. Matches perfectly.
> Also: "internal authorization/approval forms with an approval signature/date block" - not exactly this, but "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data" definitely applies.
> 
> Final label: form.

---

### `rvl_cdip__scientific_report__0002.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** No "From/To/Sent/Subject" block. There is a "DRSP/NO NO69 (DIV) B27" and "4.JUL.84" at the top right, but it looks like a fax or internal routing stamp, not a mail client header. Wait, let's look closer. "4.JUL.84 DRSP/NO NO69 (DIV) B27". This looks like a fax transmission header or internal routing. "SENT BY:" is not explicitly there, but "DRSP/NO" might be a routing code. Wait, let's look at the top right. "INBIFO" logo. "4.JUL.84 DRSP/NO NO69 (DIV) B27". There is a handwritten "DRHA 4. Juli 1984". This looks like a fax cover or internal routing, but let's check the content.
> - **Masthead/Running head:** "INBIFO Institut für biologische Forschung · Köln". This is a company/institute name, not a journal masthead. No volume/issue/page number for a journal.
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder**
>     *   Content: "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215". There is a table with "RESPONSIBILITY (a)", "DATE", "SIGN", "PROJECT NO. -/1215". Signatures for "Study Director" and "Quality Assurance". Remarks and Distribution text. Footer text. This is a full page of content, not just an ID/stamp. Not file_folder.
> 
> *   **Check 2: handwritten**
>     *   Content: Mostly typed text. Handwritten signatures and dates ("4. Jul. 84", "04. JUNI 1984", "4. Juli 1984"). Not majority handwritten. Not handwritten.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Header: "INBIFO Institut für biologische Forschung · Köln". Top right: "4.JUL.84 DRSP/NO NO69 (DIV) B27". This looks like a fax transmission header or internal routing code, but not a standard "FACSIMILE TRANSMISSION" cover sheet. Wait, let's look at the structure. It has a title "MONTHLY REPORT...". It's a report cover page. Not a fax cover sheet.
> 
> *   **Check 4: questionnaire**
>     *   No survey questions. Not questionnaire.
> 
> *   **Check 5: resume**
>     *   No career history. Not resume.
> 
> *   **Check 6: scientific_publication**
>     *   No journal running head/volume/issue. "INBIFO" is an institute. Not a publication.
> 
> *   **Check 7: financial document (invoice/budget)**
>     *   "MONTHLY REPORT ANALYTICAL CHEMISTRY". No financial tables, invoices, or budgets. Not financial.
> 
> *   **Check 8: specification**
>     *   No material safety data, product formulation, or "shall/must" language. Not specification.
> 
> *   **Check 9: presentation**
>     *   Not a slide deck. Not a press release. Not a speech. Not a photographic slide.
> 
> *   **Check 10: administrative form**
>     *   There is a table with "RESPONSIBILITY (a)", "DATE", "SIGN". Signatures for "Study Director" and "Quality Assurance". "Remarks: This page is not to be transmitted to the client." "Distribution: Original into file of AC Copies into files of GM and QA".
>     *   Wait, is this a form? It's a cover page for a report. "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215".
>     *   Let's check Check 13: scientific_report.
> 
> *   **Check 11: correspondence (email/memo/letter)**
>     *   Top left: "DR. W. FINK PME RESEARCH LABORATORIES CH-2003 NEUCHATEL". This is an address.
>     *   Top right: "4.JUL.84 DRSP/NO NO69 (DIV) B27".
>     *   Title: "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215".
>     *   This looks like a cover page for a report sent to a client (Dr. W. Fink).
>     *   Is it a memo? No TO:/FROM:/RE: block in memo style. It has an address block.
>     *   Is it a letter? No "Dear..." salutation, no closing signature (just approval signatures).
>     *   Is it an email? No mail client header. The top right looks like a fax header ("4.JUL.84 DRSP/NO..."), but the instructions say "A FAX machine transmission header... is NOT a mail-client header... classify the underlying document by its own content". The underlying document is a "MONTHLY REPORT".
> 
> *   **Check 12: news_article**
>     *   No masthead, byline, dateline. Not news.
> 
> *   **Check 13: scientific_report**
>     *   Title: "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215".
>     *   Footer: "(a) The responsibility includes, that in this report any information, that would be unexpected for the sponsor, is given with a special explanation or comment."
>     *   This is a cover page for a "MONTHLY REPORT".
>     *   Wait, is this page *just* the cover page? Yes.
>     *   Check 13 says: "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9); and a technical/project status report whose content is primarily technical..."
>     *   This page is the title/cover page of a "MONTHLY REPORT".
>     *   Let's re-read Check 9: "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. 'TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966' — is scientific_report (check 13), not presentation".
>     *   Here we have "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215". This is a title page for a report.
>     *   However, the page itself is mostly a form-like approval block (Responsibility, Date, Sign, Study Director, Quality Assurance).
>     *   Let's look at Check 10: "administrative form -> form". "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
>     *   This page has: "RESPONSIBILITY (a) DATE SIGN", "PROJECT NO. -/1215", "Study Director: [signature] [date]", "Quality Assurance: [date] [signature]".
>     *   This is an approval page / cover sheet for a report.
>     *   Is it a form? Check 10: "internal authorization/approval forms with an approval signature/date block."
>     *   But Check 13 says: "scientific_report... a technical-study title page...".
>     *   Wait, the instructions say: "Once an earlier check matches, later checks do not override it."
>     *   Let's check the order.
>     *   Check 10 comes before Check 13.
>     *   Check 10: "administrative form -> form". "Filled or blank fields... internal authorization/approval forms with an approval signature/date block."
>     *   This page is essentially an approval sheet / cover page for a monthly report. It has fields for Responsibility, Date, Sign, Project No, Study Director, Quality Assurance.
>     *   Is it a form? Yes, it captures approval data.
>     *   BUT, look at the content: "MONTHLY REPORT ANALYTICAL CHEMISTRY...". It's the cover of a report.
>     *   Let's look at the "Runner-up" logic. If I classify as form, the runner-up is scientific_report.
>     *   Let's look at Check 13 again. "Original research write-up -> scientific_report". "Running narrative prose...". This page has NO running narrative prose. It has a title, an address, a table for signatures, remarks, distribution, and a footnote.
>     *   Check 13 requires "Running narrative prose". This page does not have it. So it's not a scientific_report *text*, but is it a scientific_report *document*?
>     *   "Also scientific_report: ... a technical-study title page naming a specific experimental method/study...". This page names "MONTHLY REPORT ANALYTICAL CHEMISTRY". It doesn't name a specific experimental method/study in the title like the example. It's a monthly report cover.
>     *   Let's look at Check 10 again. "administrative form". "internal authorization/approval forms with an approval signature/date block." This page is exactly that: an approval block for a report. "Study Director", "Quality Assurance".
>     *   Wait, is this a "form"? A form captures data. This captures approval.
>     *   Let's look at the pre-scan instructions: "A page full of technical data can still be a form... but a bill is a bill even when it is printed on a form."
>     *   Here, the page is a cover/approval page for a report.
>     *   Let's look at Check 9: "presentation". "A near-blank cover or title page... is a presentation". This page is not near-blank. It has a table, signatures, remarks, distribution, footer.
>     *   Let's look at Check 11: "correspondence". Addressed to Dr. W. Fink. But no salutation/closing. It's a cover sheet.
>     *   Let's look at Check 10 vs Check 13.
>     *   Check 10: "administrative form". "internal authorization/approval forms with an approval signature/date block." This fits perfectly. The page is an approval sheet (Responsibility, Date, Sign, Study Director, QA).
>     *   Check 13: "scientific_report". Requires running narrative prose. This page has none. The footnote is a legal disclaimer. The remarks are a standard note.
>     *   So Check 10 seems to fit best. "internal authorization/approval forms with an approval signature/date block."
> 
>     *   Wait, let's re-evaluate Check 13. "Also scientific_report: ... a technical-study title page naming a specific experimental method/study (see check 9)". The example in check 9 is "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter...". This page is "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215". This is a title page for a report.
>     *   However, Check 10 is earlier. "administrative form -> form".
>     *   Does Check 10 override Check 13? Yes, "Once an earlier check matches, later checks do not override it."
>     *   Does Check 10 match? "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
>     *   The page has:
>         *   Table: RESPONSIBILITY (a) | DATE | SIGN | PROJECT NO. -/1215
>         *   Study Director: [signature] [date]
>         *   Quality Assurance: [date] [signature]
>     *   This is an approval form / cover sheet.
>     *   Is it a "form"? Yes.
> 
>     *   Let's check if there's any other category.
>     *   What about "scientific_report"? The document *is* a monthly report (scientific/technical), but this specific page is the approval/cover page.
>     *   The instructions say: "Judge each page by its FUNCTION". The function of this page is to authorize/approve the report (Study Director, QA signatures).
>     *   "internal authorization/approval forms with an approval signature/date block" -> form (Check 10).
> 
>     *   Let's look at the "Runner-up" requirement. "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
>     *   If I pick "form", the runner-up is "scientific_report". Why ruled out? Because the page lacks running narrative prose required for scientific_report (Check 13), and instead is an approval/cover sheet with signature blocks (Check 10). Or because it's a title page but Check 10 (form) comes first and matches the approval block structure.
>     *   Actually, let's look at Check 9: "Technical-study title pages... is scientific_report (check 13), not presentation". This page is a title page for a "MONTHLY REPORT". Is it a technical-study title page? "MONTHLY REPORT ANALYTICAL CHEMISTRY". It's a report title page.
>     *   But Check 10 is before Check 9 and Check 13.
>     *   Check 10: "administrative form". "internal authorization/approval forms with an approval signature/date block."
>     *   The page has "Study Director" and "Quality Assurance" with signatures and dates. This is an approval block.
>     *   So Check 10 matches.
> 
>     *   Wait, is this a "memo"?
>     *   Check 11: "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
>     *   This page has an address block (Dr. W. Fink...), but no TO/FROM/RE header block followed by prose. It has a title "MONTHLY REPORT...". Not a memo.
> 
>     *   Is this a "letter"?
>     *   Check 11: "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature".
>     *   No salutation, no prose body, no closing signature (only approval signatures). Not a letter.
> 
>     *   So it's between "form" (Check 10) and "scientific_report" (Check 13).
>     *   Check 10 is earlier.
>     *   Evidence for Check 10: "RESPONSIBILITY (a) DATE SIGN", "Study Director:", "Quality Assurance:", with handwritten dates and signatures. This is an internal authorization/approval form.
>     *   Evidence against Check 13: No running narrative prose. The page is a cover/approval sheet.
> 
>     *   Wait, let's look at the content again.
>     *   "MONTHLY REPORT ANALYTICAL CHEMISTRY, JUNE 1984 PROJECT A 0268/1215".
>     *   This is the cover page of a report.
>     *   Often, cover pages of reports are classified as the report type if they are the main content. But here, the page is *dominated* by the approval block.
>     *   "internal authorization/approval forms with an approval signature/date block" -> form.
>     *   The page is essentially a signature page for the report.
>     *   Let's check the definition of "form" again. "Filled or blank fields... internal authorization/approval forms with an approval signature/date block."
>     *   This fits perfectly.
> 
>     *   Let's check "scientific_report" definition again. "Running narrative prose...". This page has no running narrative prose. Just a title, address, table, remarks, distribution, footnote.
>     *   So it cannot be scientific_report based on the prose requirement.
>     *   Unless it's a "technical-study title page". Check 13: "Also scientific_report: ... a technical-study title page naming a specific experimental method/study".
>     *   "MONTHLY REPORT ANALYTICAL CHEMISTRY" is not naming a specific experimental method/study like "Determination And Reporting Of Total Particulate Matter". It's a generic monthly report title.
>     *   So Check 13 doesn't strongly match the "technical-study title page" exception.
>     *   Check 10 matches the "approval form" description.
> 
>     *   Final decision: form.
> 
>     *   Wait, let's look at the top right: "4.JUL.84 DRSP/NO NO69 (DIV) B27". And handwritten "DRHA 4. Juli 1984".
>     *   This looks like a fax transmission or internal routing.
>     *   Pre-scan: "A FAX machine transmission header... is NOT a mail-client header... classify the underlying document by its own content".
>     *   Underlying document content: Approval page for a monthly report.
>     *   Function: Approval/Authorization. -> Form.
> 
>     *   Let's reconsider "scientific_report".
>     *   Sometimes cover pages of reports are classified as scientific_report if the report is the main thing. But the instructions say "Judge each page by its FUNCTION". The function of this page is to get signatures (Study Director, QA).
>     *   "internal authorization/approval forms with an approval signature/date block" -> form.
> 
>     *   Let's check if there is any other possibility.
>     *   "file_folder": No, has content.
>     *   "handwritten": No.
>     *   "invoice/budget": No.
>     *   "specification": No.
>     *   "presentation": No.
>     *   "email/memo/letter": No.
>     *   "news_article": No.
> 
>     *   So it's "form".
> 
>     *   Wait, is "MONTHLY REPORT" a scientific report? Yes. But this page is the approval page.
>     *   Check 10: "administrative form".
>     *   Check 13: "scientific_report".
>     *   Order: 10 comes before 13.
>     *   Evidence for 10: "Study Director:", "Quality Assurance:", signature blocks.
>     *   Evidence against 13: No running prose.
> 
>     *   One detail: "A page whose primary structure is a memo header + prose... stays memo". Not applicable.
>     *   "Money function overrides form layout". Not applicable.
> 
>     *   Conclusion: form.
> 
>     *   Wait, let's look at the footnote: "(a) The responsibility includes, that in this report any information, that would be unexpected for the sponsor, is given with a special explanation or comment."
>     *   This is a standard disclaimer on INBIFO reports.
>     *   The page is the title/cover/approval page of an INBIFO monthly report.
>     *   Since it has the approval block (Study Director, QA), it fits "internal authorization/approval forms".
> 
>     *   Let's refine the scratchpad.
>     *   Check 1 (file_folder): No, has body content (title, table, signatures, remarks).
>     *   Check 2 (handwritten): No, mostly typed, only signatures/dates are handwritten.
>     *   Check 3 (fax): No, top right is routing/fax metadata, not a fax cover sheet header like "FACSIMILE TRANSMISSION". The underlying doc is a report cover.
>     *   Check 4 (questionnaire): No.
>     *   Check 5 (resume): No.
>     *   Check 6 (scientific_publication): No journal identifier.
>     *   Check 7 (financial): No.
>     *   Check 8 (specification): No.
>     *   Check 9 (presentation): No, not a slide deck or near-blank cover (has table, signatures, text). Not a technical-study title page naming a specific method (it's a "MONTHLY REPORT").
>     *   Check 10 (form): Yes. "RESPONSIBILITY (a) DATE SIGN", "Study Director:", "Quality Assurance:" with signatures/dates. This is an internal authorization/approval form.
>     *   Check 11 (correspondence): No, addressed to external person but no salutation/closing/prose. Just a cover sheet.
>     *   Check 12 (news): No.
>     *   Check 13 (scientific_report): No running narrative prose. The page is an approval sheet. (Runner-up).
>     *   Check 14 (advertisement): No.
> 
>     *   Final label: form.

---

### `rvl_cdip__scientific_report__0003.png`
**Expected:** `scientific_report` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. Just a Bates number "81305509" at the bottom right.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Content: "A AND B COMPOUND RESULTS SUMMARY", "FILE NO: A310", "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE", "NREC:", "SEAC:", "TESTING STATUS: ACTIVE 11-06-90", "DECISION TREE: II 11-21-90", "ISS: PENDING 11-06-90", "CHEM ABSTRACTS NUMBER: NA", "FEMA NUMBER: NA", "PH: 5.60 @ 28C", "MUTAGENICITY VEHICLE: DMSO", "IP VEHICLE:", "ORAL VEHICLE: EMUL 12MC; OIL", "IV VEHICLE: INSOLUBLE", "SPECIAL INSTRUCTIONS: FORMS EMULSION IN 12 MC AND IS SOLUBLE IN CORN OIL", "AWESI: PENDING 09-30-91", "ACUTOT RI: ORAL PENDING 09-30-91".
> - This is not identifier-only. It has a title "A AND B COMPOUND RESULTS SUMMARY" and structured data fields. Not file_folder.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Content is typed. Not handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - No fax header. Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Not a survey instrument. Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Not a resume. Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - No journal running head, volume, issue, page range. Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - No financial content. Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - "A AND B COMPOUND RESULTS SUMMARY", "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE". This looks like a data summary sheet for a chemical compound.
> - Wait, check 10 is "ADMINISTRATIVE FORM -> form". "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values); a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)..."
> - This page is titled "A AND B COMPOUND RESULTS SUMMARY" and has fields like NAME, NREC, SEAC, TESTING STATUS, DECISION TREE, ISS, CHEM ABSTRACTS NUMBER, FEMA NUMBER, PH, MUTAGENICITY VEHICLE, IP VEHICLE, ORAL VEHICLE, IV VEHICLE, SPECIAL INSTRUCTIONS, AWESI, ACUTOT RI.
> - This is a filled analytical or lab data sheet / labeled data chart. It captures factual data about a compound.
> - Let's check check 8 again: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or "shall/must" requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification".
> - Is this a product-analysis table or a filled analytical/lab data sheet? It's a summary of results/data for a compound. "A AND B COMPOUND RESULTS SUMMARY". It has fields like "NAME: ...", "TESTING STATUS: ...", "PH: ...". This looks like a form capturing data about a compound, or a specification?
> - Wait, check 10: "a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This is very similar. "A AND B COMPOUND RESULTS SUMMARY" with "NAME: ...", "PH: ...", "VEHICLE: ...". It's a lab data sheet / form.
> - Let's re-read check 8: "test-analysis tables keyed to product/part codes... A titled product-analysis table (e.g., "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" with chemical constituents and measurements) is a specification". This page is "A AND B COMPOUND RESULTS SUMMARY". It's not a table of measurements, it's a list of attributes/statuses for a compound.
> - Let's look at check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... a filled analytical or lab data sheet...". This page has labeled fields (NAME:, NREC:, SEAC:, TESTING STATUS:, etc.) and values filled in. It is capturing factual data about a compound. This fits "form" (check 10).
> 
> Let's check check 9: SLIDE DECK... -> presentation. No.
> Check 10: ADMINISTRATIVE FORM -> form. Yes, filled analytical or lab data sheet with labeled fields (NAME, NREC, SEAC, TESTING STATUS, etc.).
> Check 11: CORRESPONDENCE -> email, memo, or letter. No.
> Check 12: PUBLISHED JOURNALISM -> news_article. No.
> Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report. No running narrative prose. Just labeled fields.
> Check 14: PROMOTIONAL MATERIAL -> advertisement. No.
> 
> Let's double check check 10 vs check 8.
> Check 8: "test-analysis tables keyed to product/part codes... A titled product-analysis table... is a specification". This is not a table of test analysis results (like mainstream smoke analyses). It's a summary sheet with status, vehicles, pH, etc. It's a data capture form for a compound's properties and testing status.
> Check 10: "a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This page is "A AND B COMPOUND RESULTS SUMMARY" with "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE", "PH: 5.60 @ 28C", "MUTAGENICITY VEHICLE: DMSO", etc. It is a filled analytical/lab data sheet.
> 
> Therefore, the label is "form".
> 
> Let's review the evidence for check 10:
> - Labeled fields: "NAME:", "NREC:", "SEAC:", "TESTING STATUS:", "DECISION TREE:", "ISS:", "CHEM ABSTRACTS NUMBER:", "FEMA NUMBER:", "PH:", "MUTAGENICITY VEHICLE:", "IP VEHICLE:", "ORAL VEHICLE:", "IV VEHICLE:", "SPECIAL INSTRUCTIONS:", "AWESI:", "ACUTOT RI:".
> - Values filled in: "BICYCLO[4.4.0]DEC-1-EN-3-ONE", "ACTIVE 11-06-90", "II 11-21-90", "PENDING 11-06-90", "5.60 @ 28C", "DMSO", "EMUL 12MC; OIL", "INSOLUBLE", "FORMS EMULSION IN 12 MC AND IS SOLUBLE IN CORN OIL", "PENDING 09-30-91".
> - This is a filled analytical or lab data sheet capturing factual data.
> 
> Runner-up: specification. Ruled out because it's not a product-analysis table with measurements/constituents, nor does it have "shall/must" language; it's a data capture sheet for compound attributes and testing status.
> 
> Wait, is there any possibility it's a scientific_report? No, no running prose.
> Is it file_folder? No, it has real content (title + data fields).
> 
> Final check of the text:
> "A AND B COMPOUND RESULTS SUMMARY"
> "FILE NO: A310"
> "NAME: BICYCLO[4.4.0]DEC-1-EN-3-ONE"
> ...
> Bates number: 81305509
> 
> This is clearly a form (lab data sheet / compound summary form).
> 
> Label: form.

---

## budget → form (4 errors)

### `rvl_cdip__budget__0005.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking each condition in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a government seal, "RECIPIENT COMMITTEE CAMPAIGN STATEMENT", "Form 420 1985". No newspaper/magazine masthead or journal running head.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: "RECIPIENT COMMITTEE CAMPAIGN STATEMENT", fields for committee name, address, treasurer, etc. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed form with some handwritten entries (dates, names, signatures). Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: Not a survey instrument.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: Not a resume.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name/volume/issue/page number.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "RECIPIENT COMMITTEE CAMPAIGN STATEMENT". It's a campaign finance disclosure form. Not an invoice or budget in the sense of check 7 (line-item table, ledger, statement, voucher, check face, vendor billing, etc.). Wait, is it a budget? No, it's a statement of contributions/expenditures for a campaign committee. Let's look at check 10.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No material safety data sheet, product formulation, etc.
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck or presentation.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: "RECIPIENT COMMITTEE CAMPAIGN STATEMENT", "Form 420 1985". It has fields, boxes, checkboxes, ruled entry lines for capturing factual data (Name of Committee, Address, Name of Treasurer, Date of Election, etc.). It's a government form (California Government Code Sections 84200-84217). This perfectly matches "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application...".
> - This is a form.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - Evidence: Not correspondence.
> - Not this check.
> 
> **Check 12: PUBLISHED JOURNALISM -> news_article**
> - Evidence: Not journalism.
> - Not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - Evidence: Not a research write-up.
> - Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
> - Evidence: Not an ad.
> 
> Let's double check Check 7 vs Check 10.
> Check 7: "invoice: an outside vendor... states charges owed... budget: internal money planning... provider's periodic customer statement". This is a "RECIPIENT COMMITTEE CAMPAIGN STATEMENT" (Government Code Sections 84200-84217). It's a legal disclosure form required by government code. It's not a bill for goods/services, nor an internal budget tracking document. It's an administrative/legal form. Check 10 covers "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data". This is definitely a form.
> 
> Let's review the form content:
> - Header: RECIPIENT COMMITTEE CAMPAIGN STATEMENT (Government Code Sections 84200-84217)
> - Form 420 1985
> - Fields: Statement covers period from [1/1/85] through [3/17/85]. NAME OF COMMITTEE: THE TOBACCO INSTITUTE. ADDRESS... NAME OF TREASURER: Vijo G. Nielsen, Jr...
> - Section II: IS THIS A CONTROLLED COMMITTEE? [ ] YES [X] NO
> - Section III: CANDIDATES OR STATE MEASURE PROPONENTS...
> - Section IV: CANDIDATE(S) OR MEASURE(S)...
> - VERIFICATION section with signature.
> - Bates number at bottom: TCAL0249389.
> 
> This is a standard government form (California campaign finance disclosure). It falls squarely under Check 10: ADMINISTRATIVE FORM -> form.
> 
> Runner-up: budget. Ruled out because it's a legal disclosure statement (form) rather than an internal money planning/tracking document or a vendor bill (check 7).
> 
> Final label: form.

---

### `rvl_cdip__budget__0012.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a "CONFIDENTIAL Missouri Tobacco Litigation Case No. 972-1465" at the bottom, which is a legal stamp. "TIMO 0003608" is a Bates number. "RECEIVED MAY 1 7 1993 ACCOUNTING" is a stamp.
> 
> **Check 1: file_folder**
> - Evidence: The page has a title "CHECKLIST Political Campaign Contribution Requests", body text, filled fields, signatures. It has real content. Not file_folder.
> 
> **Check 2: handwritten**
> - Evidence: Most content is typed. Handwriting fills in fields (signatures, dates, amounts). Not handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or fax header. Not fax.
> 
> **Check 4: questionnaire**
> - Evidence: Not a survey instrument. Not a questionnaire.
> 
> **Check 5: resume**
> - Evidence: Not a resume.
> 
> **Check 6: scientific_publication**
> - Evidence: No journal running head. Not a publication.
> 
> **Check 7: financial document (invoice/budget)**
> - Evidence: Mentions "$250.00", "Account Charged: 1491-7720-0051". But it's a checklist for political campaign contribution requests, tracking the process of sending checks. It's not an invoice or a budget statement. It's an internal authorization/checklist form.
> 
> **Check 8: specification**
> - Evidence: No material safety data, product formulation, or "shall/must" requirement language. Not a specification.
> 
> **Check 9: presentation**
> - Evidence: Not a slide deck, cover, or statement. Not a presentation.
> 
> **Check 10: ADMINISTRATIVE FORM**
> - Evidence: "CHECKLIST Political Campaign Contribution Requests". Filled fields, checkboxes, ruled entry lines, signatures, dates. "Checklist for _ (number) requests from _ (state) totalling $250.00." Sections for Regional Office, State Activities Headquarters, Accounting with checkboxes and signature lines. This is a filled administrative form/checklist for capturing factual data and tracking a process. Matches check 10 perfectly.
> 
> **Check 11: correspondence**
> - Evidence: No TO:/FROM:/RE: memo header followed by prose. No letterhead with external address and salutation. Not correspondence.
> 
> **Check 12: news_article**
> - Evidence: No masthead, byline, dateline. Not news.
> 
> **Check 13: scientific_report**
> - Evidence: No running narrative prose with objectives, methods, results. Not a scientific report.
> 
> **Check 14: advertisement**
> - Evidence: No marketing layout, product imagery, slogans. Not an ad.
> 
> **Conclusion:**
> The document is a filled administrative form/checklist.
> Label: form.
> 
> Let's double check.
> Title: "CHECKLIST Political Campaign Contribution Requests"
> Content: Instructions, filled fields (state, amount, account number), checkboxes, signatures, dates.
> This is clearly a form (check 10).
> 
> Runner-up: memo, ruled out because there is no TO:/FROM:/RE: header followed by memo-style prose; it's a structured checklist with fields and checkboxes.
> Runner-up: budget, ruled out because it's not internal money planning/tracking (like an expense report or budget statement), but rather a procedural checklist for processing contribution requests (though it mentions money, the primary structure is a form/checklist). Actually, check 7 says "internal authorization/approval forms with an approval signature/date block" is a form (check 10), not budget. "an internal expenditure-authorization form... is a form (check 10), not budget". This checklist is an authorization/approval form for political contributions.
> 
> Final label: form.

---

### `rvl_cdip__budget__0013.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "65503 5219" and a notice at the bottom left.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Content: "VARIANCE SHEET", "BRONX & WILLIAMSBURG - LOUISVILLE", "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:", followed by a list of checkboxes and handwritten text "throughout rest of file".
> - This has real content (a variance sheet with checkboxes and handwritten notes). Not file_folder.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Most content is typed (the variance sheet template). Handwriting is just "throughout rest of file" and some checkmarks. Not majority handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - No fax header.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Not a survey instrument.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Not a resume.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - No journal masthead.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - No financial content.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Not a specification.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Wait, let's look at the layout. It's a scanned page with a black border (scan artifact or folder edge?).
> - Let's re-read Check 9 caveats: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ...") — is a presentation (this check), not a form."
> - Wait, this is a "VARIANCE SHEET" for "BRONX & WILLIAMSBURG - LOUISVILLE". It's checking motivations at the time of reproduction.
> - Let's check Check 10: ADMINISTRATIVE FORM -> form.
> - "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
> - This is a "VARIANCE SHEET" with checkboxes and a handwritten entry. It captures factual data about reproduction motivations.
> - Is it a presentation? The caveat says "ARCHIVE LOCATION VARIANCE SHEET" is a presentation. This is a "VARIANCE SHEET" for reproduction motivations.
> - Let's look closely at Check 9: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located... is a presentation". This sheet is stating motivations for reproduction variance, not location.
> - Let's look at Check 10: "administrative form... filled or blank fields, boxes, checkboxes... capturing factual data". This fits perfectly. It's a form used to record data (variance motivations).
> 
> Let's re-evaluate Check 9 vs Check 10.
> The document is titled "VARIANCE SHEET". It has checkboxes:
> ( ) DOCUMENT COPIES ARE IN THE SAME SEQUENCE...
> ( ) DUPLICATE DOCUMENTS APPEARED...
> ( ) PAGE NUMBER(S) MISSING...
> ( ) POOR QUALITY ORIGINAL. (checked)
> ( ) OVERLAY ITEM COULD NOT BE REMOVED...
> ( ) NO DOCUMENTS WERE FOUND WITHIN THE ORIGINAL:
>   ( ) FILE FOLDER.
>   ( ) REMOVE EXPANDABLE FILE.
>   ( ) MANITO FILE.
>   ( ) ENVELOPE.
> ( ) OTHER (SPECIFY) [handwritten: throughout rest of file] (checked)
> 
> This is a form capturing data about reproduction variance. It's an administrative form.
> Wait, let's look at the black border. "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
> The black bar is around the entire page, looking like a scanned folder or a slide mount. But the content is a typed form with checkboxes.
> Actually, the black border looks like the edge of a scanned document, maybe a folder or just a bad scan. The notice at the bottom left says "NOTICE If the file image is less clear than this notice, it is due to the quality of the document being filmed." This is typical of microfilm/film scanning notices.
> The content is a "VARIANCE SHEET".
> Is it a form (Check 10)? Yes, it has checkboxes and fields for capturing data.
> Let's check if there's any other category.
> Check 10: ADMINISTRATIVE FORM -> form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: ... internal authorization/approval forms with an approval signature/date block."
> This is definitely a form.
> 
> Let's double check Check 9 caveat: "a one-page status/location display sheet — a titled sheet stating where a record range or item is located, printed in slide-style layout with a title, a line of reference numbers, and checkbox-style options (e.g. an "ARCHIVE LOCATION VARIANCE SHEET" listing "THE NUMBER (RANGE) 2060574004-2060574012 IS LOCATED: ( ) IN THE AUDIO CABINET ( ) IN THE VIDEO CABINET ( X ) ON THE OVERSIZE SHELF ...") — is a presentation (this check), not a form."
> This sheet is a "VARIANCE SHEET" but it's not a location display sheet. It's a reproduction variance sheet. It captures data about why a variance occurred. It's a form.
> 
> Wait, is there any other check?
> Check 1: file_folder. No, it has content.
> Check 2: handwritten. No.
> Check 3: fax. No.
> Check 4: questionnaire. No.
> Check 5: resume. No.
> Check 6: scientific_publication. No.
> Check 7: financial. No.
> Check 8: specification. No.
> Check 9: presentation. The layout is a standard document scan, not a slide deck. The black border is likely the film frame or scan artifact, but the content is a form. The "ARCHIVE LOCATION VARIANCE SHEET" is a specific example of a presentation, but this is a "VARIANCE SHEET" for reproduction. Wait, the example in Check 9 is "ARCHIVE LOCATION VARIANCE SHEET". This is "VARIANCE SHEET" for "BRONX & WILLIAMSBURG - LOUISVILLE" reproduction. It's similar. But the content is checkboxes for reproduction issues. Is it a form or presentation?
> The rule says: "a one-page status/location display sheet ... is a presentation". This is a status sheet (reproduction status/variance). But it's primarily a form with checkboxes.
> Actually, let's look at the text: "AT THE TIME OF REPRODUCTION THE FOLLOWING MOTIVATIONS WERE MADE:". It's a form to be filled out.
> I will classify it as form (Check 10).
> 
> Let's re-read Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
> This perfectly matches.
> 
> Runner-up: presentation, ruled out because the page is a filled administrative form with checkboxes and handwritten data entry (a variance sheet for reproduction motivations), not a slide deck, cover, or status/location display sheet (the location variance sheet example is specific to locating records, whereas this is recording reproduction issues). Or runner-up: file_folder, ruled out because it has substantial body content (checkboxes and text).
> 
> Let's refine the scratchpad.
> Check 1: file_folder - no, has body content (variance sheet text and checkboxes).
> Check 2: handwritten - no, mostly typed template with minor handwriting.
> Check 3: fax - no.
> Check 4: questionnaire - no.
> Check 5: resume - no.
> Check 6: scientific_publication - no.
> Check 7: financial - no.
> Check 8: specification - no.
> Check 9: presentation - no, not a slide deck, cover, or status/location display sheet (the location variance sheet is a specific exception, but this is a reproduction variance form).
> Check 10: form - yes, "VARIANCE SHEET" with checkboxes and ruled lines for capturing factual data about reproduction motivations, filled with handwriting.
> Runner-up: presentation, ruled out because the document is a standard administrative form with checkboxes and data entry fields, not a slide layout or the specific "archive location variance sheet" exception.
> 
> Final label: form.

---

### `rvl_cdip__budget__0015.png`
**Expected:** `budget` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There is a Bates number "2024140844" rotated on the right side. No journal masthead.
> 
> **Check 1: file_folder**
> - Evidence: The page contains a large table with data ("QUARTERLY CLOSING P/E", "YEAR", "PM", "S&P 400", etc.). It has real content, not just an identifier/stamp.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: The page is entirely typed text and numbers in a table. No handwriting.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" header. The rotated text is a Bates number "2024140844", not a fax transmission header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: No questions, rating scales, or survey items. It's a financial table.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: No biographical info.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - Evidence: No journal name, volume, issue, page range, or DOI on the page itself.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: The table shows "QUARTERLY CLOSING P/E" (Price-to-Earnings ratio), "DISCOUNT TO S&P 400", "S&P 500", "DISCOUNT TO S&P 500", "SHORT-TERM INTEREST". Years from 1980 to 1993. This is financial data, but is it an invoice or budget?
> - Invoice: outside vendor charges. No.
> - Budget: internal money planning, tracking, forecast vs actual, expense reports, statement of account, check face, check/payment register, or status report whose PRIMARY content is budget and spend tracking. Also covers money-only records.
> - Wait, is this a budget? It's a table of P/E ratios and interest rates. It's financial data. Let's look at the remaining categories.
> - Actually, let's look at Check 10: ADMINISTRATIVE FORM.
> - "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form (check 10)".
> - The table has headers: YEAR, PM, S&P 400, DISCOUNT TO S&P 400, S&P 500, DISCOUNT TO S&P 500, SHORT-TERM INTEREST. It's a labeled data chart/table.
> - Let's re-read Check 7: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a table of financial ratios/metrics, not a ledger, statement, voucher, or check face. It's a data table.
> - Let's re-read Check 10: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form (check 10)". This table is a standalone labeled data chart/table.
> - Wait, is there a better fit?
> - Let's check Check 13: scientific_report. "Requires running narrative prose". No prose here.
> - Let's check Check 8: specification. No "shall/must", no material safety data.
> - Let's check Check 9: presentation. No sparse slide layout.
> - Let's check Check 10: form. "A standalone labeled data chart or table ... is a form". This table is exactly that. It captures financial data in a structured table format.
> - Wait, could it be budget? "budget: internal money planning, tracking, or disbursement ... status report whose PRIMARY content is budget and spend tracking." This table is historical P/E ratios and interest rates. It's not really a budget or an invoice. It's a data table.
> - The rule for Check 10 says: "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form (check 10)".
> - Let's verify if there's any other check.
> - Check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But this isn't a billing page.
> - "A provider's periodic customer statement ... is budget, not invoice". This isn't a customer statement.
> - This is a table of market data (P/E ratios, S&P 500, interest rates). It's a labeled data chart/table. Therefore, form.
> 
> Let's double check Check 10 evidence:
> - "QUARTERLY CLOSING P/E" header.
> - Columns: YEAR, PM, S&P 400, DISCOUNT TO S&P 400, S&P 500, DISCOUNT TO S&P 500, SHORT-TERM INTEREST.
> - Rows: 1980-1993, ongoing.
> - This is a standalone labeled data chart/table. It fits Check 10 perfectly.
> 
> Let's review the "form" definition in Check 10:
> "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; ... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: ... a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
> This table is a standalone labeled data chart/table with numeric values.
> 
> Is there any other category?
> - advertisement: no.
> - email: no.
> - invoice: no.
> - letter: no.
> - memo: no.
> - news_article: no.
> - presentation: no.
> - questionnaire: no.
> - resume: no.
> - scientific_publication: no.
> - scientific_report: no (no running prose).
> - specification: no.
> 
> So the label is `form`.
> 
> Let's quickly check if it could be `budget`.
> "budget: internal money planning, tracking, or disbursement ... status report whose PRIMARY content is budget and spend tracking."
> This table tracks P/E ratios and interest rates over years. It's not really budget/spend tracking. It's market data. The rule "standalone labeled data chart or table ... is a form" applies.
> 
> Let's check if it could be `scientific_report`.
> "Requires running narrative prose". There is no prose.
> 
> Let's check if it could be `presentation`.
> "Slide/overhead layouts ... A near-blank cover ... A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> Explicitly stated in Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> 
> So `form` is the correct label.
> 
> Scratchpad:
> - file_folder: no — page has a large data table with headers and rows of numbers, not just an identifier.
> - handwritten: no — entirely typed.
> - fax: no — no fax header, rotated text is a Bates number.
> - questionnaire: no — no survey questions.
> - resume: no.
> - scientific_publication: no — no journal running head.
> - financial (invoice/budget): no — this is a table of market metrics (P/E ratios, S&P indices, interest rates), not a billing document, ledger, or budget tracking sheet. Check 9 explicitly says a standalone chart/table of values is a form.
> - specification: no — no "shall/must" or product formulation.
> - presentation: no — Check 9 explicitly states "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> - form: yes — the page is a standalone labeled data chart/table ("QUARTERLY CLOSING P/E" with columns for YEAR, PM, S&P 400, etc., and rows of numeric values from 1980-1993). Check 10 covers "a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)".
> - correspondence: no.
> - news_article: no.
> - scientific_report: no — no running narrative prose.
> - advertisement: no.
> 
> Runner-up: presentation, ruled out because Check 9 explicitly states "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> Another runner-up: budget, ruled out because the table tracks market metrics (P/E ratios, interest rates) rather than internal budget/spend tracking, and the standalone table rule in Check 10 applies.
> 
> Final label: form.

---

## specification → form (4 errors)

### `rvl_cdip__specification__0006.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "50052 7368" on the right edge. No journal masthead.
> 
> **Check 1: file_folder**
> - Content: The page has typed field labels ("Analytical information (detailed)", "Quantitative (all figures)", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography"). It has a block of text at the bottom describing a patent ("British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE..."). This is not just an identifier/stamp. It's a structured data capture sheet.
> - Not file_folder.
> 
> **Check 2: handwritten**
> - Mostly typed. There is a handwritten word "Goldshield" at the top. Not majority handwritten.
> - Not handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - No fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Not a survey instrument.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Not a resume.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - No journal running head.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - No financial content.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - The bottom text mentions "MATERIAL FOR FILTERING TOBACCO SMOKE - CONTAINING CARBON PARTICLES COATED INTERNALLY - EXTERNALLY WITH POROUS LAYER OF ORGANIC POLYMER." and patent numbers.
> - However, the page itself is a form for capturing analytical information about a substance/material. It has fields for "Analytical information (detailed)", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups", "Derivatives", "Types of Tobacco", "Tox.-Pharm. Inform.", "Reference", "Bibliography".
> - Is it a specification? A specification defines what a product will be. This looks like a data sheet or form for recording analytical data about a material (possibly for a patent or technical file).
> - Let's look at Check 10: ADMINISTRATIVE FORM. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table... a filled analytical or lab data sheet". This page is a blank (mostly) analytical data sheet / form for capturing information about a material.
> - Wait, check 8 says: "test-analysis tables keyed to product/part codes... A titled product-analysis table... is a specification". But this is a form with fields to fill out. "Analytical information (detailed) ... Quantitative ... Qualitative ... Structural Formula ... Mol. Form ...". This is a form for capturing data.
> - Let's re-read check 10: "A filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions) ... is a form". This page is exactly that: a lab data sheet / analytical information form.
> - Let's check check 8 again: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or "shall/must" requirement language." This page doesn't have "shall/must", it's not an MSDS, it's not a product formulation instruction. It's a form to record analytical info.
> - So check 10 is a better fit.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Not a slide deck.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data"
> - "a filled analytical or lab data sheet"
> - The page has fields: "Analytical information (detailed)", "Quantitative (all figures)", "Qualitative only", "Structural Formula", "Mol. Form", "Mol. Weight", "Chem. Groups", "Derivatives", "Types of Tobacco (all details)", "Tox.-Pharm. Inform. and other Notes", "Reference", "Bibliography".
> - It has instructions at the bottom: "If there is not sufficient space available for any of the categories, use reverse side, identifying category(ies), and write "over" on this side. List all answerable information for each constituent and do so in index style."
> - This is clearly a form for capturing analytical/lab data.
> - Matches check 10 perfectly.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - No correspondence structure.
> - Not this check.
> 
> **Check 12: PUBLISHED JOURNALISM -> news_article**
> - No masthead.
> - Not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - No running narrative prose. It's a form with labels.
> - Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
> - Not an ad.
> - Not this check.
> 
> Conclusion: form.
> 
> Let's double check check 8 vs check 10.
> Check 8: "test-analysis tables keyed to product/part codes... A titled product-analysis table (e.g., "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" with chemical constituents and measurements) is a specification".
> This page is not a table of analysis results. It is a blank template/form with field labels for someone to fill in analytical information. The text at the bottom is a reference to a patent ("British American Tobacco Limited... MATERIAL FOR FILTERING TOBACCO SMOKE..."). This looks like a data extraction form or a technical data sheet form used in patent analysis or product development to capture details about a material.
> Check 10 explicitly covers "a filled analytical or lab data sheet". Even if blank, it's a form for capturing data. The instructions "List all answerable information for each constituent..." confirm it's a form to be filled out.
> 
> Therefore, form is the correct label.
> 
> Scratchpad:
> - file_folder: no — page has structured field labels and instructions for capturing analytical data, not just an ID/stamp.
> - handwritten: no — mostly typed, only a small handwritten word "Goldshield" at the top.
> - questionnaire: no — not a survey instrument.
> - scientific_publication: no — no journal running head.
> - specification: no — not a product-change authorization or MSDS; it's a data capture form.
> - form: yes — structured fields ("Analytical information", "Structural Formula", "Mol. Form", etc.) and instructions for filling out analytical/lab data ("List all answerable information for each constituent..."). Matches "analytical or lab data sheet" form.
> - Runner-up: specification, ruled out because the page is a blank data-capture form with field labels and instructions, not a product specification or test-analysis table with results.
> 
> Final label: form.

---

### `rvl_cdip__specification__0013.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None. (There's a date/time at the top left "DATE . FRI, MAR 1, 1985, 8:21 AM" and "PAGE 1 OF 3", but this looks like a fax transmission header or a system printout header, not a mail-client From/To/Sent/Subject block. Wait, let's look closer. "DATE . FRI, MAR 1, 1985, 8:21 AM", "PAGE 1 OF 3". This is typical of a fax transmission header or a computer printout. No "From:", "To:", "Subject:".)
> - Masthead or running head: No newspaper/magazine masthead. No journal running head/volume/issue/page number. There is a Bates number "50512 3457" at the bottom right.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of body content (test number, requested by, test purpose, special instructions, filter making, making & packing, testing). It is not an identifier-only page.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: The page is entirely typed (computer printout/typewriter). No majority handwriting.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: "DATE . FRI, MAR 1, 1985, 8:21 AM", "PAGE 1 OF 3". This is a fax header or system printout, but the document itself is not a "FACSIMILE TRANSMISSION" cover sheet. It's a test request or work order.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: "TEST PURPOSE: CONSUMER SATISFACTION PROGRAM", "TYPE OF PANEL TESTING: CLT". But this is an internal work order/request for a test, not the survey instrument itself or a transmittal note for it.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: None.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "CHARGE NUMBER: 1300". But no line-item table of charges, no budget tracking. It's a test request.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: Mentions "TOBACCO VARIETY C53-44X", "BLEND FORMULATION", "FILTER MAKING", "MAKING & PACKING". But this is instructions for a test/production run, not a Material Safety Data Sheet or product formulation specification document itself. Wait, let's look at Check 10.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck, not a press release, not a speech.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: The page has structured fields: "DATE", "TEST NUMBER", "CHARGE NUMBER", "PRIORITY", "REQUESTED BY", "DATE REQUESTED", "RELATED TEST NUMBER", "DIVISION", "CLASSIFICATION", "TEST PURPOSE", "MAKING AND PACKING DATE", "MAIL OUT DATE", "TYPE OF PANEL TESTING", "SPECIAL INSTRUCTIONS", "TOBACCO PROCESSING", "FILTER MAKING", "MAKING & PACKING", "TESTING". It is a structured form capturing factual data / a work order / test request form. It has labeled fields and filled-in text.
> - Let's verify: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms...". This is a test request form or work order form. It captures data about a test (test number, requested by, purpose, instructions).
> - Is it a specification? "Product-referenced test data is a specification. A titled product-analysis table... is a specification". This is not a product-analysis table. It's a request/instruction sheet for making and testing a product.
> - Is it a form? Yes, it's a structured document with labeled fields (DATE, TEST NUMBER, REQUESTED BY, etc.) and filled-in content. It's an administrative form / work order / test request form.
> 
> Let's re-read Check 10 carefully: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block." This page has labeled fields ("REQUESTED BY:", "TEST PURPOSE:", "SPECIAL INSTRUCTIONS:") and filled-in text. It's a form.
> 
> Let's check if there's any other match.
> Could it be a memo? "REQUESTED BY: WILSON, JOHN (5979)". No TO:/FROM:/RE: header block.
> Could it be a scientific_report? No running narrative prose. It's structured data/instructions.
> 
> Let's review the fields:
> DATE . FRI, MAR 1, 1985, 8:21 AM
> PAGE 1 OF 3
> TEST NUMBER: PD00237
> CHARGE NUMBER: 1300
> PRIORITY:
> REQUESTED BY: WILSON, JOHN (5979)
> DATE REQUESTED: 840705
> RELATED TEST NUMBER:
> DIVISION: 775
> CLASSIFICATION: WINS KS
> TEST PURPOSE: CONSUMER SATISFACTION PROGRAM
> MAKING AND PACKING DATE:
> MAIL OUT DATE:
> TYPE OF PANEL TESTING: CLT
> SPECIAL INSTRUCTIONS:
> TOBACCO PROCESSING: ...
> FILTER MAKING: ...
> MAKING & PACKING: ...
> TESTING: ...
> 
> This is clearly a form (a test request or work order form).
> 
> Let's check Check 8 again: "specification ... manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language." The text says "USE AS DESCRIBED IN BLEND FORMULATION", "PREPARE FILTERS AS DESCRIBED USING CURRENT WIN. KS CONFIGURATION AND SPECS", "DO NOT SAMPLE ON MAKING AND PACKING FLOOR". These are instructions, not a specification document itself. The document is a form capturing the request and instructions for a test.
> 
> Therefore, Check 10 (form) is the best match.
> 
> Let's double check Check 11 (correspondence):
> No mail-client header. No memo header (TO:/FROM:/RE:). No letter structure.
> 
> Let's double check Check 12 (news_article):
> No.
> 
> Let's double check Check 13 (scientific_report):
> No running narrative prose.
> 
> Let's double check Check 14 (advertisement):
> No.
> 
> So the label is `form`.
> 
> Wait, could it be `file_folder`? No, it has real content.
> Could it be `handwritten`? No, it's typed.
> 
> The document is a typed form with labeled fields and filled-in text. It's a test request/work order form.
> Label: form.
> 
> Let's quickly review the "Runner-up" requirement.
> Runner-up: specification, ruled out because the page is a structured request/instruction form with labeled fields (test number, requested by, special instructions) rather than a product-analysis table, MSDS, or product-change authorization defining the product's composition/properties.
> Or runner-up: scientific_report, ruled out because the page lacks running narrative prose and is instead a structured form with labeled fields and filled-in data.
> 
> I will write the scratchpad and output `form`.
> Pre-scan:
> - Mail header: None. "DATE . FRI, MAR 1, 1985, 8:21 AM" and "PAGE 1 OF 3" are fax/system printout headers, not mail-client From/To/Sent/Subject.
> - Masthead: None. Bates number 50512 3457 at bottom right.
> 
> Check 1: file_folder. Evidence: Page has extensive body content (test details, instructions). Not identifier-only.
> Check 2: handwritten. Evidence: Page is entirely typed.
> Check 3: fax transmission sheet. Evidence: No "FACSIMILE TRANSMISSION" cover sheet layout; the top header is just a date/page count, not a fax cover form.
> Check 4: questionnaire. Evidence: Mentions "CONSUMER SATISFACTION PROGRAM", but this is an internal work order/request for a test, not the survey instrument itself.
> Check 5: resume. Evidence: None.
> Check 6: scientific_publication. Evidence: No journal running head, volume, or page range.
> Check 7: financial document. Evidence: "CHARGE NUMBER: 1300" is present, but no line-item billing or budget tracking.
> Check 8: specification. Evidence: Contains instructions ("USE AS DESCRIBED", "PREPARE FILTERS AS DESCRIBED"), but is not a product-analysis table, MSDS, or product-change authorization.
> Check 9: presentation. Evidence: Not a slide deck, press release, or speech.
> Check 10: form. Evidence: Structured document with labeled fields ("TEST NUMBER:", "REQUESTED BY:", "TEST PURPOSE:", "SPECIAL INSTRUCTIONS:") and filled-in text capturing factual data and instructions for a test/work order.
> Check 11: correspondence. Evidence: No mail-client header, no memo TO:/FROM:/RE: block, no letter salutation/closing.
> Check 12: news_article. Evidence: No masthead, byline, or multi-column news typography.
> Check 13: scientific_report. Evidence: No running narrative prose; it is a structured form.
> Check 14: advertisement. Evidence: No marketing layout, product imagery, or slogans.
> 
> Final label: form.
> Runner-up: specification (ruled out because it's a request/instruction form, not a product specification or analysis table) or scientific_report (ruled out because it lacks running prose). I'll use scientific_report as the runner-up.
> Actually, the prompt says "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
> Runner-up: scientific_report, ruled out because the page is a structured form with labeled fields and filled-in data, not running narrative prose.
> Or: specification, ruled out because the page is a test request form with instructions, not a product-analysis table or product-change authorization.
> 
> I'll go with scientific_report as the runner-up.
> "scientific_report: no — the page is a structured form with labeled fields and filled-in data, not running narrative prose."
> Wait, the runner-up line should be: "Runner-up: scientific_report, ruled out because the page is a structured form with labeled fields and filled-in data, not running narrative prose."
> 
> Let's refine the scratchpad text to be concise.
> file_folder: no — the page has extensive body content (test details, instructions), not just an identifier/stamp.
> handwritten: no — the page is entirely typed.
> fax: no — the top header is a date/page count, not a "FACSIMILE TRANSMISSION" cover sheet.
> questionnaire: no — mentions "CONSUMER SATISFACTION PROGRAM", but this is an internal work order, not the survey instrument.
> resume: no — no career history content.
> scientific_publication: no — no journal running head, volume, or page range.
> financial: no — "CHARGE NUMBER" is present, but no billing line items or budget tracking.
> specification: no — contains instructions, but is not a product-analysis table, MSDS, or product-change authorization.
> presentation: no — not a slide deck, press release, or speech.
> form: yes — structured document with labeled fields ("TEST NUMBER:", "REQUESTED BY:", "TEST PURPOSE:", "SPECIAL INSTRUCTIONS:") and filled-in text capturing factual data and instructions.
> correspondence: no — no mail-client header, memo TO:/FROM:/RE: block, or letter structure.
> news_article: no — no masthead, byline, or multi-column news typography.
> scientific_report: no — no running narrative prose; it is a structured form.
> advertisement: no — no marketing layout or product imagery.
> 
> Runner-up: scientific_report, ruled out because the page is a structured form with labeled fields and filled-in data, not running narrative prose.
> 
> Looks solid.
> I will output the final label.

---

### `rvl_cdip__specification__0017.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Fax transmission header: None.
> - Masthead/running head: There is a vertical number "50623 9622" on the right side, which looks like a Bates number. No journal masthead.
> 
> **Check 1: file_folder**
> - Content: Data tables, chamber conditions, analyte data, signature. Not just an identifier/stamp.
> - Result: not this check.
> 
> **Check 2: handwritten**
> - Content: Mostly typed data, tables, and text. There is a signature "D. L. HEAVNER" and a handwritten signature. Not majority handwritten.
> - Result: not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - No fax cover sheet header.
> - Result: not this check.
> 
> **Check 4: questionnaire**
> - Not a survey instrument.
> - Result: not this check.
> 
> **Check 5: resume**
> - Not a career history.
> - Result: not this check.
> 
> **Check 6: scientific_publication**
> - No journal running head, volume, issue, page range, DOI. The "50623 9622" is a Bates number. "ASYST Version 2.00", "Page 1 A:AL116.RPT 11/17/87 16:00:04.59". No journal identifier.
> - Result: not this check.
> 
> **Check 7: FINANCIAL DOCUMENT**
> - No financial content (invoice, budget). It's scientific/technical data (mass, analytes, chamber conditions).
> - Result: not this check.
> 
> **Check 8: specification**
> - Material Safety Data Sheet? No. Product formulation? No. "shall/must"? No.
> - Result: not this check.
> 
> **Check 9: presentation**
> - Not a slide deck, cover, or statement.
> - Result: not this check.
> 
> **Check 10: ADMINISTRATIVE FORM**
> - Filled or blank fields, boxes, checkboxes? It has a table of data, but it's a data output report ("ASYST Version 2.00", "Page 1 A:AL116.RPT"). It's a data summary or analytical data sheet. Wait, check 10 says: "a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This page has "TWO HOUR INTEGRATED AVERAGES(BACKGROUND SUBTRACTED)", "ANALYTE", "TOTAL", "/CIG", and values. It also has "CHAMBER CONDITIONS". It looks like a lab data sheet or analytical data summary. Let's look at check 13.
> 
> **Check 11: CORRESPONDENCE**
> - No email, memo, or letter structure.
> - Result: not this check.
> 
> **Check 12: news_article**
> - No masthead, byline, etc.
> - Result: not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page with authors and an internal affiliation and no journal identifiers. Requires running prose..."
> - Wait, does this page have running prose? It has data tables, chamber conditions, and a note: "NOTE: OK--SUBJ#1 = D. WINGATE , SUBJ #2 = B. HAMLIN". And a signature "D. L. HEAVNER".
> - Let's re-read check 10: "This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet...". This page is exactly a filled analytical or lab data sheet / data output report from a test (CIGARETTE: 2 1R4F SEMS, PORT #, PUFF COUNT, MASS, ANALYTE, etc.).
> - Wait, check 13 says: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" under a contract number with a Principal Investigator line, a grant application's structured section headings, or a QA parameter-review sheet's listed parameters/dates) is a filled form (check 10), not a scientific report."
> - This page is essentially a data output report / analytical data sheet. It has tables of data (PORT #, PUFF COUNT, MASS; ANALYTE, TOTAL, /CIG). It has chamber conditions. It has a signature. It is a lab data sheet / analytical data summary. Therefore, it is a form (check 10).
> - Let's check check 10 again: "a filled analytical or lab data sheet ("ANALYTICAL DATA SUMMARY" with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". This page is a data output from a cigarette analysis (mass consumed, analytes like CO, NOx, NO, NO2, FID, CO2, PIEZO1, RAM-1, CNC). It's a lab data sheet.
> - Is there any running prose? No, just headers, tables, conditions, a note, and a signature.
> - So it's a form (check 10).
> 
> Let's double check check 13: "Requires running prose — a page that is only labeled field-value entries ... is a filled form (check 10), not a scientific report."
> This page has labeled field-value entries (tables, conditions) and no running prose. So it's check 10.
> 
> Let's review the page content:
> - RUN DATE: 23 NOV 87 FILENAME: A:AL116.DAT CIGARETTE: 2 1R4F SEMS
> - Table: PORT #, PUFF COUNT, INITIAL MASS(mg), FINAL MASS(mg), MASS CONSUMED(mg)
> - CHAMBER CONDITIONS: STATIC MODE/100% FANS 72F/50% RH, PRESSURE, TEMPERATURE, PIEZO1 LPM, PIEZO1 SLPM
> - TWO HOUR INTEGRATED AVERAGES(BACKGROUND SUBTRACTED)
> - Table: ANALYTE, TOTAL, /CIG (CO, NOx, NO, NO2, FID, CO2, PIEZO1, RAM-1, CNC)
> - NOTE: OK--SUBJ#1 = D. WINGATE , SUBJ #2 = B. HAMLIN
> - D. L. HEAVNER [signature]
> - 50623 9622 (Bates number)
> - ASYST Version 2.00 Page 1 A:AL116.RPT 11/17/87 16:00:04.59
> 
> This is a data output report / analytical data sheet. It fits "filled analytical or lab data sheet" under check 10.
> 
> Let's check if it could be scientific_report. Check 13 explicitly says: "Requires running prose — a page that is only labeled field-value entries (even an "ANALYTICAL DATA SUMMARY" ... ) is a filled form (check 10), not a scientific report."
> This page is exactly that: labeled field-value entries (tables, conditions). No running prose.
> 
> Therefore, the label is `form`.
> 
> Let's quickly check if there's any other category.
> - advertisement: no
> - budget: no
> - email: no
> - file_folder: no
> - handwritten: no
> - invoice: no
> - letter: no
> - memo: no
> - news_article: no
> - presentation: no
> - questionnaire: no
> - resume: no
> - scientific_publication: no
> - scientific_report: no (no running prose)
> - specification: no (no "shall/must", not an MSDS, not a product change authorization)
> 
> The evidence for form (check 10): "a filled analytical or lab data sheet" with tables of data (PORT #, PUFF COUNT, MASS, ANALYTE, TOTAL, /CIG), chamber conditions, and a signature block. No running prose, so not scientific_report.
> 
> Runner-up: scientific_report, ruled out because the page lacks running narrative prose and consists only of labeled data tables, field-value entries, and a signature (which the instructions explicitly classify as a filled form under check 10).
> 
> Final check of the text:
> "ASYST Version 2.00" - ASYST is a statistical analysis software. This is a report generated by the software. It's a data output.
> Check 10: "This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet..."
> Yes, form.

---

### `rvl_cdip__specification__0019.png`
**Expected:** `specification` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "398015304" at the bottom right. No journal masthead.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: tables with "CASING CROSS-REFERENCE", "BLEND CODE CROSS-REFERENCE", dates, change numbers, active dates, cut tobacco codes, signatures. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed tables. There are two handwritten signatures at the bottom ("Wayne Sandee 9/30/96", "JG Sneed 5/1/98"). Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header. The top right has "04/30/96 16:16", which is a timestamp, not a fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions, rating scales, or transmittal note.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No career history.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: No financial data, invoices, budgets, or money tracking. It's about casing and blend codes for tobacco.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: The page contains "CASING CROSS-REFERENCE" and "BLEND CODE CROSS-REFERENCE". It lists "CUT TOBACCO", "STATUS", "CHANGE NUMBER", "ACTIVE DATE". It has product codes like "CS68XTOB CS68MAP", "Casing: C-407", "Blend: BW-2117". This looks like a technical specification or cross-reference document for product materials (casing, blend codes, cut tobacco). Wait, let's look at check 8 carefully. "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification". This is a cross-reference table for casing and blend codes. Is it a specification? Let's check check 10.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck. Dense tables.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... internal authorization/approval forms with an approval signature/date block."
> - The page has tables: "CASING CROSS-REFERENCE", "BLEND CODE CROSS-REFERENCE". It has columns: "CUT TOBACCO", "STATUS", "CHANGE NUMBER", "ACTIVE DATE". It has handwritten signatures at the bottom ("Wayne Sandee 9/30/96", "JG Sneed 5/1/98"). This looks like an approval or authorization document, or a data table/chart. Wait, check 8 says "test-analysis tables keyed to product/part codes... is a specification". But this is a cross-reference of casing and blend codes. Let's re-read check 8: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
> - This table is keyed to product codes (CS68XTOB, C-407, BW-2117). It shows change numbers and active dates. It's a cross-reference document. Is it a specification or a form?
> - Let's look at the signatures: "Wayne Sandee 9/30/96", "JG Sneed 5/1/98". This implies approval or review.
> - Check 10: "internal authorization/approval forms with an approval signature/date block."
> - Check 8: "manufacturing-change authorization... A titled product-analysis table... is a specification".
> - The document is a "CASING CROSS-REFERENCE" and "BLEND CODE CROSS-REFERENCE". It lists change numbers and active dates. It's essentially a data table / chart. "A standalone labeled data chart or table... is a form (check 10)".
> - Let's consider if it's a specification. Specifications usually have "shall/must" or define properties. This is just a cross-reference of codes, statuses, change numbers, and dates. It's a data table. So it's a form (check 10).
> 
> Let's re-evaluate Check 8 vs Check 10.
> Check 8: "test-analysis tables keyed to product/part codes... A titled product-analysis table... is a specification". This is not a test-analysis table. It's a cross-reference table.
> Check 10: "A standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... internal authorization/approval forms with an approval signature/date block."
> The page has tables with labeled columns (CUT TOBACCO, STATUS, CHANGE NUMBER, ACTIVE DATE) and rows of data. It has approval signatures at the bottom. This fits "standalone labeled data chart or table" and "internal authorization/approval forms with an approval signature/date block". So it's a form.
> 
> Let's check if there's any other category.
> Could it be a scientific_report? No running prose.
> Could it be a memo? No TO/FROM/RE header.
> 
> Let's look closely at the content:
> "CS68XTOB CS68MAP CASING CROSS-REFERENCE 04/30/96 16:16"
> "CASING: C-407"
> Columns: CUT TOBACCO, STATUS, CHANGE NUMBER, ACTIVE DATE.
> Rows: MT-019, MT-082, etc. with descriptions like "CAPRI MENTHOL EXPORT", "CAPRI MENTHOL LTS @ 14.5".
> This is a data table / cross-reference.
> Bottom has signatures: "Wayne Sandee 9/30/96", "JG Sneed 5/1/98".
> This is an approval or review of the cross-reference data.
> Fits Check 10: ADMINISTRATIVE FORM -> form. "Filled or blank fields... standalone labeled data chart or table... internal authorization/approval forms with an approval signature/date block."
> 
> Let's double check Check 8: "manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language."
> This document is a cross-reference of casing and blend codes. It's not really a manufacturing-change authorization (which would describe changes to a product). It's a reference table. The signatures might be for approval of the reference table itself.
> "A standalone labeled data chart or table... is a form (check 10), not a specification."
> Yes, this is a labeled data chart/table.
> 
> Therefore, the label is `form`.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no - has tables and signatures.
> 2. handwritten: no - mostly typed, only signatures at bottom.
> 3. fax: no - no fax header.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial: no.
> 8. specification: no - it's a cross-reference data table, not a test-analysis table or product formulation with "shall/must". It's a labeled data chart/table.
> 9. presentation: no.
> 10. form: yes - standalone labeled data charts/tables ("CASING CROSS-REFERENCE", "BLEND CODE CROSS-REFERENCE") with columns (CUT TOBACCO, STATUS, CHANGE NUMBER, ACTIVE DATE) and rows of data, plus approval signatures at the bottom ("Wayne Sandee 9/30/96", "JG Sneed 5/1/98"). Fits "standalone labeled data chart or table" and "internal authorization/approval forms with an approval signature/date block".
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no - no running prose.
> 14. advertisement: no.
> 
> Runner-up: specification, ruled out because the page is a labeled data chart/table (cross-reference of codes, change numbers, dates) without "shall/must" language or test-analysis data, and check 10 explicitly covers standalone labeled data charts/tables and approval forms with signature blocks.
> 
> Wait, is there any possibility it's a specification?
> "test-analysis tables keyed to product/part codes... is a specification"
> This is not a test-analysis table. It's a cross-reference.
> "A titled product-analysis table... is a specification... But a generic labeled chart or table with no product/material tie-in at all, no requirement language, and no 'shall/must' text is an administrative form (check 10), not a specification."
> This has product tie-in (CS68XTOB, C-407, Capri), but no requirement language, no "shall/must", and it's not a test-analysis table. It's a cross-reference table. So it's a form.
> 
> Final check of the text:
> "CS68XTOB CS68MAP CASING CROSS-REFERENCE"
> "CASING: C-407"
> "CUT TOBACCO ... STATUS ... CHANGE NUMBER ... ACTIVE DATE"
> "MT-019 CAPRI MENTHOL EXPORT... HIST 94-0049 3/18/94"
> This is clearly a data table.
> Signatures at the bottom indicate approval.
> Check 10 covers "standalone labeled data chart or table" and "internal authorization/approval forms with an approval signature/date block".
> 
> Label: form.

---

## invoice → budget (3 errors)

### `rvl_cdip__invoice__0001.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header:** No "From/To/Sent/Subject" visible. There is a "RECEIPT MAIL REGISTE" stamp and a "DATE-IN" stamp. No fax transmission header like "SENT BY: ... # N/N". Wait, let's look closer. "RECEIPT MAIL REGISTE 1174". "DATE-IN 19-DEC-033" (looks like 19-DEC-03 or similar, maybe 19-DEC-1993? No, looks like 19-DEC-033... actually 19-DEC-033 is weird. Let's look at the date in the text: "Brussel, 01/04/1993"). No mail header.
> - **Masthead/Running head:** No newspaper masthead. No journal running head. There is a company name "SLOUGH PROPERTIES N.V." and address details.
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: There is a Bates number "2028741084". There is a "DATE-IN" stamp. There is a "RECEIPT MAIL REGISTE" stamp.
>     *   Content: There is a table on the right side. "Omschrijving", "Periode", "Bedrag". "huur", "01/04/1993 tot 30/06/1993", "669060", "Totaal te betalen", "669060".
>     *   There is a box "REKENING NR. 930058".
>     *   There is address info: "C.R.C. CONTRACT RESEARCH CENTER BVBA TOLLAAN 101 C 1932 - SINT-STEVENS-WOLUWE".
>     *   There is sender info: "SLOUGH PROPERTIES N.V. (Gr INAMOIRE HIRE GAUNTLET N.V. - SA)".
>     *   This is not just an identifier. It has a table of charges. So not file_folder.
> 
> *   **Check 2: handwritten**
>     *   Evidence: Mostly typed text. Some black smudges/blacks out text. No significant handwriting. Not handwritten.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" header. No fax cover sheet layout. Not a fax sheet.
> 
> *   **Check 4: questionnaire**
>     *   Evidence: No survey questions. Not a questionnaire.
> 
> *   **Check 5: resume**
>     *   Evidence: No career history. Not a resume.
> 
> *   **Check 6: scientific_publication**
>     *   Evidence: No journal name/volume/page. Not a publication.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: The page is a bill/invoice.
>     *   "SLOUGH PROPERTIES N.V." is sending a bill to "C.R.C. CONTRACT RESEARCH CENTER BVBA".
>     *   "REKENING NR. 930058" (Account No. 930058).
>     *   Table: "Omschrijving" (Description), "Periode" (Period), "Bedrag" (Amount).
>     *   Row: "huur" (rent), "01/04/1993 tot 30/06/1993", "669060" (likely cents or a specific currency unit, maybe Belgian Francs? 6690.60?). "Totaal te betalen" (Total to pay): "669060".
>     *   This is a billing document for "huur" (rent) for a period.
>     *   Is it an invoice or a budget?
>     *   Invoice definition: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher... a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work... A hotel/motel guest bill... is an invoice".
>     *   Budget definition: "internal money planning... provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T 'MONTHLY INVOICE' for phone service... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold." Wait. Let's re-read carefully.
>     *   "budget: ... ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
>     *   "invoice: ... A hotel/motel guest bill or folio — a statement of charges for a specific stay (room, tax, balance due), often printed on a reservation form with checkboxes and a guest signature — is an invoice: it bills for a one-off service performed (lodging), not a periodic account statement."
>     *   Here we have "huur" (rent) for a period "01/04/1993 tot 30/06/1993". Rent is a periodic charge for an ongoing account (leasing a building/space).
>     *   Wait, let's look at the "invoice" definition again. "an outside vendor... states charges owed... for goods or services SOLD". Rent is a service (leasing).
>     *   Let's look at the "budget" definition again. "provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer... is budget, not invoice".
>     *   This is a bill from "SLOUGH PROPERTIES N.V." (a property company) to "C.R.C. CONTRACT RESEARCH CENTER BVBA" for "huur" (rent) for the period 01/04/1993 to 30/06/1993. This is a periodic statement of charges for an ongoing account (rent/lease).
>     *   Therefore, it fits the "budget" category under check 7: "provider's periodic customer statement... is budget, not invoice".
>     *   Wait, is it an invoice? "A billing or payment page stays financial even when it is printed on a form...".
>     *   Let's check the labels. "invoice" vs "budget".
>     *   The text says: "A hotel/motel guest bill... is an invoice... A running 'BALANCE DUE' column does not make a bill a budget 'statement of account'."
>     *   The text says: "budget: ... ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
>     *   Rent is like a utility or subscription (ongoing account for space). The period is 3 months (April to June). This is a periodic statement. So it should be **budget**.
>     *   Let's re-evaluate "invoice". "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report... itemized billing statement listing ACTUAL billable charges...".
>     *   Is rent a "good or service sold" (invoice) or "ongoing account" (budget)?
>     *   Usually, a rent bill is an invoice for the service of leasing. But the rule says: "provider's periodic customer statement... is budget". Rent is a periodic charge.
>     *   Let's look at the document structure. It's a "REKENING" (Bill/Invoice/Statement). "REKENING NR. 930058".
>     *   "Omschrijving: huur". "Periode: 01/04/1993 tot 30/06/1993". "Bedrag: 669060". "Totaal te betalen: 669060".
>     *   This is a statement of account for rent.
>     *   According to the rule: "provider's periodic customer statement... is budget, not invoice". Rent is a periodic service (ongoing account). So **budget**.
> 
>     *   Wait, let's look at Check 10: Administrative Form.
>     *   "Filled or blank fields... A form does NOT have to be blank... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   So if it's a billing document, it's Check 7.
> 
>     *   Let's reconsider Invoice vs Budget.
>     *   Invoice: "charges owed for goods or services SOLD". Rent is a service.
>     *   Budget: "provider's periodic customer statement... statement of charges for an ongoing account".
>     *   The period is 3 months. This is a periodic statement. So **budget**.
> 
>     *   Let's look at the label "invoice". "an outside vendor... states charges owed...".
>     *   Often, a single bill for rent is called an invoice. But the specific rule distinguishes: "provider's periodic customer statement... is budget".
>     *   Let's look at the text: "A hotel/motel guest bill... is an invoice". A hotel bill is for a specific stay (one-off service). Rent is for a period (ongoing account).
>     *   So this is likely **budget**.
> 
>     *   Wait, is there an "invoice" header? No. Just "REKENING NR." (Account No / Bill No).
>     *   Is there an "invoice" label? No.
>     *   The content is a bill for rent.
>     *   Let's check the rule for "invoice" again. "invoice: an outside vendor... states charges owed...".
>     *   Let's check the rule for "budget" again. "budget: ... provider's periodic customer statement... is budget, not invoice".
>     *   This is a statement from a property company (vendor) to a research center (customer) for rent (ongoing account). So **budget**.
> 
>     *   Wait, is it a form? "administrative form... filled or blank fields...". The table has headers "Omschrijving", "Periode", "Bedrag". It's a structured table. But Check 7 says "Money function overrides form layout... a billing or payment page stays financial...". And "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   So Check 7 overrides Check 10.
> 
>     *   So it's either invoice or budget.
>     *   The period is 01/04/1993 to 30/06/1993. This is a quarterly statement.
>     *   Rule: "provider's periodic customer statement... is budget".
>     *   So **budget**.
> 
>     *   Let's look really closely. Is there any other category?
>     *   Letter? No salutation, no closing. Just address blocks and a table.
>     *   Memo? No TO/FROM/RE header block followed by prose.
> 
>     *   Let's re-read the "invoice" definition carefully.
>     *   "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due... a payment voucher... a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work... It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
>     *   "budget: ... provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
> 
>     *   Rent ("huur") is a charge for an ongoing account (leasing property). The period is 3 months. This fits "periodic customer statement" / "statement of account for an ongoing account".
>     *   So **budget**.
> 
>     *   Wait, could it be **invoice**?
>     *   If I treat "huur" as a service sold.
>     *   But the rule explicitly says "utility or subscription statement" is budget. Rent is very similar to a utility/subscription (ongoing access to space).
>     *   Also, the document is titled "REKENING NR. 930058". In Dutch, "Rekening" means bill/invoice/statement.
>     *   The table shows "Totaal te betalen" (Total to pay).
>     *   This is a bill.
>     *   Let's look at the "invoice" example: "hotel/motel guest bill... is an invoice". Why? "bills for a one-off service performed (lodging), not a periodic account statement".
>     *   Rent is NOT a one-off service. It's a periodic account statement (for the period 01/04-30/06).
>     *   So **budget** is the correct label based on the specific exclusion in the rules.
> 
>     *   Wait, is there any other check?
>     *   Check 10: Form. "A form does NOT have to be blank... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   So if it's money, it's Check 7.
> 
>     *   Let's check if there's any "invoice" specific evidence.
>     *   No "INVOICE" text.
>     *   The text is Dutch. "SLOUGH PROPERTIES N.V.", "C.R.C. CONTRACT RESEARCH CENTER BVBA", "TOLLAAN 101 C", "SINT-STEVENS-WOLUWE", "Brussel". This is Belgium.
>     *   "REKENING" = Invoice/Bill/Statement.
>     *   "Omschrijving" = Description.
>     *   "Periode" = Period.
>     *   "Bedrag" = Amount.
>     *   "huur" = Rent.
>     *   "Totaal te betalen" = Total to pay.
> 
>     *   Decision: This is a periodic statement of charges for rent (ongoing account). Rule says this is **budget**.
> 
>     *   Wait, let's look at the "invoice" definition again. "an agency/vendor billing document for COMPLETED work... itemized billing statement listing ACTUAL billable charges".
>     *   Rent is a charge for the period. It is actual charges incurred.
>     *   But the "budget" definition has a specific carve-out: "provider's periodic customer statement... is budget, not invoice".
>     *   Rent is the classic example of a periodic account statement (like electricity, phone, rent).
>     *   So **budget**.
> 
>     *   Let's check if it could be **form**.
>     *   The page has a table. But Check 7 says money records are invoice/budget.
>     *   So not form.
> 
>     *   Final decision: **budget**.
> 
>     *   Wait, let's look at the "invoice" definition one more time. "invoice: ... an outside vendor ... states charges owed ...".
>     *   Is a rent bill an invoice? In common parlance, yes. In this specific classification scheme:
>     *   "budget: ... provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice".
>     *   Rent is a service bill / statement of account for an ongoing account.
>     *   So **budget**.
> 
>     *   Let's check the runner-up.
>     *   Runner-up: invoice. Ruled out because the document is a periodic statement of charges for an ongoing account (rent for a 3-month period), which the rules classify as budget ("provider's periodic customer statement... is budget, not invoice"), not a one-off bill for goods sold or completed work (invoice).
> 
>     *   Wait, is there any chance it's **invoice**?
>     *   "A hotel/motel guest bill ... is an invoice".
>     *   "A running 'BALANCE DUE' column does not make a bill a budget 'statement of account'."
>     *   This page has "Totaal te betalen" (Total to pay), not "Balance Due".
>     *   The period is explicitly defined: "01/04/1993 tot 30/06/1993". This confirms it's a periodic statement.
>     *   So **budget**.
> 
>     *   One more check: **form**.
>     *   The table is structured. But Check 7 overrides. "Money function overrides form layout... billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   Wait, "money-only forms are budget". This is a billing document (has description, period, amount). So it's financial.
>     *   Check 7 applies.
> 
>     *   So **budget**.
> 
>     *   Let's re-read the pre-scan instructions.
>     *   "A mail-client header block... If present, the page is email". Not present.
>     *   "A masthead or running head...". Not present.
> 
>     *   Scratchpad:
>     *   file_folder: no — page has a table with financial data, address blocks, and a bill number, not just an ID.
>     *   handwritten: no — typed text.
>     *   fax: no — no fax header.
>     *   questionnaire: no.
>     *   resume: no.
>     *   scientific_publication: no.
>     *   financial document (Check 7): yes — page is a bill/statement ("REKENING NR. 930058") from "SLOUGH PROPERTIES N.V." to "C.R.C. CONTRACT RESEARCH CENTER BVBA" for "huur" (rent) for the period "01/04/1993 tot 30/06/1993" with amount "669060". This is a provider's periodic customer statement for an ongoing account (rent), which the rules classify as budget.
>     *   specification: no.
>     *   presentation: no.
>     *   form: no — Check 7 overrides for money records.
>     *   correspondence: no — no letter/memo structure (no salutation, no closing, no TO/FROM prose). It's a billing statement.
>     *   news_article: no.
>     *   scientific_report: no.
>     *   advertisement: no.
> 
>     *   Wait, is it a **letter**?
>     *   "letter: letterhead with an external recipient address, date, 'Dear ...' salutation, prose body, and a closing with signature".
>     *   This page has address blocks (Sender: Slough Properties, Recipient: C.R.C.), date ("Brussel, 01/04/1993"), but no salutation, no prose body, no closing signature. It's just the header info and the table.
>     *   So not a letter.
> 
>     *   Is it a **memo**?
>     *   "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
>     *   No prose. Not a memo.
> 
>     *   So it falls to Check 7.
>     *   Invoice vs Budget.
>     *   Rule: "provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer ... is budget, not invoice".
>     *   This is a statement for rent ("huur") for a period (3 months). Rent is an ongoing account service.
>     *   So **budget**.
> 
>     *   Wait, could "huur" be considered "goods or services SOLD" -> invoice?
>     *   The rule says: "budget ... provider's periodic customer statement ... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
>     *   Rent is definitely an ongoing account.
>     *   So **budget**.
> 
>     *   Final check on labels.
>     *   budget.
> 
>     *   Wait, is there any possibility of **invoice**?
>     *   If the system considers a rent bill an invoice.
>     *   But the prompt is very specific: "provider's periodic customer statement ... is budget, not invoice".
>     *   I must follow the prompt's specific rules.
>     *   The rule explicitly distinguishes based on "ongoing account" vs "goods sold/one-off service".
>     *   Rent is ongoing.
>     *   So **budget**.
> 
>     *   One detail: "REKENING NR. 930058". "Rekening" can mean invoice.
>     *   But the content (periodic rent) dictates the category.
> 
>     *   Let's check the runner up again.
>     *   Runner-up: invoice. Ruled out because the document is a periodic statement of charges for an ongoing account (rent for a 3-month period), which the rules classify as budget ("provider's periodic customer statement... is budget, not invoice"), not a one-off bill for goods sold (invoice).
> 
>     *   Wait, is there any other category?
>     *   What about **form**?
>     *   "administrative form... filled or blank fields...".
>     *   The table is a form.
>     *   But Check 7: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>     *   So Check 7 wins.
> 
>     *   Final conclusion: **budget**.

---

### `rvl_cdip__invoice__0008.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking each condition in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "77709 7 7 0 4" at the bottom, and a notice about the image. No journal masthead.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: "PRINT PRODUCTION ESTIMATE", tables, line items, approval blocks. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed text with some handwritten signatures and numbers. Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions or transmittal.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No career history.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal running head, volume, issue, page range.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: The document is titled "PRINT PRODUCTION ESTIMATE".
> - It lists "ARTWORK (DETAIL)" with "ESTIMATED COSTS" (Stock Photo 900.00, Photolettering 185.00, etc.).
> - It has "NET TOTAL $3,280.00", "AGENCY 20% 656.00", "COMMISSION 400.00", "SALES TAX 229.60", "GROSS TOTAL $4,565.60".
> - It has a section "Production Cost Against Budget For: SECOND HALF, 1971" with columns "Estimate", "Actual", "Invoice #", "Date".
> - The title is "PRINT PRODUCTION ESTIMATE".
> - Let's look at the definition of invoice vs budget.
> - invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, "A production estimate report... listing ACTUAL billable charges... is an invoice." But this is an "ESTIMATE".
> - budget: "internal money planning, tracking, or disbursement... money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice... An agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report... is scientific_report... A provider's periodic customer statement... is budget... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> - Wait, the document is a "PRINT PRODUCTION ESTIMATE" from "TED BATES & COMPANY, INC." to "RIGDON & WILLIAMSON TOBACCO CORPORATION".
> - It lists estimated costs for artwork, typography, etc. Total $3,280.00 + agency 20% + commission + tax = $4,565.60.
> - This is an estimate (planning/projected spend) from an agency (Ted Bates) to a client (Rigdon & Williamson).
> - "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice... An agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This is an estimate of costs for a print production (Kool brand, Pure Menthol). It's an estimate, not a bill for completed work. So it's a budget.
> - Let's re-read check 7 carefully: "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, if it lists ACTUAL billable charges, it's an invoice. But this is an "ESTIMATE" with "ESTIMATED COSTS".
> - "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> - This document is an "ESTIMATE" with "ESTIMATED COSTS". It is planning projected spend. So it's a budget.
> - Let's check if there's any other category. Form? No, it's a financial document.
> - Is it a form? "internal authorization/approval forms with an approval signature/date block" -> form. But this has financial content as its primary structure (line-item table, costs, totals). "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> - So it's budget.
> 
> Let's double check.
> Title: "PRINT PRODUCTION ESTIMATE"
> Vendor: TED BATES & COMPANY, INC.
> Client: RIGDON & WILLIAMSON TOBACCO CORPORATION
> Date: JULY 16, 1971
> Revised November 17, 1971.
> Line items: Stock Photo 900.00, Photolettering 185.00, Photomasked Illustration 500.00, Mechanical (Test) 75.00, Mechanicals (4 other sizes) 300.00. Total 1,320.00.
> Quantity Reprints 1600 Reprints ... 1,320.00.
> Net Total $3,280.00.
> Agency 20% 656.00.
> Commission 400.00.
> Sales Tax 229.60.
> Gross Total $4,565.60.
> This is clearly an estimate of costs for a print job. It's a budget (projected spend).
> 
> Wait, the prompt says: "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> But this document lists "ESTIMATED COSTS", not actual billable charges.
> And: "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
> This matches perfectly. It's an agency/vendor estimate projecting spend.
> 
> Let's check check 10: ADMINISTRATIVE FORM -> form.
> "A form does NOT have to be blank... This also covers: ... internal authorization/approval forms with an approval signature/date block."
> But check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> And "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form."
> By extension, an agency/vendor estimate that lists estimated charges is budget, never a form.
> 
> So the label is budget.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — page has extensive content (title, tables, costs, approvals).
> 2. handwritten: no — mostly typed, only some handwritten signatures/numbers.
> 3. form (fax): no — no fax header.
> 4. questionnaire: no — no survey.
> 5. resume: no — no career history.
> 6. scientific_publication: no — no journal header.
> 7. financial document: yes — "PRINT PRODUCTION ESTIMATE" from Ted Bates to Rigdon & Williamson, listing estimated costs, net total, agency commission, gross total. This is an agency/vendor estimate projecting projected spend, which is budget.
> 8. specification: no — not an MSDS or product formulation.
> 9. presentation: no — not a slide deck.
> 10. form: no — financial content overrides form layout.
> 11. correspondence: no — not an email, memo, or letter.
> 12. news_article: no — no masthead.
> 13. scientific_report: no — no running prose research.
> 14. advertisement: no — not a promo layout.
> 
> Runner-up: invoice. Ruled out because the document is an "ESTIMATE" with "ESTIMATED COSTS" projecting future spend, not a bill for completed goods/services with actual charges (which would be an invoice).
> 
> Wait, is there any chance it's a form?
> "internal authorization/approval forms with an approval signature/date block" -> form.
> But check 7: "Money function overrides form layout... a billing or payment page stays financial... an agency/vendor document that lists actual charges and totals owed is an invoice... never a form."
> Since this is an estimate (budget), it's budget.
> 
> Let's confirm the exact label: "budget".
> 
> Check 7 text: "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> 
> Yes, "PRINT PRODUCTION ESTIMATE" with "ESTIMATED COSTS" is an agency/vendor estimate planning projected spend. Label: budget.
> 
> Final check of the text:
> "TED BATES & COMPANY, INC."
> "RIGDON & WILLIAMSON TOBACCO CORPORATION"
> "PRINT PRODUCTION ESTIMATE"
> "ESTIMATED COSTS"
> "NET TOTAL $3,280.00"
> "AGENCY 20% 656.00"
> "GROSS TOTAL $4,565.60"
> This is definitely a budget (estimate).
> 
> I will output <label>budget</label>.

---

### `rvl_cdip__invoice__0017.png`
**Expected:** `invoice` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> First, pre-scan:
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "93219883" and some text.
> 
> Let's look at the document.
> It's a check.
> "LOEWS CLEARING CORPORATION"
> "THE CHASE MANHATTAN BANK N.A."
> "PAY TO THE ORDER OF THE SUM OF 131,416.00"
> "3-15-82 COUNCIL FOR TOBACCO RESEARCH-U.S.A. INC"
> "NO. 4506"
> "AMOUNT 131,416.00"
> "AUTHORIZED SIGNATURE"
> 
> This is a check face / check stub.
> Let's trace the checks:
> 1. file_folder: No, it has real content (a check).
> 2. handwritten: No, mostly typed/printed.
> 3. fax: No.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No.
> 7. financial document -> invoice or budget.
>    - "budget: internal money planning... check face or check stub, a check/payment register..."
>    - This is a check face. "check face or check stub" is explicitly listed under budget.
>    - Wait, is it an invoice? "invoice: an outside vendor... states charges owed... payment voucher... receipt...". A check is a payment. The instructions say: "budget: ... check face or check stub, a check/payment register...".
>    - Let's re-read check 7 carefully.
>    - "budget: internal money planning, tracking, or disbursement — budget or expense lines, forecast vs. actual, expense reports, a statement of account, a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking."
>    - So a check face is a budget.
> 8. specification: No.
> 9. presentation: No.
> 10. form: No.
> 11. correspondence: No.
> 12. news_article: No.
> 13. scientific_report: No.
> 14. advertisement: No.
> 
> Let's double check check 7.
> "budget: ... a check face or check stub ... is budget, not invoice"
> Yes, a check face is explicitly listed under budget.
> 
> Let's review the document again.
> It's a check from "THE CHASE MANHATTAN BANK N.A." to "COUNCIL FOR TOBACCO RESEARCH-U.S.A. INC" for "131,416.00".
> Date: "3-15-82".
> Number: "4506".
> Bates number: "93219883".
> 
> This is a check face.
> According to check 7: "budget: ... a check face or check stub ... is budget".
> 
> Let's check if there's any other category.
> Could it be a form? No, it's a check.
> Could it be an invoice? No, it's a check face. "a check face or check stub" is budget.
> 
> Let's write the scratchpad.
> 1. file_folder: no — the page contains a full check with payee, amount, date, and bank details, not just an identifier/stamp.
> 2. handwritten: no — the check is printed/typed, with only a signature (which is part of the check).
> 3. fax: no — no fax header.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no — no journal running head.
> 7. financial document -> budget: yes — the page is a check face ("THE CHASE MANHATTAN BANK N.A.", "PAY TO THE ORDER OF", "AMOUNT 131,416.00", "NO. 4506", date "3-15-82"). Check 7 explicitly lists "a check face or check stub" as budget.
> Runner-up: invoice, ruled out because a check face is explicitly categorized as budget in check 7, not invoice (which is for vendor charges owed).
> 
> Wait, the prompt says: "budget: ... a check face or check stub ... is budget, not invoice".
> So the label is budget.
> 
> Let's confirm the text on the check.
> "LOEWS CLEARING CORPORATION"
> "LOCK BOX 146 FIFTH AVENUE NEW YORK, N.Y. 10019"
> "THE CHASE MANHATTAN BANK N.A. SECOND & VENUE & 47TH STREET NEW YORK, N.Y. 10017"
> "NO. 4506"
> "AMOUNT 131,416.00"
> "PAY TO THE ORDER OF THE SUM OF 131,416.00"
> "DATE 3-15-82"
> "COUNCIL FOR TOBACCO RESEARCH-U.S.A. INC"
> "AUTHORIZED SIGNATURE"
> Bates number "93219883".
> 
> This is definitely a check face.
> Check 7: "budget: ... a check face or check stub ... is budget".
> 
> Final label: budget.

---

## advertisement → form (2 errors)

### `rvl_cdip__advertisement__0003.png`
**Expected:** `advertisement` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of white space, but there is a block of text at the bottom right: "Brand: Lucky 100's", "Publication: News American", "Date: 4/17/74", "Size: 8 1/2 x 14 1/4 (121.1)", "Comments: Ad Warning: 14 pt - sheet, T & N - 16 pt - 10pt neg", and a handwritten "725".
> - This is not just an identifier/stamp. It has structured data fields (Brand, Publication, Date, Size, Comments).
> - Not file_folder.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Most of the text is typed ("Brand:", "Publication:", "Date:", "Size:", "Comments:", "Ad Warning:", "T & N -"). The values are handwritten ("Lucky 100's", "News American", "4/17/74", "8 1/2 x 14 1/4 (121.1)", "14 pt - sheet", "16 pt - 10pt neg", "725").
> - The page is a printed template with handwritten entries. This is a filled form, not majority handwritten freeform paper.
> - Not handwritten.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions, rating scales, or commitment application.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No career history.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal running head, volume, issue, etc.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: No financial line items, ledger, or billing. "Publication: News American" might imply an ad placement, but there's no invoice or budget structure.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No Material Safety Data Sheet, product formulation, or "shall/must" language.
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck, cover, or press release.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: The page has typed field labels ("Brand:", "Publication:", "Date:", "Size:", "Comments:", "Ad Warning:", "T & N -") and handwritten entries filling those fields. It is capturing factual data (ad placement details: brand, publication, date, size, ad warning specs). This is a structured data capture form.
> - Matches check 10.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - Evidence: No TO/FROM/RE header, no salutation, no closing.
> - Not this check.
> 
> **Check 12: PUBLISHED JOURNALISM -> news_article**
> - Evidence: No masthead, byline, dateline, multi-column typography.
> - Not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - Evidence: No running narrative prose.
> - Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
> - Evidence: Not a marketing layout, product imagery, slogans. It's a metadata sheet for an ad.
> - Not this check.
> 
> **Conclusion:**
> The page is a form capturing ad placement details (Brand, Publication, Date, Size, Comments). It has printed field labels and handwritten entries. This fits "ADMINISTRATIVE FORM -> form" (Check 10).
> 
> Let's double check.
> "Brand: Lucky 100's"
> "Publication: News American"
> "Date: 4/17/74"
> "Size: 8 1/2 x 14 1/4 (121.1)"
> "Comments: Ad Warning: 14 pt - sheet T & N - 16 pt - 10pt neg"
> This is a form used to record advertising placement specifications. It has labeled fields (Brand, Publication, Date, Size, Comments) and filled values. It is a form.
> 
> Runner-up: file_folder. Ruled out because it has structured data fields (Brand, Publication, Date, Size, Comments) rather than just an identifier/stamp.
> Runner-up: advertisement. Ruled out because it's a metadata/spec sheet for an ad, not the ad itself (no product imagery, slogans).
> 
> Final label: form.

---

### `rvl_cdip__advertisement__0015.png`
**Expected:** `advertisement` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> Image analysis:
> The image shows a mostly blank page with some handwritten text and a number "1127" in the top right.
> The handwritten text is:
> "Brand: Lucky Ten"
> "Publication: El Diario"
> "Date: 11/8/74"
> "Size: 3 1/2 x 7 (24.5 sq.in)"
> 
> Let's check the pre-scan:
> - Mail-client header block: None.
> - Masthead or running head: None.
> 
> Check 1: IDENTIFIER-ONLY PAGE -> file_folder
> - Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card.
> - Here we have "1127" (likely a Bates number or similar ID) and a short handwritten note with fields "Brand:", "Publication:", "Date:", "Size:".
> - Wait, is this a form? The fields "Brand:", "Publication:", "Date:", "Size:" are printed? Let's look closely.
> - "Brand:", "Publication:", "Date:", "Size:" look like printed text, and the values "Lucky Ten", "El Diario", "11/8/74", "3 1/2 x 7 (24.5 sq.in)" are handwritten.
> - If it's a printed template with fields filled by hand, it's a form (check 10).
> - Let's re-read check 1: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
> - Is this a note? "Handwriting filling in labeled printed fields is form, not handwritten".
> - Let's check check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten. "This includes meeting-minutes sheets and log tables printed with ruled columns and headers... The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten. Handwriting filling in labeled printed fields is form, not handwritten".
> - Here, "Brand:", "Publication:", "Date:", "Size:" are printed field labels. The values are handwritten. So it's a filled form.
> - Wait, are they printed? "Brand:", "Publication:", "Date:", "Size:" look like typewritten or printed labels. Let's assume they are printed labels.
> - If they are printed labels, it's a form (check 10).
> - Let's check check 10: ADMINISTRATIVE FORM -> form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
> - This page has printed labels "Brand:", "Publication:", "Date:", "Size:" and handwritten data. This is a filled form.
> 
> Let's re-evaluate check 1: file_folder.
> - "A page is NOT file_folder if it carries any real content... a note."
> - Is this just a note? If the labels are printed, it's a form. If the labels are handwritten, it's handwritten.
> - Looking at the text: "Brand: Lucky Ten" - "Brand:" is in a different font than "Lucky Ten". "Publication:" is in a different font than "El Diario". "Date:" is in a different font than "11/8/74". "Size:" is in a different font than "3 1/2 x 7 (24.5 sq.in)".
> - The labels "Brand:", "Publication:", "Date:", "Size:" are printed (likely typewritten or pre-printed). The values are handwritten.
> - Therefore, it is a filled form.
> 
> Let's check check 2: handwritten.
> - "Handwriting filling in labeled printed fields is form, not handwritten". So not handwritten.
> 
> Check 3: FAX TRANSMISSION SHEET -> form. No.
> 
> Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire. No.
> 
> Check 5: PERSON'S CAREER HISTORY -> resume. No.
> 
> Check 6: PUBLISHED EVIDENCE -> scientific_publication. No.
> 
> Check 7: FINANCIAL DOCUMENT -> invoice or budget. No.
> 
> Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification. No.
> 
> Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation. No.
> 
> Check 10: ADMINISTRATIVE FORM -> form.
> - "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells."
> - The page has printed field labels ("Brand:", "Publication:", "Date:", "Size:") and handwritten data filling them. This is a filled form.
> 
> Let's double check if it could be file_folder.
> - "A page is NOT file_folder if it carries any real content... a note."
> - If the labels are just handwritten, it would be handwritten. But the labels are printed.
> - "Brand:" is printed. "Lucky Ten" is handwritten.
> - This is a form capturing factual data (brand, publication, date, size of an ad or placement).
> 
> Wait, what about check 14: advertisement?
> - "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures."
> - This is just a data capture sheet about an advertisement (Lucky Ten in El Diario, 11/8/74, size 3.5x7). It's not the ad itself. It's a form recording ad placement data.
> 
> So check 10 (form) is the correct match.
> 
> Let's review the evidence for check 10:
> - Printed field labels: "Brand:", "Publication:", "Date:", "Size:".
> - Handwritten values filling these fields: "Lucky Ten", "El Diario", "11/8/74", "3 1/2 x 7 (24.5 sq.in)".
> - This matches "Filled or blank fields... for capturing factual data... including handwriting in its cells."
> 
> Runner-up: file_folder. Ruled out because the page contains filled printed field labels (Brand, Publication, Date, Size) with data, which is real content (a filled form), not just pure filing metadata like a Bates number or folder tab.
> Another runner-up: handwritten. Ruled out because the handwriting fills printed labeled fields, which makes it a form, not freeform handwriting.
> 
> Let's confirm the labels are printed.
> "Brand:" is in a monospaced, typewriter-like or printed font. "Lucky Ten" is cursive/handwritten.
> "Publication:" is same font. "El Diario" is handwritten.
> "Date:" is same font. "11/8/74" is handwritten.
> "Size:" is same font. "3 1/2 x 7 (24.5 sq.in)" is handwritten.
> Yes, printed labels with handwritten entries. This is a filled form.
> 
> Final check of the steps:
> 1. file_folder: no — has filled printed fields.
> 2. handwritten: no — handwriting fills printed labels.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. financial: no.
> 8. specification: no.
> 9. presentation: no.
> 10. form: yes — printed field labels ("Brand:", "Publication:", "Date:", "Size:") with handwritten data filling them.
> 
> The label is "form".

---

## invoice → form (2 errors)

### `rvl_cdip__invoice__0006.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: No "From/To/Sent/Subject" email headers. There is a "REQUISITIONER'S COPY" and "PURCHASE ORDER NO. A 21248". No fax transmission header like "SENT BY: ... # N/N". Wait, there's a "T-045" at the top right, but no fax header.
> - Masthead/running head: "The American Tobacco Company" logo at the top left. This is a company letterhead/header, not a newspaper/magazine masthead or journal running head.
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
>     *   Evidence: The page has a lot of content: purchase order details, billing instructions, supplier info, description of posters, quantities, prices, accounting charge no.
>     *   Result: not this check.
> 
> *   **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
>     *   Evidence: Mostly typed text. There is a handwritten signature at the bottom right and some handwritten annotations (lines crossing through), but the majority is typed.
>     *   Result: not this check.
> 
> *   **Check 3: FAX TRANSMISSION SHEET -> form**
>     *   Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
>     *   Result: not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: No survey questions.
>     *   Result: not this check.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: No CV/resume content.
>     *   Result: not this check.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range.
>     *   Result: not this check.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: "PURCHASE ORDER NO. A 21248", "DATE January 21, 1976". It lists "TARYTON 30-Sheet Posters... @ $9.62 ea.", Quantity "2,012". It mentions "Your plant- please ship prepaid and add transportation charges to your invoice."
>     *   Wait, is this an invoice or a purchase order (which is a form)?
>     *   Let's look at Check 10: ADMINISTRATIVE FORM.
>     *   Let's look at Check 7 again: "invoice: an outside vendor... states charges owed... a payment voucher... a receipt...". "budget: internal money planning...".
>     *   This is a Purchase Order (P.O. No. A 21248). A purchase order is a request to buy goods. It's not an invoice (bill for completed work) yet, nor a budget (planning/tracking). Wait, let's look at the structure.
>     *   It has fields: "PURCHASE ORDER NO.", "DATE", "REQ. NO.", "TO:", "SHIP TO:", "SHIPMENT TO ARRIVE NOT LATER THAN", "VIA", "TERMS", "QUANTITY", "CODE NO.", "DESCRIPTION", "PRICE".
>     *   This is a structured form for ordering.
>     *   Let's check Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application...". A purchase order is a form.
>     *   Wait, is a purchase order an invoice? "an outside vendor... states charges owed". This is from The American Tobacco Company (buyer) to MacNaughton Lithograph Company (vendor). It's a purchase order, not an invoice from the vendor.
>     *   Is it a budget? "internal money planning...". A purchase order authorizes a purchase. Check 7 says: "an internal expenditure-authorization form ('ADVERTISING AND SELLING AUTHORIZATION', purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget". This document has billable charges listed (Quantity 2,012 @ $9.62 ea.), but it's a Purchase Order, which is a form to request goods.
>     *   Actually, let's look at the content. It's a "PURCHASE ORDER". Purchase orders are forms.
>     *   Let's re-read Check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." But this is a Purchase Order, not a billing page. It's a request to buy.
>     *   Check 10: "administrative form...". A purchase order is a classic administrative form.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: "TARYTON 30-Sheet Posters... Posters to be printed a combination of offset and silk-screen...". This describes the product to be manufactured.
>     *   Wait, Check 8: "product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables...". "A titled product-analysis table... is a specification".
>     *   Is this a specification? It describes the posters to be printed. "Posters to be printed a combination of offset and silk-screen in six colors...". "Posters (new design) captioned for identification 'TARYTON is Better'." "Posters supplied to be capable of withstanding a 45 day outdoor posting period...". "Overruns or underruns must not exceed 5%."
>     *   This looks like a specification for the posters. But it's wrapped in a Purchase Order form.
>     *   Check 8 says: "Product-referenced test data is a specification. A titled product-analysis table... is a specification".
>     *   Check 10 says: "administrative form...".
>     *   Let's look at the hierarchy. Check 7 (Financial) vs Check 10 (Form).
>     *   Actually, let's look at Check 10 again. "Filled or blank fields... for capturing factual data". This is a filled purchase order.
>     *   Is it a specification? "manufacturing-change authorization...". This is a new order, not a change authorization.
>     *   The description is detailed, but the primary function is a Purchase Order (form).
>     *   Wait, let's look at Check 7 again. "invoice...". This is not an invoice. "budget...". This is not a budget.
>     *   So it's likely a form (Check 10).
> 
> *   **Check 9: SLIDE DECK... -> presentation**
>     *   Evidence: No.
>     *   Result: not this check.
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: "PURCHASE ORDER NO. A 21248", "REQUISITIONER'S COPY". Fields for Supplier, Ship To, Quantity, Code No, Description, Price. Billing instructions. Accounting charge no. "Corporate Media Dept. A.T.Co.".
>     *   This is a Purchase Order form. It has fields, boxes, checkboxes (Billing Instructions checkboxes: "MAIL YOUR INVOICES...", "ADVERTISING EXPENSE DIVISION", etc.).
>     *   Result: YES. This is a form.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: No TO:/FROM:/RE: memo header followed by prose. No letterhead with external address + Dear... + closing signature (though there is a signature at the bottom, it's a form signature). The structure is a form with fields.
>     *   Result: not this check.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: No.
>     *   Result: not this check.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: No running narrative prose of research.
>     *   Result: not this check.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: No.
>     *   Result: not this check.
> 
> **Re-evaluating Check 7 vs Check 10:**
> The document is a Purchase Order.
> Check 7: "invoice... budget...". A purchase order is neither an invoice (bill for completed work) nor a budget (planning/tracking). It's a request to purchase.
> Check 10: "administrative form...". A purchase order is a standard administrative form.
> The text says: "an internal expenditure-authorization form ('ADVERTISING AND SELLING AUTHORIZATION', purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget". This document has billable charges (Quantity 2,012 @ $9.62), but it's a Purchase Order, which is a form to initiate a transaction.
> Actually, let's look at the "Billing Instructions" box: "MAIL YOUR INVOICES IN TRIPLICATE TO CONSIGNEE...". This confirms the document is a Purchase Order (requesting goods), and the vendor will send an Invoice later. So this document is NOT an invoice.
> Therefore, it is a form (Check 10).
> 
> **Re-evaluating Check 8 (Specification):**
> The description contains specifications: "Bleed Size 12.5" x 27.2"", "six colors", "70# poster paper", "45 day outdoor posting period", "Overruns or underruns must not exceed 5%".
> Check 8: "product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables... tolerances, or 'shall/must' requirement language."
> "Overruns or underruns must not exceed 5%." -> "must" language.
> "Posters to be shipped in sufficient time..."
> Is this a specification page?
> Check 8 says: "A titled product-analysis table... is a specification". This is not a table.
> Check 8 says: "manufacturing-change authorization...". This is a new order.
> Check 10 says: "administrative form...".
> Usually, a purchase order with detailed specs is still classified as a form (purchase order) because its primary function is the administrative request/contract, even if it contains specs. The specs are part of the order description.
> However, look at the layout. It's a standard Purchase Order form (Requisitioner's Copy). The top has "The American Tobacco Company", "PURCHASE ORDER NO.", "DATE". The middle has the line items. The bottom has accounting info.
> This is a classic form.
> 
> Let's check the labels again.
> form: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data...". This fits perfectly. Purchase order forms have checkboxes (Billing Instructions), fields (To, Ship To, Quantity, Description, Price), and ruled lines.
> 
> Let's double check if it could be an invoice.
> "Your plant- please ship prepaid and add transportation charges to your invoice." -> This implies the invoice is a separate document to be sent later. So this is not an invoice.
> 
> Let's double check if it could be a budget.
> "ACCOUNTING CHARGE NO. Corporate Media Dept. A.T.Co." -> It's charging a department. But it's a specific purchase order for 2,012 posters. Not a budget statement.
> 
> So, **form** is the best fit.
> 
> **Scratchpad walk-through:**
> 1. file_folder: No, has lots of content (Purchase Order details).
> 2. handwritten: No, mostly typed.
> 3. fax: No fax header.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No journal header.
> 7. financial (invoice/budget): It mentions a purchase order and invoice, but the document itself is a Purchase Order (request to buy), not an invoice (bill) or budget (planning). The billing instructions say "MAIL YOUR INVOICES...", confirming this is the PO, not the invoice.
> 8. specification: Contains specs ("must not exceed 5%"), but it's a Purchase Order form with detailed description. The primary structure is a form (PO). Wait, is a PO with specs a specification? Check 8: "manufacturing-change authorization...". This is not a change authorization. It's a new order. The specs are just the description of goods. Check 10 covers forms capturing data. A PO captures order data.
> 9. presentation: No.
> 10. form: Yes. "PURCHASE ORDER NO.", checkboxes for billing instructions, fields for Supplier, Ship To, Quantity, Description, Price. It's a filled administrative form (Purchase Order).
> 11. correspondence: No memo/letter structure.
> 12. news_article: No.
> 13. scientific_report: No.
> 14. advertisement: No.
> 
> Runner-up: invoice. Ruled out because the text says "add transportation charges to your invoice", meaning this document is the Purchase Order requesting the goods, not the invoice billing for them. Also, it's from the buyer (American Tobacco) to the vendor (MacNaughton), whereas an invoice is from vendor to buyer.
> 
> Final decision: form.
> 
> One detail: "The American Tobacco Company... REQUISITIONER'S COPY". "PURCHASE ORDER NO. A 21248".
> This is definitely a form.
> 
> Let's check the "specification" check again.
> "Material Safety Data Sheet... product formulation... manufacturing-change authorization... test-analysis tables... tolerances, or 'shall/must' requirement language."
> "Overruns or underruns must not exceed 5%." -> "must" language.
> But the document is a Purchase Order. The specs are embedded in the description field of the form.
> Check 10: "administrative form...".
> Check 8: "Product-referenced test data is a specification. A titled product-analysis table... is a specification".
> This is not a titled product-analysis table. It's a line item in a PO.
> The primary function is ordering (form).
> 
> I will go with **form**.
> 
> Wait, looking closely at the image:
> Top: "The American Tobacco Company", "REQUISITIONER'S COPY".
> Box: "BILLING INSTRUCTIONS - MAIL YOUR INVOICES IN TRIPLICATE TO CONSIGNEE UNLESS INSTRUCTED OTHERWISE BELOW". Checkboxes: "MAIL YOUR INVOICES...", "ADVERTISING EXPENSE DIVISION", "COST DIVISION", "SALESMEN'S EXPENSE DIVISION", "CORPORATE ACCOUNTING DIVISION", "AS SHOWN BELOW".
> "TO: MacNaughton Lithograph Company..."
> "PURCHASE ORDER NO. A 21248", "DATE January 21, 1976".
> Table headers: "QUANTITY", "CODE NO.", "DESCRIPTION", "PRICE".
> Row: "2,012", (blank), "TARYTON 30-Sheet Posters...", "@ $9.62 ea.".
> Bottom: "ACCOUNTING CHARGE NO. Corporate Media Dept. A.T.Co.", checkboxes for tax/exemption.
> This is a Purchase Order form.
> 
> Label: form.

---

### `rvl_cdip__invoice__0014.png`
**Expected:** `invoice` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None. There's a "REQUISITIONER'S COPY", "PURCHASE ORDER NO. M 13174", "DATE May 27, 1992", "REQ. NO. Auth #R-44". No From/To/Sent/Subject.
> - Masthead/running head: "THE AMERICAN TOBACCO COMPANY", "SIX STAMFORD FORUM". Not a newspaper/magazine masthead or journal running head.
> 
> **Check 1: file_folder**
> - Evidence: The page has a lot of content: purchase order details, line items, descriptions, prices, approval signature. Not just an identifier/stamp.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: Mostly typed. Handwriting is just a signature "L. Cannarota" and "By [signature]". Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
> - Not this check.
> 
> **Check 4: questionnaire**
> - Evidence: No survey instrument or transmittal.
> - Not this check.
> 
> **Check 5: resume**
> - Evidence: No career history.
> - Not this check.
> 
> **Check 6: scientific_publication**
> - Evidence: No journal running head.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: The page is a purchase order / invoice-like document. Wait, let's look closer.
> - "REQUISITIONER'S COPY"
> - "PURCHASE ORDER NO. M 13174"
> - Line items: "CARLTON Tar Chart 'Reward and Shelter' Direct Mail Units", "Plus Prep., Proof, Programming", "Advanced Postage - 3rd Class Bulk Rate - Indicia", "Non-Standard Ink Charge".
> - Prices: "$787.21/M", "$7,600.00", "($93,200.00)", "$250.00/ea".
> - "Accounting Charge No. Marketing Adv. Exp."
> - "STATE SALES TAX NOT TO BE CHARGED"
> - "Please contact on any questions regarding this Purchase Order."
> - Is this an invoice or a budget or a form?
> - Let's check the definitions.
> - invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> - budget: "internal money planning, tracking, or disbursement... a provider's periodic customer statement... is budget, not invoice".
> - Wait, this is a "PURCHASE ORDER". A purchase order is a request to buy. But it has line items and prices.
> - Let's look at check 10: ADMINISTRATIVE FORM. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
> - Wait, check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> - But is this a billing page? It says "REQUISITIONER'S COPY", "PURCHASE ORDER NO.", "SHIP TO", "TERMS Net 20 Days". It's a purchase order.
> - Let's re-read check 7: "invoice: an outside vendor, supplier, or agency states charges owed...". This is from "THE AMERICAN TOBACCO COMPANY" to "Webcraft Technologies, Inc." Wait, American Tobacco is the buyer? "MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE... GENERAL ACCOUNTING OFFICE... CHESTER, VIRGINIA". So American Tobacco is the consignee/buyer. Webcraft is the supplier.
> - This is a purchase order issued by American Tobacco to Webcraft.
> - Is a purchase order an invoice? No, an invoice is from the vendor. A purchase order is a request.
> - Is it a budget? "internal money planning, tracking, or disbursement... a check face or check stub, a check/payment register, or a status report whose PRIMARY content is budget and spend tracking. Also covers money-only records: a contribution/expenditure request or approval form whose whole content is an amount..."
> - Wait, check 10: "internal authorization/approval forms with an approval signature/date block." A purchase order is an authorization to spend money / buy goods.
> - Let's look at check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> - This document has a purchase order number, line items, prices, and an approval signature ("By [signature]"). It is an authorization for a purchase. It has billable charges listed (prices, amounts), but it's a purchase order, not an invoice from the vendor.
> - Wait, the line items are "CARLTON Tar Chart... Direct Mail Units", prices "$787.21/M", "$7,600.00". This looks like a quote or a purchase order detailing the costs.
> - Since it's an internal authorization/purchase order (Requisitioner's copy, Purchase Order No., Accounting Charge No., Marketing Adv. Exp., signature block), it fits "internal authorization/approval forms" in check 10.
> - Let's re-read check 7: "invoice: ... an agency/vendor billing document for COMPLETED work ... It does not have to be titled 'INVOICE' — a voucher, recap, or change order that bills charges already incurred and totals is an invoice." This is a purchase order, not a vendor bill.
> - "budget: ... a contribution/expenditure request or approval form whose whole content is an amount ... is budget". But this has line items and prices.
> - Let's look at check 10: "internal authorization/approval forms with an approval signature/date block." This has "REQUISITIONER'S COPY", "PURCHASE ORDER NO.", "DATE", "REQ. NO.", "By [signature]". It's a purchase requisition / approval form.
> - Wait, is it a form? Yes, it has fields: TO, SHIP TO, QUANTITY, CODE NO., DESCRIPTION, PRICE, ACCOUNTING CHARGE NO., checkboxes for EXEMPTION CERTIFICATE, DIRECT PAYMENT PERMIT, IN YOUR FILES, ATTACHED.
> - Let's check if it could be an invoice. "MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE". This is instructions for the vendor. The document itself is the Purchase Order / Requisition.
> - Therefore, it's an administrative form (check 10).
> 
> Let's double check check 7 vs check 10.
> Check 7: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> But is this a billing or payment page? No, it's a purchase order / requisition. "REQUISITIONER'S COPY", "PURCHASE ORDER NO. M 13174".
> Check 7 caveat: "an internal expenditure-authorization form ("ADVERTISING AND SELLING AUTHORIZATION", purchase/requisition approval, with an approval signature/date block but no billable charges) is a form (check 10), not budget — authorizing a single expenditure is not planning or tracking money."
> This document has billable charges listed (the line items and prices), but it's a purchase order/requisition, which is an authorization to buy. The line items describe what is being purchased and the estimated costs, but it's not a bill from a vendor (invoice) nor a budget tracking document. It's a purchase requisition/approval form.
> Actually, let's look at the structure:
> - Header: THE AMERICAN TOBACCO COMPANY, SIX STAMFORD FORUM
> - Box: BILLING INSTRUCTIONS - MAIL YOUR INVOICES...
> - REQUISITIONER'S COPY, L. Cannarota (handwritten)
> - PURCHASE ORDER NO. M 13174, DATE May 27, 1992, REQ. NO. Auth #R-44
> - TO: Webcraft Technologies, Inc. ...
> - SHIP TO: Mail 3rd Class Bulk Rate ...
> - SHIPMENT TO ARRIVE NOT LATER THAN: Mail June 15, 1992 Complete
> - F.O.B. Chalfont, PA
> - TERMS: Net 20 Days
> - Table: QUANTITY, CODE NO., DESCRIPTION, PRICE
> - 400,000 | | CARLTON Tar Chart "Reward and Shelter" Direct Mail Units | $787.21/M
> - | | Plus Prep., Proof, Programming | $7,600.00
> - 400,000 | | Advanced Postage - 3rd Class Bulk Rate - Indicia | ($93,200.00)
> - 3 | | Non-Standard Ink Charge | $250.00/ea
> - Text: Costs include 42 basic plates... Refund due, if any...
> - ACCOUNTING CHARGE NO. Marketing Adv. Exp.
> - Checkboxes: STATE SALES TAX NOT TO BE CHARGED, EXEMPTION CERTIFICATE, DIRECT PAYMENT PERMIT, IN YOUR FILES, ATTACHED.
> - Signature: By [signature]
> 
> This is a purchase order / requisition form. It captures data for an internal authorization/purchase.
> Check 10: "administrative form -> form. Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... internal authorization/approval forms with an approval signature/date block."
> This perfectly matches an internal authorization/approval form (purchase requisition/order) with an approval signature/date block.
> 
> Let's check if it could be an invoice. "an outside vendor, supplier, or agency states charges owed for goods or services SOLD". This is from the buyer (American Tobacco) to the supplier (Webcraft), stating what they want to buy and the agreed prices. It's a purchase order, not an invoice. An invoice would be from Webcraft to American Tobacco. The billing instructions say "MAIL YOUR INVOICES IN DUPLICATE TO CONSIGNEE". So this document is the PO, not the invoice.
> 
> Could it be a budget? "budget: internal money planning, tracking, or disbursement... a contribution/expenditure request or approval form whose whole content is an amount". This has line items and prices, but it's a specific purchase authorization, not a budget statement or tracking document. The caveat in check 7 says "an internal expenditure-authorization form... is a form (check 10), not budget". This is exactly that.
> 
> So check 10 is the correct match.
> 
> Let's review the checks again to be sure.
> 1. file_folder: No, has content.
> 2. handwritten: No, mostly typed.
> 3. FAX: No.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No.
> 7. financial document: Not an invoice (it's a PO from buyer to vendor), not a budget (it's an expenditure authorization form, per check 7 caveat).
> 8. specification: No.
> 9. presentation: No.
> 10. form: Yes, internal authorization/approval form (purchase requisition/order) with fields, checkboxes, and approval signature.
> 11. correspondence: No.
> 12. news_article: No.
> 13. scientific_report: No.
> 14. advertisement: No.
> 
> Runner-up: invoice. Ruled out because the document is a "REQUISITIONER'S COPY" / "PURCHASE ORDER" from the buyer (American Tobacco) to the supplier (Webcraft), with billing instructions for the vendor to mail invoices. It is an internal authorization/purchase form, not a vendor billing document. Also, check 7 caveat explicitly excludes internal expenditure-authorization forms from budget/invoice.
> 
> Wait, is there any chance it's an invoice? "Please contact on any questions regarding this Purchase Order." Definitely a Purchase Order.
> Is a Purchase Order a form? Yes, "internal authorization/approval forms with an approval signature/date block" is explicitly listed under check 10 (form).
> 
> Let's confirm the label: `form`.
> 
> Scratchpad:
> - file_folder: no — page has detailed line items, prices, and approval blocks, not just an identifier.
> - handwritten: no — mostly typed, only a signature and name.
> - fax: no — no fax header.
> - questionnaire: no — no survey items.
> - resume: no — no career history.
> - scientific_publication: no — no journal identifier.
> - financial_document: no — this is a "REQUISITIONER'S COPY" / "PURCHASE ORDER" from the buyer (American Tobacco) to the supplier (Webcraft), not a vendor invoice. Check 7 caveat: "an internal expenditure-authorization form... is a form (check 10), not budget".
> - specification: no — no material safety data or product formulation.
> - presentation: no — not a slide deck or cover.
> - form: yes — "REQUISITIONER'S COPY", "PURCHASE ORDER NO.", fields for TO/SHIP TO/QUANTITY/DESCRIPTION/PRICE, checkboxes (EXEMPTION CERTIFICATE, etc.), and an approval signature block ("By [signature]"). This is an internal authorization/approval form (purchase requisition/order).
> - correspondence: no — no memo/letter structure.
> - news_article: no — no masthead.
> - scientific_report: no — no running narrative prose.
> - advertisement: no — not a promotional layout.
> 
> Runner-up: invoice, ruled out because the document is a purchase order/requisition from the buyer to the vendor (with instructions to mail invoices), and check 7 caveat classifies internal expenditure-authorization forms as forms, not financial documents.
> 
> Final label: form.

---

## budget → invoice (2 errors)

### `rvl_cdip__budget__0006.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "TIIL 002783" and "THE TOBACCO INSTITUTE INC" at the bottom. Top has "11660", "011660", "11/30/93", "194.50".
> 
> **Check 1: file_folder**
> - Evidence: Not just an identifier. Has financial data, vendor info, invoice details.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: No majority handwriting. Typed text throughout.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or fax cover sheet header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: No survey questions or transmittal.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: No resume/CV.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - Evidence: No journal name, volume, issue, page range.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "One Hundred Ninety Four and 50/100 US Dollars". Vendor: "ALLTECH ASSOCIATES INC.", "P.O. BOX 23, DEERFIELD, IL 60015". Table with "INVOICE DATE", "INVOICE NO.", "DESCRIPTION", "INVOICE AMOUNT", "NET AMOUNT". Values: "11/08/93", "892301", "$194.50", "$194.50". Check date "11/30/93", Check number "011660", Vendor number "11350".
> - This is clearly a payment voucher or check stub / invoice payment record. It bills for goods/services (vendor Alltech Associates) and shows invoice amount and net amount. Wait, is it an invoice or a budget?
> - "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work... Look for goods sold or one-off services performed (items, quantities, unit prices)."
> - "budget: ... a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
> - This looks like a check payment record or a payment voucher for an invoice. "INVOICE DATE 11/08/93 892301 ... INVOICE AMOUNT $194.50 ... NET AMOUNT $194.50". It's a payment document for an invoice from Alltech Associates. This falls under invoice (payment voucher / billing document for completed work). Let's re-read check 7: "a payment voucher... is an invoice". Yes.
> - Let's check if it's a budget. No, it's a specific payment for a specific invoice (892301) from a vendor.
> - So, invoice.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
> - Evidence: No material safety data sheet, product formulation, etc.
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT**
> - Evidence: No slide layout.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM**
> - Evidence: It has a table, but it's a financial document (check 7 takes precedence for financial content that is the primary structure). Wait, check 7 says "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is a check face / payment voucher. So check 7 applies.
> 
> **Check 11: CORRESPONDENCE**
> - Evidence: No TO/FROM/RE memo header, no letter format.
> - Not this check.
> 
> **Check 12: PUBLISHED JOURNALISM**
> - Evidence: No masthead, byline, etc.
> - Not this check.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP**
> - Evidence: No running narrative prose.
> - Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL**
> - Evidence: No marketing layout.
> - Not this check.
> 
> Let's double check Check 7.
> The page has:
> - "One Hundred Ninety Four and 50/100 US Dollars"
> - "ALLTECH ASSOCIATES INC."
> - "P.O. BOX 23, DEERFIELD, IL 60015"
> - MICR line: "*O11660* 10540000301: 12*08269752*"
> - "11350" (VENDOR NUMBER), "11/30/93" (CHECK DATE), "011660" (CHECK NUMBER)
> - Table: "INVOICE DATE" (11/08/93), "INVOICE NO." (892301), "DESCRIPTION" (blank or illegible), "INVOICE AMOUNT" ($194.50), "NET AMOUNT" ($194.50)
> - Bottom: "TIIL 002783", "THE TOBACCO INSTITUTE INC"
> 
> This is a check payment stub or a payment voucher recording the payment of an invoice. According to Check 7: "invoice: ... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work ... Look for goods sold or one-off services performed". A payment voucher for an invoice is an invoice document in this classification scheme (or at least, falls under the invoice/budget split, and since it's paying a vendor invoice, it's invoice). Wait, is it a budget? "budget: ... a provider's periodic customer statement ... is budget, not invoice". This is not a periodic statement, it's a specific payment for invoice 892301. So it's invoice.
> 
> Let's review the label options: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
> The document is a payment record / check stub for an invoice. The category is `invoice`.
> 
> Let's quickly check if it could be `form`. Check 10: "administrative form -> form". But Check 7 says "Check 7 applies only when financial content IS the page's primary structure... a line-item table, ledger, statement, voucher, or check face." This is a check face / voucher. So Check 7 wins.
> 
> Final check of the text:
> "INVOICE DATE", "INVOICE NO.", "DESCRIPTION", "INVOICE AMOUNT", "NET AMOUNT".
> It explicitly says "INVOICE AMOUNT".
> Therefore, `invoice`.
> 
> Scratchpad summary:
> - file_folder: no — has financial data, vendor info, invoice details.
> - handwritten: no — typed throughout.
> - fax: no — no fax header.
> - questionnaire: no — no survey.
> - resume: no.
> - scientific_publication: no — no journal ID.
> - financial document (invoice): yes — "INVOICE DATE", "INVOICE NO.", "INVOICE AMOUNT", vendor "ALLTECH ASSOCIATES INC.", check number, check date, amount "$194.50". This is a payment voucher/check face for an invoice.
> - specification: no.
> - presentation: no.
> - form: no — check 7 (financial document) takes precedence over check 10 (administrative form) when financial content is the primary structure (check face/voucher).
> - correspondence: no.
> - news_article: no.
> - scientific_report: no.
> - advertisement: no.
> 
> Runner-up: form, ruled out because the page's primary structure is a financial payment record/check face with invoice details (Check 7), which overrides the generic administrative form check (Check 10).
> Runner-up 2: budget, ruled out because it is a payment for a specific vendor invoice (one-off/completed work) rather than a periodic customer statement or internal budget tracking.
> 
> Label: invoice.

---

### `rvl_cdip__budget__0008.png`
**Expected:** `budget` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> Document analysis:
> - Header: "LEO BURNETT U.S.A. A DIVISION OF LEO BURNETT COMPANY, INC. ADVERTISING"
> - Title: "MAGAZINE ESTIMATE RECAP - PMO1(D)"
> - Period: "01/01/89 TO 12/31/89"
> - Date: "02/10/89"
> - Client: "P.M. INC."
> - Desc: "702A CAMBRIDGE SUPPLEMENTS"
> - Table: "TOTALS BY PRODUCT/MONTH ON SALE DATE" with columns PRODUCT, PERIOD, GROSS AMOUNT, GROSS CHANGE, GROSS LESS C/D.
> - Rows: 32-CAMBRIDGE, APR 1989, MAY, QUARTER 2, SEP, QUARTER 3, OCT, QUARTER 4, TOTAL.
> - Bottom right: Bates number "2040766038"
> - Bottom left: "FORM M-01 REV 05-82"
> 
> Let's go through the checks:
> 
> 1. IDENTIFIER-ONLY PAGE -> file_folder
>    - Has a table with financial data, headers, etc. Not identifier-only.
>    - Not this check.
> 
> 2. MAJORITY-HANDWRITTEN PAGE -> handwritten
>    - Typed throughout.
>    - Not this check.
> 
> 3. FAX TRANSMISSION SHEET -> form
>    - No fax header.
>    - Not this check.
> 
> 4. SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire
>    - Not a survey.
>    - Not this check.
> 
> 5. PERSON'S CAREER HISTORY -> resume
>    - Not a resume.
>    - Not this check.
> 
> 6. PUBLISHED EVIDENCE -> scientific_publication
>    - No journal masthead.
>    - Not this check.
> 
> 7. FINANCIAL DOCUMENT -> invoice or budget
>    - "ESTIMATE RECAP"
>    - "MAGAZINE ESTIMATE RECAP - PMO1(D)"
>    - "CLIENT: P.M. INC."
>    - "DESC: 702A CAMBRIDGE SUPPLEMENTS"
>    - Table with "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D".
>    - Check 7 says: "budget: internal money planning, tracking, or disbursement... ALSO a provider's periodic customer statement... Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice... But an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
>    - Wait, the text says: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
>    - Let's re-read check 7 carefully:
>      "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
>      Wait! "estimate recap" is explicitly listed under invoice!
>      Let's re-read: "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
>      Ah! "estimate recap" is an invoice!
>      Let's check the text again: "MAGAZINE ESTIMATE RECAP - PMO1(D)".
>      "TOTALS BY PRODUCT/MONTH ON SALE DATE"
>      "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D".
>      This is an estimate recap from an agency (Leo Burnett) to a client (P.M. Inc.). It lists charges (Gross Amount, Gross Change, Gross Less C/D).
>      Wait, is it budget or invoice?
>      "invoice: ... agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges..."
>      Yes, "estimate recap" is explicitly an invoice under check 7.
>      Let's double check budget: "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>      Wait, there's a distinction.
>      "invoice: ... estimate recap ... listing ACTUAL billable charges"
>      "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>      Let's look at the table: "ON SALE DATE", "APR 1989", "MAY", "QUARTER 2", "SEP", "QUARTER 3", "OCT", "QUARTER 4". Period is "01/01/89 TO 12/31/89". Date of document is "02/10/89".
>      The table shows "GROSS AMOUNT" 144,288.74 for APR 1989. "GROSS CHANGE" 72,144.37. "GROSS LESS C/D" 141,835.84.
>      This looks like an estimate recap of charges. The header says "ESTIMATE RECAP".
>      Is it billing completed work or projecting future work?
>      "APR 1989", "MAY", "QUARTER 2" (which is May, June, July). "SEP", "QUARTER 3". "OCT", "QUARTER 4".
>      Since the document date is 02/10/89, and it covers 01/01/89 to 12/31/89, it's likely an estimate/recap of the budget or charges for the year.
>      Wait, the check 7 text says:
>      "invoice: ... agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
>      "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
>      This is tricky. "ESTIMATE RECAP" is in both.
>      Let's look at the columns: "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D". "C/D" usually means Commission/Discount or Commission/Disbursements. This is typical advertising agency billing (Gross amount, less commission/disbursements = net).
>      If it's an estimate recap of charges, it's an invoice.
>      Let's re-read the invoice definition: "an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
>      The document is from Leo Burnett (an advertising agency) to P.M. Inc. (client). It's an "ESTIMATE RECAP". It lists "GROSS AMOUNT", "GROSS CHANGE", "GROSS LESS C/D". This is a billing document (invoice) for advertising services.
>      Wait, could it be a form? "FORM M-01 REV 05-82" is at the bottom left.
>      Check 10: "administrative form -> form. Filled or blank fields... A form does NOT have to be blank... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
>      So if it's a billing document, it's invoice (check 7), overriding form (check 10).
>      Is it budget or invoice?
>      "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
>      "invoice: ... an agency/vendor billing document for COMPLETED work: ... estimate recap ... listing ACTUAL billable charges"
>      "budget: ... an agency/vendor estimate or recap that projects upcoming placements/periods ... plans projected spend rather than billing completed work — budget, not invoice."
>      The table has "ON SALE DATE", "APR 1989", "MAY", "QUARTER 2", etc. These are past/current months relative to Feb 1989. It's likely a recap of actuals or an estimate of actuals for the year. Given "GROSS LESS C/D" (Commission/Disbursements), this is a standard agency invoice/billing format. Leo Burnett is the vendor, P.M. Inc. is the client. Vendor billing client = invoice.
>      Let's assume invoice.
> 
> Let's check the labels again.
> 1. file_folder: no
> 2. handwritten: no
> 3. form (fax): no
> 4. questionnaire: no
> 5. resume: no
> 6. scientific_publication: no
> 7. invoice/budget: yes. "MAGAZINE ESTIMATE RECAP", "CLIENT: P.M. INC.", "LEO BURNETT U.S.A.", table with "GROSS AMOUNT", "GROSS LESS C/D". Vendor billing client. Invoice.
> 8. specification: no
> 9. presentation: no
> 10. form: "FORM M-01 REV 05-82" is present, but check 7 says "It does NOT cover money records: billing documents are invoice (check 7)". So invoice overrides form.
> 11. correspondence: no
> 12. news_article: no
> 13. scientific_report: no
> 14. advertisement: no
> 
> Let's verify invoice vs budget.
> "invoice: ... an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> The document is an "ESTIMATE RECAP" from Leo Burnett (vendor) to P.M. Inc. (client). It lists gross amounts and "GROSS LESS C/D" (which is net billing). This is a billing document (invoice).
> Therefore, invoice.
> 
> Let's do the scratchpad.
> Check 1: file_folder. Evidence: none. Has a full table of financial data.
> Check 2: handwritten. Evidence: none. Typed text.
> Check 3: fax. Evidence: none.
> Check 4: questionnaire. Evidence: none.
> Check 5: resume. Evidence: none.
> Check 6: scientific_publication. Evidence: none.
> Check 7: invoice/budget. Evidence: "LEO BURNETT U.S.A." (vendor), "CLIENT: P.M. INC.", "MAGAZINE ESTIMATE RECAP", table with "GROSS AMOUNT", "GROSS LESS C/D". Vendor billing document for services. Invoice.
> Check 8: specification. Evidence: none.
> Check 9: presentation. Evidence: none.
> Check 10: form. Evidence: "FORM M-01 REV 05-82" at bottom left. But check 7 overrides money records/billing documents.
> Check 11: correspondence. Evidence: none.
> Check 12: news_article. Evidence: none.
> Check 13: scientific_report. Evidence: none.
> Check 14: advertisement. Evidence: none.
> 
> Runner-up: form, ruled out because check 7 explicitly states that billing documents (money records) are invoice, overriding the form layout (check 10).
> 
> Final label: invoice.
> Wait, let's re-read the budget definition just in case.
> "budget: ... Money PLANNING for future work is budget: an agency/vendor estimate or recap that projects upcoming placements/periods (e.g. an "ESTIMATE RECAP" of planned bus-shelter ad buys by future month) plans projected spend rather than billing completed work — budget, not invoice."
> Does this document project future work or bill completed work?
> Date: 02/10/89. Period: 01/01/89 TO 12/31/89.
> Table shows: APR 1989 (144,288.74), MAY (.00), QUARTER 2 (144,288.74), SEP (72,144.37), QUARTER 3 (72,144.37), OCT (72,144.37), QUARTER 4 (72,144.37).
> Total: 288,577.48.
> Since it's Feb 1989, April, September, October are in the future. But it has "GROSS AMOUNT" and "GROSS LESS C/D". In advertising, an "estimate recap" is often a document that recaps the estimated charges for the year, which serves as the billing/invoice basis or tracks the budget. However, the check explicitly says: "invoice: ... agency/vendor billing document for COMPLETED work: ... estimate recap ... listing ACTUAL billable charges". And "budget: ... estimate or recap that projects upcoming placements ... plans projected spend rather than billing completed work".
> Given "GROSS LESS C/D" (Commission/Disbursements), this is a standard agency invoice format. Leo Burnett is billing P.M. Inc. Even if it's an "estimate" recap, it's a vendor billing document. The presence of "CLIENT:" and vendor name strongly points to invoice (billing). I will go with invoice.
> 
> Let's double check if there's any other category.
> Could it be a form? "FORM M-01 REV 05-82". But check 7: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)." So invoice is correct.
> 
> I'm confident in invoice.

---

## file_folder → presentation (2 errors)

### `rvl_cdip__file_folder__0004.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There is a Bates number "2065213892" and a rotated text "PRODUCT INTEGRITY - FDA - PRESENTATION". There is a faint vertical text on the top left, maybe a Bates number or archive ID, but it's very faint. Let's look closer. "2065213892" is clearly visible. "PRODUCT INTEGRITY - FDA - PRESENTATION" is rotated 90 degrees.
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: "PRODUCT INTEGRITY - FDA - PRESENTATION" is a bold topical heading (rotated 90 degrees). "2065213892" is a Bates number.
>     *   Rule: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." "A prominent topical heading always counts as real content, subtitle or not." "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder".
>     *   Is this a folder tab? The text is "PRODUCT INTEGRITY - FDA - PRESENTATION". This sounds like a presentation title or section divider, not a folder tab label (which would be like "NEWTROL", "Litigation Content", "FEBRUARY"). Wait, let's look at the layout. It's mostly blank white space. There's a black bar at the bottom (scan artifact for slide?). The text is sparse and off-center (lower right, rotated).
>     *   Rule for presentation: "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."
>     *   So this is likely a presentation cover/divider or slide.
> 
> *   **Check 2: handwritten**
>     *   Evidence: None. Mostly blank.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: None.
> 
> *   **Check 4: questionnaire**
>     *   Evidence: None.
> 
> *   **Check 5: resume**
>     *   Evidence: None.
> 
> *   **Check 6: scientific_publication**
>     *   Evidence: None. No journal header.
> 
> *   **Check 7: financial document**
>     *   Evidence: None.
> 
> *   **Check 8: specification**
>     *   Evidence: None.
> 
> *   **Check 9: presentation**
>     *   Evidence: "PRODUCT INTEGRITY - FDA - PRESENTATION" is a bold headline title. The page is mostly empty space (sparse text). There is a solid black bar along the bottom edge (scan artifact). The text is placed off-center (lower right, rotated).
>     *   Rule: "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation (this check), not file_folder (check 1)." "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
>     *   This fits perfectly. It's a slide or deck cover. "PRODUCT INTEGRITY - FDA - PRESENTATION".
> 
> *   **Check 10: form**
>     *   Evidence: None.
> 
> *   **Check 11: correspondence**
>     *   Evidence: None.
> 
> *   **Check 12: news_article**
>     *   Evidence: None.
> 
> *   **Check 13: scientific_report**
>     *   Evidence: None. No running prose.
> 
> *   **Check 14: advertisement**
>     *   Evidence: None.
> 
> **Conclusion:**
> The page is a near-blank page with a bold rotated heading "PRODUCT INTEGRITY - FDA - PRESENTATION" and a Bates number "2065213892". There is a black bar at the bottom. This matches the "presentation" category (slide deck cover or section divider). The heading is a topical title, not a folder tab label (it names a presentation topic, not a folder contents like a product name or date range in a filing context, although "PRESENTATION" is in the text, it's the title of the deck/section). Wait, let's re-read the folder tab rule. "a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab (product/collection/month/file name, e.g. 'NEWTROL', 'Litigation Content', 'FEBRUARY') is a folder-tab label and stays file_folder". "PRODUCT INTEGRITY - FDA - PRESENTATION" is a title for a presentation, not a folder tab label. Also, the scan artifact (black bar) and sparse text point to a slide.
> 
> Let's check the text again: "PRODUCT INTEGRITY - FDA - PRESENTATION". This is clearly a title for a presentation.
> The layout is sparse, mostly white space, text rotated 90 degrees in the lower right area. Black bar at the bottom.
> This is a presentation (slide cover or section divider).
> 
> Final check:
> - file_folder: No, has a prominent topical heading "PRODUCT INTEGRITY - FDA - PRESENTATION".
> - presentation: Yes, near-blank cover/title page with bold headline title, sparse text, scan artifact (black bar).
> 
> Label: presentation.

---

### `rvl_cdip__file_folder__0006.png`
**Expected:** `file_folder` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header:** None. No From/To/Sent/Subject.
> - **Masthead/Running head:** No newspaper/magazine masthead. No journal running head with volume/issue/page number. There is a Bates number "2061696347" on the right side. There is a name "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74".
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a large graphic/image (looks like a map or abstract shape with "ISSUE MODULE PRODUCT INTEGRITY" and "PHILIP MORRIS INTERNATIONAL" text overlaid). It has a name "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74". It has a Bates number "2061696347".
>     *   Is it a folder tab? No, it looks like a designed title page or slide. The text "ISSUE MODULE PRODUCT INTEGRITY" is a bold headline title. "PHILIP MORRIS INTERNATIONAL" is at the bottom.
>     *   Wait, let's look closer. It looks like a slide or a presentation cover. "ISSUE MODULE PRODUCT INTEGRITY". "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74".
>     *   Check 1 says: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only." "A prominent topical heading always counts as real content... even alongside a small handwritten letter or number annotation".
>     *   This page has a prominent heading "ISSUE MODULE PRODUCT INTEGRITY" and "PHILIP MORRIS INTERNATIONAL". It looks like a slide or a cover page. So not file_folder.
> 
> *   **Check 2: handwritten**
>     *   Evidence: None. It's typed/printed text and graphics.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: None. No "FACSIMILE" header.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: None. No questions, no survey instrument.
> 
> *   **Check 5: PERSON'S CAREER HISTORY -> resume**
>     *   Evidence: None. "Roger Whidden" is just a name, not a full CV.
> 
> *   **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
>     *   Evidence: No journal name, volume, issue, page range.
> 
> *   **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
>     *   Evidence: None. No financial data.
> 
> *   **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
>     *   Evidence: None. No MDS, no formulation, no "shall/must".
> 
> *   **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
>     *   Evidence: "ISSUE MODULE PRODUCT INTEGRITY" is a bold title. "PHILIP MORRIS INTERNATIONAL" is at the bottom. "Roger Whidden", "PM - Worldwide Regulatory Affairs", "Control #74". This looks like a title slide or a section divider for a presentation.
>     *   Check 9 says: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... a single-word/short-phrase heading with no subtitle at all... is a presentation".
>     *   The layout is sparse. Large text "ISSUE MODULE PRODUCT INTEGRITY". "PHILIP MORRIS INTERNATIONAL". A graphic background (looks like a map or abstract shape).
>     *   "Technical-study title pages... is scientific_report". This doesn't look like a technical study title page. It looks like a corporate presentation slide/cover. "ISSUE MODULE" sounds like a corporate program or module.
>     *   "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead". There are black bars at the top and bottom. The text is sparse.
>     *   This fits "presentation" (deck cover or section divider).
> 
> *   **Check 10: ADMINISTRATIVE FORM -> form**
>     *   Evidence: None. No fields, boxes, checkboxes.
> 
> *   **Check 11: CORRESPONDENCE -> email, memo, or letter**
>     *   Evidence: None. No TO/FROM/RE header, no salutation, no closing.
> 
> *   **Check 12: PUBLISHED JOURNALISM -> news_article**
>     *   Evidence: None. No masthead, byline, dateline.
> 
> *   **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
>     *   Evidence: None. No running narrative prose.
> 
> *   **Check 14: PROMOTIONAL MATERIAL -> advertisement**
>     *   Evidence: None. Not a product ad with slogans/imagery in a marketing sense, though it has the company name. It looks like an internal presentation cover.
> 
> **Re-evaluating Check 9 vs Check 1:**
> The page has "ISSUE MODULE PRODUCT INTEGRITY" and "PHILIP MORRIS INTERNATIONAL".
> Is it a folder tab?
> Check 1: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
> This page has a large graphic, text overlaid on a map-like shape. It doesn't look like a folder tab. A folder tab is usually a small protruding piece of cardboard. This looks like a full page scan of a slide or a designed cover page.
> The text "ISSUE MODULE PRODUCT INTEGRITY" is a bold headline title.
> Check 9: "a deck title or section-divider page... A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation".
> The page has a large graphic background (looks like a map of the world or a continent, maybe South America/Africa? Actually looks like a stylized map). Text "ISSUE MODULE PRODUCT INTEGRITY" is in the center. "PHILIP MORRIS INTERNATIONAL" at the bottom. "Roger Whidden / PM - Worldwide Regulatory Affairs / Control #74" at the top right.
> This is definitely a presentation cover or section divider. "Issue Module" sounds like a module in a training or corporate presentation.
> 
> Let's look at the "Scan-artifact signal" in Check 9: "a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation".
> There is a thick black bar at the top and bottom. The text is sparse. The background is a high-contrast, grainy image (looks like a slide scan).
> This fits presentation perfectly.
> 
> **Runner-up:** file_folder. Ruled out because the page carries a prominent topical heading ("ISSUE MODULE PRODUCT INTEGRITY") and a designed layout (company name, author name), not just filing metadata. It's a slide/cover page.
> 
> **Final decision:** presentation.
> 
> Let's double check Check 13 (scientific_report).
> "Technical-study title pages: a title page naming a specific study or methodology with a date... is scientific_report".
> Title: "ISSUE MODULE PRODUCT INTEGRITY". Not a specific study/methodology. "Roger Whidden, PM - Worldwide Regulatory Affairs". Not a scientific author/affiliation in the typical sense (though PM is a company). "Control #74".
> This is corporate/regulatory affairs. "Issue Module" likely refers to a public affairs or regulatory issue module.
> So presentation is correct.
> 
> Let's double check Check 1 (file_folder).
> "A prominent topical heading always counts as real content... even alongside a small handwritten letter or number annotation".
> "ISSUE MODULE PRODUCT INTEGRITY" is a prominent heading.
> "PHILIP MORRIS INTERNATIONAL" is a company name.
> This is content. Not file_folder.
> 
> So, presentation.
> 
> One detail: "Control #74". This looks like a slide number or control number for a presentation deck.
> "Roger Whidden, PM - Worldwide Regulatory Affairs". Presenter name.
> "ISSUE MODULE PRODUCT INTEGRITY". Title.
> "PHILIP MORRIS INTERNATIONAL". Company.
> This is a title slide for a presentation.
> 
> Label: presentation.

---

## presentation → form (2 errors)

### `rvl_cdip__presentation__0001.png`
**Expected:** `presentation` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "2071860450" and "Philip Morris USA" at the bottom (rotated). No journal masthead.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of data: "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION", tables with "Share of Market", "Price Gaps", etc. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Typed text throughout. No majority handwriting.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No career history.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal running head.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: Contains financial data (shares, pricing, Nielsen data), but it's a performance triggers table, not an invoice or budget (internal money planning/tracking). Wait, is it a budget? No, it's market share data.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No material safety data, no product formulation, no "shall/must".
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: The page is rotated 90 degrees. It has a title "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION (4WM Nielsen Shares, Biweekly Consumer Shares, Nielsen Pricing) As of 6/15/98". It has a table of data. Wait, is this a presentation slide or a form?
> - Let's look at the layout. It's a table with rows and columns. "Share of Market", "Share of Segment", "Share of Young Adults", "Price Gaps", "Promotion Incidence".
> - Wait, check 9 says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> - Let's check check 10.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
> - The page is a labeled data chart/table: "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION" with rows like "Philip Morris USA", "Marlboro", "Premium Category", etc., and columns "Trigger 1H 1998", "Latest Data 4WM", "98 O.B.", "FULL YR 1997", "4th QTR 1997".
> - This is a standalone labeled data chart/table.
> - Wait, is it a presentation? "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..." This page is dense with data, a table. Check 9 explicitly says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> - So this is a form.
> 
> Let's re-read check 9 and 10 carefully.
> Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> Check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
> 
> The page is a table of values: "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION". It has rows (Philip Morris USA, Marlboro, etc.) and columns (Trigger 1H 1998, Latest Data 4WM, etc.).
> It is a labeled data chart/table.
> Therefore, it is a form.
> 
> Let's double check if there's any other category.
> Could it be a scientific_report? No running prose.
> Could it be a budget? No, it's market share data, not internal money planning.
> Could it be an invoice? No.
> 
> The document is a table of performance triggers (market share, pricing, promotion incidence) for Philip Morris USA. It's a data table.
> According to the rules: "a standalone labeled data chart or table ... is a form (check 10)".
> 
> Let's review the scratchpad steps:
> 1. file_folder: no, has real content (table).
> 2. handwritten: no, typed.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. invoice/budget: no, it's market share data, not financial document (invoice/budget). Wait, check 7 says "financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." This is market share, not financial (money) content.
> 8. specification: no.
> 9. presentation: no, "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> 10. form: yes, "standalone labeled data chart or table".
> 
> Runner-up: presentation, ruled out because the page is a standalone labeled data chart/table of values, which the rules explicitly classify as a form (check 10), not a slide.
> 
> Let's confirm the text on the page.
> "Philip Morris USA"
> "PM-USA PERFORMANCE TRIGGERS FOR DISCUSSION"
> "(4WM Nielsen Shares, Biweekly Consumer Shares, Nielsen Pricing) As of 6/15/98"
> Columns: Trigger 1H 1998, Latest Data 4WM, 98 O.B., FULL YR 1997, 4th QTR 1997.
> Rows: Share of Market (Philip Morris USA, Marlboro, Premium Category, Basic Less GPC (Shipments), Basic Less Doral (Shipments)), Share of Segment, Share of Young Adults, Price Gaps, Promotion Incidence.
> Footer: "2071860450" (Bates number).
> 
> This is definitely a standalone labeled data chart/table.
> Label: form.

---

### `rvl_cdip__presentation__0011.png`
**Expected:** `presentation` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header: None.
> - Masthead/running head: None. There's a B&W logo, a title "American Key Brand Shares And Percent of Shipments", a pie chart, and a footer "May 1993 MSA 12mm Share" with a Bates number "361002052".
> 
> **2. Scratchpad checks:**
> - Check 1: file_folder. The page has a pie chart and a title "American Key Brand Shares And Percent of Shipments". It has real content (a chart and title). Not file_folder.
> - Check 2: handwritten. No handwriting. Not handwritten.
> - Check 3: FAX TRANSMISSION SHEET. No fax header. Not this.
> - Check 4: questionnaire. No survey questions. Not this.
> - Check 5: resume. No career history. Not this.
> - Check 6: scientific_publication. No journal running head. Not this.
> - Check 7: financial document (invoice/budget). The chart shows brand shares and percent of shipments (numbers like 1.38, 1.32, 19.8%, etc.). This is market share data, not an invoice or budget. Not this.
> - Check 8: specification. No material safety data, product formulation, or "shall/must" language. Not this.
> - Check 9: presentation. The page is a pie chart with a title "American Key Brand Shares And Percent of Shipments", a B&W logo, and a footer "May 1993 MSA 12mm Share". The layout is sparse, chart-per-page look. Wait, let's look at the rules for presentation. "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)... A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." Wait. "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." Let's re-read check 9 and check 10 carefully.
>     - Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." Wait, let's read check 10.
>     - Check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
>     - Let's look at the page again. It's a pie chart titled "American Key Brand Shares And Percent of Shipments". It has labels like PALL MALL 1.38, CARLTON 1.32, etc. It's a chart.
>     - Wait, is it a form? "A standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values) ... is a form".
>     - Let's re-read check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
>     - So a chart is a form? Let's check the labels. "form" is one of the labels.
>     - Let's re-read check 10: "Administrative form -> form. Filled or blank fields... This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
>     - The page has a pie chart with data values (percentages and numbers like 1.38, 1.32). It is a standalone labeled data chart. So it should be `form`.
>     - Wait, is there any other category? "presentation" says "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)." This is a very specific rule.
>     - Let's check if there's any other evidence. The page has a B&W logo (B&W - Brown & Williamson?), title "American Key Brand Shares And Percent of Shipments", pie chart, footer "May 1993 MSA 12mm Share", Bates number "361002052".
>     - It's a chart of market share data. According to the rules: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
>     - Let's verify this rule in Check 9: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
>     - Let's verify this rule in Check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
>     - So the label is `form`.
> 
> Let's double check.
> - Is it a presentation? Check 9 explicitly says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> - Is it a scientific_report? No running prose.
> - Is it a specification? No.
> - Is it a budget? No, it's market share data, not internal money planning.
> - Is it an invoice? No.
> 
> The page is a pie chart showing brand shares. It is a standalone labeled data chart. Therefore, it is a form.
> 
> Wait, is there any possibility it's a presentation?
> "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look)..."
> But the caveat in Check 9 says: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> This caveat overrides the general "chart-per-page deck look" description. The page is literally just a chart with a title and footer. It has no running text, no bullets. It's a chart. So it falls under the caveat -> form.
> 
> Let's review the evidence for `form`:
> - Check 10: "This also covers: a standalone labeled data chart or table (e.g. "CHART 1" with rows A-Z and numeric values)..."
> - The page contains a pie chart with labeled data values (percentages and shipment numbers for brands like Pall Mall, Carlton, Montclair, Misty Slims, etc.).
> - Check 9 explicitly rules out presentation for standalone charts: "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> 
> Therefore, the label is `form`.
> 
> Let's do a quick pass of other checks to be sure.
> 1. file_folder: No, has real content (chart + title).
> 2. handwritten: No.
> 3. fax: No.
> 4. questionnaire: No.
> 5. resume: No.
> 6. scientific_publication: No journal head.
> 7. financial: No, market share data, not invoice/budget.
> 8. specification: No.
> 9. presentation: Ruled out by caveat "A standalone chart or table of values alone is NOT a slide — it is a form (check 10)."
> 10. form: Yes, standalone labeled data chart.
> 11. correspondence: No.
> 12. news_article: No.
> 13. scientific_report: No running prose.
> 14. advertisement: No, it's a data chart, not a marketing layout with slogans/imagery (though it has brand names, it's a market share chart, not an ad).
> 
> Final decision: form.

---

## presentation → file_folder (2 errors)

### `rvl_cdip__presentation__0017.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "2071969205" and a small "F" or similar mark at the top right. The left side has some faint, noisy, vertical banding, possibly a scanned artifact or a very faint image, but mostly blank. Wait, let's look closer.
> - The left side has a vertical band of noise/artifacts.
> - Bottom right has "2071969205" rotated 90 degrees.
> - Top right has a small "F" or similar symbol.
> - This looks like a mostly blank page with a Bates number and some scan artifacts.
> 
> **2. Scratchpad procedure:**
> 
> *Check 1: IDENTIFIER-ONLY PAGE -> file_folder*
> - Evidence: The page is almost entirely blank. There is a Bates number "2071969205" at the bottom right (rotated). There is a small "F" or similar mark at the top right. The left side has vertical noise/artifacts, possibly from a scan edge or a very faint image, but no readable text, no topical title, no sentences.
> - Wait, is there a folder tab? The left side has a vertical band of noise. It could be a photographed folder tab, but it looks more like scan noise. Let's re-read the file_folder definition.
> - "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
> - "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content"
> - Here, we have a Bates number "2071969205". Is there a photographic image? The left side has a vertical band of grainy texture. It looks like a scanned edge of a page or a very faint, degraded image. Let's look at the bottom left. There's a darker rectangular area with horizontal lines. It looks like a degraded scan of a chart or text, but it's completely illegible.
> - Wait, look at the top right: "F" or a rotated "L" or a bracket.
> - Let's look at the left side again. It's a vertical strip of noise. Bottom left is a darker block of noise. This looks like a blank page with scan artifacts (dust, edge noise).
> - If it's just a Bates number and scan noise, is it file_folder?
> - "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
> - "Scan noise is not handwriting... If the dominant recognizable elements are a stamp, faint archival text, or an ID/number, with only a small rotated handwritten annotation on the side, classify by the stamp/identifier (often file_folder)..."
> - This page has a Bates number "2071969205". The rest is blank/noise. This fits "file_folder" (identifier-only page).
> 
> Let's check other checks just in case.
> 
> *Check 2: handwritten*
> - No handwriting visible.
> 
> *Check 3: FAX*
> - No fax header.
> 
> *Check 4: questionnaire*
> - No questions.
> 
> *Check 5: resume*
> - No career history.
> 
> *Check 6: scientific_publication*
> - No journal header.
> 
> *Check 7: financial*
> - No financial data.
> 
> *Check 8: specification*
> - No product data.
> 
> *Check 9: presentation*
> - "A near-blank cover or title page... is a presentation... EXCEPTION: ... a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab ... is file_folder".
> - "A standalone photographic image ... carrying only a Bates number is a photographic slide (this check), not file_folder".
> - Is the left side a photographic image? It looks like vertical scan noise (dust/scratches on the scanner glass or edge of the paper). It doesn't look like a deliberate photograph. It looks like a blank page scanned with some edge artifacts.
> - "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB".
> - Here, there is no text, just noise. The Bates number is the only clear content.
> - "If the dominant recognizable elements are a stamp, faint archival text, or an ID/number... classify by the stamp/identifier (often file_folder)".
> - This strongly points to file_folder.
> 
> *Check 10: form*
> - No fields.
> 
> *Check 11: correspondence*
> - No text.
> 
> *Check 12: news_article*
> - No masthead.
> 
> *Check 13: scientific_report*
> - No prose.
> 
> *Check 14: advertisement*
> - No ad content.
> 
> **Conclusion:**
> The page is essentially blank with a Bates number "2071969205" and some scan artifacts (vertical noise on the left, possibly a scanned edge or dust). The dominant recognizable element is the Bates number/ID. This fits the definition of `file_folder` (identifier-only page).
> 
> Let's re-evaluate "presentation" (Check 9).
> - "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation". There is no bold headline title.
> - "A standalone photographic image (people, a scene, an event photo) carrying only a Bates number is a photographic slide (this check), not file_folder". The left side is not a clear photographic image; it's vertical noise/grain. It looks like a blank page with scanner artifacts.
> - "Scan noise is not handwriting... If the dominant recognizable elements are a stamp, faint archival text, or an ID/number... classify by the stamp/identifier (often file_folder)".
> 
> Therefore, `file_folder` is the correct classification.
> 
> Wait, is there a folder tab?
> - "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number stamped on the folder body."
> - The left side noise could be the edge of a folder tab, but there's no readable label. Even if there is, it's file_folder.
> - The definition says: "A page is NOT file_folder if it carries any real content... A prominent topical heading always counts as real content". There is no prominent topical heading.
> - "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content".
> - Here, we have a Bates number. Is there a photographic image? The left side is just noise. It doesn't look like a deliberate photo. It looks like a blank page.
> - So it's file_folder.
> 
> Let's double check the "F" at the top right. It looks like a small logo or mark. Maybe a Bates number prefix or a page marker. Doesn't change the classification.
> 
> Final decision: file_folder.
> 
> Scratchpad:
> - file_folder: yes — page is almost entirely blank/white space with only a Bates number "2071969205" (rotated) and a small mark "F" at top right; left side has vertical scan noise/artifacts but no readable text, topical title, or clear photographic image. Dominant recognizable element is the ID number.
> - presentation: no — no bold headline title, no designed deck page, no clear photographic slide image (left side is scan noise, not a deliberate photo).
> - Runner-up: presentation, ruled out because there is no bold title or clear image, just a Bates number and scan artifacts.
> 
> Wait, looking very closely at the left side... it's a vertical band of static. Bottom left is a darker block. This is typical of a blank page scanned with a dirty scanner platen or edge. It's not a photograph.
> So file_folder is correct.
> 
> One more check: "A page whose only purpose is labeling a folder or index entry for ONE item... Pure filing metadata only."
> The Bates number is filing metadata.
> 
> Label: file_folder.

---

### `rvl_cdip__presentation__0018.png`
**Expected:** `presentation` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> Image analysis:
> - The page is mostly blank white space.
> - There is a thick black vertical line on the right side.
> - Top right, rotated 90 degrees: "1991-84" and "foundation". Wait, let's look closer. "1991-84" and "foundation". Actually, it looks like "1991-84" and "foundation" or "foundation" is something else. Let's re-read: "1991-84" and "foundation". Wait, it's "1991-84" and "foundation" written vertically. Let's assume it's a label.
> - Bottom right, near the black line: "465246617" (Bates number).
> - The black line on the right edge is a solid black bar. This is a common scanning artifact for slides/transparencies or photographed folder tabs.
> - Let's check the rules for file_folder vs presentation.
> - Check 1: IDENTIFIER-ONLY PAGE -> file_folder.
>   - "Almost no body content: only an archive/Bates number, a stamp, a short label or ID, folder/box markings, or a filing index card... No sentences, no topical title."
>   - "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard... bearing a short filing label that names the folder's contents... usually with a Bates number stamped on the folder body. The label IS filing metadata... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees, even when the folder body photographs as a solid black bar/border along one or more edges..."
>   - "How to tell a folder-tab page from a presentation cover/divider (check 9): a folder-tab page's ENTIRE content is the tab, its short filing label, and a Bates/stamp — nothing else is designed on the page. A presentation cover/divider is a DESIGNED title page... If the page is ONLY a folder tab with its label and a Bates number, it is file_folder, not presentation."
>   - "Scan-artifact signal: a solid black bar along one edge of the page... combined with sparse text placed off-center... points to a photographed slide/overhead — presentation — even if the sparse text sounds like a research title... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."
> 
> Let's look at the text: "1991-84" and "foundation". This looks like a filing label on a folder tab. "1991-84" could be a date range, "foundation" could be the collection name (e.g., "Foundation" files).
> The black bar is on the right edge. The text is rotated 90 degrees.
> This perfectly matches the "folder-tab page" description in Check 1: "a short filing label that names the folder's contents... usually with a Bates number... The page stays file_folder even when the label is rotated 90 degrees, even when the folder body photographs as a solid black bar/border along one or more edges".
> The label is "1991-84" and "foundation". This is filing metadata (date range and collection name).
> Bates number: "465246617".
> No sentences, no topical title (it's a folder tab label).
> 
> Let's check Check 9 just in case: "SLIDE DECK... -> presentation".
> "Scan-artifact signal: a solid black bar along one edge... combined with sparse text... points to a photographed slide/overhead — presentation... BUT this signal applies only to a photographic image... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label (product/collection/month/file name), and a Bates number is file_folder..."
> The text "1991-84 foundation" is a short filing label (date range + collection name). It is not a designed deck page or a photographic image of a scene/slide. It's a folder tab.
> 
> Therefore, Check 1 matches: file_folder.
> 
> Let's double check the text. "1991-84" and "foundation". Wait, could it be "1984-91"? The text is rotated. Let's read it: "1991-84" or "1984-91". It looks like "1991-84" or maybe "1984-91". Actually, it looks like "1991-84" and "foundation". Or maybe "1984-91" and "foundation". Regardless, it's a short label.
> Bates number: 465246617.
> 
> Check 1: IDENTIFIER-ONLY PAGE -> file_folder.
> Evidence: Bates number "465246617", short rotated filing label "1991-84 foundation" (or similar date range and collection name), solid black bar on the right edge (photographed folder body/tab edge). Entire content is the tab, its short filing label, and a Bates number. No sentences, no topical title.
> 
> Check 2: handwritten - no.
> Check 3: fax - no.
> Check 4: questionnaire - no.
> Check 5: resume - no.
> Check 6: scientific_publication - no.
> Check 7: financial - no.
> Check 8: specification - no.
> Check 9: presentation - no, ruled out by folder-tab exception.
> Check 10: form - no.
> Check 11: correspondence - no.
> Check 12: news_article - no.
> Check 13: scientific_report - no.
> Check 14: advertisement - no.
> 
> Final label: file_folder.
> Runner-up: presentation, ruled out because the page is a photographed file-folder tab with a short filing label ("1991-84 foundation") and a Bates number, not a designed deck page or photographic slide image (Check 1 exception to Check 9's scan-artifact signal).

---

## scientific_publication → news_article (2 errors)

### `rvl_cdip__scientific_publication__0006.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead or running head: Top of the page has "New Scientist 17 June 1982" and "M O N I T O R". Page number "772" on the top left. "Sfool 050" (Bates number?). This looks like a newspaper/magazine masthead or running head. "New Scientist" is a general-audience news outlet (science magazine). Wait, is it a research journal? "New Scientist" is a popular science magazine. Let's look at the content. It's an article titled "All routes are leading to the same few cancer genes" and "Carcinogens act on irritated tissues". It has multi-column typography, byline/dateline style (though no explicit byline, it's a magazine article). Let's check check 12.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: Page has dense text, headlines, multi-column layout. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Typed text throughout.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No CV/resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: "New Scientist 17 June 1982". New Scientist is a weekly magazine covering science and technology. Is it a research journal? No, it's a general-audience outlet (magazine). Check 6 says: "Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece ... is news_article (check 12), not a publication". New Scientist is a magazine. Let's look at check 12.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: No financial content.
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: No product specs.
> - Not this check.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - Evidence: Not a slide deck.
> - Not this check.
> 
> **Check 10: ADMINISTRATIVE FORM -> form**
> - Evidence: Not a form.
> - Not this check.
> 
> **Check 11: CORRESPONDENCE -> email, memo, or letter**
> - Evidence: Not correspondence.
> - Not this check.
> 
> **Check 12: PUBLISHED JOURNALISM -> news_article**
> - Evidence: "New Scientist 17 June 1982" at the top. "M O N I T O R" (section title). Multi-column news typography. Headlines "All routes are leading to the same few cancer genes" and "Carcinogens act on irritated tissues". This is a magazine article from New Scientist. New Scientist is a general-audience magazine (popular science). Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography... Also a magazine feature... from a GENERAL-AUDIENCE outlet". New Scientist fits this.
> - Let's verify if New Scientist is considered a research journal. No, it's a news magazine. The text cites "Nature", "Science", "Proceedings of the National Academy of Sciences", but these are references within the text. The page itself has "New Scientist 17 June 1982" and page number 772. This is a magazine page.
> - So news_article is the correct label.
> 
> **Check 13: ORIGINAL RESEARCH WRITE-UP -> scientific_report**
> - Evidence: It's a published magazine article, not an internal research write-up. The running prose is journalistic summary of research, not original research write-up with methods/results of the authors' own work (it summarizes others' work: "Edward Scolnick and his colleagues...", "The second part of this story comes from...").
> - Not this check.
> 
> **Check 14: PROMOTIONAL MATERIAL -> advertisement**
> - Evidence: Not an ad.
> - Not this check.
> 
> Let's double check Check 6 vs Check 12.
> Check 6: "Caveat — general news outlets: a page that presents itself as a newspaper, general-magazine, or encyclopedia piece ... is news_article (check 12), not a publication, even if its text is scientific, names an author with credentials, or cites journal articles as references within the prose".
> New Scientist is a general-magazine (popular science magazine). The page has "New Scientist 17 June 1982" at the top. This is a masthead/running head for a magazine.
> Therefore, news_article.
> 
> Let's review the scratchpad requirements.
> Walk checks 1-14 in order.
> State evidence or "none".
> If evidence present, STOP HERE.
> Add final line naming runner-up and evidence that ruled it out.
> 
> Check 1: file_folder. Evidence: none. (Dense text, headlines).
> Check 2: handwritten. Evidence: none. (Typed text).
> Check 3: form (fax). Evidence: none.
> Check 4: questionnaire. Evidence: none.
> Check 5: resume. Evidence: none.
> Check 6: scientific_publication. Evidence: "New Scientist 17 June 1982" is a magazine masthead, not a research journal running head. The page cites Nature, Science, PNAS, but these are references. Not this check (points to check 12).
> Check 7: invoice/budget. Evidence: none.
> Check 8: specification. Evidence: none.
> Check 9: presentation. Evidence: none.
> Check 10: form. Evidence: none.
> Check 11: correspondence. Evidence: none.
> Check 12: news_article. Evidence: "New Scientist 17 June 1982" masthead/running head, "M O N I T O R" section title, multi-column typography, headlines "All routes are leading to the same few cancer genes", "Carcinogens act on irritated tissues". This is a magazine article from a general-audience outlet.
> Runner-up: scientific_publication, ruled out because "New Scientist" is a general-audience magazine, not a research journal, and the page presents as magazine editorial content (check 12 precedes check 6 for general outlets, or rather check 6 caveat directs to check 12). Actually, check 6 says if it's a research journal's own running head, it's scientific_publication. If it's a general magazine, it's news_article. New Scientist is a general magazine.
> 
> Let's refine the scratchpad text.
> file_folder: no — page has dense multi-column text and headlines.
> handwritten: no — typed throughout.
> fax: no — no fax header.
> questionnaire: no — no survey items.
> resume: no — no career history.
> scientific_publication: no — "New Scientist 17 June 1982" is a general-audience magazine masthead, not a research journal identifier; the page cites journals (Nature, Science) but they are references in the prose. Points to check 12.
> invoice/budget: no — no financial content.
> specification: no — no product/material documentation.
> presentation: no — not a slide deck or cover.
> form: no — no administrative fields.
> correspondence: no — no TO/FROM/letter structure.
> news_article: yes — "New Scientist 17 June 1982" masthead, "M O N I T O R" section title, multi-column news typography, headlines "All routes are leading to the same few cancer genes" and "Carcinogens act on irritated tissues"; presents as magazine editorial content from a general-audience outlet.
> Runner-up: scientific_publication, ruled out because the running head "New Scientist" belongs to a general-audience magazine, not a research journal, and the page's dominant layout is magazine journalism (check 12 caveat in check 6).
> 
> Wait, the prompt says: "If nothing matches, choose the label whose defining evidence is closest...". But news_article matches check 12.
> 
> Final label: news_article.

---

### `rvl_cdip__scientific_publication__0016.png`
**Expected:** `scientific_publication` | **Predicted:** `news_article`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I need to follow a specific scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead or running head: Top right says "HOSPITAL-TRADEMARK" (wait, "HOSPITAL-TRADEMARK"? No, "HOSPITAL-TRADEMARK" is probably "HOSPITAL-TRADEMARK" or something. Let's look closely at the top right: "Monday, February 2, 1971". Top center: "HOSPITAL-TRADEMARK"? Wait, "HOSPITAL-TRADEMARK" is likely "HOSPITAL-TRADEMARK" or maybe "HOSPITAL-TRADEMARK" is a misread. Let's look at the top right: "Monday, February 2, 1971". Top center: "HOSPITAL-TRADEMARK" -> actually it looks like "HOSPITAL-TRADEMARK" or "HOSPITAL-TRADEMARK". Wait, "HOSPITAL-TRADEMARK" is probably "HOSPITAL-TRADEMARK". Let's re-read: "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". Ah, "HOSPITAL-TRADEMARK" is probably "HOSPITAL-TRADEMARK". Let's look at the top right: "Monday, February 2, 1971". Top center: "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". Wait, "HOSPITAL-TRADEMARK" is likely "HOSPITAL-TRADEMARK". Let's assume it's a newspaper/magazine masthead. "Monday, February 2, 1971" is a date. "16" is a page number. This looks like a newspaper page. "Theory of Emphysema CauseRaisesQuestions" is a headline. "Surgeon General" is a column. "Clinic at U. of Va. Offers Health Care to Families" is another headline. "Antitrypsin Lack Might Increase Fertility" is another. This is clearly a newspaper or magazine page. Let's check for masthead. Top right: "Monday, February 2, 1971". Top center: "HOSPITAL-TRADEMARK" -> maybe "HOSPITAL-TRADEMARK" is "HOSPITAL-TRADEMARK". Actually, it looks like "HOSPITAL-TRADEMARK" is "HOSPITAL-TRADEMARK". Wait, "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". Let's assume it's a newspaper. "Monday, February 2, 1971" is a date. Page number 16. Multi-column news typography. Bylines: "By Jack Lieberman", "By Dr. James L. Adamson". This is a news article.
> 
> Let's check the checks in order.
> 
> 1. IDENTIFIER-ONLY PAGE -> file_folder: No, lots of text.
> 2. MAJORITY-HANDWRITTEN PAGE -> handwritten: No, typed.
> 3. FAX TRANSMISSION SHEET -> form: No.
> 4. SURVEY INSTRUMENT -> questionnaire: No.
> 5. PERSON'S CAREER HISTORY -> resume: No.
> 6. PUBLISHED EVIDENCE -> scientific_publication: No journal running head on THIS page. The top says "Monday, February 2, 1971" and "16". "HOSPITAL-TRADEMARK" might be "HOSPITAL-TRADEMARK". Wait, is it a journal? "Monday, February 2, 1971" is a newspaper date. "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". Actually, it's "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". Let's assume it's a newspaper. "Monday, February 2, 1971" is definitely a newspaper date format.
> 7. FINANCIAL DOCUMENT -> invoice/budget: No.
> 8. PRODUCT OR MATERIAL DOCUMENTATION -> specification: No.
> 9. SLIDE DECK -> presentation: No.
> 10. ADMINISTRATIVE FORM -> form: No.
> 11. CORRESPONDENCE -> email/memo/letter: No.
> 12. PUBLISHED JOURNALISM -> news_article: Yes. Newspaper/magazine masthead (or date/page number layout), multi-column news typography, bylines ("By Jack Lieberman"), dateline ("Monday, February 2, 1971"), headlines ("Theory of Emphysema CauseRaisesQuestions", "Clinic at U. of Va. Offers Health Care to Families", "Antitrypsin Lack Might Increase Fertility"). This is a newspaper page.
> 13. ORIGINAL RESEARCH WRITE-UP -> scientific_report: No, it's a news article about science.
> 14. PROMOTIONAL MATERIAL -> advertisement: No.
> 
> Let's re-evaluate check 6 vs 12.
> Check 6: "does THIS page itself carry a running head/masthead with volume, issue, page range, DOI, or copyright line belonging to a journal or published proceedings?"
> The page has "16" (page number), "Monday, February 2, 1971" (date). This is a newspaper layout. "HOSPITAL-TRADEMARK" is probably "HOSPITAL-TRADEMARK" or "HOSPITAL-TRADEMARK". Actually, it might be "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". Wait, "HOSPITAL-TRADEMARK" is likely "HOSPITAL-TRADEMARK". Let's look at the text: "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". It's probably "HOSPITAL-TRADEMARK". Regardless, "Monday, February 2, 1971" and page "16" and multi-column layout with headlines and bylines is classic newspaper.
> Check 12: "Newspaper or magazine masthead, byline, dateline, multi-column news typography, '- more -' continuation, or wire-service credit."
> We have bylines ("By Jack Lieberman", "By Dr. James L. Adamson"), dateline ("Monday, February 2, 1971"), multi-column news typography, headlines. This is a news_article.
> 
> Let's confirm the text:
> Top center: "HOSPITAL-TRADEMARK" -> actually it looks like "HOSPITAL-TRADEMARK" or "HOSPITAL-TRADEMARK". Wait, "HOSPITAL-TRADEMARK" -> "HOSPITAL-TRADEMARK". Maybe "HOSPITAL-TRADEMARK" is "HOSPITAL-TRADEMARK". It doesn't matter, it's a newspaper.
> Headline: "Theory of Emphysema CauseRaisesQuestions"
> Subhead: "Hospitals-World Wide Report"
> Byline: "By Jack Lieberman"
> Another headline: "Clinic at U. of Va. Offers Health Care to Families"
> Subhead: "Charlottesville-Travel Report"
> Another headline: "Antitrypsin Lack Might Increase Fertility"
> Subhead: "Hamburg-World Wide Report"
> This is definitely a newspaper page (news_article).
> 
> Scratchpad:
> 1. file_folder: no — page has dense multi-column text, headlines, bylines.
> 2. handwritten: no — typed text throughout.
> 3. form: no — no fax header.
> 4. questionnaire: no — not a survey.
> 5. resume: no — not a career history.
> 6. scientific_publication: no — no journal running head/volume/issue on this page; "Monday, February 2, 1971" and page "16" indicate a newspaper.
> 7. invoice/budget: no — no financial structure.
> 8. specification: no — no product/material documentation.
> 9. presentation: no — not a slide deck.
> 10. form: no — no administrative fields.
> 11. correspondence: no — no email/memo/letter structure.
> 12. news_article: yes — newspaper layout with date "Monday, February 2, 1971", page number "16", multi-column typography, headlines ("Theory of Emphysema CauseRaisesQuestions"), bylines ("By Jack Lieberman"), and datelines ("Charlottesville", "Hamburg").
> 13. scientific_report: no — although the topic is scientific (emphysema, antitrypsin), the layout is a newspaper article, not a research write-up with running narrative prose of a study.
> 14. advertisement: no — not a promotional layout.
> 
> Runner-up: scientific_report, ruled out because the page is a newspaper page with headlines, bylines, and a date (check 12), not an original research write-up.
> 
> Final label: news_article.

---

## form → budget (1 errors)

### `rvl_cdip__form__0001.png`
**Expected:** `form` | **Predicted:** `budget`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I need to follow a strict set of checks in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "77917 7 9 / 4" at the bottom, and a black bar at the bottom (scan artifact or folder edge? Wait, the black bar at the bottom has text "NOTICE IF THE FILM IMAGE IS LESS CLEAR THAN THIS NOTICE...". This looks like a microfilm notice, not a folder tab. The top has "Ted Bates new york/advertising", "BROWN & WILLIAMSON TOBACCO CORPORATION", "PRINT PRODUCTION ESTIMATE".
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of content: "PRINT PRODUCTION ESTIMATE", fields, tables, costs. Not identifier-only.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Mostly typed, with some handwritten numbers in the "Actual Total Cost" column (e.g., "3144", "4125", "548 + 312"). Not majority handwritten.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET -> form**
> - Evidence: No "FACSIMILE" or fax header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal masthead, volume, issue, page range.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: "PRINT PRODUCTION ESTIMATE". It has line items: "Dye Transfer", "Dupp. Dye Transfers", "Re-Touching (2)", "Transparencies", "C-Prints (3)", "Photolettering (3)". It has "Cost Per Ad/Item", "No. of Ads/Items", "Estimated Total Cost", "Actual Total Cost".
> - Let's look at the definition of invoice vs budget.
> - Invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." Wait, "A production estimate report... listing ACTUAL billable charges... is an invoice." But this is an "ESTIMATE".
> - Budget: "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical... is scientific_report... An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
> - Wait, the title is "PRINT PRODUCTION ESTIMATE". It has "Estimated Total Cost" and "Actual Total Cost" columns. The "Actual Total Cost" has handwritten numbers. Is it an invoice or a budget?
> - Let's re-read check 7 carefully:
>   - "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." -> Wait, this says a production estimate report listing ACTUAL billable charges is an invoice.
>   - "budget: ... Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical ... is scientific_report ... An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
> - The document is titled "PRINT PRODUCTION ESTIMATE". It's from "Ted Bates new york/advertising" to "BROWN & WILLIAMSON TOBACCO CORPORATION". It's an estimate for print production (advertising).
> - Is it an invoice or a budget?
> - "An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
> - The document has "Estimated Total Cost" and "Actual Total Cost". The "Actual Total Cost" has handwritten entries. This looks like a budget/estimate tracking document, or an invoice for the actuals?
> - Wait, "PRINT PRODUCTION ESTIMATE" is the title. It's an estimate. Estimates are budget (planning).
> - Let's look at the fields: "BRAND PIGEON/ESCAPE", "CAPTION ESCAPE TO PHOENIX 120'S", "SUBJECT PAINT POSTER", "EST. # NP-75-15R2", "JOB # BR-7477".
> - It's an estimate for a specific job.
> - Let's re-read the invoice definition: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> - Wait, the text says: "a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed." This is under "invoice".
> - But under "budget": "An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
> - This document is titled "PRINT PRODUCTION ESTIMATE". It has "Estimated Total Cost" and "Actual Total Cost". The actuals are filled in by hand. This is likely a budget/estimate tracking sheet, or an invoice?
> - Actually, let's look at Check 10: ADMINISTRATIVE FORM -> form. "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... internal authorization/approval forms with an approval signature/date block."
> - Is this a form? It has fields: BRAND, CAPTION, SUBJECT, PHOTOGRAPHER/ARTIST, REVISED DATE, EST. #, JOB #. Then a table with columns: AD TITLES, PUBLICATION(S), COVER DATE(S), SIZE(S), COLOR. Then a cost table.
> - But Check 7 says: "Check 7 applies only when financial content IS the page's primary structure — a line-item table, ledger, statement, voucher, or check face." Here, the primary structure is a line-item table of costs (Photographer's Fee, Model Fee, Dye Transfer, etc.).
> - Is it an invoice or budget?
> - "An estimate/recap projecting FUTURE work is budget (planning), not invoice". The title is "PRINT PRODUCTION ESTIMATE". It's an estimate. Even though it has "Actual Total Cost" filled in, it's fundamentally an estimate document (budget).
> - Wait, could it be a form (check 10)? "A hand-plotted experimental GRAPH... is scientific_report... It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> - So if it's money-related, it's invoice or budget.
> - Let's distinguish invoice vs budget again.
> - Invoice: "charges owed for goods or services SOLD... billing document for COMPLETED work... listing ACTUAL billable charges".
> - Budget: "internal money planning, tracking, or disbursement... estimate/recap projecting FUTURE work is budget".
> - The document is an "ESTIMATE". Estimates are for future work (planning). The fact that "Actual Total Cost" is filled in might mean it's being used to track actuals against the estimate, which is "tracking" -> budget. "budget: internal money planning, tracking, or disbursement... expense reports... statement of account". Tracking actuals against an estimate is budget tracking.
> - Also, it's from an agency (Ted Bates) to the client (Brown & Williamson). An agency estimate is a budget/planning document for the client to approve the spend. Once approved and completed, an invoice would be sent. This is an "ESTIMATE". So it's budget.
> 
> Let's check if there's any other category.
> - Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification. No.
> - Check 9: SLIDE DECK... -> presentation. No.
> - Check 10: ADMINISTRATIVE FORM -> form. "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)." Since this is a financial document (estimate/budget), check 7 overrides check 10.
> - Check 11: CORRESPONDENCE. No.
> - Check 12: PUBLISHED JOURNALISM. No.
> - Check 13: ORIGINAL RESEARCH WRITE-UP. No.
> - Check 14: PROMOTIONAL MATERIAL. No.
> 
> So it's between invoice and budget.
> Title: "PRINT PRODUCTION ESTIMATE".
> Content: Line items for advertising production (photography, dye transfer, etc.) with "Estimated Total Cost" and "Actual Total Cost".
> Definition of budget: "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical ... is scientific_report ... An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
> Wait, the text says: "an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." This is under the budget definition? Let's re-read carefully:
> "budget: ... ALSO a provider's periodic customer statement: a monthly service bill or statement of account issued by a vendor to the company as a customer (e.g. an AT&T "MONTHLY INVOICE" for phone service, a utility or subscription statement) is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold. Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form. And a technical/project status report whose content is primarily technical (project description, technical approach, research activity prose) is scientific_report (check 13), even if it embeds a budget-vs-actual COSTS section — one cost table does not make a technical status report financial."
> Ah! "Money PLANNING for future work is budget: an agency/vendor document that lists actual charges and totals owed is an invoice (this check), never a form." -> This sentence is confusingly placed. Let's read the invoice part again:
> "invoice: ... a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed. It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> So if it lists ACTUAL billable charges and totals owed, it's an invoice.
> But the title is "PRINT PRODUCTION ESTIMATE". And it has "Estimated Total Cost" and "Actual Total Cost". The actuals are handwritten. This looks like a budget/estimate sheet where actuals are being tracked.
> Wait, "An estimate/recap projecting FUTURE work is budget (planning), not invoice; a bill for completed goods/services is invoice."
> Since the title is "ESTIMATE", it's projecting future work (or at least, it's an estimate document). The primary function is an estimate (budget).
> Let's consider "budget" as the label.
> 
> Wait, is there any chance it's a form (check 10)?
> "Check 7 applies only when financial content IS the page's primary structure... If the page is otherwise formatted as correspondence... classify it as correspondence... instead."
> Here, the primary structure IS the financial content (the estimate table). So check 7 applies.
> Under check 7, is it invoice or budget?
> "An estimate/recap projecting FUTURE work is budget (planning), not invoice". The document is an "ESTIMATE". Therefore, budget.
> 
> Let's double check check 10 just in case.
> "A research grant application... stays form... A QA/parameter review sheet... stays form".
> But check 7 explicitly says: "It does NOT cover money records: billing documents are invoice (check 7), and money-only forms are budget (check 7)."
> So if it's money records, it's check 7.
> 
> Is it an invoice? "a production estimate report... listing ACTUAL billable charges... is an invoice." But this is an "ESTIMATE" report, not a report listing actual billable charges as the primary function. The primary function is an estimate (budget). The "Actual Total Cost" column is filled in, probably to track the budget vs actual. This is "tracking" -> budget. "budget: internal money planning, tracking, or disbursement".
> 
> Therefore, budget.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — page has extensive content (title, fields, cost table).
> 2. handwritten: no — mostly typed, only some handwritten numbers in the cost column.
> 3. fax: no — no fax header.
> 4. questionnaire: no — no survey items.
> 5. resume: no.
> 6. scientific_publication: no — no journal identifier.
> 7. financial document: yes — primary structure is a line-item cost table ("PRINT PRODUCTION ESTIMATE" with "Estimated Total Cost" and "Actual Total Cost" columns, listing photography and production fees). It is an estimate/recap projecting/tracking work, which falls under budget (planning/tracking), not an invoice for completed goods/services billed as a final statement (though it has actuals, the document type is an estimate).
> 8. specification: no.
> 9. presentation: no.
> 10. form: no — check 7 overrides for money records.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Runner-up: form, ruled out because the page's primary structure is a financial cost table/estimate (check 7), which overrides the generic form check for money records.
> Or runner-up: invoice, ruled out because the document is titled "PRINT PRODUCTION ESTIMATE" and functions as a planning/tracking document (budget) rather than a final bill for completed goods/services (invoice).
> 
> Let's refine the runner-up. The most likely trap is "form" or "invoice".
> I'll say runner-up: invoice, ruled out because the document is an "ESTIMATE" (planning/tracking) rather than a final billing statement for completed work (invoice).
> 
> Wait, the prompt says: "Once an earlier check matches, later checks do not override it."
> Check 7 matches. I will output budget.
> 
> Let's re-read the invoice definition: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> If it's an "agency/vendor billing document for COMPLETED work: a production estimate report... listing ACTUAL billable charges", then it's an invoice.
> But this document is from Ted Bates (agency) to Brown & Williamson (client). It's an "ESTIMATE". Estimates are for future work. The fact that actuals are filled in means it's being used to track the budget. "budget: internal money planning, tracking, or disbursement". Tracking actuals against an estimate is budget tracking.
> Also, the title is "PRINT PRODUCTION ESTIMATE". I'll stick with budget.
> 
> Final check of the text:
> "Ted Bates new york/advertising"
> "BROWN & WILLIAMSON TOBACCO CORPORATION"
> "PRINT PRODUCTION ESTIMATE"
> "REVISED: JULY 29, 1976"
> "REVISED DATE: FEBRUARY 18, 1976 / JULY 8, 1975"
> "EST. # NP-75-15R2"
> "JOB # BR-7477"
> Table with costs.
> This is definitely a budget/estimate document.
> 
> Label: budget.

---

## form → file_folder (1 errors)

### `rvl_cdip__form__0004.png`
**Expected:** `form` | **Predicted:** `file_folder`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header: None.
> - Masthead/running head: None. There is text "Insecticides" at the top right (rotated) and "51303 2938" at the bottom right (rotated). These look like a topical heading and a Bates number. Wait, let's look closer.
> - The text "Insecticides" is at the top right, rotated 90 degrees counter-clockwise.
> - The text "51303 2938" is at the bottom right, rotated 90 degrees counter-clockwise.
> - There is a thin black line running vertically along the right side, and another at the bottom. This looks like a scanned page from a document, possibly a section divider or a folder tab, or just a mostly blank page with a heading.
> - Wait, check the rules for `file_folder` vs `presentation` (check 9) vs `scientific_report` (check 13).
> - "A prominent topical heading always counts as real content, subtitle or not." -> "RECOMMENDATIONS" with no subtitle is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder.
> - "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider even alongside a small handwritten letter/number annotation — but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab... is a folder-tab label and stays file_folder (check 1)."
> - Is "Insecticides" a short filing label on a folder tab, or a section divider heading?
> - Let's look at the layout. There's a black bar on the right and bottom. This looks like a photographed folder tab or a slide.
> - Wait, the text "Insecticides" is just a word. "51303 2938" is a Bates number.
> - Let's re-read check 1: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only. ... A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image ... or with a bold headline title (even a single word/short phrase like 'RECOMMENDATIONS' with no subtitle, or a large heading rotated 90 degrees like 'COMPETITIVE BAR PROGRAMS' — even alongside a small handwritten letter or number annotation) carries real content — it is a cover/title page, section divider, or photographic slide (presentation, check 9), not file_folder."
> - So if "Insecticides" is a bold headline title rotated 90 degrees, it's a section divider -> presentation (check 9).
> - BUT, check 1 also says: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB ... bearing a short filing label that names the folder's contents: a product name, collection/company name, month or date range, contract/file description, or alphanumeric identifier, usually with a Bates number stamped on the folder body. The label IS filing metadata ... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees..."
> - Is "Insecticides" a folder tab label or a section divider heading? "Insecticides" is a topical heading. But it could be a folder tab label naming the folder's contents (e.g., a folder containing documents about insecticides).
> - Let's look at the black bar. "a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center ... points to a photographed slide/overhead — presentation". BUT "this signal applies only to a photographic image ... or a designed deck page — it does NOT apply to a photographed file-folder TAB (check 1): a page whose content is a physical folder tab, a short filing label ... and a Bates number is file_folder even though the folder body photographs as a solid black bar and the label may be rotated."
> - So if it's a folder tab, it's `file_folder`. If it's a section divider, it's `presentation`.
> - How to distinguish? "Insecticides" is a very short label. Folder tabs often have short labels like "Litigation Content", "NEWTROL", "PMI Pricing Plans", "PALL MALL FAMOUS-Monitor test 1992", "FEBRUARY". "Insecticides" fits the pattern of a folder tab label (naming the folder's contents).
> - Also, the Bates number "51303 2938" is typical.
> - Let's consider `file_folder`. The page has almost no content: just "Insecticides" (rotated) and "51303 2938" (rotated). The black bar is the folder body. This perfectly matches the "Folder-tab pages" exception in check 1.
> - Let's check check 9: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note ... is a presentation (this check), not file_folder (check 1). EXCEPTIONS: ... a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab ... is a folder-tab label and stays file_folder (check 1)."
> - "Insecticides" is a short filing label naming the folder's contents. The black bar is the photographed folder body. Thus, it is `file_folder`.
> 
> Let's double check.
> Text: "Insecticides" (top right, rotated).
> Text: "51303 2938" (bottom right, rotated).
> Layout: White space, thin black lines on right and bottom (folder body/tab edge).
> This is a scanned folder tab.
> Category: `file_folder`.
> 
> Let's review the checks:
> 1. IDENTIFIER-ONLY PAGE -> file_folder. Evidence: "Insecticides" (short filing label on folder tab), "51303 2938" (Bates number), black bar (folder body). No sentences, no topical title (it's a folder label). Matches folder-tab bullet.
> 2. MAJORITY-HANDWRITTEN PAGE -> handwritten. None.
> 3. FAX TRANSMISSION SHEET -> form. None.
> 4. SURVEY INSTRUMENT -> questionnaire. None.
> 5. PERSON'S CAREER HISTORY -> resume. None.
> 6. PUBLISHED EVIDENCE -> scientific_publication. None.
> 7. FINANCIAL DOCUMENT -> invoice/budget. None.
> 8. PRODUCT OR MATERIAL DOCUMENTATION -> specification. None.
> 9. SLIDE DECK -> presentation. Ruled out because it's a folder tab, not a slide/deck. The black bar is the folder body, not a slide scan artifact. The label "Insecticides" is a filing label, not a section divider heading.
> 10. ADMINISTRATIVE FORM -> form. None.
> 11. CORRESPONDENCE -> email/memo/letter. None.
> 12. PUBLISHED JOURNALISM -> news_article. None.
> 13. ORIGINAL RESEARCH WRITE-UP -> scientific_report. None.
> 14. PROMOTIONAL MATERIAL -> advertisement. None.
> 
> Conclusion: `file_folder`.
> 
> Wait, could "Insecticides" be a section divider for a presentation?
> "A large heading rotated 90 degrees (e.g. 'COMPETITIVE BAR PROGRAMS') is a section divider ... but a rotated SHORT FILING LABEL that names a folder's contents on a photographed folder tab ... is a folder-tab label and stays file_folder (check 1)."
> "Insecticides" is a very short label (one word). It names the contents of a folder (documents about insecticides). The black bar is the folder body. The Bates number is on the folder body. This is a classic folder-tab page.
> 
> Therefore, `file_folder`.
> 
> Let's write the scratchpad.
> - Pre-scan: No mail header. No masthead. "Insecticides" is rotated text at top right, "51303 2938" is rotated text at bottom right. Black bar on right/bottom edges.
> - Check 1: file_folder. Evidence: Page is mostly blank with a short rotated label "Insecticides" and a Bates number "51303 2938", plus a black bar along the edge. This matches the "Folder-tab pages" exception: a photograph of a physical folder tab bearing a short filing label ("Insecticides") and a Bates number, with the folder body photographing as a black bar. The label is filing metadata, not a bold topical title.
> - Check 9: presentation. Ruled out because the black bar is the photographed folder body, not a slide scan artifact, and "Insecticides" is a short filing label on a folder tab, not a designed section divider heading.
> - Runner-up: presentation, ruled out because the page is a scanned folder tab with a short filing label and Bates number, not a designed deck cover or slide.
> 
> Final label: file_folder.

---

## form → invoice (1 errors)

### `rvl_cdip__form__0005.png`
**Expected:** `form` | **Predicted:** `invoice`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking each condition in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Fax transmission header: None.
> - Masthead/running head: None.
> 
> **Check 1: file_folder**
> - Evidence: The page has a table with "Publication Title", "Year", "Volume", "Issue", "Start Page", "End Page", "Author", "Qty", "Acctn No.", "Process Fee", "Copyrt Fee", "Rush Fee", "Total Cost", "Media Notes". It has an order date, order number, ship-to address. This is not an identifier-only page.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: There is a handwritten "USA" and a small mark, but the majority of the content is typed text and a table.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - Evidence: No survey questions or transmittal for a survey.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - Evidence: No CV/resume content.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - Evidence: No journal running head, volume, issue, DOI.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: The document is titled "Order Confirmation - NOT an Invoice". It lists "Publication Title", "Year", "Volume", "Issue", "Start Page", "End Page", "Author", "Qty", "Acctn No.", "Process Fee", "Copyrt Fee", "Rush Fee", "Total Cost", "Media Notes". It has "Order Date: 02/13/1998", "Order Number: 13132", "Ship to: MARGARET A. SOUTHWICK". It is a billing document for completed work (articles published in a journal, likely a reprint order or article ordering service). Wait, "Order Confirmation - NOT an Invoice". But it has line items with costs (Process Fee 8.00, Copyrt Fee 1.50, Total Cost 9.50). It's a statement of charges for goods/services (reprints/articles). Let's look closely at the definition of invoice: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due... a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work... It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> Wait, this is an "Order Confirmation". Is it an invoice? "NOT an Invoice". But it has line items and total cost. Let's re-read check 7.
> "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD... It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> "budget: internal money planning... provider's periodic customer statement... is budget, not invoice — it is a statement of charges for an ongoing account, not a bill for goods sold."
> This looks like an order confirmation for journal articles (reprints). "Publication Title: 132 ARTICLES", "Year: 1998", "Volume: 13", "Issue: 1", "Start Page: 190", "End Page: 190", "Author: Dremelur+", "Qty: 1", "Acctn No.: YP368", "Process Fee: 8.00", "Copyrt Fee: 1.50", "Rush Fee: 0.00", "Total Cost: 9.50".
> This is a billing document for completed work (ordering articles/reprints). Even though it says "NOT an Invoice", it functions as a statement of charges for goods/services sold (the articles). Wait, is it a form?
> Let's check Check 10: ADMINISTRATIVE FORM.
> "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data... A standalone labeled data chart or table... internal authorization/approval forms..."
> But Check 7 says: "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> Also: "an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed."
> This page lists "Process Fee", "Copyrt Fee", "Total Cost". It's a billing statement for the articles. So it's an invoice.
> Wait, let's look at the label "Order Confirmation - NOT an Invoice". Does this mean it's not an invoice? The instructions say: "It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice." The text "NOT an Invoice" might be a legal disclaimer, but the function is billing for the articles (Process fee, Copyright fee, Total cost).
> Let's re-read carefully: "an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due... It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> This is an order confirmation for reprints/articles. It has line items and total cost. It's an invoice.
> 
> Let's check if there's any other category.
> Could it be a form? "administrative form -> form. Filled or blank fields... A standalone labeled data chart or table...". But check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." and "an agency/vendor billing document for COMPLETED work... is an invoice".
> So invoice is the best fit.
> 
> Let's double check Check 7:
> "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD ... It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice. Look for goods sold or one-off services performed (items, quantities, unit prices). ... A running "BALANCE DUE" column does not make a bill a budget "statement of account"."
> This page has:
> - Publication Title: 132 ARTICLES
> - Year: 1998, Volume: 13, Issue: 1, Start Page: 190, End Page: 190
> - Author: Dremelur+
> - Qty: 1
> - Acctn No.: YP368
> - Process Fee: 8.00
> - Copyrt Fee: 1.50
> - Rush Fee: 0.00
> - Total Cost: 9.50
> This is clearly a billing document for goods/services (articles/reprints). The "NOT an Invoice" is likely a disclaimer because it's an "Order Confirmation" that will be followed by an invoice, or it's a confirmation of charges. But functionally, it's a statement of charges. Wait, if it's an order confirmation, is it an invoice? "an agency/vendor billing document for COMPLETED work... is an invoice". The work (printing the articles) is completed or being ordered. The fees are for the order.
> Actually, let's consider if it's a form. "administrative form -> form. ... A standalone labeled data chart or table ... internal authorization/approval forms". But check 7 explicitly overrides form for billing documents. "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> 
> Let's review the whole page:
> "Order Confirmation - NOT an Invoice"
> SHIP TO: MARGARET A. SOUTHWICK ...
> Order Date: 02/13/1998
> Order Number: 13132
> Ship to: ...
> Account #: 8012
> Phone: 804-274-2661
> Email: ...
> Contract Id: 164
> PAX: 804-274-2160
> 
> Table:
> Publication Title | Year | Volume | Issue | Start Page | End Page | Author | Qty | Acctn No. | Process Fee | Copyrt Fee | Rush Fee | Total Cost | Media Notes
> 132 ARTICLES | 1998 | 13 | 1 | 190 | 190 | Dremelur+ | 1 | YP368 | 8.00 | 1.50 | 0.00 | 9.50 9 | RM21014 CANCRMAN
> 
> Handwritten: "USA"
> 
> This is a billing statement / invoice for journal articles (reprints). The title says "Order Confirmation - NOT an Invoice", but it contains all the elements of an invoice (line items, fees, total cost, account number, ship to). The instructions say: "It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice." The text "NOT an Invoice" is just the document's own title, but its function is to state charges owed (or to be invoiced). Actually, an order confirmation with charges is often treated as an invoice in these classification tasks if it has line items and totals. Wait, if it explicitly says "NOT an Invoice", should I classify it as something else?
> What if it's a form? "administrative form -> form". But check 7 says "Money function overrides form layout: a billing or payment page stays financial...".
> Is there any other financial category? "budget". No, it's not internal planning.
> So it must be invoice. The label "invoice" is the correct functional classification for a document that bills for goods/services, even if the vendor loosely calls it an "Order Confirmation". The prompt says: "a bill is a bill even when it is printed on a form... Do not rush to the label that matches the page's subject matter... commit to the FIRST one with strong, concrete evidence". The evidence is line items with fees and a total cost, which matches the invoice definition.
> 
> Let's check if there's any email header. No.
> Any fax header? No.
> Any masthead? No.
> 
> Let's re-read check 7 carefully:
> "invoice: an outside vendor, supplier, or agency states charges owed for goods or services SOLD — an "INVOICE" header with line items and amount due, a payment voucher, a vendor's price or hourly-rate schedule, a receipt, a payment request, or an agency/vendor billing document for COMPLETED work: a production estimate report, estimate change order, estimate recap, or itemized billing statement listing ACTUAL billable charges, unit prices, amounts, and totals owed. It does not have to be titled "INVOICE" — a voucher, recap, or change order that bills charges already incurred and totals is an invoice."
> 
> The document has:
> - "Process Fee 8.00"
> - "Copyrt Fee 1.50"
> - "Total Cost 9.50"
> - "Acctn No. YP368"
> - "Account #: 8012"
> This is an itemized billing statement. It is an invoice.
> 
> Runner-up: form. Ruled out because check 7 (financial document) overrides form layout when the page is a billing document with line items and totals (money function overrides form layout).
> 
> Let's confirm there is no other check.
> Check 10: form. "A standalone labeled data chart or table... internal authorization/approval forms". But check 7 says "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks." This page is printed on a form-like layout (table with headers), but it's a billing document. So invoice wins.
> 
> Final check of the text: "Order Confirmation - NOT an Invoice". Even with this text, the functional content is a billing statement for articles (reprints). The fees (Process, Copyright) are charges for the goods/services. I will classify as invoice.
> 
> Wait, is there any possibility it's a "specification"? No.
> "presentation"? No.
> 
> I'm confident in "invoice".
> Evidence for invoice: line-item table with "Process Fee", "Copyrt Fee", "Total Cost", "Acctn No.", "Account #", "Order Date", "Order Number", billing for "132 ARTICLES".
> Runner-up: form, ruled out because check 7 explicitly states "Money function overrides form layout: a billing or payment page stays financial even when it is printed on a form with fields and approval blocks."
> 
> Let's quickly review the "NOT an Invoice" text. If a document explicitly says it's not an invoice, could it be a form? "administrative form -> form. Filled or blank fields...". But the instructions say "commit to the FIRST one with strong, concrete evidence you can actually read... a bill is a bill even when it is printed on a form". The presence of fees and total cost makes it a bill/invoice functionally. The "NOT an Invoice" is likely a legal disclaimer from the publisher (e.g., "This is an order confirmation, not an invoice; an invoice will follow"). But functionally, it's an invoice/billing document. I'll stick with invoice.
> 
> Actually, is there any chance it's a "budget"? No, it's a one-off charge for articles.
> Is there any chance it's a "letter"? No.
> 
> I will output invoice.

---

## form → specification (1 errors)

### `rvl_cdip__form__0013.png`
**Expected:** `form` | **Predicted:** `specification`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: There is a Bates number "620423067" at the bottom right. No journal masthead.
> 
> **Check 1: file_folder**
> - Evidence: The page has a table with many rows and columns, filled with data (Brand, Production Date, Cigarette dimensions, Weight, Filter, Paper, Tar, Nicotine, etc.). It has real content, not just an identifier/stamp.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: Most of the content is typed labels (Brand, P.D., Weight, Filter, Paper, Tar, Nicotine, etc.) with some handwritten numbers in the columns. The structure is a printed table. Handwriting fills the fields of a printed structured form/table.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No "FACSIMILE" or "FAX COVER SHEET" header.
> - Not this check.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
> - Evidence: No survey questions, rating scales, or commitment application. It's a data table.
> - Not this check.
> 
> **Check 5: PERSON'S CAREER HISTORY -> resume**
> - Evidence: No biographical info.
> - Not this check.
> 
> **Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - Evidence: No journal name, volume, issue, page range, or DOI on the page itself. Just a Bates number.
> - Not this check.
> 
> **Check 7: FINANCIAL DOCUMENT -> invoice or budget**
> - Evidence: No financial data (money, charges, budget lines). It's technical data (Tar, Nicotine, dimensions).
> - Not this check.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION -> specification**
> - Evidence: The table is titled/structured with "BRAND", "PRODUCTION DATE", "OPERATOR NUMBER", "DATE ANALYSIS EXPECTED", "DATE RECEIVED". Then sections: "CIGARETTE" (P.D., Weight, Circ.), "FILTER" (Texcel/Pillow, Triceratin, TEODA, Ventilation Rate), "PAPER" (Porosity, Citrate, Phosphate), "TOB. ANALYSES (%)", "SMOKING (Cis)", "Tar", "Nicotine", "Resistance", "Puffs", "NO", "CO", "Cig. Perf. Fairness", "End Stability", "Coal Retention", "Corr. BORE FV", "BORE FV Moisture", "Corr. FILL VALUE", "FV MOISTURE".
> - This is a product-analysis table or test-analysis table keyed to product codes/brands. "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" is an example of a specification. This table is clearly a product analysis / test data sheet for cigarette brands (St. James C4 1001 BA, P57L D6, P57L D15).
> - Wait, check 8 says: "A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough".
> - Here, the top row has "BRAND St. James C4 1001 BA", "P57L D6", "P57L D15". It's a product analysis table.
> - Let's check check 10: "standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values)... filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)".
> - Wait, check 8 says: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification."
> - Is this a specification or a form?
> - Check 10: "A form does NOT have to be blank — a filled form recording data is still a form, including handwriting in its cells. This also covers: a standalone labeled data chart or table... a filled analytical or lab data sheet".
> - Let's re-read check 8: "Material Safety Data Sheet... product formulation or preparation/mixing instructions, manufacturing-change authorization, test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table... is a specification".
> - The page has a table with product names (St. James C4 1001 BA, P57L D6, P57L D15) and rows of analytical data (Tar, Nicotine, dimensions, etc.). This is a "test-analysis table keyed to product/part codes" or "product-referenced test data". Thus, it's a specification.
> - Wait, is it a form? "filled analytical or lab data sheet" is a form (check 10). But check 8 says "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
> - Let's look closely at the table. It has columns for different products (St. James C4 1001 BA, P57L D6, P57L D15). The rows are parameters: P.D. (Inches), Weight (MG), Circ. (MM), Texcel/Pillow (%), Triceratin (%), TEODA (%), Ventilation Rate (%), Porosity (CORSETA), Citrate (%), Phosphate (%), B.P.M. (% INC), Lamine, Recon. Tob., Stem, Puffed, Alkaloids, Total Sugar, Reducing Sugar, Moist. (Cond.), Moist. (Pkg), Menthol, Prop. Glycol, Glycerin, Nitrate, Tar (MG), Nicotine (MG), Resistance (%), Puffs, NO (MG), CO (MG), Cig. Perf. Fairness, End Stability, Coal Retention, Corr. BORE FV, BORE FV Moisture, Corr. FILL VALUE, FV MOISTURE.
> - This is a product analysis / test data table. Check 8 explicitly covers "test-analysis tables keyed to product/part codes" and "Product-referenced test data is a specification."
> - Let's check if there's any other match.
> - Check 13: scientific_report. Requires running narrative prose. This is just a table. So not scientific_report.
> - Check 10: form. "filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)". But check 8 overrides for "test-analysis tables keyed to product/part codes". The table is keyed to products (St. James C4, P57L D6, P57L D15).
> - Let's re-read check 8 carefully: "test-analysis tables keyed to product/part codes, tolerances, or 'shall/must' requirement language. Product-referenced test data is a specification. A titled product-analysis table (e.g., 'MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER' with chemical constituents and measurements) is a specification even without an explicit alphanumeric product/part code in the table itself — the title naming the product/material being analyzed is enough; you don't need a code like 'PD 142A' specifically, just clear evidence the table's subject is a product's own composition or properties."
> - This table is exactly that: a product-analysis table with chemical constituents (Tar, Nicotine, etc.) and measurements for specific products. So it's a specification.
> 
> Let's double check check 10 vs check 8.
> Check 10: "standalone labeled data chart or table (e.g. 'CHART 1' with rows A-Z and numeric values); a filled analytical or lab data sheet ('ANALYTICAL DATA SUMMARY' with COMPOUND:, FORMULA:, FORMULA WEIGHT:, HPLC entries and spectrum captions)" -> form.
> Check 8: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification. A titled product-analysis table... is a specification".
> The table here is keyed to products (St. James C4 1001 BA, P57L D6, P57L D15) and contains product properties (Tar, Nicotine, dimensions, ventilation rate, etc.). This matches check 8 perfectly.
> 
> Let's check if there's any other evidence.
> Top row: "BRAND St. James C4 1001 BA", "P57L D6", "P57L D15".
> "PRODUCTION DATE", "OPERATOR NUMBER", "DATE ANALYSIS EXPECTED", "DATE RECEIVED".
> This is a lab data sheet for product analysis.
> Since it's product-referenced test data (composition/properties of cigarettes), it's a specification (check 8).
> 
> Wait, what about check 10's "filled analytical or lab data sheet"?
> Check 8 says: "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
> The example in check 8: "MAINSTREAM SMOKE ANALYSES FOR PRODUCTS CONTAINING CARBONIZED FILLER" with chemical constituents and measurements.
> This page has exactly that: analyses for products (St. James, P57L) with chemical constituents (Tar, Nicotine, etc.) and measurements.
> So it's specification.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — has a full table of data.
> 2. handwritten: no — typed labels, handwritten numbers in a printed table.
> 3. fax: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no — no journal header.
> 7. financial: no — no money.
> 8. specification: yes — product-analysis table keyed to product codes (St. James C4 1001 BA, P57L D6, P57L D15) with chemical constituents (Tar, Nicotine, etc.) and measurements. Matches "test-analysis tables keyed to product/part codes" and "Product-referenced test data is a specification."
> 9. presentation: no.
> 10. form: no — check 8 overrides for product-referenced test data / product-analysis tables.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no — no running narrative prose, just a table.
> 14. advertisement: no.
> 
> Runner-up: form. Ruled out because the table is a product-analysis table keyed to product codes with chemical constituents and measurements, which is explicitly a specification (check 8) per the rule "test-analysis tables keyed to product/part codes... Product-referenced test data is a specification."
> 
> Final label: specification.

---

## handwritten → advertisement (1 errors)

### `rvl_cdip__handwritten__0003.png`
**Expected:** `handwritten` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a 7-Eleven logo, Camel Winston ad, and a mailing label with handwritten text.
> 
> **2. Scratchpad procedure:**
> - Check 1: file_folder. The page has a lot of content: an ad, a mailing label, handwritten text. Not file_folder.
> - Check 2: handwritten. There is handwritten text ("Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/98."), but it's just a note on a mailing label/ad. Not majority handwritten.
> - Check 3: FAX transmission sheet. No.
> - Check 4: questionnaire. No.
> - Check 5: resume. No.
> - Check 6: scientific_publication. No.
> - Check 7: invoice/budget. No.
> - Check 8: specification. No.
> - Check 9: presentation. No.
> - Check 10: form. No.
> - Check 11: correspondence. No.
> - Check 12: news_article. No.
> - Check 13: scientific_report. No.
> - Check 14: advertisement. The dominant content is a 7-Eleven / Camel Winston coupon/ad ("$3.50 off a carton", "35¢ off a pack"), along with a mailing label and a handwritten note about the addressee being deceased. Wait, let's look closer.
> The image is rotated 90 degrees counter-clockwise. Let's rotate it mentally.
> Top part (right side in original): 7-Eleven logo, "$3.50 off a carton", "35¢ off a pack", "CAMEL WINSTON". "THIS IS NOT A COUPON See other side for details."
> Bottom part (left side in original): Mailing label for "NANCY EVERITT", "2705 SUPERIOR DR", "LIVERMORE CA 94550-6615". Handwritten note: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/98."
> Also a "PAID" stamp, "Change Service Requested".
> This is a direct mail piece, specifically an advertisement/coupon mailing. The dominant content is the advertisement (7-Eleven, Camel Winston). The handwritten note is just a mailroom annotation.
> Wait, let's re-read the checks.
> Check 14: PROMOTIONAL MATERIAL -> advertisement. Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content.
> The page is a coupon/advertisement for Camel Winston cigarettes at 7-Eleven. The handwritten note is just a mailroom routing note. The dominant content is the advertisement.
> 
> Let's check the labels again.
> advertisement: yes.
> 
> Let's double check.
> The page contains:
> - 7-Eleven logo
> - "$3.50 off a carton"
> - "35¢ off a pack"
> - "CAMEL WINSTON"
> - "THIS IS NOT A COUPON See other side for details."
> - Mailing address label.
> - Handwritten note: "Please remove, Addressee is deceased. Died of smoking-related illness on 11/15/98."
> - "PAID" stamp.
> - "Change Service Requested"
> 
> This is clearly an advertisement (specifically a direct mail ad/coupon). The dominant content is the promotional material.
> 
> Let's trace the checks:
> 1. file_folder: no, has ad and mailing label.
> 2. handwritten: no, mostly printed.
> 3. FAX: no.
> 4. questionnaire: no.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. invoice/budget: no.
> 8. specification: no.
> 9. presentation: no.
> 10. form: no.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: yes. The page is a direct mail advertisement/coupon for Camel Winston cigarettes at 7-Eleven. The handwritten note is a mailroom annotation, not the primary content. The dominant layout is the ad.
> 
> Runner-up: form (mailing label), ruled out because the ad/coupon is the dominant content and function (promotional material), and the mailing label is just part of the direct mail piece. Or maybe handwritten, ruled out because it's just a small note.
> 
> Final label: advertisement.

---

## scientific_report → handwritten (1 errors)

### `rvl_cdip__scientific_report__0016.png`
**Expected:** `scientific_report` | **Predicted:** `handwritten`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. There's a Bates number "2505336064" on the right side, and "2197" at the top right. No journal masthead.
> 
> **Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Evidence: The page has a lot of handwritten text, a table at the bottom, and typed headers. It's not just an identifier.
> - Not this check.
> 
> **Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - Evidence: Most of the content is freeform handwriting (lists of effects like "nose", "larynx", "trachea", "lung" with sub-items like "reserve cell", "hyperplasia", etc.). The top has some typed headers ("EFFECT", "1 R4F", "UR5J4S-35", "FACTOR") and a typed table at the bottom ("TABLE DOSE RATIO CALCULATION..."). However, the vast majority of the page's body content is handwritten notes listing biological effects. Wait, let's look closer.
> - The handwritten text lists: nose (Level 1, reserve cell, hyperplasia, squamous metaplasia, Level 2, atrophy), larynx (base of epiglottis, squamous metaplasia, hyperplasia, arytenoid projections, ventral depression, hyperplasia, floor of larynx, vocal cords, lower metachondria, hyperplasia, squamous metaplasia), larynx morphometry (ventral depression, floor of larynx, vocal cords), trachea (reserve cell, hyperplasia), lung (reserve cell, hyperplasia, goblet cell, hyperplasia).
> - There is a typed table at the bottom: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RACE RATS, 92-DAY INHALATION PERIOD".
> - Is it majority handwritten? Yes, the main body is handwritten lists.
> - Wait, is it a form? No printed field labels/boxes for the handwritten part. It's freeform handwriting on blank paper (with some typed headers at the top and a typed table at the bottom).
> - Let's re-read check 2: "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template... The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
> - This page has typed headers at the top and a typed table at the bottom, but the main content is handwritten notes on blank paper.
> - Let's check if it's a scientific_report. Check 13 requires "Running narrative prose". This is a list of effects, not running narrative prose.
> - Let's check if it's a specification. Check 8: "test-analysis tables keyed to product/part codes...". The bottom table is "TABLE DOSE RATIO CALCULATION...". But the main content is handwritten notes.
> - Wait, look at the bottom table: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RACE RATS, 92-DAY INHALATION PERIOD". This looks like a scientific data table or a note about a scientific calculation.
> - Is it handwritten? "Most of the content is freeform handwriting". Yes, the left 2/3rds is entirely handwritten lists. The top has typed headers. The bottom has a typed table caption. The right side has a Bates number.
> - Let's evaluate "handwritten" vs "scientific_report". Scientific report requires "Running narrative prose". This is just a list of histological effects (nose, larynx, trachea, lung) and a table caption. No running prose. So not scientific_report.
> - Is it a form? No printed fields to fill.
> - Is it a specification? No "shall/must" language, no material safety data.
> - So it's likely handwritten. Let's re-read check 2 carefully. "Most of the content is freeform handwriting... NOT on a printed template." This page has some typed elements at the top and bottom, but the main body is freeform handwriting on blank paper. "A typed page with only a signature, stamp, or margin note is not handwritten." Here, the typed elements are headers and a table caption, but the bulk of the page is handwritten notes.
> - Wait, could it be a scientific_report? "A lab or technical study title page with authors and an internal affiliation and no journal identifiers." No title page here. "Running narrative prose..." No.
> - Let's look at the handwritten text again. It's a list of biological effects (hyperplasia, metaplasia, atrophy) for different anatomical sites (nose, larynx, trachea, lung). This is a note from a pathology report or a scientific study. Since it lacks running narrative prose, it doesn't fit scientific_report. It fits handwritten.
> 
> Let's check if there's any other category.
> - form: No.
> - invoice/budget: No.
> - presentation: No.
> - questionnaire: No.
> - resume: No.
> - email/memo/letter: No.
> - news_article: No.
> - advertisement: No.
> 
> Let's reconsider "handwritten".
> "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
> The page has typed headers: "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR", "N", "INTER-CEPT", "SLOPE", "N", "INTER-CEPT", "SLOPE".
> And a typed table at the bottom: "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RACE RATS, 92-DAY INHALATION PERIOD".
> The rest is handwritten.
> Is this "majority handwritten"? Yes, the area covered by handwriting is much larger than the typed text.
> Is it on a printed template? No, it's blank paper with some typed text at the top and bottom.
> So "handwritten" is a strong candidate.
> 
> Wait, is there any chance this is a "scientific_report"?
> Check 13: "Running narrative prose with objectives, methods, results, or discussion... Requires running prose — a page that is only labeled field-value entries... is a filled form... not a scientific report."
> This page is only lists and a table caption. No running prose. So not scientific_report.
> 
> Is it a "specification"?
> Check 8: "test-analysis tables keyed to product/part codes...". The bottom table is a caption for a table, not the table itself. The handwritten part is a list of effects. Not a specification.
> 
> Therefore, "handwritten" is the best fit.
> 
> Let's double check Check 2: "A log/diary sheet is freeform, not a form... A handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
> This is a handwritten note (list of effects) on blank paper.
> 
> Let's review the whole page.
> Top right: "2197" (handwritten or typed? looks typed).
> Top headers: "EFFECT", "1 R4F", "UR5J4S-35", "FACTOR". Sub-headers: "N", "INTER-CEPT", "SLOPE", "N", "INTER-CEPT", "SLOPE".
> Left side: Handwritten list of anatomical sites and effects.
> Right side: Bates number "2505336064".
> Bottom: Typed table caption "TABLE DOSE RATIO CALCULATION FOR EQUAL BIOLOGICAL EFFECTS BASED ON ... CONCENTRATION, UR5J4S-35 ... ENERGY, RACE RATS, 92-DAY INHALATION PERIOD". Handwritten "4" below it.
> 
> The dominant content is the handwritten list. It's a note.
> Label: handwritten.
> 
> Wait, could it be a "form"?
> Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data...". No, there are no fields or boxes. The typed text at the top looks like column headers for a table that was never filled in (or filled in by hand but not in a structured way). The handwritten text is just a list, not filling a table.
> 
> Could it be a "presentation"?
> Check 9: "Slide/overhead layouts...". No.
> 
> Could it be a "file_folder"?
> Check 1: "Almost no body content...". No, there is body content (the handwritten list and typed table caption).
> 
> So "handwritten" is the correct label.
> 
> Let's refine the scratchpad:
> - file_folder: no — page has substantial handwritten body content and typed table caption, not just an identifier.
> - handwritten: yes — the majority of the page consists of freeform handwritten notes listing biological effects (nose, larynx, trachea, lung) on blank paper, with only minor typed headers at the top and a table caption at the bottom. No printed form fields or running narrative prose.
> - scientific_report: no — lacks running narrative prose; it is a list of effects and a table caption.
> - form: no — no printed fields, boxes, or ruled entry lines; the handwritten text is freeform notes, not filling a structured template.
> 
> Runner-up: scientific_report, ruled out because the page lacks running narrative prose (requires check 13) and is primarily a handwritten note/list.
> 
> Final check of the text: "Most of the content is freeform handwriting... NOT on a printed template."
> The typed headers and table caption are just marginal/structural, the core content is the handwritten list.
> Matches "handwritten".

---

## news_article → form (1 errors)

### `rvl_cdip__news_article__0008.png`
**Expected:** `news_article` | **Predicted:** `form`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** No "From/To/Sent/Subject" email headers. There is a "Subject", "Date", "Circulation", "Client", "Leadership" block, but it looks like a press clipping cover sheet, not an email. Wait, let's look closer. "HILL AND KNOWLTON International Public Relations Counsel", "Press Clipping", "Client: Tobacco Institute of Hong Kong Limited". "Subject: Publication: Oriental Daily News", "Date: March 4, 1987", "Circulation: 650,000". This is a press clipping cover sheet. Not an email.
> - **Masthead/Running head:** There is a clipping of a newspaper article (vertical text, Chinese characters). The main text is English. No journal running head. No newspaper masthead on this page itself (the clipping is embedded).
> 
> **2. Scratchpad checks:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a title "Press Clipping", client info, subject info, a newspaper clipping image, and a paragraph of text. It has real content. Not file_folder.
> 
> *   **Check 2: handwritten**
>     *   Evidence: The text is typed. The newspaper clipping is printed. No majority handwriting. Not handwritten.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or fax header. Not a fax sheet.
> 
> *   **Check 4: questionnaire**
>     *   Evidence: Not a survey instrument. Not a questionnaire.
> 
> *   **Check 5: resume**
>     *   Evidence: Not a CV or resume.
> 
> *   **Check 6: scientific_publication**
>     *   Evidence: No journal running head, volume, issue, page number (except the Bates number 2501454254 and page number 30 at the bottom right, which looks like a Bates number and page count from the archive, not a journal page number). The text is about a seminar. Not a scientific publication.
> 
> *   **Check 7: financial document (invoice/budget)**
>     *   Evidence: No financial tables, invoices, or budgets. "Circulation: 650,000" is media data. Not financial.
> 
> *   **Check 8: specification**
>     *   Evidence: No product data, safety data, or "shall/must" language. Not a specification.
> 
> *   **Check 9: presentation**
>     *   Evidence: Not a slide deck. Not a press release ("FOR IMMEDIATE RELEASE"). Not a speech. Not a photographic slide (it's a press clipping cover). Wait, is it a presentation? No.
> 
> *   **Check 10: administrative form**
>     *   Evidence: It has fields like "Subject:", "Date:", "Circulation:", "Client:", "Leadership:". But it's a cover sheet for a press clipping. Is it a form? "Press Clipping" cover sheet. Let's look at the content. It's a summary of a press clipping.
> 
> *   **Check 11: correspondence (email, memo, letter)**
>     *   Evidence: "HILL AND KNOWLTON... Press Clipping". "Client: Tobacco Institute...". "Subject: Publication: Oriental Daily News". "Date: March 4, 1987". "Circulation: 650,000". "Leadership:". Then a clipping. Then a paragraph: "In a 'passive smoking' seminar held yesterday...". This looks like a memo or a cover letter for a press clipping.
>     *   Wait, let's look at the structure. It has "Subject", "Date", "Client". It looks like a memo or a cover sheet.
>     *   Is it a memo? "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose". Here we have "Subject:", "Date:", "Client:", "Leadership:". It's not a standard memo header.
>     *   Is it a letter? No external address, no "Dear...", no closing signature.
>     *   Is it an email? No mail-client headers.
>     *   Let's re-evaluate. This is a "Press Clipping" cover sheet from a PR firm (Hill and Knowlton) to a client (Tobacco Institute). It summarizes a clipping.
>     *   Wait, look at the text body: "In a 'passive smoking' seminar held yesterday, Mr Steve Kroos... called for rational debate...". This is the text of the press clipping or a summary of it.
>     *   Actually, this looks like a **news_article** or a clipping. But the page itself is a cover sheet for a press clipping.
>     *   Let's check the labels again. `news_article`: "Newspaper or magazine masthead... Also a magazine feature or an encyclopedia entry/excerpt... or any page that presents as published periodical editorial content from a GENERAL-AUDIENCE outlet". This page presents a press clipping. The clipping is from "Oriental Daily News". The page itself is a PR summary.
>     *   Is there a better label?
>     *   Let's look at `advertisement`. No.
>     *   Let's look at `form`. "Filled or blank fields...". This has fields. But it's a specific type of document.
>     *   Let's look at `letter`. No.
>     *   Let's look at `memo`. No.
> 
> Let's reconsider the content.
> The page is a "Press Clipping" cover sheet.
> Top: "HILL AND KNOWLTON International Public Relations Counsel".
> "Press Clipping".
> "Client: Tobacco Institute of Hong Kong Limited".
> Right side: "Subject Publication: Oriental Daily News", "Date: March 4, 1987", "Circulation: 650,000".
> "Leadership:".
> Then a vertical Chinese newspaper clipping.
> Then a paragraph of English text summarizing the event.
> Bottom right: Bates number "2501454254" and page number "30".
> 
> This is a press clipping summary.
> Is it a `news_article`? The text describes a news event ("In a 'passive smoking' seminar held yesterday..."). But the page is a PR cover sheet.
> Is it a `form`? It has fields. But it's not a generic administrative form.
> Is it a `letter`? No.
> Is it a `memo`? No.
> 
> Let's look at the checks again.
> Check 12: `news_article`. "Newspaper or magazine masthead...". The clipping is from a newspaper. But the page is a PR cover sheet.
> Wait, "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement... is an advertisement... news_article requires the page to present primarily as editorial/multi-story news content". This page is not editorial news content primarily; it's a PR summary.
> 
> Let's look at `advertisement`. No.
> 
> What about `form`?
> Check 10: "Administrative form -> form. Filled or blank fields, boxes, checkboxes...". This page has fields (Subject, Date, Circulation, Client). It's a cover sheet for a press clipping. Is a press clipping cover sheet a form?
> Usually, PR firms use forms to track clippings. "Press Clipping" form.
> Let's check the definition of `form`: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data; an application... a records-management inventory... a QA/parameter review sheet... A form does NOT have to be blank... This also covers: a standalone labeled data chart or table... internal authorization/approval forms".
> This page captures data about a press clipping: Publication, Date, Circulation, Client. It is a form used by a PR firm to log a press clipping.
> 
> Let's look at `letter`.
> "A dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."
> The "Client" is Tobacco Institute. The "Leadership" field is empty.
> The text below is the content of the clipping/summary.
> 
> Let's look at `memo`.
> "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose".
> This has "Subject", "Date". But no "To", "From". It has "Client". It's a cover sheet.
> 
> Let's reconsider `news_article`.
> The text "In a 'passive smoking' seminar held yesterday..." is the content.
> The clipping is the content.
> But the page is a cover sheet.
> 
> Actually, looking closely at the text:
> "In a 'passive smoking' seminar held yesterday, Mr Steve Kroos, Chairman of the Tobacco Institute of Hong Kong, called for rational debate on the issue that smoking is hazardous to health. He said that discussion by the public on the issue has apparently became sensational and politicalized. Two US scholars pointed out that, although a number of researchs have been conducted throughout the world, no association between passive smoking and health hazards has been established."
> 
> This is a summary of a news event.
> The page is a "Press Clipping" cover sheet from Hill and Knowlton.
> This is a standard PR clipping report page.
> Is it a `form`? Yes, it's a structured document capturing metadata about a press clipping (Publication, Date, Circulation, Client).
> Is it a `news_article`? No, it's a PR summary of a news article. The dominant layout is the cover sheet metadata + the clipping image + the summary text.
> 
> Wait, is there a label for "Press Clipping"? No.
> The labels are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
> If I have to choose between `form` and `news_article` or `letter` or `memo`.
> The page has a header block: "HILL AND KNOWLTON", "Press Clipping", "Client: ...", "Subject: ...", "Date: ...", "Circulation: ...".
> This looks like a cover sheet for a report or a form.
> In the tobacco archive, PR firms (Hill and Knowlton) produced "Press Clipping" reports. These are often forms or letters.
> If it's a cover letter, it would have "Dear ...". It doesn't.
> If it's a memo, it needs TO/FROM. It doesn't.
> If it's a form, it captures data. It captures data about the clipping.
> 
> Let's look at Check 10 (Form): "Filled or blank fields... for capturing factual data". This page has fields for Publication, Date, Circulation, Client. It is a form used to log a press clipping.
> Also, the text body is the content of the clipping/summary.
> The page is a "Press Clipping" form/cover sheet.
> 
> Let's check if it could be `news_article`.
> Check 12: "Newspaper or magazine masthead...". The clipping has Chinese text, vertical. The main page has English text. The English text is a summary. The page itself is not a newspaper page. It's a PR document. So not `news_article`.
> 
> Let's check `letter`.
> Check 11: "letterhead with an external recipient address, date, 'Dear ...' salutation...". No salutation. No closing signature. Not a letter.
> 
> Let's check `memo`.
> Check 11: "internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". We have "Subject", "Date". We have "Client". We don't have "To", "From". We don't have memo-style prose immediately following. The prose is a summary of the clipping. Not a memo.
> 
> So it's likely `form`.
> The page is a structured cover sheet for a press clipping, capturing metadata (Publication, Date, Circulation, Client). This fits "capturing factual data" or a specific type of administrative form (clipping log).
> Wait, "A page whose primary structure is a memo header + prose... stays memo". This doesn't have a memo header.
> "A page whose primary structure is a letter... stays letter". No.
> 
> Is it `presentation`?
> Check 9: "Slide/overhead layouts... deck title... meeting/program/speaker cover page... corporate press release...".
> "Press Clipping" is not a press release ("FOR IMMEDIATE RELEASE").
> It's not a slide deck.
> 
> Is it `scientific_report`?
> Check 13: "Running narrative prose...". The text is a short paragraph (4 lines). Not a full report.
> 
> So `form` seems the best fit. It's a form for logging press clippings.
> Actually, let's look at the structure again.
> Header: Hill and Knowlton.
> Title: Press Clipping.
> Fields: Client, Subject, Date, Circulation, Leadership.
> Content: Image of clipping, text summary.
> This is a standard "Press Clipping Report" page. In document classification for this archive, these are often classified as `form` (administrative form for tracking) or `letter` (if it's a cover letter).
> Since there's no salutation/closing, and it has specific fields for data capture (Publication, Date, Circulation), `form` is appropriate.
> Wait, is there a label `press_clipping`? No.
> The labels are fixed.
> 
> Let's reconsider `news_article`.
> The text is about a news event. But the page is a PR summary.
> Check 12 says: "Judge by DOMINANT content... news_article requires the page to present primarily as editorial/multi-story news content". This page presents as a PR cover sheet with a clipping. Not primarily editorial news content.
> 
> Let's reconsider `advertisement`.
> No.
> 
> Let's reconsider `file_folder`.
> No, it has content.
> 
> Let's look at the "Leadership:" field. It's empty.
> The fields are:
> Subject: Publication: Oriental Daily News
> Date: March 4, 1987
> Circulation: 650,000
> Client: Tobacco Institute of Hong Kong Limited
> 
> This is a metadata block.
> The document is a "Press Clipping" cover sheet.
> In the tobacco archive, these Hill and Knowlton press clipping reports are often forms or letters.
> If I have to choose, `form` fits "capturing factual data" (metadata about the clipping).
> However, the text body is a summary.
> Is it a `memo`? "A dated internal note addressed to a named person by NAME + INTERNAL TITLE... with memo-style prose... IS a memo even without literal TO:/FROM: labels".
> Here, "Client: Tobacco Institute...". "Leadership:" (empty).
> The text is "In a 'passive smoking' seminar...". This is not addressed to a person. It's a summary.
> 
> Let's look at the label `form`.
> Check 10: "Administrative form -> form. Filled or blank fields... for capturing factual data...".
> This page has fields for Publication, Date, Circulation. It captures factual data about the press clipping.
> The text below is the content being captured/summarized.
> So `form` is a strong candidate.
> 
> Wait, is it `letter`?
> Sometimes cover sheets are considered letters if they accompany a document. But this page *is* the document (the cover sheet + the clipping summary).
> If it's a cover letter, it needs "Dear...". It doesn't have it.
> 
> Let's look at the example worked examples.
> Worked example 1: Questionnaire.
> Worked example 2: Scientific report.
> Worked example 3: Scientific publication.
> 
> This page: "HILL AND KNOWLTON... Press Clipping".
> It's a PR document.
> If I look at similar documents in the tobacco archive (I can't, but I can infer), press clipping summaries from PR firms are often classified as `form` (if structured) or `letter` (if cover letter) or `news_article` (if the clipping itself is the main content and the page is just the clipping).
> Here, the page has a lot of metadata (Hill and Knowlton header, Client, Subject, Date, Circulation). This is structured data.
> The text is a short summary.
> The image is a clipping.
> This looks like a `form` (a press clipping log form).
> 
> Let's check if it could be `news_article` because of the content.
> The content is about "passive smoking".
> But the page is a PR cover sheet.
> Check 12: "a page that presents itself as a newspaper... is news_article". This page does not present itself as a newspaper. It presents itself as a "Press Clipping" from "Hill and Knowlton".
> 
> So `form` is the most logical choice among the 16.
> Wait, is there any other label?
> `specification`? No.
> `budget`? No.
> `invoice`? No.
> 
> Let's refine the `form` argument.
> Check 10: "Filled or blank fields, boxes, checkboxes, and ruled entry lines for capturing factual data".
> The page has:
> - Client: [Text]
> - Subject: [Text]
> - Date: [Text]
> - Circulation: [Text]
> - Leadership: [Empty]
> These are fields capturing factual data about the press clipping.
> The page is a template/cover sheet for a press clipping.
> So `form` is correct.
> 
> One counter-argument: The text body is a narrative summary.
> Check 13 (scientific_report): "Requires running prose". This is 4 lines of prose. Not a report.
> Check 11 (memo/letter): No proper header/salutation/closing.
> 
> So `form` is the best fit.
> 
> Wait, looking closely at the text:
> "In a 'passive smoking' seminar held yesterday..."
> This is the text of the article or a summary.
> The page is a "Press Clipping" cover.
> In many classification schemes for this archive, PR press clipping reports are classified as `form` (if they are structured logs) or `letter` (if they are cover letters).
> Given the fields "Subject", "Date", "Circulation", "Client", it's a structured form.
> 
> Final decision: `form`.
> 
> Wait, let's look at the "Leadership:" field. It's likely "Leadership:" followed by names, but it's cut off or empty.
> The text "Leadership:" is there.
> 
> Let's double check `news_article`.
> Could the dominant content be the news article?
> The page has a large vertical Chinese clipping.
> And a paragraph of English text.
> And the header metadata.
> The metadata takes up the top 1/3. The clipping takes up the middle. The text takes up the bottom 1/3.
> The page is a PR summary. Not a news article.
> 
> So `form`.
> 
> One more check: `advertisement`.
> No.
> 
> One more check: `presentation`.
> No.
> 
> The label is `form`.
> 
> Wait, is it `letter`?
> "A dated note addressed to a named EXTERNAL person (e.g. 'Mr. T. E. Sandefur') with prose and no TO:/FROM: block."
> The "Client" is an organization, not a named person. "Tobacco Institute of Hong Kong Limited".
> So not a letter to an external person.
> 
> Is it `memo`?
> "A dated internal note addressed to a named person by NAME + INTERNAL TITLE... with memo-style prose".
> No named person addressed.
> 
> So `form`.
> 
> The page is a "Press Clipping" form from Hill and Knowlton.
> 
> <scratchpad>
> file_folder: no — page has header metadata, a newspaper clipping image, and a paragraph of text.
> handwritten: no — typed text and printed clipping.
> fax: no — no fax header.
> questionnaire: no — not a survey.
> resume: no — not a CV.
> scientific_publication: no — no journal running head.
> financial: no — no financial tables.
> specification: no — no product data.
> presentation: no — not a slide deck or press release.
> form: yes — structured cover sheet with fields for "Client", "Subject" (Publication), "Date", "Circulation", "Leadership" capturing metadata about a press clipping from Hill and Knowlton. The page functions as a form to log/summarize a press clipping.
> runner-up: news_article, ruled out because the page is a PR cover sheet/summary (Hill and Knowlton Press Clipping) with metadata fields, not primarily editorial news content from a general outlet (the clipping is embedded, but the page itself is a PR document).
> letter/memo: no — lacks external address/salutation/closing (letter) or TO/FROM header with memo prose (memo). The "Client" field is organizational, not a named individual addressee for a memo/letter.
> </scratchpad>
> <label>form</label>

---

## news_article → advertisement (1 errors)

### `rvl_cdip__news_article__0020.png`
**Expected:** `news_article` | **Predicted:** `advertisement`

**Reasoning:**
> The user wants me to classify a scanned business document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: Top of the page has "THE NEW YORK TIMES, MONDAY, SEPTEMBER 18, 1989". This is a newspaper masthead. Wait, let's look closer. "THE NEW YORK TIMES, MONDAY, SEPTEMBER 18, 1989". This is a newspaper masthead. But let's check the dominant content. The page is an advertisement from "the tobacco institute". Let's check check 12 and 14.
> 
> **Check 1: file_folder**
> - Evidence: No, there is a lot of text and layout.
> - Not this check.
> 
> **Check 2: handwritten**
> - Evidence: No, it's typed text.
> - Not this check.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - Evidence: No fax header.
> - Not this check.
> 
> **Check 4: questionnaire**
> - Evidence: No survey instrument.
> - Not this check.
> 
> **Check 5: resume**
> - Evidence: No career history.
> - Not this check.
> 
> **Check 6: scientific_publication**
> - Evidence: No journal running head. The top has "THE NEW YORK TIMES", which is a newspaper.
> - Not this check.
> 
> **Check 7: financial document**
> - Evidence: No financial table or invoice.
> - Not this check.
> 
> **Check 8: specification**
> - Evidence: No material safety data sheet or product formulation.
> - Not this check.
> 
> **Check 9: presentation**
> - Evidence: No slide deck layout.
> - Not this check.
> 
> **Check 10: administrative form**
> - Evidence: No form fields.
> - Not this check.
> 
> **Check 11: correspondence**
> - Evidence: No email/memo/letter structure.
> - Not this check.
> 
> **Check 12: news_article**
> - Evidence: Top has "THE NEW YORK TIMES, MONDAY, SEPTEMBER 18, 1989". But the dominant content is an advertisement. Let's look at check 14.
> 
> **Check 13: scientific_report**
> - Evidence: No running narrative prose of a lab study.
> - Not this check.
> 
> **Check 14: advertisement**
> - Evidence: "the tobacco institute 1776 K Street, N.W., Washington, D.C. 20006". "What Is Advertising Age? The national newspaper of the advertising and marketing industry. A constant champion of truth in advertising. Not a defender of smoking." The page is an ad from the Tobacco Institute promoting "Advertising Age". It has product imagery (newspaper clipping), slogans ("All Advertising Should Be Truthful", "The Truth Seems a Little Twisted"), brand styling.
> - Judge by DOMINANT content: a single brand ad with product imagery, slogans, and a Surgeon General warning (maybe not here, but it's an ad) is advertisement even if it sits on a newspaper page with a running masthead. The page is clearly an advertisement placed in a newspaper (Advertising Age or NYT? The top says "THE NEW YORK TIMES", but the content is an ad for "Advertising Age" by "the tobacco institute"). Wait, the top says "THE NEW YORK TIMES, MONDAY, SEPTEMBER 18, 1989". The ad is "Reprinted with permission from November 10, 1969, the Advertising Age". The ad is promoting "Advertising Age" and "the tobacco institute". This is an advertisement.
> - Check 14: "Marketing layout: product imagery, slogans, brand styling, coupons, flyers, brochures. Judge by DOMINANT content (see check 12): a single brand ad with product imagery, slogans, and a Surgeon General warning is advertisement even if it sits on a newspaper page with a running masthead and some surrounding text."
> 
> Let's double check check 12 vs 14.
> Check 12: "Judge by DOMINANT content: a page whose dominant layout is a single brand advertisement (product imagery, slogans, a Surgeon General warning, brand styling) is an advertisement (check 14) even when printed inside a newspaper/magazine with a running masthead and some surrounding text; news_article requires the page to present primarily as editorial/multi-story news content, not as one promotional layout."
> The page is entirely an advertisement from "the tobacco institute" for "Advertising Age". It has the headline "All Advertising Should Be Truthful", a clipping from Advertising Age titled "The Truth Seems a Little Twisted", and a section "What Is Advertising Age?". This is an advertisement.
> 
> Therefore, the label is advertisement.
> 
> Let's review the scratchpad steps:
> 1. file_folder: no — page has extensive text and layout.
> 2. handwritten: no — typed text throughout.
> 3. FAX: no — no fax header.
> 4. questionnaire: no — no survey.
> 5. resume: no — no career history.
> 6. scientific_publication: no — no journal identifier.
> 7. financial: no — no financial data.
> 8. specification: no — no product specs.
> 9. presentation: no — not a slide deck.
> 10. form: no — no form fields.
> 11. correspondence: no — no memo/letter structure.
> 12. news_article: no — although there is a newspaper masthead ("THE NEW YORK TIMES"), the dominant content is a single promotional layout/advertisement, not editorial news content.
> 13. scientific_report: no — no research prose.
> 14. advertisement: yes — page is a promotional layout from "the tobacco institute" for "Advertising Age", featuring slogans ("All Advertising Should Be Truthful"), brand styling, and a description of the publication ("What Is Advertising Age?"). Dominant content is an advertisement.
> 
> Runner-up: news_article, ruled out because the page's dominant layout is a single brand advertisement (check 14) rather than editorial/multi-story news content, despite the newspaper masthead at the top.
> 
> Final label: advertisement.

---

## presentation → memo (1 errors)

### `rvl_cdip__presentation__0013.png`
**Expected:** `presentation` | **Predicted:** `memo`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header:** No "From:", "To:", "Sent:", "Subject:" headers. No forwarded trail.
> - **Masthead/Running head:** No newspaper/magazine masthead. No journal running head/volume/issue/page number.
> - **Content:** Mostly blank white space.
>     - Top center: Handwritten "DLG", "XJNT" (or similar initials).
>     - Typed text: "First draft for April 29. Please add."
>     - Typed text: "Lance"
>     - Bottom right: Vertical number "526001380" (Bates number).
>     - Bottom edge: Some black bars/artifacts (scan artifacts or folder edges?). Wait, looking closely at the bottom, there are black shapes. Let's look at the bottom edge. There are black rectangular shapes. This looks like a scanned page with some artifacts.
>     - Wait, is this a handwritten note? "First draft for April 29. Please add." and "Lance". And handwritten initials "DLG", "XJNT".
>     - Let's check the checks.
> 
> **2. Check 1: IDENTIFIER-ONLY PAGE -> file_folder**
> - Content: "First draft for April 29. Please add.", "Lance", handwritten "DLG", "XJNT", Bates number "526001380".
> - Is there a bold headline title? No.
> - Is it a folder tab? No.
> - Is it almost no body content? It has a short note. "First draft for April 29. Please add." and "Lance". This is a note.
> - Wait, check 1 says: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note."
> - "Pure filing metadata only." -> This page has a note ("First draft for April 29. Please add.") and a name ("Lance"). So it's not file_folder. Wait, is a short note enough to disqualify file_folder?
> - "A page is NOT file_folder if it carries any real content — ... or a note."
> - So check 1 is NO.
> 
> **3. Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten**
> - "Most of the content is freeform handwriting... NOT on a printed template."
> - Here, we have typed text: "First draft for April 29. Please add." and "Lance".
> - Handwriting: "DLG", "XJNT".
> - Is most of the content freeform handwriting? No, it's mostly typed text and blank space. The handwriting is just initials.
> - Wait, let's look at the definition: "A typed page with only a signature, stamp, or margin note is not handwritten."
> - This is a typed note with some handwritten initials. So not handwritten.
> 
> **4. Check 3: FAX TRANSMISSION SHEET -> form**
> - No fax header.
> 
> **5. Check 4: SURVEY INSTRUMENT -> questionnaire**
> - No.
> 
> **6. Check 5: RESUME -> resume**
> - No.
> 
> **7. Check 6: PUBLISHED EVIDENCE -> scientific_publication**
> - No journal header.
> 
> **8. Check 7: FINANCIAL DOCUMENT -> invoice/budget**
> - No.
> 
> **9. Check 8: PRODUCT DOCUMENTATION -> specification**
> - No.
> 
> **10. Check 9: SLIDE DECK / PRESENTATION -> presentation**
> - "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."
> - "A single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page)... is a presentation".
> - Here we have "First draft for April 29. Please add." and "Lance".
> - Wait, is this a presentation cover? Or a memo?
> - Let's look at Check 11: CORRESPONDENCE -> memo.
> - "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... Without that header-then-prose structure it is not a memo."
> - "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
> - Here we have "Lance" (name). "First draft for April 29. Please add." (prose/note). Handwritten initials "DLG" (sender?).
> - This looks like a memo or a note. "Lance" is the recipient. "DLG" is the sender (David L. ...?). "First draft for April 29. Please add." is the message.
> - Let's re-read Check 11 memo definition: "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION (e.g. 'Mr. R. J. Smith, Manager - Hanmer Division' from 'T. P. Pettigrew, Manufacturing Services Manager - Research and Development') with memo-style prose and no external address, no 'Dear ...' salutation, and no closing signature IS a memo even without literal 'TO:/FROM:' labels — internal names + titles + date + prose, with no salutation or closing, is a memo header."
> - Here: "Lance" (name). "First draft for April 29. Please add." (prose). "DLG" (sender initials). Date implied "April 29".
> - This fits the memo definition: internal note, named person (Lance), prose ("First draft..."), no salutation/closing.
> 
> Let's check Check 9 again: "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note (e.g. 'Internal Communication 2000 Plan' with 'Draft for discussion'), a single-word/short-phrase heading with no subtitle at all (e.g. 'RECOMMENDATIONS' centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
> - The text is "First draft for April 29. Please add." and "Lance". This is not a bold headline title. It's a note.
> - Is it a presentation? No, it's a note to Lance.
> 
> Let's check Check 11 again.
> - "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block followed directly by memo-style prose... OR a dated internal note addressed to a named person by NAME + ... with memo-style prose... IS a memo".
> - Evidence: "Lance" (named person), "First draft for April 29. Please add." (prose/note), "DLG" (sender initials). No external address, no salutation, no closing.
> - This is a memo.
> 
> Wait, is there any other category?
> - "handwritten": "Most of the content is freeform handwriting...". Here, most content is blank space, some typed text, some handwriting. Not majority handwritten.
> - "file_folder": "A page is NOT file_folder if it carries any real content — ... or a note." This page carries a note ("First draft for April 29. Please add."). So not file_folder.
> 
> So it's a memo.
> 
> Let's refine the memo evidence:
> - Addressed to "Lance".
> - Message: "First draft for April 29. Please add."
> - Sender initials: "DLG" (handwritten).
> - No salutation, no closing signature, no external address.
> - Fits "dated internal note addressed to a named person... with memo-style prose... IS a memo".
> 
> Let's check if it could be a letter.
> - "letter: letterhead with an external recipient address... OR a dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."
> - "Lance" is likely an internal person (Lance is a first name, common in internal memos). "DLG" are initials. No external address. So memo.
> 
> Final check of the text:
> - Top: "DLG" (handwritten), "XJNT" (handwritten, maybe initials or code).
> - "First draft for April 29. Please add."
> - "Lance"
> - Bottom right: "526001380" (Bates number).
> 
> This is a short internal memo/note.
> 
> Label: memo.
> 
> Wait, let's look at the "presentation" check again.
> - "A near-blank cover or title page... is a presentation".
> - But this has a specific message to "Lance". It's a note/memo.
> - Check 11 says: "A dated internal note addressed to a named person by NAME... with memo-style prose... IS a memo".
> - This matches perfectly.
> 
> One detail: "XJNT" might be "XINT" or something. Doesn't matter.
> "DLG" is likely the sender.
> 
> So, memo.
> 
> Scratchpad:
> - file_folder: no — page carries a note ("First draft for April 29. Please add.") and a name ("Lance"), not just filing metadata.
> - handwritten: no — mostly typed text and blank space; handwriting is just initials ("DLG", "XJNT").
> - fax: no — no fax header.
> - questionnaire: no.
> - resume: no.
> - scientific_publication: no — no journal header.
> - financial: no.
> - specification: no.
> - presentation: no — not a deck cover or slide; it's a note to a person.
> - form: no.
> - email: no — no mail-client header.
> - memo: yes — internal note addressed to "Lance" with prose "First draft for April 29. Please add." and sender initials "DLG", no salutation/closing, no external address.
> - news_article: no.
> - scientific_report: no.
> - advertisement: no.
> 
> Runner-up: file_folder, ruled out because the page contains a real note ("First draft for April 29. Please add.") and a recipient name ("Lance"), not just an identifier/stamp. Or runner-up: presentation, ruled out because it's a note to a named individual ("Lance") with specific instructions, not a title page or slide.
> 
> Actually, the instruction says: "add one final line naming the runner-up label you almost picked instead and the single piece of evidence that ruled it out."
> Runner-up: file_folder. Evidence ruled it out: the page contains a real note ("First draft for April 29. Please add.") and a recipient name ("Lance"), which constitutes real content, not just filing metadata.
> 
> Wait, is "Lance" a name? Yes.
> Is "First draft for April 29. Please add." prose? Yes.
> 
> Final label: memo.

---

## questionnaire → scientific_report (1 errors)

### `rvl_cdip__questionnaire__0003.png`
**Expected:** `questionnaire` | **Predicted:** `scientific_report`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> 
> **1. Pre-scan:**
> - **Mail-client header block:** None. No From/To/Sent/Subject.
> - **Masthead/Running head:** No newspaper/magazine masthead. No journal running head/volume/issue/page number (except a page number "1" at the bottom and a Bates number "2023226545" rotated on the right).
> 
> **2. Scratchpad procedure:**
> 
> *   **Check 1: file_folder**
>     *   Evidence: The page has a title "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS (PHYSICAL DEPENDENCE)" and a paragraph of text starting with "Q: Dr. Henningfield...". It has a page number "1" and a Bates number "2023226545".
>     *   Result: Not file_folder. It has real content (a question and title).
> 
> *   **Check 2: handwritten**
>     *   Evidence: The text is typed. No significant handwriting.
>     *   Result: Not handwritten.
> 
> *   **Check 3: FAX TRANSMISSION SHEET**
>     *   Evidence: No "FACSIMILE" or fax header.
>     *   Result: Not this check.
> 
> *   **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL -> questionnaire**
>     *   Evidence: The title is "QUESTIONS FOR DeNOBLE...". The text starts with "Q: Dr. Henningfield...". This looks like a set of questions for a deposition or testimony (Dr. Henningfield and Dr. DeNoble). Wait, is this a questionnaire?
>     *   Let's look at the definition: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
>     *   This is a list of questions for a person (Dr. DeNoble) to answer in a legal context (Subcommittee, Surgeon General, Philip Morris). It's not a survey instrument for consumers. It's a set of questions for testimony.
>     *   Wait, let's look at other categories. Is it a memo? Letter? Scientific report?
>     *   Let's re-read the content. "Q: Dr. Henningfield and the Surgeon General have testified... Isn't it true that your experiments... found that nicotine use does not create a physical dependence?"
>     *   This is a question for a deposition or hearing. It's not a survey.
> 
> *   **Check 5: resume**
>     *   Evidence: No.
> 
> *   **Check 6: scientific_publication**
>     *   Evidence: No journal header. Just a Bates number and page number.
> 
> *   **Check 7: financial document**
>     *   Evidence: No money.
> 
> *   **Check 8: specification**
>     *   Evidence: No.
> 
> *   **Check 9: presentation**
>     *   Evidence: The title is "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS (PHYSICAL DEPENDENCE)". It's a single page with a question. Not a slide deck.
> 
> *   **Check 10: administrative form**
>     *   Evidence: No fields, boxes, checkboxes. Just a question.
> 
> *   **Check 11: correspondence -> email, memo, or letter**
>     *   Evidence: No TO/FROM/RE header. No salutation "Dear...". No closing signature. It's just a question "Q: ...".
>     *   Wait, is it a memo? "internal TO:/FROM:/RE:/SUBJECT:/DATE: header block followed directly by memo-style prose". No header.
>     *   Is it a letter? "letterhead with an external recipient address, date, 'Dear ...' salutation...". No.
> 
> *   **Check 12: news_article**
>     *   Evidence: No masthead.
> 
> *   **Check 13: scientific_report**
>     *   Evidence: "Running narrative prose with objectives, methods, results, or discussion; a draft manuscript... a lab or technical study title page...".
>     *   This page is a question for a deposition. "QUESTIONS FOR DeNOBLE".
>     *   Wait, let's look at the content again. It's a question about scientific findings.
>     *   Is it a scientific_report? "Requires running prose — a page that is only labeled field-value entries... is a filled form". This page has running prose (the question itself).
>     *   But is it a report? It's a question for testimony.
>     *   Let's look at the labels again.
>     *   advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
>     Let's re-evaluate "questionnaire".
>     "The page asks the reader to answer...". This page asks Dr. DeNoble to answer. But it's a legal question, not a survey.
>     However, look at the title: "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS".
>     This looks like a document from a legal archive (tobacco industry archive).
>     Could it be a "memo"? No header.
>     Could it be a "letter"? No.
> 
>     Let's look at Check 13 again: "scientific_report".
>     "Running narrative prose with objectives, methods, results, or discussion...".
>     This is a single question. It's not really a report.
> 
>     Let's look at Check 9: "presentation".
>     "Slide/overhead layouts... deck title or section-divider page...".
>     This is page 1 of a document. "QUESTIONS FOR DeNOBLE...".
>     Maybe it's a section divider? "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle... is a presentation".
>     This page has a title and a paragraph of text. Not near-blank.
> 
>     Let's look at Check 10: "form".
>     "Filled or blank fields...". No.
> 
>     Let's reconsider the content. It's a question for a deposition.
>     Is there a category for legal documents? No.
>     The categories are: advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
>     Let's look at "questionnaire" again.
>     "The page asks the reader to answer, rate, choose, or commit...".
>     In a broad sense, a deposition question is asking the reader (witness) to answer.
>     But usually "questionnaire" in this dataset refers to surveys.
>     Wait, "A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... is still questionnaire".
>     This is a page numbered "1". It has "Q: ...".
>     Is this a survey instrument? "Dr. Henningfield and the Surgeon General have testified... Isn't it true that your experiments... found that nicotine use does not create a physical dependence?"
>     This is a question for a legal proceeding (likely the Master Settlement Agreement or similar tobacco litigation).
>     In the tobacco archive, these are often "Questions for Deposition" or "Interrogatories".
>     If it's not a survey, what is it?
> 
>     Let's look at "scientific_report".
>     "Original research write-up...". This is not original research. It's a question about research.
> 
>     Let's look at "memo".
>     "internal TO:/FROM:/RE:/SUBJECT:/DATE: header block...". No.
>     "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
>     This page has no date, no from/to. Just "Q: ...".
> 
>     Let's look at "letter".
>     "dated note addressed to a named EXTERNAL person...". No.
> 
>     Let's look at "form".
>     "administrative form...". No.
> 
>     Is it a "presentation"?
>     "speech text — the typed text of a speech... is a presentation". No.
>     "deck title or section-divider page".
>     The title is "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS (PHYSICAL DEPENDENCE)".
>     This looks like a title page for a section of questions.
>     But there is body text (the question itself).
> 
>     Let's re-read the checks carefully.
>     Check 4: questionnaire. "The page asks the reader to answer...".
>     Check 13: scientific_report. "Running narrative prose...".
> 
>     Actually, let's look at the structure.
>     Title: QUESTIONS FOR DeNOBLE...
>     Text: Q: [Question text].
>     Page number: 1.
>     Bates number: 2023226545.
> 
>     This is a page from a deposition transcript or a set of questions prepared for a deposition.
>     In the tobacco archive classification tasks (like the one this prompt is based on, likely the UCR tobacco archive or similar), documents like "Questions for Deposition" are often classified as... what?
>     Wait, the prompt says "You classify scanned business documents (tobacco-industry archive...".
>     If it's a set of questions for a witness, is it a "questionnaire"?
>     Definition of questionnaire: "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
>     This doesn't fit well. It's a legal question.
> 
>     Is it a "scientific_report"?
>     The content is about scientific findings (nicotine dependence).
>     But the format is a question.
> 
>     Let's look at "memo" again.
>     Sometimes legal memos or internal documents are memos. But this lacks the header.
> 
>     Let's look at "form".
>     No fields.
> 
>     Let's look at "file_folder".
>     No, it has content.
> 
>     Let's look at "presentation".
>     "A near-blank cover or title page... is a presentation".
>     This page has a title and a paragraph. Not near-blank.
> 
>     What about "letter"?
>     No.
> 
>     Let's reconsider "questionnaire".
>     In some contexts, a list of questions for an interview or deposition is treated like a questionnaire instrument.
>     "The page asks the reader to answer...". Dr. DeNoble is asked to answer.
>     But the definition says "survey instrument".
>     "A page does not have to show questions to be a questionnaire: an appendix page... of a survey instrument".
>     This is not a survey instrument.
> 
>     Let's look at the label "scientific_report".
>     "Running narrative prose with objectives, methods, results, or discussion".
>     The text is: "Dr. Henningfield and the Surgeon General have testified... It is my understanding that... Isn't it true that...?"
>     This is running prose. It discusses scientific findings (nicotine use creates physical dependence).
>     It's a question *about* a scientific report/findings.
>     Is the document itself a scientific report? No.
> 
>     Wait, is there a category I missed?
>     advertisement, budget, email, file_folder, form, handwritten, invoice, letter, memo, news_article, presentation, questionnaire, resume, scientific_publication, scientific_report, specification.
> 
>     Let's look at the "Calibration" section.
>     "form, scientific_report, and handwritten are historically the most over-predicted labels".
>     "news_article and presentation are historically under-predicted".
> 
>     Let's look at the document again.
>     It's page 1. "QUESTIONS FOR DeNOBLE...".
>     This is likely the first page of a set of questions for a deposition of Dr. DeNoble.
>     In many document classification schemas for legal/tobacco archives, deposition questions or interrogatories might be classified as "form" (if structured) or "letter" or "memo" or just "other".
>     But I must choose from the 16 labels.
> 
>     Let's look at Check 11: Correspondence.
>     "memo: internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". No.
>     "letter: letterhead with an external recipient address...". No.
>     "email: mail-client header block...". No.
> 
>     Let's look at Check 10: Administrative Form.
>     "Filled or blank fields, boxes, checkboxes...". No.
>     "A standalone labeled data chart or table...". No.
> 
>     Let's look at Check 9: Presentation.
>     "Slide/overhead layouts...". No.
>     "deck title or section-divider page".
>     "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle... is a presentation".
>     This page has a title and a block of text.
>     "A large heading rotated 90 degrees... is a section divider". The heading is not rotated.
>     "Technical-study title pages... is scientific_report". The title is "QUESTIONS FOR DeNOBLE...", not a technical study title.
> 
>     Let's look at Check 4: Questionnaire.
>     "The page asks the reader to answer...".
>     The text is a question "Q: ...".
>     Is this a survey? No.
>     But maybe in this dataset, any page with "Q:" and a question is a questionnaire?
>     "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines..."
>     This is an open-response line (the answer would be "Yes" or "No" or a narrative).
>     "A page does not have to show questions to be a questionnaire: an appendix page, section cover, transmittal note, or page-numbered part of a survey instrument... is still questionnaire".
>     This is page 1. It has "Q:". It is part of a set of questions.
>     If the document is a set of questions for a witness, is it a questionnaire?
>     Technically, a questionnaire is a research instrument. A deposition question is a legal instrument.
>     However, if I have to choose, "questionnaire" is the closest functional match (asking for an answer).
>     BUT, the definition says "survey instrument".
> 
>     Let's look at Check 13: scientific_report.
>     "Original research write-up...". No.
>     "scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up".
>     This is a question *about* a study's data. "Isn't it true that your experiments... found that...?"
>     This is a critique/challenge of data.
>     "Comments to Y.-P. Sun et al. analyzing whether the data support the authors' conclusion is a research write-up".
>     This page is a question challenging Dr. DeNoble's experiments.
>     It is a "scientific commentary/critique" in the form of a deposition question.
>     So it could be scientific_report.
>     "Requires running prose". The text is running prose (the question is a paragraph of prose).
>     "a scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up, not an email or letter."
>     This fits! The text is arguing/challenging the data: "It is my understanding that... Isn't it true that... found that nicotine use does not create a physical dependence?"
>     This is a critique of the scientific findings.
>     So, scientific_report.
> 
>     Let's verify.
>     Content: "Q: Dr. Henningfield and the Surgeon General have testified... Isn't it true that your experiments at Philip Morris... found that nicotine use does not create a physical dependence?"
>     This is a question posed to a witness (Dr. DeNoble) regarding his scientific findings.
>     Is the document itself a scientific report?
>     The document is a set of questions.
>     But the text is a "scientific commentary/critique with running argument about a study's data and conclusions".
>     The check says: "A scientific commentary/critique with running argument about a study's data and conclusions (e.g. 'Comments to Y.-P. Sun et al.' analyzing whether the data support the authors' conclusion) is a research write-up, not an email or letter."
>     This page is essentially a critique/challenge of the data (asserting that the experiments found no dependence, contrary to the Surgeon General).
>     So it falls under scientific_report (check 13).
> 
>     Let's check the labels again.
>     scientific_report: "Original research write-up... Also scientific_report: ... A scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up".
>     The text is a question, but it contains a running argument/critique: "It is my understanding that... Isn't it true that...".
>     It's prose.
>     It's not a form, not a memo (no header), not a letter (no salutation/closing).
>     It's not a publication (no journal header).
>     It's not a presentation (not sparse slide layout).
> 
>     Wait, is there any other category?
>     What about "form"? No.
>     What about "letter"? No.
> 
>     Let's look at the "questionnaire" definition again.
>     "The page asks the reader to answer...".
>     If I classify this as questionnaire, it's because it asks a question.
>     But the definition specifies "survey instrument". "opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
>     This is a legal deposition question. Not a survey.
> 
>     So scientific_report seems the best fit among the options, specifically the "scientific commentary/critique" part of check 13.
>     The text is challenging the scientific conclusion ("nicotine use does not create a physical dependence").
>     "Requires running prose". The question is written in running prose (a long paragraph).
> 
>     Let's double check Check 11 (Correspondence).
>     "memo: ... internal 'TO:/FROM:/RE:/SUBJECT:/DATE:' header block...". None.
>     "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo".
>     Is this a dated internal note?
>     No date. No "From". No "To" (except implied "Q: Dr. Henningfield...").
>     Actually, "Q:" implies a questioner.
>     It's not a memo.
> 
>     Let's double check Check 9 (Presentation).
>     "speech text... is a presentation".
>     Is this a speech? No, it's a question for a deposition.
> 
>     Let's consider "form" (Check 10).
>     "administrative form...". No.
> 
>     So it's likely scientific_report.
>     Why? Because it's a text discussing scientific findings (nicotine dependence) and challenging them. It's a "scientific commentary/critique".
>     The label "scientific_report" covers "Original research write-up" and "scientific commentary/critique".
>     Even though it's formatted as a question "Q:", the content is scientific critique.
> 
>     Wait, let's look at the title: "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS (PHYSICAL DEPENDENCE)".
>     This looks like a document prepared by lawyers or scientists to ask Dr. DeNoble about his findings.
>     It's a "questionnaire" in the sense of a list of questions?
>     No, the definition of questionnaire is strict: "survey instrument".
> 
>     Let's look at the "Calibration" note: "form, scientific_report, and handwritten are historically the most over-predicted labels".
>     This suggests I should be careful not to pick scientific_report just because it's technical.
>     "news_article and presentation are historically under-predicted".
> 
>     Is it a presentation?
>     "deck title or section-divider page".
>     The page is titled "QUESTIONS FOR DeNOBLE...".
>     It is page 1.
>     Maybe it's a section divider for a presentation of questions?
>     "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle... is a presentation".
>     This page has a title and a paragraph of text. Not near-blank.
> 
>     Is it a letter?
>     No.
> 
>     Let's reconsider "questionnaire".
>     In some datasets, "Questions for..." documents are classified as questionnaires if they are structured questions.
>     But this is a single question on a page.
>     "The page asks the reader to answer...".
>     If I have to choose between scientific_report and questionnaire...
>     The content is about science (nicotine dependence).
>     The format is a question.
>     But the definition of questionnaire requires a "survey instrument". This is a legal deposition question.
> 
>     Let's look at the example worked out in the prompt? No, I have to do it myself.
>     Wait, the prompt gives worked examples.
>     Example 1: questionnaire (survey instrument).
>     Example 2: scientific_report (title page with summary).
>     Example 3: scientific_publication (journal reprint).
> 
>     This document:
>     Title: QUESTIONS FOR DeNOBLE...
>     Text: Q: [Long paragraph about nicotine dependence experiments].
>     Page 1. Bates number.
> 
>     If I classify as scientific_report:
>     Evidence: "scientific commentary/critique with running argument about a study's data and conclusions". The text argues that Dr. DeNoble's experiments found no dependence, challenging the Surgeon General's testimony. It is running prose.
>     Counter-evidence: It's a question, not a report. "Requires running prose — a page that is only labeled field-value entries... is a filled form". This is not field-value entries. It's a paragraph.
> 
>     If I classify as questionnaire:
>     Evidence: "The page asks the reader to answer". It has "Q:".
>     Counter-evidence: Not a survey instrument.
> 
>     If I classify as form:
>     Evidence: None.
> 
>     If I classify as memo:
>     Evidence: None.
> 
>     Let's look at the label "scientific_report" again.
>     "Original research write-up...". No.
>     "draft manuscript". No.
>     "lab or technical study title page". No.
>     "Requires running prose". Yes, the question is a paragraph of prose.
>     "scientific commentary/critique... is a research write-up". Yes, it critiques the data.
> 
>     So scientific_report is the best fit.
> 
>     Wait, is there a chance it's a "letter"?
>     "A dated note addressed to a named EXTERNAL person... with prose and no TO:/FROM: block."
>     No date.
> 
>     Is it a "memo"?
>     "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo even without literal 'TO:/FROM:' labels".
>     Is there a name and title? "Dr. Henningfield" (mentioned in text), "Dr. DeNoble" (in title). No "From". No date.
> 
>     So scientific_report.
> 
>     One more check: "advertisement". No.
>     "budget". No.
>     "email". No.
>     "file_folder". No.
>     "handwritten". No.
>     "invoice". No.
>     "news_article". No.
>     "resume". No.
>     "scientific_publication". No (no journal header).
>     "specification". No.
> 
>     Final decision: scientific_report.
>     Reasoning: The page contains running prose that constitutes a scientific commentary/critique (challenging the findings of nicotine dependence experiments). It fits the "scientific commentary/critique" clause of check 13.
> 
>     Wait, let's look at the title again: "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS".
>     This implies the document is a set of questions *about* DeNoble's findings.
>     The text is one such question.
>     Is a set of questions a "scientific_report"?
>     The check says: "A scientific commentary/critique with running argument about a study's data and conclusions... is a research write-up".
>     This question is a critique: "Isn't it true that your experiments... found that nicotine use does not create a physical dependence?"
>     It's an argumentative question.
> 
>     Alternative: "questionnaire".
>     If the dataset considers any "Q: ..." page as a questionnaire...
>     But the definition is specific: "survey instrument".
>     "The page asks the reader to answer, rate, choose, or commit: opinion items, rating scales, multiple choice, open-response lines, an enrolment/commitment application, or a cover letter transmitting a survey."
>     This is a legal question.
> 
>     I will stick with scientific_report because of the "scientific commentary/critique" clause and the running prose about scientific data.
> 
>     Wait, let's look at the "Calibration" note again.
>     "form, scientific_report, and handwritten are historically the most over-predicted labels".
>     This is a warning. I should be careful.
>     Is it a form? No.
>     Is it handwritten? No.
>     Is it scientific_report? Maybe over-predicted.
> 
>     What if it's a "presentation"?
>     "deck title or section-divider page".
>     "A near-blank cover or title page... is a presentation".
>     This page is not near-blank. It has a full paragraph.
> 
>     What if it's a "letter"?
>     No.
> 
>     Let's look at the content source. Tobacco industry archive.
>     These are often litigation documents.
>     Deposition questions.
>     How are deposition questions classified in this schema?
>     If not questionnaire (survey), not memo, not letter...
>     Maybe "form"? No.
>     Maybe "scientific_report"?
>     The text is technical/scientific.
>     "A technical/project status report whose content is primarily technical... is scientific_report".
>     This is not a status report.
> 
>     Let's reconsider "questionnaire".
>     "The page asks the reader to answer...".
>     In a very broad sense, a deposition is a Q&A.
>     But the definition says "survey instrument".
> 
>     Let's look at Check 13 again.
>     "Requires running prose".
>     This page has running prose (the question).
>     "a page that is only labeled field-value entries... is a filled form". This is not.
>     So it's not a form.
> 
>     If I have to choose between scientific_report and questionnaire...
>     The content is scientific (nicotine, physical dependence, experiments).
>     The format is a question.
>     If I choose scientific_report, I rely on the "commentary/critique" clause.
>     If I choose questionnaire, I rely on the "asks the reader to answer" clause.
> 
>     Let's look at the example 1: questionnaire.
>     "titled 'QUESTIONNAIRE', asks 'Do you smoke...'".
>     This is clearly a survey.
> 
>     This document: "QUESTIONS FOR DeNOBLE".
>     It's not a survey. It's a legal document.
>     Legal documents in this archive (tobacco) are often memos, letters, or reports.
>     Since it lacks headers, it's hard to classify as memo/letter.
>     The content is scientific critique.
>     So scientific_report is the most logical fit among the imperfect options.
> 
>     Wait! Look at the title: "QUESTIONS FOR DeNOBLE FINDINGS AND ADVICE TO SUPERIORS".
>     This is a document *for* DeNoble? Or *about* DeNoble?
>     "Questions for DeNoble" -> Questions directed at DeNoble.
>     "Findings and Advice to Superiors" -> The content of his findings and advice.
>     This is a summary or a set of questions based on his findings.
> 
>     Actually, looking at the text: "Dr. Henningfield and the Surgeon General have testified... Isn't it true that your experiments... found that nicotine use does not create a physical dependence?"
>     This is a question posed to Dr. DeNoble (presumably by a lawyer or committee member).
>     The document is a page from a deposition or a set of prepared questions.
> 
>     In the absence of a "legal_document" category, and given the content is scientific critique/prose:
>     scientific_report.
> 
>     One distinct possibility: Is it a "memo"?
>     "A dated internal note addressed to a named person by NAME + INTERNAL TITLE/DIVISION... with memo-style prose... IS a memo even without literal 'TO:/FROM:' labels".
>     Is there a date? No.
>     Is there a name + title? "Dr. Henningfield" (in text). "Dr. DeNoble" (in title).
>     No internal title/division visible.
> 
>     I'll go with scientific_report.
> 
>     Wait, let's look at the label "form" again.
>     "administrative form...". No.
> 
>     Let's look at "file_folder".
>     "Almost no body content...". This has body content.
> 
>     Final check: "scientific_report".
>     Evidence: Running prose discussing scientific findings (nicotine dependence) and challenging them ("scientific commentary/critique").
>     Runner-up: questionnaire, ruled out because it's a legal deposition question, not a survey instrument (no survey context, scales, etc.).
> 
>     Wait, is there any chance it's a "presentation"?
>     "speech text... is a presentation".
>     No.
> 
>     I will output scientific_report.
> 
>     Re-reading Check 13: "A scientific commentary/critique with running argument about a study's data and conclusions (e.g. 'Comments to Y.-P. Sun et al.' analyzing whether the data support the authors' conclusion) is a research write-up, not an email or letter."
>     This page is exactly that: analyzing/challenging the data/conclusions of Dr. DeNoble's experiments. "Isn't it true that your experiments... found that nicotine use does not create a physical dependence?"
>     It's a critique.
>     So scientific_report is correct.

---

## questionnaire → presentation (1 errors)

### `rvl_cdip__questionnaire__0005.png`
**Expected:** `questionnaire` | **Predicted:** `presentation`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> **Pre-scan:**
> - Mail-client header block: None.
> - Masthead/running head: None. "Bellomy Research" logo at top. "AROMA MINI GROUPS" in the middle. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991" at bottom right. Address at bottom. Bates number "50918 7883" on the right edge. Handwritten "File Props" at top right.
> 
> **Check 1: file_folder**
> - Almost no body content? There is a title "AROMA MINI GROUPS", a logo "Bellomy Research", "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". This is a cover/title page for a document or presentation. Not file_folder.
> 
> **Check 2: handwritten**
> - Most content is freeform handwriting? No, mostly typed text with a small "File Props" handwritten note.
> 
> **Check 3: FAX TRANSMISSION SHEET**
> - No fax header.
> 
> **Check 4: SURVEY INSTRUMENT OR ITS TRANSMITTAL**
> - No survey instrument.
> 
> **Check 5: PERSON'S CAREER HISTORY**
> - No resume.
> 
> **Check 6: PUBLISHED EVIDENCE**
> - No journal masthead or running head.
> 
> **Check 7: FINANCIAL DOCUMENT**
> - No financial content.
> 
> **Check 8: PRODUCT OR MATERIAL DOCUMENTATION**
> - No specification content.
> 
> **Check 9: SLIDE DECK, DECK COVER, OR COMPANY STATEMENT -> presentation**
> - "Bellomy Research" logo, "AROMA MINI GROUPS" centered, "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". This looks like a cover page for a presentation or a report. Wait, let's look at the layout. It's a title page. "AROMA MINI GROUPS" is a short phrase heading. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991".
> - Is it a presentation cover? "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation (this check), not file_folder (check 1)."
> - Let's check the text: "AROMA MINI GROUPS" is the title. "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". This is a title page for a document prepared for RJR. It could be a presentation cover or a report cover.
> - Wait, check 9 says: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note (e.g. "Internal Communication 2000 Plan" with "Draft for discussion"), a single-word/short-phrase heading with no subtitle at all (e.g. "RECOMMENDATIONS" centered on an otherwise blank page), a deck cover, or a section divider — is a presentation (this check), not file_folder (check 1)."
> - The page has "AROMA MINI GROUPS" centered, "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991" at the bottom right. This is a classic presentation cover or report cover. Given the sparse layout, it fits "presentation" (deck cover or title page).
> - Let's re-read check 9: "Slide/overhead layouts... a deck title or section-divider page, a meeting/program/speaker cover page... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date... is a presentation".
> - Is there any other category? What about scientific_report? No running prose.
> - What about form? No fields.
> - Let's consider if it's a presentation. Yes, "Bellomy Research" prepared this for RJR. It's likely a presentation deck cover or a report cover. The instructions say: "a near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation". This page is mostly empty space, with "AROMA MINI GROUPS" as the title, and "Prepared For... November 1991" as date/recipient. This matches presentation.
> 
> Let's double check check 1: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only. ... A prominent topical heading always counts as real content, subtitle or not. EXCEPTION — folder tabs...". This is not a folder tab. It's a designed title page.
> 
> Let's double check check 9: "Technical-study title pages: a title page naming a specific study or methodology with a date — e.g. "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter... / November 28, 1966" — is scientific_report (check 13), not presentation". "AROMA MINI GROUPS" is not a specific study or methodology, it's a topic for a presentation or report. Given the sparse layout, it's a presentation cover.
> 
> Wait, is there any other evidence?
> "Bellomy Research" logo. "File Props" handwritten. "AROMA MINI GROUPS". "Prepared For: R. J. REYNOLDS TOBACCO COMPANY November 1991". Address at bottom.
> This is a cover page. Cover pages for decks/reports in this archive are often classified as presentation if they are near-blank with a title and date.
> Let's consider if it could be a scientific_report. No, no running prose.
> Could it be a form? No.
> 
> Let's review the definition of presentation: "Slide/overhead layouts (large sparse type, bullet lists, chart-per-page deck look), a deck title or section-divider page, a meeting/program/speaker cover page, a corporate press release / issued statement... A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or "Draft" note... is a presentation".
> This page is mostly empty space, bold headline title "AROMA MINI GROUPS", date "November 1991", recipient "R. J. REYNOLDS TOBACCO COMPANY". This perfectly matches the "near-blank cover or title page" exception for presentation.
> 
> Let's check if there's any other check.
> Check 10: form. No fields.
> Check 11: correspondence. No TO/FROM/RE or Dear/Salutation.
> Check 12: news_article. No.
> Check 13: scientific_report. No running prose.
> Check 14: advertisement. No.
> 
> So the label is presentation.
> 
> Wait, is "AROMA MINI GROUPS" a technical-study title page? "TECHNICAL DATA and RECOMMENDATIONS / Determination And Reporting Of Total Particulate Matter, Water In Total Particulate Matter, And Nicotine In Cigarette Smoke / November 28, 1966" is an example of scientific_report. "AROMA MINI GROUPS" is just a topic. It's likely a presentation deck cover.
> 
> Let's confirm the evidence for presentation:
> - "mostly empty space with only a bold headline title" ("AROMA MINI GROUPS")
> - "perhaps a subtitle, date" ("November 1991")
> - "Prepared For: R. J. REYNOLDS TOBACCO COMPANY"
> - Logo "Bellomy Research"
> This is a near-blank cover/title page.
> 
> Runner-up: file_folder. Ruled out because the page has a prominent topical heading ("AROMA MINI GROUPS") and a prepared-for block, which counts as real content, not just filing metadata. Also not a folder tab.
> 
> Let's write the scratchpad.
> - file_folder: no — the page has a prominent topical heading ("AROMA MINI GROUPS"), a company logo, and a "Prepared For" block with a date, which constitutes real content (a cover/title page), not just filing metadata.
> - handwritten: no — only a small "File Props" handwritten note; the rest is typed.
> - questionnaire: no — no survey instrument or questions.
> - presentation: yes — a near-blank cover/title page with mostly empty space, a bold headline title ("AROMA MINI GROUPS"), a recipient ("Prepared For: R. J. REYNOLDS TOBACCO COMPANY"), and a date ("November 1991"), matching the presentation cover definition.
> - scientific_report: no — no running narrative prose, just a title page.
> - form: no — no fields, boxes, or ruled lines for data capture.
> 
> Final label: presentation.

---

## questionnaire → handwritten (1 errors)

### `rvl_cdip__questionnaire__0016.png`
**Expected:** `questionnaire` | **Predicted:** `handwritten`

**Reasoning:**
> The user wants me to classify a scanned document into one of 16 categories.
> I will follow the scratchpad procedure, checking 1-14 in order.
> 
> Image analysis:
> - Top: handwritten "79-0414"
> - Middle: handwritten "Lab plan & Questionnaire"
> - Bottom right: stamped "50130 8150" (looks like a Bates number or archive stamp)
> - Left edge: black bar (scan artifact or folder edge?)
> - Bottom right: small handwritten "1" or "f"
> 
> Let's evaluate the checks:
> 
> Pre-scan:
> - Mail-client header: none.
> - Masthead/running head: none.
> 
> Check 1: IDENTIFIER-ONLY PAGE -> file_folder
> - Content: "79-0414", "Lab plan & Questionnaire", "50130 8150".
> - Is it a folder tab? The left edge has a solid black bar. The text is handwritten. Wait, is this a folder tab?
> - "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB — a protruding tab-shaped piece of cardboard... bearing a short filing label... usually with a Bates number stamped on the folder body."
> - The text "Lab plan & Questionnaire" is handwritten. Is it a folder tab? The black bar on the left could be the folder body. But the text is handwritten, not a printed label. Wait, the instructions say: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
> - "Lab plan & Questionnaire" is a note/title. But it's handwritten.
> - Let's look at Check 2: HANDWRITTEN PAGE.
> 
> Check 2: MAJORITY-HANDWRITTEN PAGE -> handwritten
> - "Most of the content is freeform handwriting (notes, letters, memos, drafts) NOT on a printed template."
> - The page has "79-0414" and "Lab plan & Questionnaire" handwritten.
> - Is it a note? Yes, a handwritten note.
> - Wait, what about the black bar on the left? "Scan noise is not handwriting... If the dominant recognizable elements are a stamp, faint archival text, or an ID/number, with only a small rotated handwritten annotation on the side, classify by the stamp/identifier (often file_folder), not handwritten — handwriting must legibly make up most of the page's actual content, not just be the only thing you can partly read on a noisy scan."
> - Here, the handwriting "Lab plan & Questionnaire" is quite large and central. But is it a folder tab?
> - Let's re-read Check 1: "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The label IS filing metadata... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees..."
> - But this label is handwritten. Folder tabs usually have printed labels, but can be handwritten? "a short filing label that names the folder's contents... usually with a Bates number".
> - Wait, if it's a handwritten note on a blank page with a Bates number, it's handwritten.
> - Let's check the text: "79-0414" (handwritten), "Lab plan & Questionnaire" (handwritten). Bottom right: "50130 8150" (stamped, vertical). Small "1" or "f" handwritten.
> - This looks like a handwritten note on a blank page, possibly a cover page or a folder tab with handwritten text.
> - If it's a folder tab, it's file_folder. If it's a handwritten note, it's handwritten.
> - "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
> - "Lab plan & Questionnaire" is a note. So it's not file_folder.
> - Therefore, Check 2: handwritten. "Most of the content is freeform handwriting... This wins over a typed letter or memo layout."
> - Wait, is "Lab plan & Questionnaire" a note? Yes.
> - Let's check if there's any other check.
> - Check 4: questionnaire. "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing... is a transmittal note for the instrument — questionnaire (check 4)". But this is just "Lab plan & Questionnaire", not a note about a questionnaire's revision. It's a title or a note indicating contents.
> - Actually, if it's just "Lab plan & Questionnaire" handwritten, it's a handwritten note.
> - Let's re-read Check 2: "The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note containing a name, address, or other personal/demographic details written freely on blank or lined paper (no printed field labels, boxes, or ruled entry cells) is handwritten."
> - This page is freeform handwriting on blank paper. So it's handwritten.
> 
> Let's carefully consider Check 1 vs Check 2.
> If the page is a folder tab, it's file_folder. "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The label IS filing metadata... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees..."
> But the label here is handwritten. Can a folder tab have a handwritten label? Yes, people handwrite labels on folder tabs.
> However, "Lab plan & Questionnaire" is a topical title. "A page is NOT file_folder if it carries any real content — ... or a note. Pure filing metadata only."
> If it's a handwritten note on a blank page, it's handwritten.
> Let's look at the black bar on the left. "a solid black bar along one edge of the page (a common scanning artifact for slides/transparencies) combined with sparse text placed off-center... points to a photographed slide/overhead — presentation". But this is handwritten text.
> Wait, "Scan noise is not handwriting: on a heavily degraded, noisy scan, don't let illegibility read as 'majority handwritten.' If the dominant recognizable elements are a stamp, faint archival text, or an ID/number, with only a small rotated handwritten annotation on the side, classify by the stamp/identifier (often file_folder), not handwritten — handwriting must legibly make up most of the page's actual content, not just be the only thing you can partly read on a noisy scan."
> Here, the handwriting "Lab plan & Questionnaire" is large and legible. It makes up most of the content. The stamp "50130 8150" is small.
> So it's handwritten.
> 
> Wait, is there any chance it's a file_folder?
> "A Bates number or archive stamp alone is NOT enough: a page that pairs a Bates number with a photographic image... or with a bold headline title... carries real content — it is a cover/title page... not file_folder."
> Here, the "headline title" is handwritten "Lab plan & Questionnaire". It carries real content. So not file_folder.
> 
> Is it a presentation? "A near-blank cover or title page — mostly empty space with only a bold headline title and perhaps a subtitle, date, or 'Draft' note... is a presentation (this check), not file_folder (check 1)."
> But this is handwritten. Check 2 says: "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." Does it win over presentation?
> Check 2: "This includes meeting-minutes sheets and log tables... The real test is PRINTED FIELD LABELS/BOXES vs. FREEFORM PAPER: a handwritten note... is handwritten."
> If it's a handwritten note on a blank page, it's handwritten.
> 
> Let's check the text again: "79-0414", "Lab plan & Questionnaire".
> This is a handwritten note. Label: handwritten.
> 
> Let's double check Check 4: questionnaire.
> "Notes ABOUT a survey instrument are questionnaire, not handwritten: a handwritten note about a questionnaire's revision, distribution, or routing (e.g. 'Revised questionnaire to be used VIII-IV. Revisions highlighted in VIII file. CPP questionnaire was not changed.') is a transmittal note for the instrument — questionnaire (check 4), even though it is freeform handwriting on blank paper."
> This page just says "Lab plan & Questionnaire". It doesn't describe a revision or routing. It's just a title or a note. So it's handwritten.
> 
> What about Check 1 folder tab?
> "Folder-tab pages: many file_folder pages are photographs/scans of a physical manila folder TAB... bearing a short filing label... usually with a Bates number... The label IS filing metadata... so it is NOT a 'topical title' for this check. The page stays file_folder even when the label is rotated 90 degrees, even when the folder body photographs as a solid black bar/border along one or more edges, and even when the label names something that sounds like a document..."
> If this is a folder tab with a handwritten label "Lab plan & Questionnaire", it would be file_folder.
> But the instructions say: "A page is NOT file_folder if it carries any real content — a photograph or slide image, a table, a questionnaire appendix, or a note. Pure filing metadata only."
> If it's a handwritten note, it's not pure filing metadata.
> Also, the text is not rotated 90 degrees. It's upright. "Lab plan & Questionnaire" is written horizontally.
> The black bar is on the left edge.
> I will classify as handwritten.
> 
> Wait, looking closely at the image:
> The text "79-0414" is at the top.
> "Lab plan & Questionnaire" is in the middle.
> "50130 8150" is a stamp at the bottom right, rotated 90 degrees.
> There is a small "1" or "f" near the stamp.
> This looks like a handwritten note on a blank page, possibly a cover sheet or a folder tab. But since it's handwritten and not a printed label on a folder tab, and it's not just an identifier, it's handwritten.
> 
> Let's review the checks:
> 1. file_folder: no, has handwritten note "Lab plan & Questionnaire".
> 2. handwritten: yes, majority content is freeform handwriting on blank paper.
> 3. form: no.
> 4. questionnaire: no, not a note about a questionnaire's revision/routing, just a title.
> 5. resume: no.
> 6. scientific_publication: no.
> 7. invoice/budget: no.
> 8. specification: no.
> 9. presentation: no, it's handwritten, not a designed deck page or slide.
> 10. form: no.
> 11. correspondence: no.
> 12. news_article: no.
> 13. scientific_report: no.
> 14. advertisement: no.
> 
> Final label: handwritten.
> Runner-up: file_folder, ruled out because the page contains a handwritten note ("Lab plan & Questionnaire") rather than just pure filing metadata like a Bates number or printed folder-tab label.
> 
> Wait, is "Lab plan & Questionnaire" a note? Yes.
> Is it a folder tab? The black bar on the left could be the folder body. But the label is handwritten. "Folder-tab pages... bearing a short filing label... usually with a Bates number". If it's a handwritten label on a folder tab, is it file_folder?
> "A page is NOT file_folder if it carries any real content — ... or a note."
> If it's a note, it's handwritten.
> I'll go with handwritten.
> 
> Let's re-read: "If the dominant recognizable elements are a stamp, faint archival text, or an ID/number, with only a small rotated handwritten annotation on the side, classify by the stamp/identifier (often file_folder), not handwritten — handwriting must legibly make up most of the page's actual content, not just be the only thing you can partly read on a noisy scan."
> Here, the handwriting "Lab plan & Questionnaire" is large and central, making up most of the page's content. The stamp is small. So it's handwritten.
> 
> One more check: could it be a presentation? "A near-blank cover or title page — mostly empty space with only a bold headline title... is a presentation". But this is handwritten. Check 2 says "Most of the content is freeform handwriting... This wins over a typed letter or memo layout." It doesn't explicitly say it wins over presentation, but presentation is for "Slide/overhead layouts... a deck title or section-divider page...". A handwritten note is not a deck title.
> 
> I am confident in handwritten.

---
