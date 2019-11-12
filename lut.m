
t = xlsread('test.xls');

origin = t(1:4913,1:3);
result = t(1:4913,4:6);

% for i=1:4913
%     for j=1:3
%         result(i,j) = 255 - origin(i,j);        %������ֵȡ�����������ԡ�
%     end
% end



im = imread('test1.jpg');
figure(1);imshow(im);

[M,N,L] = size(im);


out_im = zeros(M,N,L);
out_im2 = zeros(M,N,L);



%   �ֱ��ȡRGB
im_r=im(:,:,1);
im_g=im(:,:,2);
im_b=im(:,:,3);

for i=1:M
    for j=1:N
        %ͨ��RGB��ֵ�õ�RGB�ռ����꣬ȡֵ��ΧΪ0~16��
        if im_r(i,j) == 255
            im_r(i,j) = 256; %�Ŵ�һλ�������ڼ���������
        end
        if im_g(i,j) == 255
            im_g(i,j) = 256;
        end
        if  im_b(i,j) == 255
             im_b(i,j) = 256;
        end
        
        pos_r = im_r(i,j)/16;     %�ȵõ�8��������������С���Ǹ�
        pos_g = im_g(i,j)/16;
        pos_b = im_b(i,j)/16 + 1;
        
        rem_r = rem(im_r(i,j),16);      %ͨ�����������������
        rem_g = rem(im_g(i,j),16);
        rem_b = rem(im_b(i,j),16);
        remainder = [rem_r,rem_g,rem_b];
        remainder = uint16(remainder);
        
        % �򻯰����Բ�ֵ
        %   ����repos(pos_r,pos_g,pos_b)��ʾ��RGB����ת��Ϊ��ά���еĺ�����        
%         if pos_r < 16 && pos_g < 16 && pos_b < 16
%             out_im(i,j,1) = (result(repos(pos_r,pos_g,pos_b),1) * (16 - remainder(1)) + result(repos(pos_r+1,pos_g,pos_b),1) * remainder(1)) / 16;
%             out_im(i,j,2) = (result(repos(pos_r,pos_g,pos_b),2) * (16 - remainder(2)) + result(repos(pos_r,pos_g+1,pos_b),1) * remainder(2)) / 16;
%             out_im(i,j,3) = (result(repos(pos_r,pos_g,pos_b),3) * (16 - remainder(3)) + result(repos(pos_r,pos_g,pos_b+1),1) * remainder(3)) / 16;
%         end
       
        
        %��ȷ�����Բ�ֵ
        temp_00 = zeros(1,3);
        temp_10 = zeros(1,3);
        temp_01 = zeros(1,3);
        temp_11 = zeros(1,3);
        temp_0 = zeros(1,3);
        temp_1 = zeros(1,3);
        temp = zeros(1,3);
        
        %����߽�㣬����Խ��
        if pos_r > 15
            pos_r = 15;
            remainder(1) =15;
        end
        if pos_g > 15
            pos_g = 15;
            remainder(2) =15;
        end
        if pos_b > 15
            pos_b = 15;
            remainder(3) =15;
        end     

        for k = 1:3
            temp_00(1,k) = (result(repos(pos_r,pos_g,pos_b),k) * (16 - remainder(3)) + result(repos(pos_r,pos_g,pos_b + 1),k) * remainder(3)) / 16;
            temp_10(1,k) = (result(repos(pos_r,pos_g + 1,pos_b),k) * (16 - remainder(3)) + result(repos(pos_r,pos_g + 1,pos_b + 1),k) * remainder(3)) / 16;
            temp_01(1,k) = (result(repos(pos_r + 1,pos_g,pos_b),k) * (16 - remainder(3)) + result(repos(pos_r + 1,pos_g,pos_b + 1),k) * remainder(3)) / 16;
            temp_11(1,k) = (result(repos(pos_r + 1,pos_g + 1,pos_b),k) * (16 - remainder(3)) + result(repos(pos_r + 1,pos_g + 1,pos_b + 1),k) * remainder(3)) / 16;

            temp_0(1,k) = (temp_00(1,k) * (16 - remainder(2)) + temp_10(1,k) * remainder(2)) / 16;
            temp_1(1,k) = (temp_01(1,k) * (16 - remainder(2)) + temp_11(1,k) * remainder(2)) / 16;

            temp(1,k) = (temp_0(1,k) * (16 - remainder(1)) + temp_1(1,k) * remainder(1)) / 16;

        end   

        out_im2(i,j,:) = temp;
        
    end
end
out_im;
%figure(2);imshow(uint8(out_im));
figure(3);imshow(uint8(out_im2));
 imwrite(uint8(out_im2),'test111.jpg'); 
