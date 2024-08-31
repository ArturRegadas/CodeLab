<?php
echo "Funcionário: ";
$nome = trim(fgets(STDIN));
echo "\n";

echo "Salário: ";
$salario = trim(fgets(STDIN));
echo "\n";
$sa = (float)$salario;
$pct;

if ($sa <= 400.00) {
    $pct = 15;
} elseif ($sa <= 700.00) {
    $pct = 12;
} elseif ($sa <= 1000.00) {
    $pct = 10;
} elseif ($sa <= 1800.00) {
    $pct = 7;
} elseif ($sa <= 2500.00) {
    $pct = 4;
} else {
    $pct = 0;
}

$ns = $sa + ($sa * $pct / 100);

echo "Nome do funcionário: $nome\n";
echo "% de aumento: $pct%\n";
echo "Salário atual: R$ " . number_format($sa, 2) . "\n";
echo "Novo salário: R$ " . number_format($ns, 2) . "\n";
?>
