"use client"
import React from 'react';
import ReactFlow, {
  Background,
  Controls,
  useNodesState,
  useEdgesState,
} from 'reactflow';
import 'reactflow/dist/style.css';

// Componente personalizado para los nodos UML
const UMLNode = ({ data }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow-lg border-2 border-gray-200 min-w-[200px]">
      {/* Header */}
      <div className="text-center mb-2">
        {data.isInterface && (
          <div className="text-purple-600 text-sm bg-purple-50 rounded-md p-1 mb-1">
            &lt;&lt;interface&gt;&gt;
          </div>
        )}
        {data.isAbstract && !data.isInterface && (
          <div className="text-blue-600 text-sm bg-blue-50 rounded-md p-1 mb-1">
            &lt;&lt;abstract&gt;&gt;
          </div>
        )}
        <div className="font-bold text-gray-800">{data.label}</div>
      </div>
      
      {/* Attributes */}
      <div className="border-t border-gray-200 pt-2">
        {data.attributes.map((attr, index) => (
          <div key={index} className="text-sm text-gray-600">
            + {attr}
          </div>
        ))}
      </div>
      
      {/* Methods */}
      <div className="border-t border-gray-200 mt-2 pt-2">
        {data.methods.map((method, index) => (
          <div key={index} className="text-sm text-gray-600">
            + {method}
            {method.includes('*') && (
              <span className="text-red-500 ml-1">*</span>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

// Configuración inicial de nodos
const initialNodes = [
  {
    id: '1',
    type: 'umlNode',
    position: { x: 250, y: 0 },
    data: {
      label: 'IProfesor',
      isInterface: true,
      attributes: [
        'nombre: String',
        'especialidad: String'
      ],
      methods: [
        'teach_method()* : void'
      ]
    }
  },
  {
    id: '2',
    type: 'umlNode',
    position: { x: 50, y: 200 },
    data: {
      label: 'ProfesorMath',
      attributes: [
        'usa_calculadora: boolean'
      ],
      methods: [
        'teach_method() : void'
      ]
    }
  },
  {
    id: '3',
    type: 'umlNode',
    position: { x: 250, y: 200 },
    data: {
      label: 'ProfesorHistory',
      attributes: [
        'periodo_especialidad: String'
      ],
      methods: [
        'teach_method() : void'
      ]
    }
  },
  {
    id: '4',
    type: 'umlNode',
    position: { x: 450, y: 200 },
    data: {
      label: 'ProfesorEnglish',
      attributes: [
        'nivel_cambridge: String'
      ],
      methods: [
        'teach_method() : void'
      ]
    }
  },
  {
    id: '5',
    type: 'umlNode',
    position: { x: 650, y: 0 },
    data: {
      label: 'Escuela',
      isAbstract: true,
      attributes: [
        'nombre: String',
        'profesores: List<IProfesor>'
      ],
      methods: [
        'matricularAlumno()* : void',
        'contratarProfesor()* : void'
      ]
    }
  },
  {
    id: '6',
    type: 'umlNode',
    position: { x: 550, y: 200 },
    data: {
      label: 'EscuelaPublica',
      attributes: [
        'fondos_gubernamentales: float'
      ],
      methods: [
        'matricularAlumno() : void',
        'solicitar_recursos() : void'
      ]
    }
  },
  {
    id: '7',
    type: 'umlNode',
    position: { x: 750, y: 200 },
    data: {
      label: 'EscuelaPrivada',
      attributes: [
        'cuota_mensual: float'
      ],
      methods: [
        'matricularAlumno() : void',
        'cobrar_cuotas() : void'
      ]
    }
  }
];

// Configuración inicial de conexiones
const initialEdges = [
  // Implementación de IProfesor
  {
    id: 'e1-2',
    source: '1',
    target: '2',
    type: 'smoothstep',
    style: { strokeDasharray: 5, stroke: '#333', strokeWidth: 2 },
    animated: true,
  },
  {
    id: 'e1-3',
    source: '1',
    target: '3',
    type: 'smoothstep',
    style: { strokeDasharray: 5, stroke: '#333', strokeWidth: 2 },
    animated: true,
  },
  {
    id: 'e1-4',
    source: '1',
    target: '4',
    type: 'smoothstep',
    style: { strokeDasharray: 5, stroke: '#333', strokeWidth: 2 },
    animated: true,
  },
  // Herencia de Escuela
  {
    id: 'e5-6',
    source: '5',
    target: '6',
    type: 'smoothstep',
    style: { stroke: '#333', strokeWidth: 2 },
  },
  {
    id: 'e5-7',
    source: '5',
    target: '7',
    type: 'smoothstep',
    style: { stroke: '#333', strokeWidth: 2 },
  },
  // Agregación entre Escuela y IProfesor
  {
    id: 'e5-1',
    source: '5',
    target: '1',
    type: 'smoothstep',
    style: { stroke: '#333', strokeWidth: 2 },
    label: 'tiene >',
  }
];

const nodeTypes = {
  umlNode: UMLNode,
};

export default function UMLDiagram() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  return (
    <div className="w-screen h-screen">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
        className="bg-slate-50"
      >
        <Background variant="dots" gap={12} size={1} />
        <Controls />
      </ReactFlow>
    </div>
  );
}