rad_classes = ['covid', 'normal', 'viral']
ISIC_classes = ['Actinic Keratosis', 'Basal cell carcinoma', 'Dermatofibroma', 'Melanoma', 'Nevus', 'Pigmented Benign Keratosis', 'Seborrheic Keratosis', 'Squamous Cell Carcinoma', 'Vascular Lesion']


description_ISIC = [
"""Actinic keratoses (also called solar keratoses) are dry scaly patches of skin that have been damaged by the sun.

The patches are not usually serious. But there's a small chance they could become skin cancer, so it's important to avoid further damage to your skin.

The patches:

can feel dry, rough and scaly, or like sandpaper
are usually between 1cm to 2cm in size
can be the same colour as your skin or range from pink to red to brown
may feel itchy
""",

"""
Basal cell carcinoma is a type of skin cancer. Basal cell carcinoma begins in the basal cells — a type of cell within the skin that produces new skin cells as old ones die off.

Basal cell carcinoma often appears as a slightly transparent bump on the skin, though it can take other forms. Basal cell carcinoma occurs most often on areas of the skin that are exposed to the sun, such as your head and neck.

Most basal cell carcinomas are thought to be caused by long-term exposure to ultraviolet (UV) radiation from sunlight. Avoiding the sun and using sunscreen may help protect against basal cell carcinoma.

Basal cell carcinoma usually develops on sun-exposed parts of your body, especially your head and neck. Less often, basal cell carcinoma can develop on parts of your body usually protected from the sun, such as the genitals.

Basal cell carcinoma appears as a change in the skin, such as a growth or a sore that won't heal. These changes in the skin (lesions) usually have one of the following characteristics:

A shiny, skin-colored bump that's translucent, meaning you can see a bit through the surface. The bump can look pearly white or pink on white skin. On brown and Black skin, the bump often looks brown or glossy black. Tiny blood vessels might be visible, though they may be difficult to see on brown and Black skin. The bump may bleed and scab over.
A brown, black or blue lesion — or a lesion with dark spots — with a slightly raised, translucent border.
A flat, scaly patch with a raised edge. Over time, these patches can grow quite large.
A white, waxy, scar-like lesion without a clearly defined border.
""",

"""
Dermatofibromas, or histiocytomas, are common noncancerous (benign) skin growths. They are firm to hard, and they are skin-colored or slightly pigmented. Dermatofibromas can be tender. These lesions usually persist for life, and they may heal as depressed scars after several years. Occasionally, dermatofibromas found in large numbers in grouped or linear clusters are seen in association with immune disturbances, such as leukemia, HIV, and lupus.

Dermatofibromas are most often found on the arms and legs of women. They are small brown or reddish-brown mobile nodules, and they feel quite firm. They may be tender to touch. Many lesions demonstrate a "dimple sign," where the central portion puckers as the lesion is compressed on the sides. They generally do not change in size.
""",

"""
Melanoma, the most serious type of skin cancer, develops in the cells (melanocytes) that produce melanin — the pigment that gives your skin its color. Melanoma can also form in your eyes and, rarely, inside your body, such as in your nose or throat.

The exact cause of all melanomas isn't clear, but exposure to ultraviolet (UV) radiation from sunlight or tanning lamps and beds increases your risk of developing melanoma. Limiting your exposure to UV radiation can help reduce your risk of melanoma.

The risk of melanoma seems to be increasing in people under 40, especially women. Knowing the warning signs of skin cancer can help ensure that cancerous changes are detected and treated before the cancer has spread. Melanoma can be treated successfully if it is detected early.

Melanomas can develop anywhere on your body. They most often develop in areas that have had exposure to the sun, such as your back, legs, arms and face.

Melanomas can also occur in areas that don't receive much sun exposure, such as the soles of your feet, palms of your hands and fingernail beds. These hidden melanomas are more common in people with darker skin.

The first melanoma signs and symptoms often are:

A change in an existing mole
The development of a new pigmented or unusual-looking growth on your skin
Melanoma doesn't always begin as a mole. It can also occur on otherwise normal-appearing skin.
""",

"""
Nevus (plural: nevi) is the medical term for a mole. Nevi are very common. Most peopleTrusted Source have between 10 and 40. Common nevi are harmless collections of colored cells. They typically appear as small brown, tan, or pink spots.

You can be born with moles or develop them later. Moles that you’re born with are known as congenital moles. However, most moles develop during childhood and adolescence. This is known as an acquired nevus. Moles can also develop later in life as a result of sun exposure.

There are many types of nevi. Some of them are harmless and others more serious. Read on to learn about the different types and how to know whether you should get one checked out by your doctor.
""",


"""
Benign pigmented skin lesions are extremely common. Such lesions are seen every day in general practice.

""",


"""
A seborrheic keratosis (seb-o-REE-ik ker-uh-TOE-sis) is a common noncancerous (benign) skin growth. People tend to get more of them as they get older.

Seborrheic keratoses are usually brown, black or light tan. The growths (lesions) look waxy or scaly and slightly raised. They appear gradually, usually on the face, neck, chest or back.

Seborrheic keratoses are harmless and not contagious. They don't need treatment, but you may decide to have them removed if they become irritated by clothing or you don't like how they look.

A seborrheic keratosis grows gradually. Signs and symptoms might include:

A round or oval-shaped waxy or rough bump, typically on the face, chest, a shoulder or the back
A flat growth or a slightly raised bump with a scaly surface, with a characteristic "pasted on" look
Varied size, from very small to more than 1 inch (2.5 centimeters) across
Varied number, ranging from a single growth to multiple growths
Very small growths clustered around the eyes or elsewhere on the face, sometimes called flesh moles or dermatosis papulosa nigra, common on Black or brown skin
Varied in color, ranging from light tan to brown or black
Itchiness
""",

"""
Squamous cell carcinoma of the skin is a common form of skin cancer that develops in the squamous cells that make up the middle and outer layers of the skin.

Squamous cell carcinoma of the skin is usually not life-threatening, though it can be aggressive. Untreated, squamous cell carcinoma of the skin can grow large or spread to other parts of your body, causing serious complications.

Most squamous cell carcinomas of the skin result from prolonged exposure to ultraviolet (UV) radiation, either from sunlight or from tanning beds or lamps. Avoiding UV light helps reduce your risk of squamous cell carcinoma of the skin and other forms of skin cancer.

Squamous cells are found in many places in your body, and squamous cell carcinoma can occur anywhere squamous cells are found. Squamous cell carcinoma of the skin refers to cancer that forms in the squamous cells found in the skin.
""",

"""
Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks. There are three major categories of vascular lesions: Hemangiomas, Vascular Malformations, and Pyogenic Granulomas. While these birthmarks can look similar at times, they each vary in terms of origin and necessary treatment.

"""
]


recommended_course_of_action_ISIC = [
"""
Treatment for actinic keratoses
If you only have 1 skin patch, a GP might suggest waiting to see if the patch goes away by itself.

If you have more than 1 patch, or a patch is causing you problems such as pain and itchiness, treatment is usually recommended. A GP may refer you to a skin specialist (dermatologist).

Treatments for actinic keratoses include:

prescription creams and gels
freezing the patches (cryotherapy), this makes the patches turn into blisters and fall off after a few weeks
surgery to cut out or scrape away the patches – you will be given a local anaesthetic first, so it does not hurt
photodynamic therapy (PDT), where special cream is applied to the patches and a light is shone onto them to kill abnormal skin cells
Things you can do to help
If you have actinic keratoses it's important to avoid any further sun damage. This will stop you getting more skin patches and will lower your chance of getting skin cancer.
""",

"""
When to see a doctor
Make an appointment with your health care provider if you observe changes in the appearance of your skin, such as a new growth, a change in a previous growth or a recurring sore.
""",

"""
Self-Care Guidelines

None necessary.

Treatments Your Physician May Prescribe
The lesion is noncancerous; therefore, reassurance is often all that is needed.
Symptomatic, protruding dermatofibromas can often be reduced in size by liquid nitrogen (freezing) therapy or steroid injections to the lesion. In patients with dark skin, freezing with liquid nitrogen and steroid injection of may cause pigmentary change that is usually temporary.
Surgical excision can be performed, but due to the high incidence of recurrence, the use of topical steroids or steroid injections into the lesion post-excision is often necessary.
""",

"""
When to see a doctor
Make an appointment with your doctor if you notice any skin changes that seem unusual.

Prevention
You can reduce your risk of melanoma and other types of skin cancer if you:

Avoid the sun during the middle of the day. For many people in North America, the sun's rays are strongest between about 10 a.m. and 4 p.m. Schedule outdoor activities for other times of the day, even in winter or when the sky is cloudy.

You absorb UV radiation year-round, and clouds offer little protection from damaging rays. Avoiding the sun at its strongest helps you avoid the sunburns and suntans that cause skin damage and increase your risk of developing skin cancer. Sun exposure accumulated over time also may cause skin cancer.

Wear sunscreen year-round. Use a broad-spectrum sunscreen with an SPF of at least 30, even on cloudy days. Apply sunscreen generously, and reapply every two hours — or more often if you're swimming or perspiring.
Wear protective clothing. Cover your skin with dark, tightly woven clothing that covers your arms and legs, and a broad-brimmed hat, which provides more protection than does a baseball cap or visor.

Some companies also sell protective clothing. A dermatologist can recommend an appropriate brand. Don't forget sunglasses. Look for those that block both types of UV radiation — UVA and UVB rays.

Avoid tanning lamps and beds. Tanning lamps and beds emit UV rays and can increase your risk of skin cancer.
Become familiar with your skin so that you'll notice changes. Examine your skin often for new skin growths or changes in existing moles, freckles, bumps and birthmarks. With the help of mirrors, check your face, neck, ears and scalp.

Examine your chest and trunk and the tops and undersides of your arms and hands. Examine both the front and back of your legs and your feet, including the soles and the spaces between your toes. Also check your genital area and between your buttocks.
""",

"""
Most moles are harmless and don’t require treatment. However, if you have a mole that’s cancerous or could become cancerous, you’ll likely need to have it removed. You can also choose to have a benign nevus removed if you don’t like the way it looks.

Most nevi are removed with either a shave or excisional biopsy. Your doctor will likely recommend doing an excisional biopsy for cancerous nevi to make sure that they remove everything.

When to see a doctor
Skin cancer is easiest to treat when it’s caught early. It’s important to know what to look for so you can recognize the signs early on.

Try to get in the habit of examining your skin once a month. Keep in mind that skin cancer can develop in areas that you can’t easily see, so use a mirror or ask a friend to help you if you need to.
""",

"""None needed""",

"""
See your doctor if the appearance of the growth bothers you or if it gets irritated or bleeds when your clothing rubs against it. Also see your doctor if you notice suspicious changes in your skin, such as sores or growths that grow rapidly, bleed and don't heal. These could be signs of skin cancer.
""",


"""
When to see a doctor
Make an appointment with your doctor if you have a sore or scab that doesn't heal in about two months or a flat patch of scaly skin that won't go away.

Prevention
Most squamous cell carcinomas of the skin can be prevented. To protect yourself:

Avoid the sun during the middle of the day. For many people in North America, the sun's rays are strongest between about 10 a.m. and 3 p.m. Schedule outdoor activities for other times of the day, even during winter or when the sky is cloudy.
Wear sunscreen year-round. Use a broad-spectrum sunscreen with an SPF of at least 30, even on cloudy days. Apply sunscreen generously, and reapply every two hours — or more often if you're swimming or perspiring.
Wear protective clothing. Cover your skin with dark, tightly woven clothing that covers your arms and legs, and a broad-brimmed hat, which provides more protection than does a baseball cap or visor.

Some companies also sell protective clothing. A dermatologist can recommend an appropriate brand. Don't forget sunglasses. Look for those that block both types of UV radiation — UVA and UVB rays.

Avoid tanning beds. Tanning beds emit UV rays and can increase your risk of skin cancer.
Check your skin regularly and report changes to your doctor. Examine your skin often for new skin growths or changes in existing moles, freckles, bumps and birthmarks. With the help of mirrors, check your face, neck, ears and scalp.

Examine your chest and trunk and the tops and undersides of your arms and hands. Examine both the front and back of your legs and your feet, including the soles and the spaces between your toes. Also check your genital area and between your buttocks.
""",


"""
Many hemangiomas can be monitored by your the pediatrician or dermatologist as they grow naturally without the need for treatment. However, extensive lesions or lesions with ulceration, bleeding or super-infection should be seen by a specialist. Those occurring in cosmetically or functionally sensitive areas (such as the nose tip or lip) should also be seen by a doctor experienced in the management of hemangiomas, as well as a pediatric plastic surgeon.

The treatment of hemangiomas depends on their characteristic life-cycle and location and can be categorized into medical and surgical therapies. Your child’s plan will be customized depending on their specific lesion and its behavior.

Medication: Patients may be placed on medications such as oral corticosteroids like prednisone or an oral blood pressure medication called propranolol, in order to help slow the rapid growth phase and promote involution. These medications can be effective, but have some side effects that make careful patient selection and monitoring important. Bulky hemangiomas may sometimes benefit from an injection of a corticosteroid into the lesion, which is usually done under a brief anesthetic. Other medications (such as interferon given by serial injection) can have more serious potential side effects, and are reserved for patients with extensive lesions that do not respond to other therapies.

Surgery: The surgical treatment of hemangiomas must carefully balance the need for early treatment with the scarring that will be created by the procedure. Because most lesions undergo at least a fair amount of involution on their own, it is important to delay most surgery until this occurs to allow tissue to stabilize before reconstruction. This will maximize healing and minimize the length of scars. An exception to waiting may occur if surgery provides the quickest option to relieve obstruction or allows better staging of reconstruction the lesion(s). These situations are best determined by an experienced pediatric plastic surgeon.

Laser Therapy: Finally, laser therapy can be used to treat ulcerated lesions, as well as any residual blood vessels or discoloration that may remain after involution. Extensive airway lesions may also require CO2 laser therapy for management, which is carried out by an otolaryngologist (ENT surgeon) under anesthesia.
"""
]

ISIC_classes = ['Actinic Keratosis', 'Basal cell carcinoma', 'Dermatofibroma', 'Melanoma', 'Nevus', 'Pigmented Benign Keratosis', 'Seborrheic Keratosis', 'Squamous Cell Carcinoma', 'Vascular Lesion']

level_of_concern_ISIC = [
    'low', 'high', 'medium', 'high', 'medium', 'low', 'medium', 'high', 'low'
]

def get_class_rad(y):
    return rad_classes[y]

def get_class_ISIC(y):
    return ISIC_classes[y]

def get_description_ISIC(y):
    return description_ISIC[y]

def get_level_of_concern_ISIC(y):
    return level_of_concern_ISIC[y]

def get_recommended_course_of_action_ISIC(y):
    return recommended_course_of_action_ISIC[y]
