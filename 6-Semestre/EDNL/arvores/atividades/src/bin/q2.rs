#[derive(Debug)]
struct Node {
    value: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Node {
    pub fn new(
        value: i32,
        left: Option<Box<Node>>,
        right: Option<Box<Node>>,
    ) -> Self {
        Self {
            value,
            left,
            right,
        }
    }

    pub fn insert(
        &mut self,
        no: Node,
    ) {
        if no.value < self.value {
            match &mut self.left {
                Some(left) => {
                    left.insert(no);
                }
                None => {
                    self.left = Some(Box::new(no));
                }
            }
        } else {
            match &mut self.right {
                Some(right) => {
                    right.insert(no);
                }
                None => {
                    self.right = Some(Box::new(no));
                }
            }
        }
    }
}

fn main() {
    let nums = vec![
        45, 20, 60, 10,
        30, 50, 70, 25,
    ];

    let mut raiz = Box::new(Node::new(45, None, None));

    for num in &nums[1..] {
        raiz.insert(Node::new(*num, None, None));
    }

    println!("{:#?}", raiz);
}