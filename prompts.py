def domain_1_prompt(title, authors, retraction_status, retraction_details, expression_of_concern, author_track_record, author_retractions):
    return f"""
I will give you some additional information about the study, retrieved from retractiondatabase.org
Paper Title: {title}
Authors: {authors}
Retraction Status: {retraction_status}, details: {retraction_details}
Expression of Concern: {expression_of_concern}
Authors Track Record: {author_track_record}, details: {author_retractions}

Based on the above information, please answer the Domain 1 questions:

Domain 1:  Inspecting post-publication notices

Does the study have an associated retraction?
•	Users should check whether the publication or publications describing the study have been retracted.  This can typically be performed by accessing the online version of the publication 
on the journal website and by searching the Retraction Watch database  http://retractiondatabase.org/  .  
•	If the main results paper associated with a study has been retracted,  a judgement of “serious concerns”  will typically be warranted, regardless of the reason for the retraction.  An exception would be where a study has been retracted and subsequently replaced by a new version (e.g. to correct an error).  The replacement can then be assessed using INSPECT-SR.

Does the study have an associated expression of concern or other relevant post publication notice?
•	Can be checked while looking whether publications associated with the study have been retracted, by checking journal website and Retraction Watch database http://retractiondatabase.org/ .
•	The reason for the Expression of Concern should be considered when making a judgement. If the Expression of Concern relates to concerns about data validity, for example, this may warrant a judgement” of “serious concerns”.
•	One complication is that Expressions of Concern are used in a variable fashion, with some journals and publishers using them primarily to highlight an ongoing investigation relating to the integrity of a study and others using them to indicate that an investigation has been conducted, but that the outcome of the investigation was not sufficiently clear to justify a retraction nor to fully assuage concerns. The content and purpose of the notice therefore must be carefully considered when making a judgement, but we anticipate that a judgement  at least as severe as “some concerns” will typically be warranted where an Expression of Concern is present. 
•	The term “Expression of Concern” may not always be used, and so authors should consider relevant post publication notices from journals and publishers even if they are not labelled using this term.
•	We make a distinction between post publication notices issued by journals or publishers and post publication comments posted by researchers in the form of letters to the editor or posts on PubPeer (for example) relating to trsutworthiness. The presence of the latter should not automatically trigger concerns, because some critiques of this nature may lack merit. We recommend that these comments should be carefully considered however, as it might assist the user in completing their assessment using the draft INSPECT-SR tool (for example, by directing attention to a problematic feature which can then be incorporated into the corresponding domain-level judgement).

Do other studies by the research team highlight causes for concern (critical retraction, expression of concern, relevant post-publication notices?)
•	We suggest the user searches the first and last author (at minimum) on the Retraction Watch database. 
•	A track record of problems relating to trustworthiness may introduce doubts about the index study. 
•	The user should pay close attention to any notices associated with the author. For example, a previous retraction due to an honest error may not warrant any concerns based on the author’s track record. 
•	If the user does perform these searches in relation to a middle author, the user should consider whether a track record of integrity problems relating to a middle author on the index study are sufficient to introduce concerns about the trustworthiness of the index study.
•	If comments relating to integrity issues on other studies from the author team are identified in other locations, not originating from the journal or publisher (for example, in a letter to the editor or PubPeer) we suggest that the user considers the content of the comment as it may be useful in helping to identify problematic features of the index study.
"""

def domain_2_prompt(title, authors, study_json):
    return f"""
Paper Title: {title}
Authors: {authors}

We have retrieved some additional information about the study from clinicaltrials.gov
Study Details from ClinicalTrials.gov: {study_json}

Based on the above information, answer the Domain 2 questions:
Domain 2: Inspecting conduct, governance and transparency

Are there concerns relating to ethical approval?
•	The user should look for details of the ethical approval for the study, which may be included in the study publication(s) or trial registration entry.
•	The user should look for a corresponding reference number, details of the panel/ board granting approval, and for the date of approval. Partial reporting of these details could warrant a response of “Unclear”.
•	If the user believes that ethical approval was not received, this should trigger a judgement of “serious concerns”. 
•	Where an ethical approval number is available, the user may wish to search for that reference number online (e.g. Google) to check that it hasn’t been taken from another, unrelated study.
•	Ideally, the user would check whether the panel/ board granting ethical approval was certified, although this is likely to be difficult in most cases. 

Are there concerns relating to the timing or absence of study registration?
•	Absent or retrospective registration makes it difficult to determine whether the reported methods and results are an accurate reflection of a planned programme of work. 
•	This check speaks of concerns relating to the timing of study registration rather than to the absence of “prospective” (as opposed to “retrospective”) registration. In a large study, registration shortly after the commencement of participant recruitment might not be strictly “prospective”, but might not warrant concerns, for example. The implications of the timing of the registration should be considered in relation to the particular details of the index study.
•	The user should be mindful of the fact that registration was a less common practice prior to 2010, and was very unusual before 2005.

Are there important inconsistencies between the publication and the registration documents?
•	Where a trial has been registered (prospectively or otherwise), the user may check for major inconsistencies between the publication(s) and registration entry. 
•	The user should consider the history of changes made to the registration page, rather than considering only the latest version.
•	Unexplained discrepancies in sample size, study dates, or eligibility criteria (for example) could be grounds for concern. 
•	The purpose of this check is not to investigate outcome reporting bias.

Is the recruitment of participants implausible?
•	The user should consider the plausibility of recruiting a cohort of the reported size in the reported timeframe, taking care not to confuse the full study duration (which includes follow-up of participants) with the recruitment period.
•	This check requires domain knowledge, for example of the prevalence of the condition under study and an idea of the number of cases likely to be available at the study site(s).
•	The numbers of participants screened and consenting to participate should be considered – inspection of a CONSORT diagram is likely to be useful here.

Are there concerns about the plausibility of conducting the study using the reported methods and resources?
•	The user should consider the plausibility of implementing the protocol as described, given the study setting and reported resources (staffing, funding).
•	This check requires domain knowledge, for example to understand the time and resource requires to administer screening questionnaires and outcome assessments.
"""
