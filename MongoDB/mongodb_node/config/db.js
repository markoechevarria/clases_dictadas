import mongoose from 'mongoose';
import dotenv from 'dotenv';
dotenv.config();

console.log("MONGODB_URI:", process.env.MONGODB_URI);

const connectDB = async () => {
    try {
        await mongoose.connect( process.env.MONGODB_URI , {
            userNewUrlParser: true,
            userUnifiedTopology: true
        } );
        console.log("Conectado a MongoDB")
    } catch (error) {
        console.log("No se ha podido conectar, hubo un error.")
        process.exit(1);
    }
}

export default connectDB