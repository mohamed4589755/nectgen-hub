with open("styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

card_image_css = """
/* Card Banner Image Styles (Sprints-style) */
.card-image-wrap {
    width: 100%;
    overflow: hidden;
    aspect-ratio: 16 / 9;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}
.card-image-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
}
.card:hover .card-image-wrap img {
    transform: scale(1.06);
}
"""

if ".card-image-wrap" not in css_content:
    css_content += card_image_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("styles.css updated with card-image styles!")


with open("internships.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace Card 1
old_card1 = """                <div class="card glass-panel" id="roleCard1">
                    <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg></div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role1_tag1">AI Research</span>
                        <span class="tag" data-i18n="intern_role1_tag2">Remote</span>
                        <span class="tag" data-i18n="intern_role1_tag3">Paid</span>
                    </div>
                    <h3 class="card-title" data-i18n="intern_role1_title">AI Research Intern (NLP & LLMs)</h3>
                    <p class="card-desc" data-i18n="intern_role1_desc">
                        Work alongside our senior researchers to evaluate, fine-tune, and deploy transformer-based models. You will assist in customizing RAG systems for enterprise document retrieval workflows.
                    </p>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                        <a href="contact.html?role=AI_Research" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole1" data-i18n="intern_apply_btn">Apply Now</a>
                    </div>
                </div>"""

new_card1 = """                <div class="card glass-panel" id="roleCard1" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_ai_research.jpg" alt="AI Research Intern">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="intern_role1_tag1">AI Research</span>
                            <span class="tag" data-i18n="intern_role1_tag2">Remote</span>
                            <span class="tag" data-i18n="intern_role1_tag3">Paid</span>
                        </div>
                        <h3 class="card-title" data-i18n="intern_role1_title">AI Research Intern (NLP & LLMs)</h3>
                        <p class="card-desc" data-i18n="intern_role1_desc">
                            Work alongside our senior researchers to evaluate, fine-tune, and deploy transformer-based models. You will assist in customizing RAG systems for enterprise document retrieval workflows.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                            <a href="contact.html?role=AI_Research" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole1" data-i18n="intern_apply_btn">Apply Now</a>
                        </div>
                    </div>
                </div>"""

html_content = html_content.replace(old_card1, new_card1)

# Replace Card 2
old_card2 = """                <div class="card glass-panel" id="roleCard2">
                    <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg></div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role2_tag1">Data Analytics</span>
                        <span class="tag" data-i18n="intern_role2_tag2">Hybrid</span>
                        <span class="tag" data-i18n="intern_role2_tag3">Paid</span>
                    </div>
                    <h3 class="card-title" data-i18n="intern_role2_title">Data Analytics Intern</h3>
                    <p class="card-desc" data-i18n="intern_role2_desc">
                        Help translate multi-channel operational and marketing metrics into executive dashboards. You will write efficient SQL queries, design beautiful dashboards, and run exploratory data analyses (EDA).
                    </p>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                        <a href="contact.html?role=Data_Analytics" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole2" data-i18n="intern_apply_btn">Apply Now</a>
                    </div>
                </div>"""

new_card2 = """                <div class="card glass-panel" id="roleCard2" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_data_analytics.jpg" alt="Data Analytics Intern">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="intern_role2_tag1">Data Analytics</span>
                            <span class="tag" data-i18n="intern_role2_tag2">Hybrid</span>
                            <span class="tag" data-i18n="intern_role2_tag3">Paid</span>
                        </div>
                        <h3 class="card-title" data-i18n="intern_role2_title">Data Analytics Intern</h3>
                        <p class="card-desc" data-i18n="intern_role2_desc">
                            Help translate multi-channel operational and marketing metrics into executive dashboards. You will write efficient SQL queries, design beautiful dashboards, and run exploratory data analyses (EDA).
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                            <a href="contact.html?role=Data_Analytics" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole2" data-i18n="intern_apply_btn">Apply Now</a>
                        </div>
                    </div>
                </div>"""

html_content = html_content.replace(old_card2, new_card2)

# Replace Card 3
old_card3 = """                <div class="card glass-panel" id="roleCard3">
                    <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg></div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role3_tag1">Machine Learning</span>
                        <span class="tag" data-i18n="intern_role3_tag2">On-site</span>
                        <span class="tag" data-i18n="intern_role3_tag3">Paid</span>
                    </div>
                    <h3 class="card-title" data-i18n="intern_role3_title">Machine Learning Engineer Intern</h3>
                    <p class="card-desc" data-i18n="intern_role3_desc">
                        Support the deployment and containerization of deep learning models in production environments. You will optimize inference latency using tools like ONNX, Docker, and Kubernetes.
                    </p>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_6m">6 Months</b></span>
                        <a href="contact.html?role=ML_Engineer" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole3" data-i18n="intern_apply_btn">Apply Now</a>
                    </div>
                </div>"""

new_card3 = """                <div class="card glass-panel" id="roleCard3" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_ml_engineer.jpg" alt="Machine Learning Engineer Intern">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="intern_role3_tag1">Machine Learning</span>
                            <span class="tag" data-i18n="intern_role3_tag2">On-site</span>
                            <span class="tag" data-i18n="intern_role3_tag3">Paid</span>
                        </div>
                        <h3 class="card-title" data-i18n="intern_role3_title">Machine Learning Engineer Intern</h3>
                        <p class="card-desc" data-i18n="intern_role3_desc">
                            Support the deployment and containerization of deep learning models in production environments. You will optimize inference latency using tools like ONNX, Docker, and Kubernetes.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_6m">6 Months</b></span>
                            <a href="contact.html?role=ML_Engineer" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole3" data-i18n="intern_apply_btn">Apply Now</a>
                        </div>
                    </div>
                </div>"""

html_content = html_content.replace(old_card3, new_card3)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("internships.html layout updated successfully!")
