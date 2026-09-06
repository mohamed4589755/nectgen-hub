with open(r'C:\NextGen Hub Website\lang.js', 'r', encoding='utf-8') as f:
    text = f.read()

en_old = '''        // Testimonials / Slideshow
        slide_tag: "Success Stories",
        slide_title: "What Our Alumni Say",
        slide_sub: "Real feedback from graduates who transitioned into tech careers through NextGen Institute.",
        slide1_quote: "NextGen Institute completely changed my career path. The Advanced AI Diploma gave me the exact hands-on experience and production-ready portfolio to land a job as a Machine Learning Engineer. The 1-on-1 mentorship is outstanding!",
        slide1_author: "Sarah K.",
        slide1_role: "ML Engineer at TechCorp",
        slide2_quote: "The Python and PowerBI projects I built during the Data Analytics track allowed me to transition from marketing into a lead analyst role. The curriculum is highly practical and aligned with real enterprise metrics.",
        slide2_author: "David M.",
        slide2_role: "Senior Data Analyst",
        slide3_quote: "Working on production systems during my internship was a game-changer. I deployed containerized models using Docker and FastAPI. It gave me the confidence to apply to senior-level roles.",
        slide3_author: "Yasmine L.",
        slide3_role: "AI Developer Intern",'''

en_new = '''        // Testimonials / Slideshow
        slide_tag: "Success Stories",
        slide_title: "What Our Alumni Say",
        slide_sub: "Real feedback from trainees who built their skills through NextGen Institute.",
        slide1_quote: "The curriculum content and practical hands-on application are excellent.",
        slide1_author: "Khaled Waleed",
        slide1_role: "Data Analytics Trainee",
        slide2_quote: "The curriculum content and practical hands-on application are excellent.",
        slide2_author: "Sherif Essam",
        slide2_role: "Data Analytics Trainee",'''

ar_old = '''        // Testimonials / Slideshow
        slide_tag: "قصص النجاح",
        slide_title: "ماذا يقول خريجونا",
        slide_sub: "آراء حقيقية من الخريجين الذين انتقلوا إلى وظائف تقنية واعدة عبر NextGen Institute.",
        slide1_quote: "لقد غيّر NextGen Institute مساري المهني تماماً. منحتني دبلومة الذكاء الاصطناعي المتقدم والتعلم العميق الخبرة العملية الدقيقة والمعرض المهني الجاهز للحصول على وظيفة كمهندسة لتعلم الآلة. التوجيه الفردي رائع للغاية!",
        slide1_author: "سارة ك.",
        slide1_role: "مهندسة تعلم آلة في TechCorp",
        slide2_quote: "مشاريع Python و PowerBI التي قمت ببنائها خلال مسار تحليل البيانات مكنتني من الانتقال من التسويق إلى دور محلل بيانات أول. المنهج عملي للغاية ومتوافق مع احتياجات المؤسسات.",
        slide2_author: "ديفيد م.",
        slide2_role: "محلل بيانات أول",
        slide3_quote: "العمل على أنظمة إنتاج حقيقية خلال فترة تدريبي كان نقطة التحول الأساسية. قمت بنشر نماذج معبأة باستخدام Docker و FastAPI. لقد منحني ذلك الثقة للتقديم على وظائف عليا.",
        slide3_author: "ياسمين ل.",
        slide3_role: "متدربة تطوير ذكاء اصطناعي",'''

ar_new = '''        // Testimonials / Slideshow
        slide_tag: "قصص النجاح",
        slide_title: "ماذا يقول متدربونا",
        slide_sub: "آراء حقيقية من المتدربين الذين طوروا مهاراتهم عبر NextGen Institute.",
        slide1_quote: "المحتوى والتطبيق العملي ممتاز.",
        slide1_author: "خالد وليد",
        slide1_role: "متدرب تحليل بيانات",
        slide2_quote: "المحتوى والتطبيق العملي ممتاز.",
        slide2_author: "شريف عصام",
        slide2_role: "متدرب تحليل بيانات",'''

text = text.replace(en_old, en_new)
text = text.replace(ar_old, ar_new)

with open(r'C:\NextGen Hub Website\lang.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Alumni updated in lang.js successfully!")
