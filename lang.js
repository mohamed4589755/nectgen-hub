const translations = {
    en: {
        // Navigation
        nav_home: "Home",
        nav_internships: "Internships",
        nav_bootcamps: "Bootcamps",
        nav_diplomas: "Diplomas",
        nav_about: "About Us",
        nav_contact: "Contact",
        
        // Footer
        footer_desc: "Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.",
        footer_links_title: "Quick Links",
        footer_connect_title: "Connect",
        footer_copyright: "&copy; 2026 NextGen Institute. All rights reserved.",
        footer_design: "Innovate. Learn. Lead.",
        
        // Index Page
        index_hero_tag: "Empower the Future",
        index_hero_title: "Empowering the Next Generation of <span class='gradient-text'>Tech Creators</span>",
        index_hero_sub: "At NextGen Institute, we bridge the gap between academic theory and practical innovation. Join our immersive programs in AI, Machine Learning, and Data Analytics to shape the future of technology.",
        index_hero_cta_primary: "Explore Programs",
        index_tech_tag: "Core Technologies",
        index_tech_title: "Powering Our Curriculum",
        index_hero_cta_secondary: "View Internships",
        index_badge_ml: "Machine Learning",
        index_badge_nn: "Neural Networks",
        index_badge_da: "Analytics",
        index_badge_pm: "Predictive Models",
        index_stat_grads: "500+",
        index_stat_grads_label: "Graduates",
        index_stat_partners: "15+",
        index_stat_partners_label: "Industry Partners",
        index_stat_rate: "94%",
        index_stat_rate_label: "Employment Rate",
        index_values_tag: "Why Choose Us",
        index_values_title: "Designed for Fast-Paced Tech Careers",
        index_values_sub: "We design our curriculum around modern industry workflows, ensuring you develop skills that are in high demand.",
        index_val1_title: "Cutting-Edge AI Curriculums",
        index_val1_desc: "Master neural networks, large language models, and computer vision with tools used by world-class tech firms.",
        index_val2_title: "Real-world Data Analytics",
        index_val2_desc: "Translate complex unstructured datasets into actionable business intelligence using Python, SQL, and PowerBI.",
        index_val3_title: "Mentorship & Internships",
        index_val3_desc: "Work directly under senior engineers and analysts during our seasonal industry-partnered internships.",
        index_cta_title: "Ready to Start Your Tech Journey?",
        index_cta_sub: "Applications for our upcoming summer cohort are now open. Spaces are limited for high-touch mentorship.",
        index_cta_btn: "Get in Touch",
        
        // Testimonials / Slideshow
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
        slide3_role: "AI Developer Intern",

                                // Internships Page
        intern_tag: "تسريع المسار المهني",
        intern_title: "فرص <span class='gradient-text'>التدريب العملي</span>",
        intern_sub: "مهام حقيقية، أنظمة إنتاجية واقعية، وتوجيه إرشادي فعلي. اكتسب خبرة عملية تبرزك أمام مسؤولي التوظيف العالميين.",
        intern_list_title: "الوظائف المتاحة",
        intern_list_sub: "اختر المسار الذي يتوافق مع تطلعاتك المهنية. نحن نقبل المرشحين لمجموعات الصيف والخريف.",
        intern_role1_tag1: "الذكاء الاصطناعي وتعلم الآلة",
        intern_role1_tag2: "عن بعد",
        intern_role1_tag3: "مدفوع",
        intern_role1_title: "متدرب الذكاء الاصطناعي وتعلم الآلة",
        intern_role1_desc: "ساعد في تقييم وتدريب ونشر نماذج التعلم العميق. اعمل مع معالجة اللغات الطبيعية ورؤية الكمبيوتر RAG مع إعداد تدفقات MLOps.",
        intern_duration_label: "المدة:",
        intern_duration_3m: "٣ أشهر",
        intern_duration_6m: "٦ أشهر",
        intern_apply_btn: "قدم الآن",
        intern_role2_tag1: "تحليل البيانات",
        intern_role2_tag2: "هجين",
        intern_role2_tag3: "مدفوع",
        intern_role2_title: "متدرب تحليل البيانات",
        intern_role2_desc: "حول البيانات المعقدة إلى رؤى أعمال قابلة للتنفيذ. اكتب استعلامات SQL فعالة، وصمم لوحات معلومات تفاعلية، وقم بإجراء تحليلات استكشافية بـ Python.",
        intern_role3_tag1: "تطوير فلاتر",
        intern_role3_tag2: "عن بعد",
        intern_role3_tag3: "مدفوع",
        intern_role3_title: "متدرب تطوير تطبيقات فلاتر (Flutter)",
        intern_role3_desc: "ابنِ تطبيقات موبايل جميلة وسريعة ومتقاطعة المنصات لنظامي iOS و Android. قم ببرمجة الواجهات وإدارة الحالة وربط الـ APIs.",
        intern_role4_tag1: "تطوير واجهات الويب",
        intern_role4_tag2: "هجين",
        intern_role4_tag3: "مدفوع",
        intern_role4_title: "متدرب تطوير واجهات الويب (Front-End)",
        intern_role4_desc: "صمم ونفذ واجهات ويب سريعة وعصرية ومتجاوبة بالكامل. اكتب أكواد نظيفة للهيكل والتنسيق وتفاعل مع Vanilla JS/React.",
        intern_benefits_tag: "المزايا",
        intern_benefits_title: "ما نقدمه لك",
        intern_benefits_sub: "تم تصميم برنامجنا لإطلاق مسيرتك المهنية الاحترافية بدعم تأسيسي متين.",
        intern_ben1_title: "توجيه إرشادي مباشر",
        intern_ben1_desc: "سيتم قرنك مع موجه متخصص في الصناعة يعقد معك جلسات مراجعة وتقييم دورية لرسم خريطة نموك المهني.",
        intern_ben2_title: "أكواد إنتاجية حقيقية",
        intern_ben2_desc: "لا توجد مهام هامشية أو عديمة الجدوى. تساهم مباشرة في الأكواد والمنتجات الفعلية للشركة وللعملاء والمكتبات المفتوحة.",
        intern_ben3_title: "التحضير للمقابلات والتوصيات",
        intern_ben3_desc: "يتلقى الخريجون خطابات توصية وتدريباً عملياً على المقابلات الفنية مع الإدارة العليا للشركة لضمان جاهزيتهم للعمل.",

        // Bootcamps Page
        boot_tag: "تدريب مكثف",
        boot_title: "معسكرات <span class='gradient-text'>صيف ٢٠٢٦</span>",
        boot_sub: "من الأساسيات إلى بيئة الإنتاج الفعلي. اختر مساراً، وابدأ التعلم، واحترف الأطر التقنية التي ترسم ملامح عصرنا الحالي.",
        boot_schedule_title: "جدول البرنامج والمناهج",
        boot_schedule_sub: "الجدول الزمني: ١ يوليو ٢٠٢٦ إلى ١ أكتوبر ٢٠٢٦. تُعقد الجلسات مباشرة عبر الإنترنت مع ساعات عمل معملية تفاعلية.",
        boot_table_th_phase: "المرحلة والتاريخ",
        boot_table_th_data: "مسار تحليل البيانات",
        boot_table_th_ai: "مسار الذكاء الاصطناعي وتعلم الآلة",
        boot_table_th_status: "الحالة",
        boot_table_status_upcoming: "قادم قريباً",
        boot_table_status_open: "مفتوح للتسجيل",
        boot_table_w14: "الأسابيع ١ - ٤",
        boot_table_w14_date: "١ يوليو - ٢٨ يوليو ٢٠٢٦",
        boot_table_w14_data_t: "أساسيات بيانات الأعمال",
        boot_table_w14_data_d: "استعلامات SQL المتقدمة، هياكل المخططات، ومعالجة البيانات في PostgreSQL.",
        boot_table_w14_ai_t: "الأسس الرياضية ومكتبة PyTorch",
        boot_table_w14_ai_d: "الجبر الخطي، التفاضل والتكامل، الاحتمالات، وتصميم الشبكات العصبية الأساسية باستخدام PyTorch.",
        boot_table_w58: "الأسابيع ٥ - ٨",
        boot_table_w58_date: "٢٩ يوليو - ٢٥ أغسطس ٢٠٢٦",
        boot_table_w58_data_t: "تصوير البيانات وذكاء الأعمال",
        boot_table_w58_data_d: "تحويل البيانات إلى رؤى مفيدة باستخدام PowerBI و Tableau ورسم المخططات المخصصة بـ Python (Seaborn).",
        boot_table_w58_ai_t: "التعلم الخاضع للإشراف وغير الخاضع للإشراف",
        boot_table_w58_ai_d: "الانحدار، نماذج التصنيف، أشجار القرار، التجميع (K-Means)، ومقاييس التحقق من صحة النماذج.",
        boot_table_w912: "الأسابيع ٩ - ١٢",
        boot_table_w912_date: "٢٦ أغسطس - ٢٢ سبتمبر ٢٠٢٦",
        boot_table_w912_data_t: "التحليل الاستكشافي ومعالجة البيانات",
        boot_table_w912_data_d: "مكتبات NumPy و Pandas، التعامل مع البيانات المفقودة، ومنهجيات هندسة الميزات المتقدمة.",
        boot_table_w912_ai_t: "التعلم العميق والنماذج الضخمة",
        boot_table_w912_ai_d: "الشبكات العصبية التلتفية للرؤية الحاسوبية، والمحولات لمعالجة اللغات الطبيعية، وضبط النماذج اللغوية مفتوحة المصدر.",
        boot_table_wfinal: "أسبوع التخرج النهائي",
        boot_table_wfinal_date: "٢٣ سبتمبر - ١ أكتوبر ٢٠٢٦",
        boot_table_wfinal_data_t: "مشروع التخرج لتحليل بيانات الأعمال",
        boot_table_wfinal_data_d: "لوحة معلومات تحليلية تفاعلية منشورة على السحابة لحل دراسة حالة تحسين الخدمات اللوجستية.",
        boot_table_wfinal_ai_t: "عمليات تعلم الآلة ونشر النماذج",
        boot_table_wfinal_ai_d: "تغليف الخوارزميات داخل FastAPI، وتعبئتها باستخدام Docker، وإدارتها على البيئات السحابية.",
        boot_register_cta: "احجز مقعدي الآن",
        boot_faq_tag: "الأسئلة الشائعة",
        boot_faq_title: "الأسئلة الأكثر تكراراً",
        boot_faq_sub: "هل تحتاج إلى مزيد من التفاصيل؟ إليك إجابات على الأسئلة الشائعة حول معسكراتنا التدريبية.",
        boot_faq1_q: "ما هي المتطلبات الأساسية لمسار الذكاء الاصطناعي وتعلم الآلة؟",
        boot_faq1_a: "يُنصح بمعرفة أساسية بلغة Python والرياضيات بمستوى المدرسة الثانوية. نحن نوفر مواد دراسية تحضيرية قبل أسبوعين من تاريخ البدء لمساعدتك على الاستعداد.",
        boot_faq2_q: "هل يتم تقديم شهادة عند التخرج؟",
        boot_faq2_a: "نعم. يتلقى جميع الخريجين الذين يكملون مشروع التخرج بنجاح ويجتازون المراجعة النهائية شهادة إتمام رقمية معتمدة وقابلة للتحقق.",

        // Diplomas Page
        diploma_tag: "التخصص طويل المدى",
        diploma_title: "الدبلومات <span class='gradient-text'>المهنية</span>",
        diploma_sub: "برامج شاملة مدتها من ٦ إلى ٩ أشهر مصممة لتأخذك من الأساسيات الصفرية إلى الخبرة الجاهزة للعمل مع فرص تدريب مباشر.",
        diploma_list_title: "مسارات التخصص المتاحة",
        diploma_list_sub: "اختر مسارك المهني. تتضمن كل دبلومة مختبرات برمجية أسبوعية، دراسات حالة مباشرة، ومشروع تخرج فني يخضع لمراجعة الخبراء.",
        diploma_d1_title: "دبلومة الذكاء الاصطناعي المتقدم والتعلم العميق",
        diploma_d1_desc: "منهج دراسي صارم يركز على الشبكات العصبية المتقدمة، معالجة اللغات الطبيعية، الرؤية الحاسوبية، وبنيات الذكاء الاصطناعي التوليدي الحديثة. مصمم لمتخصصي الذكاء الاصطناعي ومهندسي البرمجيات الطموحين.",
        diploma_d1_f1: "التعلم العميق والأسس الرياضية الفنية",
        diploma_d1_f2: "معالجة اللغات الطبيعية والنماذج اللغوية الضخمة",
        diploma_d1_f3: "الرؤية الحاسوبية ومعالجة الصور الرقمية",
        diploma_d1_f4: "عمليات تعلم الآلة، Docker، ونشر النماذج سحابياً",
        diploma_format_label: "طريقة الدراسة:",
        diploma_format_val: "هجين / عبر الإنترنت",
        diploma_enroll_btn: "طلب الالتحاق بالبرنامج",
        diploma_d2_title: "دبلومة تحليل البيانات وهندستها للمؤسسات",
        diploma_d2_desc: "احترف بنيات ذكاء الأعمال للمؤسسات الكبرى. تعلم نمذجة قواعد بيانات SQL، ومعالجة البيانات الضخمة باستخدام Python، وأتمتة لوحات المعلومات السحابية بالكامل.",
        diploma_d2_f1: "Advanced SQL & Relational Databases",
        diploma_d2_f2: "تحليل البيانات باستخدام لغة Python (Pandas, Numpy)",
        diploma_d2_f3: "بنيات ذكاء الأعمال وتصوير البيانات (PowerBI, Tableau)",
        diploma_d2_f4: "مستودعات البيانات السحابية (Snowflake/AWS)",
        diploma_benefits_tag: "التوظيف والتدريب",
        diploma_benefits_title: "مزايا الدبلومة ودعم فرص العمل",
        diploma_benefits_sub: "كيف تساعدك مسارات الدبلوم لدينا في تأمين وظائف عالية الأجر في شركات التكنولوجيا الإقليمية والعالمية.",
        diploma_ben1_title: "فرصة تدريب مضمونة ومكفولة",
        diploma_ben1_desc: "يحصل جميع طلاب الدبلوم الذين يحافظون على درجات النجاح على تدريب داخلي مدفوع الأجر لمدة ٣ أشهر مع شبكات شركائنا بعد التخرج.",
        diploma_ben2_title: "بناء معرض أعمال احترافي",
        diploma_ben2_desc: "قم ببناء ٤ مشاريع متكاملة وجاهزة للإنتاج الفعلي على Git، لتثبت لأصحاب العمل قدرتك على تصميم ونشر الأنظمة الصناعية الحقيقية.",

        // About Page
        about_banner_tag: "قصتنا",
        about_banner_title: "حول <span class='gradient-text'>NextGen Institute</span>",
        about_banner_sub: "مجموعة من المطورين، ومصممي البيانات، ومحترفي التحليلات الملتزمين بتطوير الكفاءات التقنية الإقليمية.",
        about_vision_tag: "الهدف التأسيسي",
        about_vision_title: "رعاية الابتكار، مهندس تلو الآخر",
        about_vision_sub1: "تأسس NextGen Institute بهدف بسيط: حل النقص في الكفاءات التقنية من خلال إنشاء مسارات تدريب رفيعة المستوى. نحن نؤمن بأن طرق التعلم التقليدية بطيئة جداً لمواكبة تحول الذكاء الاصطناعي الحالي. ومن خلال التركيز الصارم على التطبيق العملي، نقوم بإعداد المرشحين للعمل فوراً.",
        about_vision_sub2: "سواء كان الأمر يتعلق بتصوير البيانات للخدمات اللوجستية للمؤسسات أو تعبئة المحولات لنماذج الذكاء الاصطناعي التوليدي، فإن متدربينا يحصلون على تعرض مباشر للتحديات الفنية الحقيقية.",
        about_val1_title: "الأهمية السوقية والملاءمة",
        about_val1_desc: "تتكيف المناهج الدراسية باستمرار لتعكس أطر العمل الفعلية المستخدمة في السوق.",
        about_val2_title: "الروح التعاونية والبحثية",
        about_val2_desc: "تشجع مختبرات الأبحاث المشتركة على حل المشكلات بشكل تعاوني على مستوى الفريق.",
        about_mgr_title: "مدير البرنامج",
        about_mgr_role: "مدير NextGen Institute",
        about_mgr_bio: "مكرس لتصميم الوحدات التعليمية وتنسيق الشراكات الصناعية. التأكد من حصول كل مشارك على توجيه عالي الجودة للمشاريع، بنية تحتية حديثة، ووصول مستمر للفرص الوظيفية.",

        // Contact Page
        contact_banner_tag: "تواصل معنا",
        contact_banner_title: "اتصل <span class='gradient-text'>بفريقنا</span>",
        contact_banner_sub: "هل لديك أسئلة حول طلبات الالتحاق، المعسكرات التدريبية، أو برامج التوظيف للمؤسسات؟ دعنا نبدأ محادثة.",
        contact_info_tag: "التفاصيل",
        contact_info_title: "معلومات الاتصال",
        contact_info_sub: "يمكنك الاتصال بنا عبر البريد الإلكتروني أو وسائل التواصل الاجتماعي. نرد عادةً خلال يوم عمل واحد.",
        contact_inquiry_title: "الاستفسارات العامة",
        contact_inquiry_val: "info@nextgeninstitute.placeholder",
        contact_hq_title: "المقر الرئيسي",
        contact_hq_val: "الإسكندرية، مصر",
        contact_follow: "تابعنا على",
        contact_form_name: "الاسم الكامل",
        contact_form_email: "البريد الإلكتروني",
        contact_form_subject: "موضوع الرسالة",
        contact_form_message: "نص الرسالة",
        contact_form_btn: "إرسال الاستفسار"
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const langToggle = document.getElementById('langToggle');
    let currentLang = localStorage.getItem('selectedLang') || 'en';
    
    // Create/Insert Language switch button dynamically into navbar if not present
    const insertLangButton = () => {
        const navMenu = document.getElementById('navMenu');
        if (navMenu && !document.getElementById('langToggle')) {
            const li = document.createElement('li');
            li.style.display = 'flex';
            li.style.alignItems = 'center';
            
            const btn = document.createElement('button');
            btn.id = 'langToggle';
            btn.className = 'btn';
            btn.style.padding = '4px 12px';
            btn.style.fontSize = '0.78rem';
            btn.style.background = 'var(--bg-secondary)';
            btn.style.border = '1px solid var(--glass-border)';
            btn.style.borderRadius = 'var(--radius-pill)';
            btn.style.cursor = 'pointer';
            btn.style.color = 'var(--text-main)';
            btn.style.fontWeight = '600';
            btn.style.marginLeft = '12px';
            btn.style.transition = 'var(--transition-smooth)';
            
            // Hover effect
            btn.onmouseover = () => {
                btn.style.background = 'var(--accent-blue)';
                btn.style.color = 'var(--text-dark)';
                btn.style.borderColor = 'transparent';
            };
            btn.onmouseout = () => {
                btn.style.background = 'var(--bg-secondary)';
                btn.style.color = 'var(--text-main)';
                btn.style.borderColor = 'var(--glass-border)';
            };
            
            li.appendChild(btn);
            navMenu.appendChild(li);
            
            btn.addEventListener('click', () => {
                currentLang = currentLang === 'en' ? 'ar' : 'en';
                localStorage.setItem('selectedLang', currentLang);
                applyLanguage(currentLang);
            });
        }
    };
    
    const applyLanguage = (lang) => {
        const isRtl = lang === 'ar';
        document.documentElement.dir = isRtl ? 'rtl' : 'ltr';
        document.documentElement.lang = lang;
        
        if (isRtl) {
            document.body.classList.add('rtl');
        } else {
            document.body.classList.remove('rtl');
        }
        
        // Translate all data-i18n elements
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key]) {
                el.innerHTML = translations[lang][key];
            }
        });

        // Translate placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (translations[lang] && translations[lang][key]) {
                el.setAttribute('placeholder', translations[lang][key]);
            }
        });
        
        // Update language button label
        const toggleBtn = document.getElementById('langToggle');
        if (toggleBtn) {
            toggleBtn.textContent = lang === 'en' ? 'العربية' : 'English';
        }
    };
    
    // Init Lang
    insertLangButton();
    applyLanguage(currentLang);
});
