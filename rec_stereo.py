import cv2
cap_left = cv2.VideoCapture(2)
cap_right = cv2.VideoCapture(4)
out_left = cv2.VideoWriter('left_vid.avi',cv2.VideoWriter_fourcc(*'XVID'),30.0,(640,480))
out_right = cv2.VideoWriter('right_vid.avi',cv2.VideoWriter_fourcc(*'XVID'),30.0,(640,480))

while (cap_left.isOpened() and cap_right.isOpened()):
  ret, imagen = cap_left.read()
  ret2, imagen2 = cap_right.read()

  if ret == True and ret2 == True:
    cv2.imshow('Left Camera', imagen)
    cv2.imshow('Right Camera', imagen2)
    out_left.write(imagen)
    out_right.write(imagen2)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break

cap_left.release()
out_left.release()
cap_right.release()
out_right.release()
cv2.destroyAllWindows()
