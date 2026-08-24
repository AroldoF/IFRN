use std::collections::LinkedList;

#[derive(Debug)]
struct Node {
    value: i32,
    children: Option<LinkedList<Node>>,
}

impl Node {
    pub fn new(value: i32, children: Option<LinkedList<Node>>) -> Self {
        Node {
            value: value,
            children: children
        }
    }

    pub fn insert(&mut self, no: Node) {
        if self.children.is_none() {
            return self.children = Some(LinkedList::from([no]));
        }


        self.children
            .as_mut()
            .unwrap()
            .push_back(no);
    }
}

fn main() {
    let nums = vec![45, 20, 60, 10, 30, 50, 70, 25];
    let mut node = Node::new(45, None);

    // adiciona 31 como filho de 32
    node.insert(Node::new(31, None));
    node.insert(Node::new(66, None));

    // pega o primeiro filho de forma mutável
    let filho = node
        .children
        .as_mut()
        .unwrap()
        .front_mut()
        .unwrap();

    // adiciona 34 como filho de 31
    filho.insert(Node::new(34, None));
    filho.insert(Node::new(33, None));

    println!("{:#?}", node);
}