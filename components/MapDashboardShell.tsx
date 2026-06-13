import dynamic from 'next/dynamic';
const MapDashboard=dynamic(()=>import('./MapDashboard'),{ssr:false}); export default MapDashboard;
