class illness():
	def menu(self):
		print("MENU")
		print("What do u want to choose?")
		print("1.Physical Injuries \n 2.Internal Injuries/Illness \n 3.Allergies/Infection \n 4.Other Problem(please mention it) \n 5.Back to Main Menu")
	def physical_injuries(self):
		print("Tell me your problem type")
		print("1.Burns \n 2.Cuts \n 3.Metallic cuts \n 4.Swelling \n 5.Other Problem(please mention it) \n 6.Menu \n")
		u=int(input("Tell your type of problem through numbers as shown above"))
		if u==1:
			print("1st degree burns \n first aid:First-degree burns cause minimal skin damage. They are also called superficial burns because they affect the outermost layer of skin First-degree burns are usually treated with home care. Healing time may be quicker the sooner you treat the burn. Treatments for a first-degree burn include soaking the wound in cool water for five minutes or longer taking acetaminophen or ibuprofen for pain relief applying lidocaine (an anesthetic) with aloe vera gel or cream to soothe the skin using an antibiotic ointment and loose gauze to protect the affected area. \n medication:lidocaine \n 2nd degree burns \n first aid:Second-degree burns are more serious because the damage extends beyond the top layer of skin. This type burn causes the skin to blister and become extremely red and sore.running the skin under cool water for 15 minutes or longer. taking over-the-counter pain medication.applying antibiotic cream to blisters \n medication : acetaminophen or 	ibuprofen\n 3rd degree burns\n first aid: Excluding fourth-degree burns, third-degree burns are the most severe. They cause the most damage, extending through every layer of skin.Without surgery, these wounds heal with severe scarring and contracture. There is no set timeline for complete spontaneous healing for third-degree burns. \n medication : please consult a physician immediately near you\n")
		
		if u==2:
			print("first aid:Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. If blood soaks through the bandage, place another bandage over the first and keep applying pressure. Raise the injured body part to slow bleeding. When bleeding stops, cover the wound with a new, clean bandage. \n the cut is deep or its edges are widely separated .the cut continues to ooze and bleed even after applying pressure. the injury was caused by an animal or human bite, burn, electrical injury, or puncture wound (e.g., a nail)\n medication: zinc ointment, vitamin E oil")
	
		if u==3:
			print("first aid: You treat a cut from rusty metal the same way as any other wound: Firstly, wash your hands thoroughly. Clean the wound with plenty of saline or lightly soapy water (don't use bar soaps, antibacterial soaps or peroxides). Rinse, don't scrub, unless you have to gently loosen the dirt (dab the wound). You can apply antiseptics such as betadine or crystaderm (1% hydrogen peroxide) around the edges of the wound.\n medication:A and D ointment , cortisone ointment(if the wound is too deep and caused due to a rusty metal get urself a tt injection)")
		
		if u==4:
			print("first aid :Compression. This means wrapping the injured area to prevent swelling. Wrap the affected area with an elastic medical bandage (like an ACE bandage). ... If these symptoms don't disappear right away, seek immediate medical help.\n medication:bruise balm stick(before applying the ointment apply ice on the effected area for soothening)")
		if u==5:
			print("You have Choosen Other Problem(please mention it)")
			g=raw_input("Tell me your problem")
			print("Sorry your",g,"problem is just severe i hope you can just consult your nearest hospital")
			print("OR \n Your problem needs a physical assistance,which")
		if u==6:
			print("You have choosen Menu")
			y.menu()
			y.menu_caller()
	def Internal_or_Illness(self):
		print("Tell me your problem type")
		print("1.fever \n 2.cold/cough \n 3.head ache \n 4.internal pains \n 5.Other Problem(please mention it) \n 6.Menu \n")
		v=int(input("Tell your type of problem through numbers as shown above"))
		if v==1:
			print("A fever is a high temperature. When someones body temperature goes above the normal body temperature of 37 degrees celsius (98. 6 degrees farenheit), this is called a fever.Usually fevers are caused by infections or illnesses, such as a sore throat, earache, or chickenpox.\nfirst aid: Drink plenty of fluids to stay hydratedDress in lightweight clothing.Use a light blanket if you feel chilled, until the chills end.Take acetaminophen (Tylenol, others) or ibuprofen (Advil, Motrin IB, others)\n medication:acetaminophen ,ibuprofen, paracetamol")
		if v==2:
			print("first aid:If you develope a barky or croupy cough, sit in a steamy bathroom together for about 20 minutes.Offer plenty of fluids,Run a cool-mist humidifier in your bedroom.Use saline (saltwater) nose drops to relieve congestion.\nmedication:\ncold:zyrtec D oral tablets, inhaler\n cough:ascoril syrup , corex syrup ")
		if v==3:
			print("Take Pain Medication. Give ibuprofen (Advil, Motrin), aspirin, or acetaminophen (Tylenol) for pain. Avoid ibuprofen and other NSAIDs if the person has heart failure or kidney failure.")
		if v==4:
			print("CHEST PAIN:\n Causes of chest pain can vary from minor problems, such as indigestion or stress, to serious medical emergencies, such as a heart attack or pulmonary embolism. The specific cause of chest pain can be difficult to interpret.If you have unexplained chest pain lasting more than a few minutes, seek emergency medical help right away rather than trying to diagnose the cause yourself.\nfirst aid:Chew a regular-strength aspirin. Aspirin reduces blood clotting, which can help blood flow through a narrowed artery that's caused a heart attack.\nmedication:Heart Medication, Beta blocker, Antihypertensive drug, Calcium channel blocker, and Blood Thinners\nSTOMACH ACHE:\nfirst aid:Provide clear fluids to sip, such as water, broth, or fruit juice diluted with water. Serve bland foods, such as saltine crackers, plain bread, dry toast, rice, gelatin, or applesauce. Avoid spicy or greasy foods and caffeinated or carbonated drinks until 48 hours after all symptoms have gone away.\nmedication:acetaminophen,ibuprofen,naproxen\nBODY OR JOINT PAINS:\nfirst aid:rest, ice, compression, and elevation -- is the best first aid strategy for painful injuries to muscles, joints, and bone injuries. Rest: The injured area should be used sparingly or not at all for 48 hours. ... An over-the-counter pain reliever will help ease the pain and swelling.\nmedication:nuroflex,salonpass,other pain killing sprays\nMEDICATION:\n first aid:maintain a regular and constant diet plan, avoid fast foods\nmedication:zentac,pantorol-40")
		if v==5:
			print("You have Choosen Other Problem(please mention it)")
			h=raw_input("Tell me your problem")
			print("Sorry your",h,"problem is just severe i hope you can just consult your nearest hospital")
			print("OR \n Your problem needs a physical assistance,which")
		if v==6:
			print("You have choosen Menu")
			y.menu()
			y.menu_caller()	
	def Allergies_or_Infection(self):
		print("Tell me your problem type")
		print("1.eye infection\n 2.ear and nose infections\n 3.skin infection or rashes and sun burn\n 4.food allergy \n 5.Other Problem(please mention it) \n 6.Menu \n")
		w=int(input("Tell your type of problem through numbers as shown above"))
		if w==1:
			print("FIRST AID :To treat bacterial conjunctivitis, clean the eyes and apply any topical antibiotic. In the absence of any antibiotics, merely cleaning the eyes of discharge regularly will allow the eyes to settle in a few days.\nMEDICATION:Gatifloxacin,Moxifloxacin,Levofloxacin,Ciprofloxacin")
		if w==2:
			print("EAR ACHE:\nEaraches often need urgent medical care, and may be treated with natural home remedies, for example, warm compresses; OTC pain relievers like ibuprofen (Advil, Motrin), naproxen (Aleve), and acetaminophen (Tylenol and others); olive oil in the affected ear, and essential oils.\nNOSE INFECTION:To treat minor nosebleeds: Sit upright and lean forward to reduce blood pressure in your nose. Pinch both of your nostrils shut at the soft portion of your nose for five to 15 minutes. While completing these steps, breathe through your mouth and keep your head higher than your heart.")
		if w==3:
			print("SKIN INFECTION:The first step in the care of cuts, scrapes (abrasions) is to stop the bleeding. Most wounds respond to direct pressure with a clean cloth or bandage. ... A first aid antibiotic ointment (Bacitracin, Neosporin, Polysporin) can be applied to help prevent infection and keep the wound moist.\nmedication:dermacombin,soracare\n\nRASHES:Zinc oxide ointment is soothing to irritated skin. Calamine lotion is helpful for contact dermatitis, such as poison ivy or oak rashes. For severe itching, apply hydrocortisone cream 3 times a day until the itch is gone.\nSUN BURN:    Apply aloe or over-the-counter moisturizing lotion to skin as directed.To soothe and cool skin, take a cool bath or shower or apply cool compresses to the area.For pain, take ibuprofen (Advil, Motrin) or acetaminophen (Tylenol).If blisters form, don't break them.\n")
		if w==4:
			print("Seek emergency treatment right away. In severe cases, untreated anaphylaxis can lead to death within half an hour. An antihistamine pill, such as diphenhydramine (Benadryl), isn't sufficient to treat anaphylaxis. These medications can help relieve allergy symptoms, but work too slowly in a severe reaction.")
		if w==5:
			print("You have Choosen Other Problem(please mention it)")
			z=raw_input("Tell me your problem")
			print("Sorry your",z,"problem is just severe i hope you can just consult your nearest hospital")
			print("OR \n Your problem needs a physical assistance,which")
		if w==6:
			print("You have choosen Menu")
			y.menu()
			y.menu_caller()	


	def menu_caller(self):
		x=int(input("Tell me your choice in numbers as shown in the menu"))
		if x==1:
			print("You have Choosen Physical Injuries")
			y.physical_injuries()
			
		elif x==2:
			print("You have Choosen Internal Injuries/Illness")
			y.Internal_or_Illness()
			
		elif x==3:
			print("You have Choosen Allergies/Infection")
			y.Allergies_or_Infection()
			
		elif x==4:
			print("You have Choosen Other Problem(please mention it)")
			o=raw_input("Tell me your problem")
			print("Sorry your",o,"problem is just severe i hope you can just consult your nearest hospital")
			print("OR \n Your problem needs a physical assistance,which")
		
		elif x==5:
			print("You have Choosen Back to Main Menu\n")
		else:	
			print("You have given wrong choice\n")
			 
print("You have choosen ILLNESS ANALYZER") 
print("Dont worry ill ensure your fast recovery")
y=illness()
y.menu()
y.menu_caller()
l=raw_input("Was the info useful? \n Tell me yes or no:")
if (l=="yes" or l=="no"):
	print("Thanks for your feedback")
else:
	print("Sorry you have given invalid feedback.Anyway Thank You")

