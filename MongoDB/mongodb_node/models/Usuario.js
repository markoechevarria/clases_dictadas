import mongoose from "mongoose";

const usuarioSchema = new mongoose.Schema( {
    nombre: { type: String, required: true },
    correo: { type: String, required: true, unique: true },
    edad: { type: Number, required: true }
} )

const Usuario = mongoose.model( 'Usuario', usuarioSchema );
export default Usuario