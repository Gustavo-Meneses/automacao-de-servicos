Essa é uma automação aonde vamos pegar uma tabela de vendas pegar os seus indicadores mais importantes, calcula-los e encaminhar por email os valores indicados.

Ela se divide em 2 partes, a primeira onde vamos entrar no drive baixar a tabela disponivel e calcular os indicadores de quantidade e faturamento, e a segunda parte será a que enviamos um email com os respectivos indicadores devidamente calculados.

PARTE 1:

Passo 1 - Entrar no nosso sistema.

O passo 1 será a parte que entramos no sistema (entrar no link: Link que o arquivo a ser analisado está).


Passo 2 - Navegar no sistema.

O passo 2 consiste em navegar dentro do sistema e localizar o arquivo que queremos baixar.
- Para localizar as coordenadas de cada item a ser selecionado, usar o código:

import time
time.sleep(5)
pyautogui.position()

(Deixando claro que as coordenadas podem variar de monitor para monitor, então bem provável que as que estão no código não serão as mesmas que vocês usarão).

 Passo 3 - baixar o arquivo de vendas.
 
 Vamos agora ler o arquivo baixado para pegar os indicadores.

- Faturamento
- Quantidade de Produtos

- Passo 4 - Calcular faturamento e quantidade de produtos 



=====================================================================================================================================================



PARTE 2

Agora que temos todas as informações necessarias para o envio do email, vamos prosseguir com o mesmo.

Passo 1 - Vamos agora encaminhar um email pelo gmail.

Entraremos na interface do gmail

Passo 2 - clicar no botão escrever

Passo 3 - escrever pra quem está mandando o email, escolher o email, seguir para o campo de assunto.

Passo 4 - escrever o assunto, seguir pro corpo do email.

Passo 5 - escrever o corpo do email.

Passo 6 - enviar o email.

