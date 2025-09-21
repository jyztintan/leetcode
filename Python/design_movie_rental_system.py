class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movie_to_shops = defaultdict(SortedSet)
        self.prices = {}
        for shop, movie, price in entries:
            self.movie_to_shops[movie].add((price, shop))
            self.prices[(shop, movie)] = price
        self.rented = SortedSet()

    def search(self, movie: int) -> List[int]:
        shops = self.movie_to_shops[movie][:5]
        return list(shop[1] for shop in shops)

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.add((price, shop, movie))
        self.movie_to_shops[movie].remove((price, shop))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.movie_to_shops[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        cheapest = self.rented[:5]
        return list([shop, movie] for price, shop, movie in cheapest)

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
