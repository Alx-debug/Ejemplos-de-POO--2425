import React from 'react';

const TaskList = ({ filteredTasks, toggleComplete, deleteTask }) => {
  return (
    <div className="bg-white rounded-lg shadow-md">
      {filteredTasks.map(task => (
        <div
          key={task.id}
          className={`p-4 border-b last:border-b-0 ${task.completed ? 'bg-gray-50' : ''}`}
        >
          <div className="flex items-center gap-4">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => toggleComplete(task.id)}
              className="h-5 w-5"
            />
            <div className="flex-1">
              <h3 className={`text-lg font-medium ${task.completed ? 'line-through text-gray-500' : ''}`}>
                {task.title}
              </h3>
              <p className="text-gray-600">{task.description}</p>
              <div className="flex gap-4 mt-2 text-sm text-gray-500">
                <span className={`
                  px-2 py-1 rounded-full
                  ${task.priority === 'high' ? 'bg-red-100 text-red-800' :
                    task.priority === 'normal' ? 'bg-yellow-100 text-yellow-800' :
                    'bg-green-100 text-green-800'}
                `}>
                  {task.priority === 'high' ? 'Alta' :
                   task.priority === 'normal' ? 'Normal' : 'Baja'}
                </span>
                {task.dueDate && (
                  <span>Fecha límite: {task.dueDate}</span>
                )}
              </div>
            </div>
            <button
              onClick={() => deleteTask(task.id)}
              className="text-red-500 hover:text-red-700"
            >
              Eliminar
            </button>
          </div>
        </div>
      ))}
      {filteredTasks.length === 0 && (
        <div className="p-8 text-center text-gray-500">
          No hay tareas que mostrar
        </div>
      )}
    </div>
  );
};

export default TaskList;