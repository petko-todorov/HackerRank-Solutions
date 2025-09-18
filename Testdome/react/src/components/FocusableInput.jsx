import React from 'react';
import { createRoot } from 'react-dom/client';

const FocusableInput = (props) => {
    return <input autoFocus={props.shouldFocus} />;
};

// document.body.innerHTML = "<div id='root'></div>";
// const root = createRoot(document.getElementById('root'));
// root.render(<FocusableInput shouldFocus={true} />);
// setTimeout(() => console.log(document.getElementById('root').innerHTML), 300);
export default FocusableInput;
