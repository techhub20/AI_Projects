from flask import Flask, request, jsonify
from utils.extract_text import extract_keywords
from utils.matcher import categorize_keywords, generate_recommendations, calculate_match_score

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    resume_text = data.get('resumeText', '')
    job_desc = data.get('jobDescription', '')

    if not resume_text or not job_desc:
        return jsonify({"error": "resumeText and jobDescription are required"}), 400

    # Extract keywords from both resume and job description
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_desc)

    # Categorize keywords into skills, tools, methodologies, and domains
    resume_categories = categorize_keywords(resume_keywords)
    job_categories = categorize_keywords(job_keywords)

    # Calculate the match score
    match_scores = calculate_match_score(resume_categories, job_categories)

    # Overall match score calculation
    category_weights = {
        "skills": 0.4,
        "tools": 0.3,
        "methodologies": 0.2,
        "domains": 0.1
    }
    overall_score = round(sum(match_scores[c] * category_weights.get(c, 0) for c in match_scores))

    # Get missing keywords
    missing_keywords = {
        "skills": list(set(job_categories["skills"]) - set(resume_categories["skills"])),
        "tools": list(set(job_categories["tools"]) - set(resume_categories["tools"])),
        "methodologies": list(set(job_categories["methodologies"]) - set(resume_categories["methodologies"])),
        "domains": list(set(job_categories["domains"]) - set(resume_categories["domains"]))
    }

    # Generate recommendations based on missing keywords and overall score
    recommendations = generate_recommendations(overall_score, missing_keywords, job_keywords, resume_keywords)

    result = {
        "overallMatchScore": overall_score,
        "missingKeywords": missing_keywords,
        "recommendations": recommendations
    }

    ordered_result = {
        "overallMatchScore": result["overallMatchScore"],
        "recommendations": result["recommendations"],
        "missingKeywords": result["missingKeywords"]
    }

    return jsonify(ordered_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
