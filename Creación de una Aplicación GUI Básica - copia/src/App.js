import React, { useState } from 'react';
import TaskForm from './components/TaskForm';
import TaskFilter from './components/TaskFilter';
import TaskList from './components/TaskList';

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState({ title: '', description: '', priority: 'normal', dueDate: '' });
  const [filter, setFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');

  const addTask = () => {
    if (newTask.title && newTask.description) {
      setTasks([...tasks, { ...newTask, id: Date.now(), completed: false }]);
      setNewTask({ title: '', description: '', priority: 'normal', dueDate: '' });
    }
  };

  const deleteTask = (taskId) => {
    setTasks(tasks.filter(task => task.id !== taskId));
  };

  const toggleComplete = (taskId) => {
    setTasks(tasks.map(task =>
      task.id === taskId ? { ...task, completed: !task.completed } : task
    ));
  };

  const filteredTasks = tasks
    .filter(task => {
      if (filter === 'completed') return task.completed;
      if (filter === 'pending') return !task.completed;
      return true;
    })
    .filter(task =>
      task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      task.description.toLowerCase().includes(searchTerm.toLowerCase())
    );

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-800 mb-8">Gestor de Tareas Avanzado</h1>
        <TaskForm newTask={newTask} setNewTask={setNewTask} addTask={addTask} />
        <TaskFilter
          filter={filter}
          setFilter={setFilter}
          searchTerm={searchTerm}
          setSearchTerm={setSearchTerm}
        />
        <TaskList
          filteredTasks={filteredTasks}
          toggleComplete={toggleComplete}
          deleteTask={deleteTask}
        />
      </div>
    </div>
  );
}

export default App;