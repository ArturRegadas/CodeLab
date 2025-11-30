-- Script de INSERT para popular o banco Hotel-Feliz

-- 1. Inserir TIPOS DE QUARTO
INSERT INTO public.tipo_quarto (nome_tipo, capacidade_maxima, preco_diaria_base, descricao) 
VALUES 
  ('Solteiro', 1, 100.00, 'Quarto para uma pessoa com cama solteiro'),
  ('Casal', 2, 150.00, 'Quarto para casal com cama queen'),
  ('Suite', 4, 250.00, 'Suite luxo com sala de estar'),
  ('Standard', 2, 120.00, 'Quarto padrão com cama de solteiro ou casal');

-- 2. Inserir QUARTOS
INSERT INTO public.quarto (numero_quarto, id_tipo, status_limpeza, localizacao) 
VALUES 
  ('101', 1, 'Limpo', '1º andar'),
  ('102', 1, 'Limpo', '1º andar'),
  ('103', 2, 'Sujo', '1º andar'),
  ('104', 2, 'Limpo', '1º andar'),
  ('201', 2, 'Limpo', '2º andar'),
  ('202', 3, 'Em limpeza', '2º andar'),
  ('203', 4, 'Limpo', '2º andar'),
  ('301', 1, 'Limpo', '3º andar'),
  ('302', 2, 'Sujo', '3º andar'),
  ('303', 3, 'Limpo', '3º andar');

-- 3. Inserir PERFIS (já devem existir, mas se não...)
INSERT INTO public.perfil (nome_perfil) 
VALUES 
  ('Admin'),
  ('Gerente'),
  ('Recepcionista'),
  ('Limpeza'),
  ('Hospede')
ON CONFLICT DO NOTHING;

-- 4. Inserir USUARIOS
INSERT INTO public.usuario (nome_completo, email, senha, id_perfil) 
VALUES 
  ('Admin Sistema', 'admin@hotel.com', 'senha123', 1),
  ('João Gerente', 'joao@hotel.com', 'senha123', 2),
  ('Maria Recepcionista', 'maria@hotel.com', 'senha123', 3),
  ('Pedro Limpeza', 'pedro@hotel.com', 'senha123', 4);

-- 5. Inserir HOSPEDES
INSERT INTO public.hospede (nome_completo, documento, telefone, email, endereco) 
VALUES 
  ('Carlos Silva', '12345678901', '11987654321', 'carlos@email.com', 'Rua A, 100'),
  ('Ana Costa', '98765432101', '11912345678', 'ana@email.com', 'Rua B, 200'),
  ('Lucas Ferreira', '55544433322', '11988776655', 'lucas@email.com', 'Rua C, 300'),
  ('Julia Oliveira', '11122233344', '11997776666', 'julia@email.com', 'Rua D, 400'),
  ('Roberto Santos', '66677788899', '11999998888', 'roberto@email.com', 'Rua E, 500');

-- 6. Inserir SERVICOS
INSERT INTO public.servico (nome_servico, preco) 
VALUES 
  ('Café da manhã', 25.00),
  ('Limpeza extra', 50.00),
  ('Minibar', 15.00),
  ('Spa', 100.00),
  ('Serviço de quarto', 30.00),
  ('Transfer', 80.00);

-- 7. Inserir RESERVAS
INSERT INTO public.reserva (id_hospede, numero_quarto, data_checkin, data_checkout, status_reserva, valor_total) 
VALUES 
  (1, '101', '2025-12-01', '2025-12-03', 'Confirmada', 300.00),
  (2, '102', '2025-12-02', '2025-12-05', 'Confirmada', 450.00),
  (3, '104', '2025-12-05', '2025-12-07', 'Pendente', 300.00),
  (4, '201', '2025-12-10', '2025-12-12', 'Confirmada', 300.00),
  (5, '303', '2025-12-15', '2025-12-17', 'Confirmada', 500.00);

-- 8. Inserir FATURAS
INSERT INTO public.fatura (id_reserva, valor_diarias, valor_servicos, status_pagamento) 
VALUES 
  (1, 300.00, 0.00, 'Pendente'),
  (2, 450.00, 50.00, 'Paga'),
  (3, 300.00, 0.00, 'Pendente'),
  (4, 300.00, 100.00, 'Pendente'),
  (5, 500.00, 200.00, 'Paga');

-- 9. Inserir ITENS DA FATURA (relação entre fatura e servico)
INSERT INTO public.fatura_servico (id_fatura, id_servico, quantidade, preco_unitario) 
VALUES 
  (1, 1, 2, 25.00),
  (2, 1, 3, 25.00),
  (2, 4, 1, 100.00),
  (4, 5, 2, 30.00),
  (4, 6, 1, 80.00),
  (5, 1, 2, 25.00),
  (5, 4, 2, 100.00);

-- Commit das alterações
COMMIT;
