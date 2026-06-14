import type { Config } from 'tailwindcss';
const config: Config = {content:['./app/**/*.{ts,tsx}','./components/**/*.{ts,tsx}','./lib/**/*.{ts,tsx}'],theme:{extend:{colors:{navy:'#06101f',panel:'#0c1a2f',panel2:'#10243d',line:'#203957',amber:'#f6c453',cyan:'#54d6ff',mint:'#68f0b0',danger:'#ff6b6b'}}},plugins:[]};
export default config;
