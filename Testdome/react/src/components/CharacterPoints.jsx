import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

function CharacterAttributes({ totalPoints }) {
    const [strength, setStrength] = useState(0);
    const [speed, setSpeed] = useState(0);
    const [pointsLeft, setPointsLeft] = useState(totalPoints);

    const handleAttributeChange = (event, attributeName) => {
        let value = parseInt(event.target.value);

        if (attributeName === 'strength') {
            let newStrength = value;
            let newSpeed = speed;

            if (newStrength + newSpeed > totalPoints) {
                newSpeed = totalPoints - newStrength;
            }

            setStrength(newStrength);
            setSpeed(newSpeed);
            setPointsLeft(totalPoints - newStrength - newSpeed);
        } else if (attributeName === 'speed') {
            let newSpeed = value;
            let newStrength = strength;

            if (newStrength + newSpeed > totalPoints) {
                newStrength = totalPoints - newSpeed;
            }

            setSpeed(newSpeed);
            setStrength(newStrength);
            setPointsLeft(totalPoints - newStrength - newSpeed);
        }
    };

    return (
        <div>
            Character stats: <span id="points">{pointsLeft}</span> points
            <div>
                <input
                    type="range"
                    id="strength"
                    min="0"
                    max={totalPoints}
                    value={strength}
                    step="1"
                    onChange={(event) =>
                        handleAttributeChange(event, 'strength')
                    }
                />
                Strength {strength}
            </div>
            <div>
                <input
                    type="range"
                    id="speed"
                    min="0"
                    max={totalPoints}
                    value={speed}
                    step="1"
                    onChange={(event) => handleAttributeChange(event, 'speed')}
                />
                Speed {speed}
            </div>
        </div>
    );
}

export default CharacterAttributes;
// document.body.innerHTML = "<div id='root'></div>";
// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<CharacterAttributes totalPoints={15} />);
