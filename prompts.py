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

Please answer these questions by first giving your reasoning, and then your answer to the question. Each subquestion should be answered with either “Yes”, “No”, “Unclear” or “NA” (Not Applicable). The overall domain judgment should be given as "No concerns", "Some concerns" or "Serious concerns".

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

Please answer these questions by first giving your reasoning, and then your answer to the question. Each subquestion should be answered with either “Yes”, “No”, “Unclear” or “NA” (Not Applicable). The overall domain judgment should be given as "No concerns", "Some concerns" or "Serious concerns".

"""

def domain_3_prompt(title, authors):
    return f"""
Paper Title: {title}
Authors: {authors}

Based on the above information, answer the Domain 3 questions:
Domain 3: Inspecting text and figures

Is there any plagiarised text, or text that is incompatible with the study?
•	Plagiarised text may be detected using plagiarism software, or may be noticed while examining multiple studies included in a review. 
•	The user should consider whether duplicated text is problematic this may not be the case for generic descriptions of methods, for example.
•	Problematic studies may feature text which does not make sense in the context of the study.
•	While copying and editing of tables from other papers is known to be a feature of some problematic papers, we cannot currently recommend any software capable of reliably detecting this. The user may however notice duplication of tables while looking across studies included in the systematic review, and any concerns of this nature can be reflected in the response to this check.

As you do not have access to the figures or plagiarism software, you can skip that for now. But please indicate that this is the case.

Please answer these questions by first giving your reasoning, and then your answer to the question. Each subquestion should be answered with either “Yes”, “No”, “Unclear” or “NA” (Not Applicable). The overall domain judgment should be given as "No concerns", "Some concerns" or "Serious concerns".

"""

def domain_4_prompt(title, authors):
    return f"""
Paper Title: {title}
Authors: {authors}

Domain 4: Inspecting results in the study

Are there any unexplained discrepancies between reported data and participant inclusion criteria?
•	The user should check to see whether any results corresponding to patient characteristics are incompatible with the eligibility criteria.
•	It is crucial to check whether an explanation is provided in the manuscript.

Are any baseline data implausible?
•	The user should consider the plausibility of the baseline characteristics. 
•	‘Plausibility’ includes clinical or biological plausibility and statistical plausibility. Domain knowledge is necessary to judge clinical or biological plausibility.
•	It is important to remember that participants in a clinical trial may not be representative of any particular patient population. 
•	Magnitude, frequency, variance, and repetition of values for distinct measurements within a table should be considered. 
•	Known examples in problematic studies include an excess of even or odd numbers, and an excess of multiples of 5.
•	The degree of balance between randomised arms may be informative, with excessive balance or imbalance denoting problems. The user needs to interpret observations relating to balance carefully in the context of the allocation method used (stratified randomisation or minimisation will increase balance) and the influence of rounding (which may increase the degree of similarity or dissimilarity) and correlation between variables. 
•	The user should consider whether unusual values could be due to reporting errors (for example, standard errors reported instead of standard deviations), which may not warrant concerns about trustworthiness.

Are there any discrepancies between results reported in figures, tables, and text?
•	The user should check for contradictions where the same results are reported in multiple places (figures, tables, main text, abstract).
•	This includes checking for discrepancies between numbers of participants described and plotted in a figure.

Are the numbers of participants lost to follow-up implausible?
•	The user should consider whether numbers of participants lost to follow-up is plausible. This may require domain knowledge, for example about the plausibility of little or no attrition given the context, condition and study protocol.
•	It may be useful to consider what level of attrition was anticipated in the sample size calculation reported for the study. For example, if a substantial degree of attrition was anticipated, this may lead to concerns if there was actually little or no attrition in the study.
•	Round, equal numbers of participants lost to follow-up, or numbers lost to follow-up resulting in a perfect match with the planned sample size, may be suggestive of problems, but are unlikely to be sufficient to warrant concerns unless other problematic features are also present.

Are there any unexplained inconsistencies in the numbers of participants?
•	The user should check for unexplained inconsistencies in numbers of participants reported in different parts of the manuscript.
•	Care should be taken not to mistake differences in numbers due to e.g. loss to follow-up, exclusion of participants due to non-adherence.
•	Large unexplained discrepancies with the planned sample size should be noted.

Are any outcome data, including estimated treatment effects, implausible?
•	The user should consider the plausibility of the outcome measurement values in each arm and estimated treatment effects. 
•	‘Plausibility’ includes clinical or biological plausibility and statistical plausibility. Domain knowledge is necessary to judge clinical or biological plausibility.
•	Magnitude, frequency, variance, and repetition of values for distinct measurements within a table should be considered. 
•	While the estimated treatment effect should be considered, the user should be careful not to overinterpret the point estimate (typically the observed difference or ratio in a summary of the outcome measure for each of two study groups) without careful consideration of associated measures of statistical inference (confidence intervals, p-values). A large point estimate for a treatment effect is not unusual if it is accompanied by wide confidence intervals or nonsignificant p-values.
•	It may be useful to compare the estimated effects and CIs to those from other studies in a meta-analysis, to identify unexplained discrepancies. Meta-analysis may be conducted after trustworthiness assessment has been performed, and so this might not come to light until later on. It might therefore be necessary to revisit the assessment should problems come to light when conducting meta-analysis. 

Are the means and variances of integer data impossible?
•	This check only applies to variables which can only take integer values (e.g. 1,2,3,4,…).
•	For these variables, only certain values of the mean and standard deviation are possible for a given sample size. 
•	Consistency of reported means and standard deviations for a given sample size may be assessed using the GRIM and GRIMMER techniques. 
•	Online implementations of these checks are available at http://nickbrown.fr/GRIM (GRIM only), http://www.prepubmed.org/grimmer/ , and https://errors.shinyapps.io/scrutiny/ . The last of these offers a convenient interface for checking several of these at once. 
•	Measures of time, such as age in years or disease duration in months, may be subjected to GRIM/ GRIMMER assessment only if recorded in whole units (e.g. years or months).

Are there errors in statistical results?
•	The user should check whether results of statistical analyses are consistent with reported summary data. For example, where a t-test has been used, the user can check whether the reported p-value is consistent with the reported group means and standard deviations. 
•	Caution is needed however, as p-values based on tests of continuous variables will not generally be exactly reproducible from rounded summary data. The user should consider whether the p-value is consistent with the reported summary data. 
•	As an example, suppose a paper reports results of a t-test for two groups of 30 participants. In group 1, there is a reported mean of 20 and a standard deviation of 4. In group 2, there is a reported mean of 21 and a standard deviation of 2. The p-value is reported as p=0.02. If we try to reproduce the result using the summary data, we get a p-value of p=0.23, which may appear to contradict the reported result. However, the reported summary data is rounded. We can find the smallest p-value that would be consistent with the reported data by using values which would be rounded to those reported in the paper, while making the difference in means as large as possible and the standard deviations as small as possible. In this case, the actual group means could be 19.5 and 21.449, and the standard deviations 3.5 and 1.5. The p-value in this case would be 0.006, which is clearly smaller than the reported value. The summary data are therefore consistent with the reported p-value. If we wanted to see how large the p-value could be while remaining consistent with the summary data, we would make the means as similar as possible and the standard deviations as large as possible, while ensuring that the values would round to the reported summary data. 
•	For categorical data analysed by chi-squared test or similar, where frequencies are reported, the user can attempt to reproduce the p-value from the reported data, without concerns relating to rounding of summary data. 
•	The study authors may have used variations of the reported statistical tests. For example, variations of the chi-squared test and t-test are commonly used (e.g. use of Yates’ correction, or unequal variances t-tests) and where a discrepancy is found, the user should consider whether this could explain the issue. 
•	Following the logic set out above, for continuous data, it may be indicative of problems if the statistical results can all be reproduced exactly from the summary data, as this may imply that no underlying dataset was analysed in producing the results. 

Are any other contradictions implied by the data?
•	There may be other instances of contradictory results that would not be detected using the other checks in this domain.
•	Subgroup counts or means could conflict with results for the overall cohort.
•	A reported value could fall outside of a reported range.
•	Some combinations of outcome are not possible. For example, it is not possible to have more birth events (with one “birth event” defined as the birth of at least one child) than pregnancies.


Are there inconsistencies in descriptions of methods and results across publications describing the study?
•	The user should check for major unexplained discrepancies between publications associated with the study, such as a conference abstract and a main results paper. 
•	Conflicting results, group sizes, or descriptions of methods could warrant concerns.

Please answer these questions by first giving your reasoning, and then your answer to the question. Each subquestion should be answered with either “Yes”, “No”, “Unclear” or “NA” (Not Applicable). Even if the answer is "No", provide the details and precise data and numbers from the paper which made you conclude this. The overall domain judgment should be given as "No concerns", "Some concerns" or "Serious concerns".

"""