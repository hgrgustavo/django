function redirect_url(deleteUrl) {
  if (confirm("Você deseja deletar?")) {
    window.location.href = deleteUrl; // Redireciona para o caminho de exclusão
  }
}
