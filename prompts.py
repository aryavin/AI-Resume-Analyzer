PROMPT = """
You are an experienced HR Manager and ATS Resume Expert.

Analyze the following resume carefully.

Provide the output in exactly this format:

1. ATS Score (out of 100)
2. Resume Summary
3. Weaknesses
4. Missing Skills
5. Improvement Suggestions
6. Strengths
7. Suitable Job Roles
8. Five Interview Questions with Answers

Important instructions:
- Evaluate the resume based on ATS compatibility, skills, experience, education, projects, keywords, formatting, and job relevance.
- Give an ATS score from 0 to 100.
- Be honest and specific.
- Do not make up information that is not present in the resume.
- For missing skills, mention skills that would improve the candidate's chances for suitable roles.
- For interview questions, provide both the question and a good sample answer based only on the candidate's resume.
- Keep the response clear and easy to understand.

Resume:
{resume}
"""

