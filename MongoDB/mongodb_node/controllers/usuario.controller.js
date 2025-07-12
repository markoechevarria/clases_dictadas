import Usuario from "../models/Usuario.js"

export const getUsuarios = async (req, res) => {
    try {
        const usuarios = await Usuario.find();
        res.json(usuarios);
    } catch (error) {
        res.status(500).json({error: error.message})
    }
}

export const crearUsuario = async (req, res) => {
    try {
        const nuevoUsuario = new Usuario(req.body);
        await nuevoUsuario.save();
        res.status(201).json(nuevoUsuario)
    } catch (error) {
        res.status(400).json({error: error.message})
    }
}