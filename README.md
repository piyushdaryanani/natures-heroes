# Nature's Heroes

A waste-sorting game for children, built for robot-supported learning at UNBC's Social
Robotics Lab. Players show an item to the camera; the game recognizes it in real time and
checks whether it belongs in the recycling or compost bin. It was used in the lab's
robot-supported activities and informed our HRI '26 paper,
[*Social Robots on the Loose*](https://doi.org/10.1145/3757279.3785580).

## What it does
- Detects objects live from the webcam with TensorFlow.js and the COCO-SSD model, running
  in the browser, so no images are sent anywhere
- Recycling and compost game modes, with answer checking and scoring
- A Django back end serves the game pages and menus

## Tech stack
Python · Django · JavaScript · TensorFlow.js (COCO-SSD) · HTML · CSS

## Run it locally
```bash
git clone https://github.com/piyushdaryanani/natures-heroes.git
cd natures-heroes
python3 -m venv venv && source venv/bin/activate
pip install django
python3 manage.py runserver
```
Then open http://127.0.0.1:8000 and allow camera access.
