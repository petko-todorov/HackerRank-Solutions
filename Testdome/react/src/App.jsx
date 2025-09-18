import { useState } from 'react';
import CharacterAttributes from './components/CharacterPoints';
import TodoList from './components/TodoList';
import FocusableInput from './components/FocusableInput';
import Message from './components/ToggleMessage';

const items = [
    { text: 'Buy grocery', done: true },
    { text: 'Play guitar', done: false },
    { text: 'Romantic dinner', done: false },
];

function App() {
    return (
        <>
            <CharacterAttributes totalPoints={15} />
            <hr />
            <TodoList
                items={items}
                onListClick={(event) => console.log('List clicked!')}
                onItemClick={(item, event) => {
                    console.log(item, event);
                }}
            />
            <hr />
            <FocusableInput shouldFocus={true} />
            <hr />
            <Message />
        </>
    );
}

export default App;
