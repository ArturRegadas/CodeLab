<?php

$soma = 0;
$f1 = $f2 = $f3 = $f4 = $f5 = 0;
$fs1 = $fs2 = $fs3 = $fs4 = $fs5 = 0;
$par = $imp = 0;
$n = 0;
$maior = PHP_INT_MIN;
$menor = PHP_INT_MAX;
$escolha = 's';

while ($escolha != 'n') {
    echo "Digite um número: ";
    $nu = (int)fgets(STDIN);
    echo "\n";

    $soma += $nu;
    $n++;

    if ($nu > $maior) {
        $maior = $nu;
    }
    if ($nu < $menor) {
        $menor = $nu;
    }

    if ($nu < 0) {
        $f1++;
        $faixa = 1;
        $fs1 += $nu;
    } elseif ($nu >= 0 && $nu < 15) {
        $f2++;
        $faixa = 2;
        $fs2 += $nu;
    } elseif ($nu >= 15 && $nu < 100) {
        $f3++;
        $faixa = 3;
        $fs3 += $nu;
    } elseif ($nu >= 1000) {
        $f4++;
        $faixa = 4;
        $fs4 += $nu;
    } elseif ($nu >= 101 && $nu < 1000) {
        $f5++;
        $faixa = 5;
        $fs5 += $nu;
    } else {
        $faixa = 0;
    }

    if ($nu % 2 == 0) {
        $par++;
        echo "O número $nu é par\n";
    } else {
        $imp++;
        echo "O número $nu é ímpar\n";
    }

    echo "O número $nu está na faixa $faixa\n";

    echo "Continuar [s/n]: ";
    $escolha = trim(fgets(STDIN));
    echo "\n";
}

if ($n > 0) {
    echo "\nA média foi de " . number_format($soma / $n, 2) . "\n";
} else {
    echo "Nenhum número foi inserido.\n";
}

echo "O maior número foi $maior\n";
echo "O menor número foi $menor\n";
echo "Ao todo foram:\n";
echo "Faixa 1: $f1, soma: $fs1\n";
echo "Faixa 2: $f2, soma: $fs2\n";
echo "Faixa 3: $f3, soma: $fs3\n";
echo "Faixa 4: $f4, soma: $fs4\n";
echo "Faixa 5: $f5, soma: $fs5\n";
echo "Ao todo foram $par números pares e $imp números ímpares\n";

?>
