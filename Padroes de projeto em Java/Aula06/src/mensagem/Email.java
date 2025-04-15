package mensagem;

public class Email implements CanalEnvio {

	@Override
	public void enviar(String texto) {
		// TODO Auto-generated method stub
		System.out.println("Enviando email com conteúdo: " + texto);
		
	}

}
