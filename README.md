# GLOW App
# 7 and 1 Nights, 1001 Stories
A digital storytelling platform for the GLOW project that transforms children’s physical paper cutouts into a large-scale animated visual artwork for classroom, city-wide, and online exhibition.

## Project Overview
**7 and 1 Nights, 1001 Stories** is an interactive art and education project inspired by the idea of continuous storytelling. Children create black paper silhouettes with open-ended narrative meaning, these works are photographed and uploaded by teachers, and the system transforms them into a digital “moving tapestry” that can be projected as an endless visual story.

The platform supports the full workflow from classroom creation to digital processing and exhibition. Its purpose is to connect children, classes, schools, and municipalities into one shared artistic narrative.

## Tools & Technologies
- **Frontend:** React.js, TypeScript, Vite, PWA
- **Backend:** Python
- **Database:** MySQL
- **Cloud Server:** Hetzner
- **Management:** Jira

## Workflow
1. A teacher logs into the app.
2. he teacher uploads photographs of children’s black paper silhouettes.
3. The backend receives the files and stores the submission metadata.
4. The backend processes the images:
- detects shapes
- extracts contours
- prepares vector or clean digital assets
- organizes artworks into a collage
- applies inversion and animation logic
5. The generated output becomes available for:
- classroom projection
- school exhibition
- central GLOW exhibition
- online presentation
6. The online platform displays the final work with school and class context.

## Development Setup
**Frontend**
cd frontend
npm install
npm run dev

**Backend**
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

## Deployment Plan
The application can be deployed on Hetzner with a simple setup such as:
- one virtual server for frontend and backend
- one MySQL instance on the same server or separate managed environment
- reverse proxy for HTTPS routing
- persistent storage for uploads and generated media
