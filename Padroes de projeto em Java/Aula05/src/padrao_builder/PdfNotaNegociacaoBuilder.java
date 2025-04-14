package padrao_builder;
//Builder concreto para formato PDF
public class PdfNotaNegociacaoBuilder implements NotaNegociacaoBuilder {
	private NotaNegociacao nota;
	public PdfNotaNegociacaoBuilder() {
		this.nota = new NotaNegociacao();
	}
	@Override
	public void buildCabecalho() {
		nota.adicionarConteudo("PDF: Cabeçalho da Nota");
	}
	@Override
	public void buildOperacoes() {
		nota.adicionarConteudo("PDF: Lista de operações");
		
	}
	@Override
	public void buildSumario() {
		nota.adicionarConteudo("PDF: Sumário com totais e taxas");
		
	}
	@Override
	public NotaNegociacao getNota() {
		// TODO Auto-generated method stub
		return nota;
	}
	
}
