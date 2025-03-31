import React from 'react';

const TaskForm = ({ newTask, setNewTask, addTask }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Título</label>
          <input
            type="text"
            className="w-full p-2 border rounded-md"
            value={newTask.title}
            onChange={(e) => setNewTask({...newTask, title: e.target.value})}
            placeholder="Ingrese el título de la tarea"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">Fecha límite</label>
          <input
            type="date"
            className="w-full p-2 border rounded-md"
            value={newTask.dueDate}
            onChange={(e) => setNewTask({...newTask, dueDate: e.target.value})}
          />
        </div>
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-1">Descripción</label>
        <textarea
          className="w-full p-2 border rounded-md"
          value={newTask.description}
          onChange={(e) => setNewTask({...newTask, description: e.target.value})}
          placeholder="Ingrese la descripción de la tarea"
          rows="3"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-1">Prioridad</label>
        <select
          className="w-full p-2 border rounded-md"
          value={newTask.priority}
          onChange={(e) => setNewTask({...newTask, priority: e.target.value})}
        >
          <option value="low">Baja</option>
          <option value="normal">Normal</option>
          <option value="high">Alta</option>
        </select>
      </div>

      <button
        onClick={addTask}
        className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
      >
        Agregar Tarea
      </button>
    </div>
  );
};

export default TaskForm;