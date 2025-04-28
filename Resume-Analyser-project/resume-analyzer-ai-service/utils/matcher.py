import re

def categorize_keywords(keywords):
    skills, tools, methodologies, domains = [], [], [], []

    tech_keywords = {
        "python", "java", "c++", "javascript", "typescript", "sql", "html", "css",
        "react", "angular", "vue", "node", "django", "flask", "spring", ".net"
    }

    tool_keywords = {
        "git", "docker", "kubernetes", "jenkins", "aws", "azure", "gcp",
        "terraform", "ansible", "tableau", "powerbi"
    }

    methodology_keywords = {
        "agile", "scrum", "kanban", "waterfall", "devops", "ci/cd",
        "tdd", "bdd", "pair programming"
    }

    # Allowlist of actual domain-related terms
    domain_whitelist = {
        "cloud", "cloud computing", "restful service", "microservice",
        "database", "data warehouse", "api", "web service", "distributed system",
        "saas", "paas", "iaas", "nosql", "sql"
    }

    # If a keyword matches any of these patterns, it's NOT a domain
    exclude_if_contains = re.compile(r"experience|familiarity|understanding|year|\+|preferred|developer|team|join| - ", re.IGNORECASE)
    exclude_if_pattern = re.compile(r"[0-9]|\/|\\|-|[+]", re.IGNORECASE)

    for kw in keywords:
        clean_kw = kw.lower().strip()

        # Filter out unwanted domain-like phrases
        if clean_kw in tech_keywords:
            skills.append(clean_kw)
        elif clean_kw in tool_keywords:
            tools.append(clean_kw)
        elif clean_kw in methodology_keywords:
            methodologies.append(clean_kw)
        elif (clean_kw in domain_whitelist and not exclude_if_contains.search(clean_kw)):
            domains.append(clean_kw)

    return {
        "skills": skills,
        "tools": tools,
        "methodologies": methodologies,
        "domains": domains
    }

# Other functions like `generate_recommendations` and `calculate_match_score` stay the same


def generate_recommendations(overall_score, missing_keywords, job_keywords, resume_keywords):
    recommendations = []

    if overall_score < 50:
        recommendations.append({
            "type": "General Advice",
            "message": "Your resume has significant gaps compared to the job requirements.",
            "suggestion": "Consider gaining experience in the missing areas or highlighting transferable skills."
        })
    elif overall_score < 75:
        recommendations.append({
            "type": "General Advice",
            "message": "Your resume matches some requirements but could be improved.",
            "suggestion": "Focus on the missing skills and tools mentioned above."
        })
    else:
        recommendations.append({
            "type": "General Advice",
            "message": "Good match! Your resume covers most requirements.",
            "suggestion": "Tailor your application to emphasize the most relevant skills and experiences."
        })

    if missing_keywords["skills"]:
        recommendations.append({
            "type": "Critical Skills",
            "message": f"The job requires these key skills: {', '.join(missing_keywords['skills'][:5])}",
            "suggestion": "Highlight these skills in your skills section and provide examples of projects where you used them."
        })

    if missing_keywords["tools"]:
        recommendations.append({
            "type": "Tools",
            "message": f"The job mentions these tools/technologies: {', '.join(missing_keywords['tools'][:3])}",
            "suggestion": "If you have experience with these, add them to your technical skills. Otherwise, consider learning the basics."
        })

    if missing_keywords["methodologies"]:
        recommendations.append({
            "type": "Methodologies",
            "message": f"The job involves these methodologies: {', '.join(missing_keywords['methodologies'])}",
            "suggestion": "Mention any relevant experience with these approaches in your work history."
        })

    noise_words = {"familiarity", "understanding", "knowledge", "team", "environment", "experience", "strong", "dynamic", "working"}
    other_missing = [
        kw for kw in (set(job_keywords) - set(resume_keywords))
        if kw not in (
            missing_keywords.get("skills", []) +
            missing_keywords.get("tools", []) +
            missing_keywords.get("methodologies", []) +
            list(noise_words)
        ) and len(kw) > 3 and kw.isalpha()
    ]

    if other_missing:
        recommendations.append({
            "type": "Keywords",
            "message": f"The job description emphasizes these terms: {', '.join(other_missing[:5])}",
            "suggestion": "Incorporate these naturally into your resume where relevant."
        })

    return recommendations

def calculate_match_score(resume_categories, job_categories):
    match_scores = {}
    for category in job_categories:
        job_kws = job_categories[category]
        resume_kws = resume_categories[category]
        if not job_kws:
            match_scores[category] = 100
        else:
            matched = len(set(job_kws).intersection(resume_kws))
            match_scores[category] = round((matched / len(job_kws)) * 100)

    return match_scores
