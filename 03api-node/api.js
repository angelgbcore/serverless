'use strict';

const querystring = require("querystring");

// función que saluda [GET]
module.exports.saludo = async (event) => {
    return {
      statusCode: 200,
      body: JSON.stringify(
        {
          message: '¡¡¡¡ Hola, les dice Gabo desde esta API muy genial !!!!',
          input: event,
        },
        null,
        2
      ),
    };
}

// función que saluda al usuario [GET]
module.exports.saludoUsuario = async (event) => {
    return {
      statusCode: 200,
      body: JSON.stringify(
        {
          message: `Hola ${event.pathParameters.name}`,
          input: event,
        },
        null,
        2
      ),
    };
};

// función que "crea" al usuario [POST]
module.exports.crearUsuario = async (event) => {
    //capturar datos enviados por POST con el módulo querystring
    const body = querystring.parse(event["body"])
    return {
      statusCode: 200,
      body: JSON.stringify(
        {
          message: 'Peticion POST para crear usuarios',
          input: `Hola ${body.user}`,
        },
        null,
        2
      ),
    };
};