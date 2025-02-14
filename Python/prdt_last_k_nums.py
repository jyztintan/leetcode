class ProductOfNumbers:

    def __init__(self):
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
            self.size = 0
        else:
            self.prefix_product.append(self.prefix_product[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        return self.prefix_product[-1] // self.prefix_product[self.size - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
