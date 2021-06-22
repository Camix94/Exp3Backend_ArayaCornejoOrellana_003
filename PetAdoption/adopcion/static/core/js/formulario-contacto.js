

document.addEventListener("DOMContentLoaded", function(event) {
    document.getElementById('form_1').addEventListener('submit', 
  manejadorValidacion)
  });
  
  function manejadorValidacion(e) {
    e.preventDefault();
    var msg = document.getElementById('msg');
    msg.innerText = '';

    if(this.querySelector('[name=nombreContacto]').value == '') {
    console.log('El nombre está vacío');
    msg.innerText = 'Debes escribir un nombre';
    return;
    }

    if(! validateNombre(this.querySelector('[name=nombreContacto]').value)) 
        { console.log('El nombre no es válido');
        msg.innerText = 'Debes escribir un nombre válido'; 
        return;
    }

    if(this.querySelector('[name=correoContacto]').value == '') {
        console.log('El email está vacío');
        msg.innerText = 'Debes escribir un correo';
        return;
        }

    if(! validateEmail(this.querySelector('[name=correoContacto]').value)) 
        { console.log('El email no es válido');
        msg.innerText = 'Debes escribir un email válido'; 
        return;
    }

    if(this.querySelector('[name=fonoContacto]').value == '') {
        console.log('El teléfono está vacío');
        msg.innerText = 'Debes escribir un número de teléfono';
        return;
        }

    if(! validateFono(this.querySelector('[name=fonoContacto]').value)) 
        { console.log('El número ingresado no es válido');
        msg.innerText = 'Debes ingresar un número de teléfono valido de minímo 9 dígitos y máximo 14'; 
        return;
    }
    
    
    if(this.querySelector('[name=asuntoMensaje]').value == '') {
        console.log('El asunto está vacío');
        msg.innerText = 'Debes escribir un asunto';
        return;
    }

    if(this.querySelector('[name=mensaje]').value == '') {
        console.log('El mensaje está vacío');
        msg.innerText = 'Debes escribir un mensaje';
        return;
    }

    if(this.querySelector('[name=rut]').value == '') {
        console.log('El rut está vacío');
        msg.innerText = 'Debes escribir un número de rut sin puntos ni guión';
        return;
        }

    if(! validateRut(this.querySelector('[name=rut]').value)) 
        { console.log('El rut no es válido');
        msg.innerText = 'Debes escribir un rut válido sin puntos ni guión. Si termina en K, reemplácelo por un 0'; 
        return;
    }

    this.submit();
  }
  
  function validateEmail(correoContacto) {
    var re = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    return re.test((correoContacto).toLowerCase());
   }

   function validateNombre(nombreContacto) {
    var nom = /^[a-zA-ZÀ-ÿ\s]{3,40}$/;
    return nom.test((nombreContacto));
   }

   function validateFono(fonoContacto) {
    var fo = /^\d{9,14}$/;
    return fo.test((fonoContacto));
   }

   function validateRut(rut) {
    var fo = /^\d{8,14}$/;
    return fo.test((rut));
   }



