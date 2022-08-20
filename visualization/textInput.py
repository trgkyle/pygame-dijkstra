def write_text(pygame, screen,user_text_init, title):
	user_text = user_text_init
	title_front = pygame.font.Font('visualization/roboto.ttf', 24)
	base_font = pygame.font.Font('visualization/roboto.ttf', 24)
	# create rectangle
	input_rect = pygame.Rect(350, 280, 140, 32)

	# color_active stores color(lightskyblue3) which
	# gets active when input box is clicked by user
	color_active = pygame.Color('lightskyblue3')

	# color_passive store color(chartreuse4) which is
	# color of input box.
	color_passive = pygame.Color('chartreuse4')
	color = color_passive

	active = True
	clock = pygame.time.Clock()
 
	while True:
		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN:

				# Check for backspace
				if event.key == pygame.K_BACKSPACE:

					# get text input from 0 to -1 i.e. end.
					user_text = user_text[:-1]

				elif event.key == pygame.K_RETURN:
					return user_text
				# Unicode standard is used for string
				# formation
				else:
					user_text += event.unicode
		# it will set background color of screen
		# screen.fill((255, 255, 255))

		if active:
			color = color_active
		else:
			color = color_passive
			
		# draw rectangle and argument passed which should
		# be on screen
		pygame.draw.rect(screen, color, input_rect)

		text_surface = base_font.render(user_text, True, (255, 255, 255))
		text_title = title_front.render(title, True, (0, 0, 0))
		# render at position stated in arguments
		screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
		screen.blit(text_title, (input_rect.x , input_rect.y - 25))
		
		# set width of textfield so that text cannot get
		# outside of user's text input
		input_rect.w = max(100, text_surface.get_width()+10)
		pygame.display.flip()
		clock.tick(60)