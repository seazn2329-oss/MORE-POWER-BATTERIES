# Website Build Prompt: Car Battery Shop in Ghana

Copy this prompt into your AI coding assistant in Visual Studio Code. Replace the bracketed details when you know them; if a detail is unknown, keep it as a clearly marked placeholder rather than inventing it.

---

Build a polished, trustworthy, mobile-friendly website for a car battery shop in Ghana that serves owners of American and Asian vehicles.

## Business details
- Shop name: [MORE POWER BATTERIES]
- Location/address: [ACCRA, ABOSSEY OKAI, NEAR FANMILK]
- Phone/WhatsApp: [+233544905262]
- Opening hours: [8:00AM - 8:PM,MONDAY-SATURDAY]
- Currency: Ghana cedi (GH₵)
- Delivery area and fees: [AREAS / FEES, OR “Pickup only”]
- Social links: [OPTIONAL LINKS]

Do not fabricate business details, prices, stock, warranties, brand partnerships, delivery promises, or customer reviews. Use editable placeholders for any missing information. Make it easy for the shop owner to update products and contact details later.

## Goal and audience
Help drivers quickly find a suitable battery, confirm compatibility and availability with the shop, and choose WhatsApp/phone ordering or in-person pickup. The audience includes people using both American and Asian cars and people browsing on phones with limited time or data.

## Pages and content
Create a simple, clear site with:

1. **Home page**
   - Strong headline such as “The right battery for your car, made easy.”
   - State that the shop serves American and Asian cars, without implying every model is guaranteed to fit.
   - Prominent buttons: “Find a Battery,” “Order on WhatsApp,” and “Get Directions.”
   - A short explanation: send the car make, model, year, engine size (if known), and a photo of the current battery label/terminals to confirm the correct fit.
   - Highlight order options: WhatsApp/phone enquiry, then pickup or delivery if offered.

2. **Battery types**
   Show easy-to-understand cards for the products the shop actually stocks. Include editable examples such as:
   - Standard flooded / maintenance-free batteries
   - AGM batteries
   - EFB batteries
   - Deep-cycle batteries (only if sold)
   - Battery sizes or fitment groups (editable list)

   For each product, provide fields for name/type, suitable use, capacity (Ah), cold cranking amps (CCA) where available, dimensions, terminal layout, warranty terms, price in GH₵, availability, and product photo. Do not claim compatibility based only on vehicle origin or brand. Add a note that fitment depends on the exact model, year, engine, battery size, terminals, and vehicle requirements and should be confirmed before purchase.

3. **How to order**
   Present a clear numbered flow:
   1. Tell us the vehicle make, model, year, and engine if known.
   2. Send a photo of the battery label and terminal layout, if possible.
   3. We confirm fit, price, warranty, and current availability.
   4. Choose pickup or ask about delivery to your area.
   5. Confirm payment and collection/delivery details directly with the shop.

   Add a WhatsApp button that opens a prefilled message containing these questions: “Hello, I need a battery. My car make/model is ____, year ____, engine (if known) ____. I can send a photo of the current battery. Please confirm fit, price, availability, and warranty.” Build the link from the editable phone number. If no number is provided yet, show a placeholder and do not create a broken link.

4. **Pickup and delivery**
   Explain how to collect an order, show the shop address/landmark and opening hours, and provide a map/directions link only after a real address is supplied. If delivery is available, state service areas, charges, and timing only when provided by the owner. Otherwise say “Ask us about delivery” or mark the section as pickup-focused.

5. **Contact and FAQ**
   Include phone/WhatsApp, location, opening hours, and a short FAQ about checking battery fit, what information to send, stock confirmation, warranty, and pickup. Keep warranty answers editable and avoid making up terms.

## Design and usability
- Make it work beautifully on phones, tablets, and desktop computers.
- Use a responsive layout, readable text, large tap targets, clear contrast, and simple navigation.
- Keep pages lightweight and quick to load on mobile data.
- Use a warm, dependable automotive look; avoid clutter and excessive animation.
- Use real product images only when available. Otherwise use tasteful placeholders labelled for replacement.
- Keep important contact and ordering actions visible near the top and easy to reach on mobile.
- Use accessible semantic HTML, keyboard-friendly navigation, descriptive image text, and visible focus states.
- Include a footer with contact details, location, hours, and any supplied social links.

## Technical requirements
- First inspect the existing project and keep its current framework and conventions. If it is empty, choose a simple, maintainable approach suited to the existing tools; do not add unnecessary dependencies.
- Implement the actual working website, not just a mockup or a plan.
- Use reusable components and keep product and business information in an easy-to-edit data/config file where practical.
- Make phone links use `tel:` and WhatsApp links use the correct `wa.me` format with the Ghana country code and digits only.
- Add sensible page titles, descriptions, favicon placeholder, and social sharing metadata.
- Do not add fake checkout, account creation, payment collection, or live inventory unless explicitly configured. The initial site should support enquiries and order confirmation with the shop.
- Check the site at narrow phone and desktop widths and fix layout issues. Run the available build or lint checks if configured, and report any remaining setup steps.

## Before finishing
Summarize the pages and features created, list all placeholders the shop owner needs to fill in (especially shop name, phone, address, hours, products, prices, stock, and warranty), and explain how to run the website locally in Visual Studio Code.
