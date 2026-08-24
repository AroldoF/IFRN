#[derive(Debug)]
struct Node {
    ip: u64,
    contador_tentativas: u8,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Node {
    pub fn new(ip: u64) -> Self {
        Self {
            ip,
            contador_tentativas: 1,
            left: None,
            right: None,
        }
    }

    pub fn insert(&mut self, ip: u64) {
        if ip < self.ip {
            match &mut self.left {
                Some(left) => left.insert(ip),
                None => {
                    self.left = Some(Box::new(Node::new(ip)));
                }
            }
        } else if ip > self.ip {
            match &mut self.right {
                Some(right) => right.insert(ip),
                None => {
                    self.right = Some(Box::new(Node::new(ip)));
                }
            }
        } else {
            self.contador_tentativas += 1;
        }
    }

    pub fn find(&self, ip: u64) -> Option<&Node> {
        if ip == self.ip {
            Some(self)
        } else if ip < self.ip {
            match &self.left {
                Some(left) => left.find(ip),
                None => None,
            }
        } else {
            match &self.right {
                Some(right) => right.find(ip),
                None => None,
            }
        }
    }

    pub fn relatorio_ordenado(&self) {
        if let Some(left) = &self.left {
            left.relatorio_ordenado();
        }

        println!(
            "IP: {} | Tentativas: {}",
            self.ip,
            self.contador_tentativas
        );

        if let Some(right) = &self.right {
            right.relatorio_ordenado();
        }
    }
}

fn main() {
    let ips = vec![
        192168001001,
        100000000001,
        200000000001,
        150000000001,
        150000000001,
        150000000001,
        192168001001,
    ];

    let mut raiz = Box::new(Node::new(ips[0]));

    for ip in &ips[1..] {
        raiz.insert(*ip);
    }

    println!("Árvore:");
    println!("{:#?}", raiz);

    println!("\nRelatório ordenado:");
    raiz.relatorio_ordenado();

    println!("\nBusca:");

    match raiz.find(ips[3]) {
        Some(node) if node.contador_tentativas >= 3 => {
            println!(
                "IP {} está BLOQUEADO. Tentativas: {}",
                node.ip,
                node.contador_tentativas
            );
        }

        Some(node) => {
            println!(
                "IP {} não está bloqueado. Tentativas: {}",
                node.ip,
                node.contador_tentativas
            );
        }

        None => {
            println!("IP não encontrado na blacklist.");
        }
    }
}