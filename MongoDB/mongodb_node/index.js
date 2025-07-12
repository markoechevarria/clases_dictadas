import dotenv from 'dotenv';

dotenv.config();
console.log("MONGODB_URI:", process.env.MONGODB_URI);

import express from 'express';

import connectDB from './config/db.js';
import usuarioRoutes from './routes/usuario.routes.js';



const app = express();
app.use( express.json() );

connectDB();

app.use('/api/usuarios', usuarioRoutes)

const PORT = process.env.PORT;
app.listen( PORT, () => {
    console.log( `Servidor corriendo en puerto ${PORT}` )
}  );