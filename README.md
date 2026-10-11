# Nature's Heroes

A waste-sorting game for children, built for robot-supported learning at UNBC's Social
Robotics Lab. Players hold up an item to the camera, and the game recognizes it in real time
and checks whether it went in the right bin. It was used in the lab's robot-supported
activities and informed our HRI '26 paper,
[*Social Robots on the Loose*](https://doi.org/10.1145/3757279.3785580).

## What it does
- Detects objects live from the webcam with TensorFlow.js and the COCO-SSD model, entirely
  in the browser: no server and no images leave the computer
- Checks each answer, keeps score, and supports several game modes
- Uses a simple game-state machine, so each round moves through clear stages

## Tech stack
JavaScript · TensorFlow.js (COCO-SSD) · HTML · CSS

## Run it locally
```bash
git clone https://github.com/piyushdaryanani/natures-heroes.git
cd natures-heroes
python3 -m http.server 8000
```
Then open http://localhost:8000 and allow camera access.
