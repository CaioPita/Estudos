package mensagem;

public class SMS implements CanalEnvio {

	@Override
	public void enviar(String texto) {
		// TODO Auto-generated method stub
		System.out.println("Enviando SMS com conteúdo: " + texto);
		
	}
		
	}


