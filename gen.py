import html
E="roy_gregory@rbccoach.com"
CSS="""body{font-family:-apple-system,Helvetica,Arial,sans-serif;margin:0;background:#f3f4f6;color:#111}
main{max-width:640px;margin:auto;padding:16px}header{text-align:center}header img{max-width:220px;width:60%}
h1{font-size:1.3em;margin:.3em 0}.c{font-size:.9em;color:#333}fieldset{background:#fff;border:1px solid #ccc;border-radius:10px;margin:14px 0;padding:12px}
legend{font-weight:700;padding:0 6px}label{display:block;margin:10px 0 4px;font-weight:600;font-size:.95em}
input[type=text],input[type=tel],input[type=date],input[type=time],input[type=number],textarea{width:100%;box-sizing:border-box;font-size:16px;padding:10px;border:1px solid #999;border-radius:8px}
textarea{min-height:90px}.yn{display:flex;gap:18px;margin:4px 0}.yn label{font-weight:400;display:flex;align-items:center;gap:6px;margin:0}
.yn input{width:24px;height:24px}.note{background:#fff3cd;border-radius:8px;padding:10px;font-size:.9em}
button{width:100%;font-size:18px;padding:14px;background:#b00020;color:#fff;border:0;border-radius:10px;margin:16px 0}"""
def page(fname,title,intro,secs,subject,nxt):
    o=[]
    for leg,items in secs:
        o.append(f"<fieldset><legend>{leg}</legend>")
        for it in items:
            if isinstance(it,str): o.append(f'<p class="note">{it}</p>');continue
            lab,t,*r=it; req=" required" if r and r[0] else ""; n=html.escape(lab)
            if t=="yn": o.append(f'<label>{n}</label><div class="yn"><label><input type="radio" name="{n}" value="Yes"{req}> Yes</label><label><input type="radio" name="{n}" value="No"> No</label></div>')
            elif t=="ta": o.append(f'<label>{n}</label><textarea name="{n}"{req}></textarea>')
            elif t=="file": o.append(f'<label>{n}</label><input type="file" name="attachment" accept="image/*" multiple>')
            else: o.append(f'<label>{n}</label><input type="{t}" name="{n}"{req}>')
        o.append("</fieldset>")
    s=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} - Roberts Brothers Coach</title><style>{CSS}</style></head><body><main><header><img src="rbc_logo.png" alt="Roberts Brothers Coach logo">
<h1>{title}</h1><div class="c">Roberts Brothers Coach &bull; 155 Commerce Way, Gallatin, TN 37066<br>Questions? Roy Gregory, Director of Safety, <a href="tel:+12705261830">(270) 526-1830</a></div></header>
<p class="note">{intro}</p>
<form action="https://formsubmit.co/{E}" method="POST" enctype="multipart/form-data">
<input type="hidden" name="_subject" value="{subject}"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
<input type="text" name="_honey" style="display:none"><input type="hidden" name="_next" value="{nxt}">
{''.join(o)}<button type="submit">Submit to Roy Gregory</button></form>
<p class="c" style="text-align:center">Roy Gregory, Director of Safety &bull; (270) 526-1830</p></main></body></html>"""
    open(fname,"w").write(s)
T="text";D="date";Ti="time";P="tel";N="number";Y="yn";A="ta"
page("no-damage.html","No Damage / No Injury Acknowledgment","To the other motorist: please complete this form, answer Yes or No, and type your name as your signature.",[
("Incident Information",[("Date",D,1),("Time",Ti,1),("Location - street address / highway &amp; mile marker",T,1),("City",T),("State",T),("County (if known)",T)]),
("Roberts Brothers Coach",[("Coach name / number",T,1),("Driver name",T,1),("Driver phone",P)]),
("Other Party (Driver of Other Vehicle)",[("Full name",T,1),("Phone",P,1),("Address (street, city, state, zip)",T),("Driver's license #",T),("License state",T),("Number of occupants in vehicle (incl. driver)",N),("Vehicle year",T),("Make",T),("Model",T),("License plate #",T),("Plate state",T),("Insurance company",T),("Policy #",T)]),
("Condition Confirmation (other party answers)",[("No damage to my vehicle",Y,1),("No injuries to anyone in my vehicle",Y,1)]),
("Brief Description of What Happened",[("Description (e.g., mirror contact while passing, light bump while backing, near-miss)",A)]),
("Photos",[("Photos of both vehicles, plates, and scene (optional)","file")]),
("Acknowledgment",["By signing below, I confirm that I have looked over my vehicle and, at this time, I see no visible damage to it, and that neither I nor anyone riding in my vehicle is injured. The information I provided on this form is true to the best of my knowledge. I am signing this form voluntarily, and no one has pressured me or offered me anything to sign it. I understand this form is only a record of the condition of my vehicle and its occupants at the time I signed it.",
 ("Other party signature (type full name)",T,1),("Other party printed name",T),("Other party date",D),("Coach driver signature (type full name)",T,1),("Coach driver printed name",T),("Coach driver date",D)]),
("Witness (Optional)",[("Witness name",T),("Witness phone",P),("Witness signature (type full name)",T)]),
("Coach Drivers",["Even when this form is signed, still photograph both vehicles (all sides), both license plates, and the scene, and call Roy Gregory at (270) 526-1830 before leaving the scene."])],
"No Damage / No Injury Form submitted","https://formsubmit.co/thank-you" if False else "")
def veh(n): return (f"Other Vehicle #{n}",[(f"V{n} {x}",t) for x,t in [("driver full name",T),("phone",P),("driver's license #",T),("license state",T),("address",T),("# occupants (incl. driver)",N),("vehicle year",T),("make",T),("model",T),("color",T),("license plate #",T),("plate state",T),("insurance company",T),("policy #",T),("owner name (if different)",T)]])
page("accident-report.html","Driver Accident Report","FIRST: Ensure safety, call 911 if anyone is injured, then call Roy Gregory, Director of Safety, (270) 526-1830 BEFORE leaving the scene.",[
("1. Incident Information",[("Date",D,1),("Time",Ti,1),("Exact location / street address",T,1),("City",T),("State",T),("Highway / route &amp; mile marker",T),("Weather",T),("Road: Dry",Y),("Road: Wet",Y),("Road: Snow/Ice",Y),("Road: Other",Y),("Lighting: Daylight",Y),("Lighting: Dawn/Dusk",Y),("Lighting: Dark-lit",Y),("Lighting: Dark-unlit",Y)]),
("2. Coach &amp; Driver",[("Coach name / number",T,1),("Trailer #",T),("Driver name",T,1),("Driver phone",P,1),("Co-driver name",T),("Tour / client name",T),("# passengers on board",N)]),
("3. Police",[("Police agency / department",T),("Officer name",T),("Badge #",T),("Police report #",T),("Citation issued?",Y,1),("If yes - issued to whom / for what",T)]),
veh(1),veh(2),
("5. Injuries",[("Any injuries?",Y,1),("Transported for treatment?",Y),("If transported - to where",T),("Names of injured person(s) &amp; description of injuries",A)]),
("6. Damage",[("Coach / trailer damage - describe",A),("Coach towed?",Y),("Other vehicle(s) damage - describe",A),("Other vehicle towed?",Y)]),
("7. Witnesses",[("Witness #1 name",T),("Witness #1 phone",P),("Witness #2 name",T),("Witness #2 phone",P)]),
("8. Description of What Happened",["Describe in order: direction of travel, speed, what each vehicle was doing, point of impact, and what happened after. State facts only.",("Description",A,1)]),
("9. Photos / Diagram",[("Photos of vehicles, plates, scene, and a sketch of the scene (label coach C, others 1, 2; arrow for north)","file")]),
("10. Driver Checklist",[("Photos taken of all vehicles, plates, and the scene",Y,1),("Warning triangles placed",Y,1),("Roy Gregory notified",Y,1),("Time Roy notified",Ti),("No Damage form done (if applicable)",Y),("Accident noted in ELD",Y,1)]),
("11. Post-Accident DOT Testing &amp; Reminders",["POST-ACCIDENT DOT TESTING IS REQUIRED IF: (a) there is a fatality, OR (b) a citation is issued to the coach driver AND either someone is injured and treated away from the scene or any vehicle is towed. Alcohol test: within 8 hours (ideally within 2). Drug test: within 32 hours. Do not consume alcohol for 8 hours after the accident or until tested.","REMINDERS: Do NOT admit fault or sign anything other than the police report / company forms. Do NOT discuss the accident with the media or post on social media. Refer all questions to Roy Gregory."]),
("12. Driver Certification",["I certify that the information on this report is true and complete to the best of my knowledge.",("Driver signature (type full name)",T,1),("Printed name",T),("Certification date",D,1)])],
"Driver Accident Report submitted","")
