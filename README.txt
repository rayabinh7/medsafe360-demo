MEDSAFE 360 — PUBLIC PRESENTATION DEMO

This version includes 42 medication NAMES but NO real dosing, indications, contraindications, or preparation instructions. It is for demonstration only.

HOST ON GITHUB PAGES
1. Open Settings > Pages in this repository.
2. Under Build and deployment, select Deploy from a branch, branch main, folder /(root), then Save.
3. Wait for GitHub Pages to display the published HTTPS URL (usually https://rayabinh7.github.io/medsafe360-demo/). Open it on your phone and test a profile, such as https://rayabinh7.github.io/medsafe360-demo/#ADCD-MED-0001.
4. Generate the 42 direct-open phone QR codes with:
   pip install qrcode[pil] reportlab
   python generate_url_qr.py https://rayabinh7.github.io/medsafe360-demo/
5. Each QR encodes the published website URL followed by a profile fragment, for example #ADCD-MED-0001.

Do not publish the original internal-formulary website or its medication content without explicit permission. No clinical dose calculator or patient-data collection is included.
