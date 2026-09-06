import re

with open(r'C:\NextGen Hub Website\lang.js', 'r', encoding='utf-8') as f:
    text = f.read()

en_intern_faq = '''        // Free Internships FAQ
        intern_faq1_q: "What are the free internships?",
        intern_faq1_a: "Our free internships are practical training opportunities designed to help students gain hands-on experience and build their skills through real-world projects.",
        intern_faq2_q: "Which tracks are available?",
        intern_faq2_a: "We currently offer internships in Data Analytics, AI & Machine Learning, Flutter Development, and Front-End Development.",
        intern_faq3_q: "Are the internships really free?",
        intern_faq3_a: "Yes. The internships are completely free with no registration fees.",
        intern_faq4_q: "Are the internships online or offline?",
        intern_faq4_a: "The internships are delivered online, allowing you to learn and practice from anywhere.",
        intern_faq5_q: "Do I need prior experience to join?",
        intern_faq5_a: "No. Beginners are welcome to apply. The internship is designed to help you develop your skills through practical learning.",
        intern_faq6_q: "Will I work on projects?",
        intern_faq6_a: "Yes. You will work on practical projects related to your chosen track.",
        intern_faq7_q: "Will I receive a certificate?",
        intern_faq7_a: "Yes. Participants who successfully complete the internship receive a certificate of completion.",
        intern_faq8_q: "How long is the internship?",
        intern_faq8_a: "The internship duration depends on the specific training track and cohort.",
        intern_faq9_q: "How can I apply?",
        intern_faq9_a: "Choose your preferred track and click \\"Register Now\\" to submit your application.",
'''

en_boot_faq = '''        // Bootcamps FAQ
        boot_faq_tag: "Common Queries",
        boot_faq_title: "Frequently Asked Questions",
        boot_faq_sub: "Need more details? Here are answers to common questions about our bootcamps.",
        boot_faq1_q: "What bootcamps do you offer?",
        boot_faq1_a: "We offer intensive bootcamps focused on practical, industry-relevant skills in areas such as Data Analytics and AI & Machine Learning.",
        boot_faq2_q: "How long is each bootcamp?",
        boot_faq2_a: "The duration depends on the specific bootcamp and its curriculum.",
        boot_faq3_q: "Are the bootcamps online or offline?",
        boot_faq3_a: "Our bootcamps are delivered online, allowing you to learn from anywhere.",
        boot_faq4_q: "Do I need prior experience?",
        boot_faq4_a: "No. Our bootcamps are designed to accommodate beginners while also helping learners with existing knowledge strengthen their skills.",
        boot_faq5_q: "What will I learn?",
        boot_faq5_a: "You will learn practical tools, technologies, and workflows used in the industry.",
        boot_faq6_q: "Will I work on real projects?",
        boot_faq6_a: "Yes. Practical projects are an essential part of our bootcamps and help you build a portfolio.",
        boot_faq7_q: "Do I receive a certificate?",
        boot_faq7_a: "Yes. Participants who successfully complete the bootcamp receive a certificate of completion.",
        boot_faq8_q: "Is there instructor and mentor support?",
        boot_faq8_a: "Yes. You will receive guidance and support throughout the bootcamp.",
        boot_faq9_q: "Can I pay in installments?",
        boot_faq9_a: "Yes. Installment options are available.",
        boot_faq10_q: "How can I register?",
        boot_faq10_a: "Select the bootcamp you are interested in and click \\"Register Now\\" to start your registration.",
'''

en_diploma_faq = '''        // Diplomas FAQ
        diploma_faq1_q: "What diploma programs do you offer?",
        diploma_faq1_a: "We offer professional diploma programs in Data Analytics, AI & Machine Learning, Flutter Development, and Front-End Development.",
        diploma_faq2_q: "How long are the diploma programs?",
        diploma_faq2_a: "Each diploma program lasts 5 months.",
        diploma_faq3_q: "Are the programs online or offline?",
        diploma_faq3_a: "All programs are delivered online, allowing you to learn and practice from anywhere.",
        diploma_faq4_q: "Do I need prior experience to join?",
        diploma_faq4_a: "No. Our programs are suitable for beginners and learners who want to develop professional skills.",
        diploma_faq5_q: "What will I learn during the diploma?",
        diploma_faq5_a: "You will learn industry-relevant tools and technologies through structured learning, practical tasks, and real-world projects.",
        diploma_faq6_q: "Will I build projects during the program?",
        diploma_faq6_a: "Yes. You will work on practical projects that can be added to your portfolio.",
        diploma_faq7_q: "Do I receive a certificate?",
        diploma_faq7_a: "Yes. Students who successfully complete the program receive a certificate of completion.",
        diploma_faq8_q: "Is there support during the program?",
        diploma_faq8_a: "Yes. Students receive guidance and support throughout the program.",
        diploma_faq9_q: "Can I pay in installments?",
        diploma_faq9_a: "Yes. Installment options are available.",
        diploma_faq10_q: "How can I register?",
        diploma_faq10_a: "Choose your preferred diploma and click \\"Register Now\\" to complete the registration process.",
'''

ar_intern_faq = '''        // Free Internships FAQ (AR)
        intern_faq1_q: "ما هي التدريبات المجانية؟",
        intern_faq1_a: "تدريباتنا المجانية هي فرص تدريبية عملية صُممت لمساعدة الطلاب على اكتساب الخبرة التطبيقية وبناء مهاراتهم من خلال مشاريع واقعية.",
        intern_faq2_q: "ما هي المسارات المتاحة؟",
        intern_faq2_a: "نقدم حالياً تدريبات في تحليل البيانات، الذكاء الاصطناعي وتعلم الآلة، تطوير فلاتر، وتطوير واجهات الويب.",
        intern_faq3_q: "هل التدريبات مجانية بالفعل؟",
        intern_faq3_a: "نعم. التدريبات مجانية بالكامل بدون أي رسوم تسجيل.",
        intern_faq4_q: "هل التدريبات عبر الإنترنت أم حضورية؟",
        intern_faq4_a: "يتم تقديم التدريبات عبر الإنترنت، مما يتيح لك التعلم والتطبيق من أي مكان.",
        intern_faq5_q: "هل أحتاج إلى خبرة سابقة للانضمام؟",
        intern_faq5_a: "لا. المبتدئون مرحب بهم للتقديم. صُمم التدريب لمساعدتك على تطوير مهاراتك من خلال التعلم العملي.",
        intern_faq6_q: "هل سأعمل على مشاريع؟",
        intern_faq6_a: "نعم. ستعمل على مشاريع عملية مرتبطة بالمسار الذي اخترته.",
        intern_faq7_q: "هل سأحصل على شهادة؟",
        intern_faq7_a: "نعم. يحصل المشاركون الذين يكملون التدريب بنجاح على شهادة إتمام.",
        intern_faq8_q: "ما هي مدة التدريب؟",
        intern_faq8_a: "تعتمد مدة التدريب على المسار التدريبي المحدد والدفعة.",
        intern_faq9_q: "كيف يمكنني التقديم؟",
        intern_faq9_a: "اختر مسارك المفضل واضغط على \\"قدم الآن\\" لتقديم طلبك.",
'''

ar_boot_faq = '''        // Bootcamps FAQ (AR)
        boot_faq_tag: "أسئلة شائعة",
        boot_faq_title: "الأسئلة الأكثر تكراراً",
        boot_faq_sub: "هل تحتاج إلى مزيد من التفاصيل؟ إليك إجابات على الأسئلة الشائعة حول معسكراتنا التدريبية.",
        boot_faq1_q: "ما هي المعسكرات التي تقدمونها؟",
        boot_faq1_a: "نقدم معسكرات مكثفة تركز على المهارات العملية المطلوبة في سوق العمل في مجالات مثل تحليل البيانات والذكاء الاصطناعي وتعلم الآلة.",
        boot_faq2_q: "كم تبلغ مدة كل معسكر؟",
        boot_faq2_a: "تعتمد المدة على المعسكر المحدد ومنهجه الدراسي.",
        boot_faq3_q: "هل المعسكرات عبر الإنترنت أم حضورية؟",
        boot_faq3_a: "تُقدم معسكراتنا عبر الإنترنت، مما يتيح لك التعلم من أي مكان.",
        boot_faq4_q: "هل أحتاج إلى خبرة سابقة؟",
        boot_faq4_a: "لا. صُممت معسكراتنا لتناسب المبتدئين وتساعد أيضاً المتعلمين ذوي الخبرة السابقة على تعزيز مهاراتهم.",
        boot_faq5_q: "ماذا سأتعلم؟",
        boot_faq5_a: "ستتعلم الأدوات العملية والتقنيات ومساحات العمل المستخدمة في المجال.",
        boot_faq6_q: "هل سأعمل على مشاريع حقيقية؟",
        boot_faq6_a: "نعم. المشاريع العملية جزء أساسي من معسكراتنا وتساعدك على بناء معرض أعمالك.",
        boot_faq7_q: "هل سأحصل على شهادة؟",
        boot_faq7_a: "نعم. يحصل المشاركون الذين يكملون المعسكر بنجاح على شهادة إتمام.",
        boot_faq8_q: "هل يوجد دعم من المدربين والموجهين؟",
        boot_faq8_a: "نعم. ستتلقى التوجيه والدعم طوال فترة المعسكر.",
        boot_faq9_q: "هل يمكنني الدفع بالتقسيط؟",
        boot_faq9_a: "نعم. تتوفر خيارات الدفع بالتقسيط.",
        boot_faq10_q: "كيف يمكنني التسجيل؟",
        boot_faq10_a: "حدد المعسكر الذي تهتم به واضغط على \\"سجل الآن\\" لبدء التسجيل.",
'''

ar_diploma_faq = '''        // Diplomas FAQ (AR)
        diploma_faq1_q: "ما هي برامج الدبلوم التي تقدمونها؟",
        diploma_faq1_a: "نقدم برامج دبلوم مهنية في تحليل البيانات، الذكاء الاصطناعي وتعلم الآلة، تطوير فلاتر، وتطوير واجهات الويب.",
        diploma_faq2_q: "كم تبلغ مدة برامج الدبلوم؟",
        diploma_faq2_a: "يستغرق كل برنامج دبلوم ٥ أشهر.",
        diploma_faq3_q: "هل البرامج عبر الإنترنت أم حضورية؟",
        diploma_faq3_a: "جميع البرامج تُقدم عبر الإنترنت، مما يتيح لك التعلم والتطبيق من أي مكان.",
        diploma_faq4_q: "هل أحتاج إلى خبرة سابقة للانضمام؟",
        diploma_faq4_a: "لا. برامجنا مناسبة للمبتدئين والمتعلمين الذين يرغبون في تطوير مهارات مهنية.",
        diploma_faq5_q: "ماذا سأتعلم خلال الدبلوم؟",
        diploma_faq5_a: "ستتعلم الأدوات والتقنيات المطلوبة في سوق العمل من خلال تعلم منظم، مهام عملية، ومشاريع واقعية.",
        diploma_faq6_q: "هل سأبني مشاريع خلال البرنامج؟",
        diploma_faq6_a: "نعم. ستعمل على مشاريع عملية يمكنك إضافتها إلى معرض أعمالك.",
        diploma_faq7_q: "هل سأحصل على شهادة؟",
        diploma_faq7_a: "نعم. يحصل الطلاب الذين يكملون البرنامج بنجاح على شهادة إتمام.",
        diploma_faq8_q: "هل يوجد دعم أثناء البرنامج؟",
        diploma_faq8_a: "نعم. يتلقى الطلاب التوجيه والدعم طوال فترة البرنامج.",
        diploma_faq9_q: "هل يمكنني الدفع بالتقسيط؟",
        diploma_faq9_a: "نعم. تتوفر خيارات الدفع بالتقسيط.",
        diploma_faq10_q: "كيف يمكنني التسجيل؟",
        diploma_faq10_a: "اختر الدبلوم المفضل واضغط على \\"سجل الآن\\" لإكمال عملية التسجيل.",
'''

# Split into en and ar sections
parts = text.split('ar: {')
en_part = parts[0]
ar_part = 'ar: {' + parts[1]

# 1. Update EN Part
# Add intern FAQ before // Bootcamps Page
en_part = en_part.replace('// Bootcamps Page', en_intern_faq + '        // Bootcamps Page')

# Replace Bootcamps FAQ in EN
old_boot_en = '''        boot_faq_tag: "Common Queries",
        boot_faq_title: "Frequently Asked Questions",
        boot_faq_sub: "Need more details? Here are answers to common questions about our bootcamps.",
        boot_faq1_q: "What are the prerequisites for the AI/ML track?",
        boot_faq1_a: "Basic Python familiarity and high-school-level math are recommended. We provide pre-course self-study materials two weeks before July 1st to bring you up to speed.",
        boot_faq2_q: "Is there a certificate provided upon graduation?",
        boot_faq2_a: "Yes. All graduates who successfully complete their capstone project and pass the final review will receive an authenticated digital Certificate of Completion.",'''
en_part = en_part.replace(old_boot_en, en_boot_faq.strip())

# Add Diploma FAQ before // About Page in EN
en_part = en_part.replace('// About Page', en_diploma_faq + '        // About Page')

# 2. Update AR Part
# Add intern FAQ before // Bootcamps Page
ar_part = ar_part.replace('// Bootcamps Page', ar_intern_faq + '        // Bootcamps Page')

# Replace Bootcamps FAQ in AR
old_boot_ar = '''        boot_faq_tag: "الأسئلة الشائعة",
        boot_faq_title: "الأسئلة الأكثر تكراراً",
        boot_faq_sub: "هل تحتاج إلى مزيد من التفاصيل؟ إليك إجابات على الأسئلة الشائعة حول معسكراتنا التدريبية.",
        boot_faq1_q: "ما هي المتطلبات الأساسية لمسار الذكاء الاصطناعي وتعلم الآلة؟",
        boot_faq1_a: "يُنصح بمعرفة أساسية بلغة Python والرياضيات بمستوى المدرسة الثانوية. نحن نوفر مواد دراسية تحضيرية قبل أسبوعين من تاريخ البدء لمساعدتك على الاستعداد.",
        boot_faq2_q: "هل يتم تقديم شهادة عند التخرج؟",
        boot_faq2_a: "نعم. يتلقى جميع الخريجين الذين يكملون مشروع التخرج بنجاح ويجتازون المراجعة النهائية شهادة إتمام رقمية معتمدة وقابلة للتحقق.",'''
ar_part = ar_part.replace(old_boot_ar, ar_boot_faq.strip())

# Add Diploma FAQ before // About Page in AR
ar_part = ar_part.replace('// About Page', ar_diploma_faq + '        // About Page')

final_text = en_part + ar_part

with open(r'C:\NextGen Hub Website\lang.js', 'w', encoding='utf-8') as f:
    f.write(final_text)

print("lang.js updated perfectly!")
