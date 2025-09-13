import { useState } from 'react';
import CharacterAttributes from './components/CharacterPoints';
import TodoList from './components/TodoList';

const items = [
    { text: 'Buy grocery', done: true },
    { text: 'Play guitar', done: false },
    { text: 'Romantic dinner', done: false },
];

function App() {
    return (
        <>
            <CharacterAttributes totalPoints={15} />
            <TodoList
                items={items}
                onListClick={(event) => console.log('List clicked!')}
                onItemClick={(item, event) => {
                    console.log(item, event);
                }}
            />
        </>
    );
}

export default App;
