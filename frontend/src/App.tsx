import { useEffect, useState } from 'react';
import Empleados from './components/Empleados';
import type { Empleado } from './types';

function App() {
  const [empleados, setEmpleados] = useState<Empleado[]>([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/')
      .then(res => res.json())
      .then(data => setEmpleados(data.message));
  }, []);

  return (
    <div>
      <h1>Lista de empleados:</h1>
      <ul>
        {empleados.map((empleado) => (
          <Empleados key={empleado.id} datos={empleado} />
        ))}
      </ul>
    </div>
  );
}

export default App;
