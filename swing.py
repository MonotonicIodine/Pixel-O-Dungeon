from weapon import Sword


# class Swing:
#     def __init__(self, player, enemy):
#         self.player = player
#         self.enemy = enemy

#     def swing_Sword(self,display):
#         sword = Sword()
#         sword.position.x = self.player.position.x + 40
#         sword.position.y = self.player.position.y + 15
#         display.blit(sword.image, (sword.position.x, sword.position.y))

#         # Check for collision between sword and enemy
#         if self.check_collision():
#             self.enemy.hit_points -= sword.damage


#             print(f"Enemy's HP: {self.enemy.hit_points}")

#     def check_collision(self):
#         # Implement your collision detection logic here
#         # For simplicity, let's assume the sword and enemy are colliding
#         return True