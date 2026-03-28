package com.baozi.controller;

import com.baozi.model.Pedido;
import com.baozi.repository.PedidoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/pedidos")
public class PedidoController {

    @Autowired
    private PedidoRepository pedidoRepository;

    @PostMapping
    public ResponseEntity<Pedido> criar(@RequestBody Pedido pedido) {
        Pedido novoPedido = pedidoRepository.save(pedido);
        return ResponseEntity.status(HttpStatus.CREATED).body(novoPedido);
    }

    @GetMapping
    public ResponseEntity<List<Pedido>> listarTodos() {
        List<Pedido> pedidos = pedidoRepository.findAll();
        return ResponseEntity.ok(pedidos);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Pedido> consultarPorId(@PathVariable Long id) {
        Optional<Pedido> pedido = pedidoRepository.findById(id);
        return pedido.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletar(@PathVariable Long id) {
        if (pedidoRepository.existsById(id)) {
            pedidoRepository.deleteById(id);
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }

    @PutMapping("/{id}")
    public ResponseEntity<Pedido> atualizar(@PathVariable Long id, @RequestBody Pedido pedidoAtualizado) {
        Optional<Pedido> pedidoExistente = pedidoRepository.findById(id);
        if (pedidoExistente.isPresent()) {
            Pedido pedido = pedidoExistente.get();
            if (pedidoAtualizado.getClienteId() != null) {
                pedido.setClienteId(pedidoAtualizado.getClienteId());
            }
            if (pedidoAtualizado.getProdutoId() != null) {
                pedido.setProdutoId(pedidoAtualizado.getProdutoId());
            }
            if (pedidoAtualizado.getQuantidade() != null) {
                pedido.setQuantidade(pedidoAtualizado.getQuantidade());
            }
            Pedido pedidoSalvo = pedidoRepository.save(pedido);
            return ResponseEntity.ok(pedidoSalvo);
        }
        return ResponseEntity.notFound().build();
    }
}
